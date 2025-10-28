from distribution import Exponential, Lognormal, Triangular, TruncatedNormal
from schedule import Schedule
import pandas as pd
from typing import Any
import json
import sqlite3
import numpy as np
import os
import tempfile

class Simulation:
    def __init__(self,
                 working_hours: float,
                 scheduled_arrival: float,
                 mean_service_time: float,
                 iat_distr: TruncatedNormal,
                 service_distr: Exponential | Lognormal,
                 doctors: int=1,
                 queue_capacity: float=float('inf'),
                 cost_params: tuple[float, float, float, float]=(4.0, 0.2, 6.0, 4.0),
                 seed: int | None=None
                 ):
        self.working_hours = working_hours
        self.scheduled_arrival = scheduled_arrival
        self.mean_service_time = mean_service_time
        self.doctors = doctors
        self.queue_capacity = queue_capacity
        self.number_of_patients = int(working_hours * 60 // mean_service_time)
        self.iat_distribution = iat_distr
        self.service_distribution = service_distr
        self.schedules: list[Schedule] = []
        self.cost_params = cost_params  # idle, waiting, overtime, labor costs
        self.seed = seed

    def __getitem__(self, key: str) -> Any:
        """
        Allow dict-like access to attributes.
        """
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"Key '{key}' not found in Simulation attributes.")
    
    def __str__(self) -> str:
        # Use notation of queueing systems (e.g., M/M/1)
        return (f"{int(self.scheduled_arrival)}/{int(self.mean_service_time)}/{int(self.doctors)}")
    
    def __repr__(self) -> str:
        # Same as __str__
        return self.__str__()

    def unit_test(self, seed: int | None) -> Schedule:
        service_times = self.service_distribution.sample(size=self.number_of_patients, seed=seed)
        interarrival_deviation = self.iat_distribution.sample(size=self.number_of_patients, seed=seed)
        interarrival_times = [self.scheduled_arrival + dev for dev in interarrival_deviation]
        interarrival_times[0] -= self.scheduled_arrival  # first arrival doesn't have to wait for "previous" patient to end service
        schedule = Schedule(self.working_hours)
        schedule.setup_schedule(
            interarrival_times, 
            service_times, 
            servers=self.doctors, 
            queue_capacity=self.queue_capacity
            )
        self.schedules.append(schedule)
        return schedule

    def simulate(self, number_of_runs: int=1) -> list[Schedule]:
        for i in range(number_of_runs):
            self.unit_test(seed = None if self.seed is None else self.seed + i)
        return self.schedules

    def summary(self) -> dict[str, Any]:
        """
        Return:
          {
            "patient_metrics": { ... },
            "system_metrics": { ... },
            "averages": { ... },
            "schedules": [ pd.DataFrame, pd.DataFrame, ... ],
            "waiting_times": [ float, float, ... ]
          }
        """
        idle_times: list[float] = []
        waiting_times: list[float] = []
        overtime_times: list[float] = []
        queue_lengths: list[float] = []
        schedules_dfs: list[pd.DataFrame] = []
        doctor_utilizations: list[float] = []
        total_session_time: list[float] = []

        for schedule in self.schedules:
            df = schedule.to_dataframe()
            schedules_dfs.append(df)

            markov_chain = schedule.to_markov_chain()
            idle_times.append(markov_chain.get_server_idle_time())
            waiting_times.extend(df['waiting_time'])
            overtime_times.append(markov_chain.get_server_overtime(self.working_hours))
            queue_lengths.append(markov_chain.get_average_queue_length())
            doctor_utilizations.append(markov_chain.get_doctor_utilization())
            total_session_time.append(sum(markov_chain.staying_times))

        patient_metrics: dict[str, Any] = {
            'avg_waiting_time': np.mean(waiting_times),
            'max_waiting_time': np.max(waiting_times),
            'std_waiting_time': np.std(waiting_times),
            'patients_waiting_over_15min': np.sum(np.array(waiting_times) > 15) or 0,
            'percentage_waiting_over_15min': np.mean(np.array(waiting_times) > 15) * 100,
            'waiting_time_95th_percentile': np.percentile(waiting_times, 95)
        }

        system_metrics = {
            'doctor_utilization': np.mean(doctor_utilizations),
            'avg_queue_length': np.mean(queue_lengths),
            'throughput': np.mean([self.number_of_patients / total for total in total_session_time if total > 0]),  # patients per minute
        }

        averages = {
            "average_server_idle_time": float(np.mean(idle_times)),
            "average_patient_waiting_time": float(np.mean(waiting_times)),
            "average_server_overtime": float(np.mean(overtime_times)),
            "Total Cost": float(np.mean(idle_times) * self.cost_params[0] + 
                                np.mean(waiting_times) * self.number_of_patients * self.cost_params[1] + 
                                np.mean(overtime_times) * self.cost_params[2] + 
                                self.doctors * self.working_hours * 60.0 * self.cost_params[3])
        }

        self.summaries: dict[str, Any] = {
            "patient_metrics": patient_metrics,
            "system_metrics": system_metrics,
            "averages": averages, 
            "schedules": schedules_dfs,
            "waiting_times": waiting_times
            }
        return self.summaries
    
    def total_cost(self) -> float:
        """
        Return the total cost of the simulation using precomputed summary metrics.
        This is faster than _total_cost().
        """
        if not hasattr(self, "summaries"):
            self.summary()
        return self.summaries["averages"]["Total Cost"]

    def _total_cost(self) -> float:
        """
        Return the total cost of the simulation.

        Note: This method is slower than using summary() to get the total cost,
        as it recalculates the necessary metrics from the schedules.
        Not recommended to use.
        """
        if not self.schedules:
            raise RuntimeError("No schedules available. Run simulate() first.")

        idle_times: list[float] = []
        waiting_times: list[float] = []
        overtime_times: list[float] = []

        for schedule in self.schedules:
            df = schedule.to_dataframe()
            # markov_chain = schedule.to_markov_chain()
            idle_times.append(schedule.idle_time)
            waiting_times.extend(df['waiting_time'])
            overtime_times.append(schedule.overtime_time)

        total_cost = float(np.mean(idle_times) * self.cost_params[0] +
                            np.mean(waiting_times) * self.number_of_patients * self.cost_params[1] +
                            np.mean(overtime_times) * self.cost_params[2] +
                            self.doctors * self.working_hours * 60.0 * self.cost_params[3])
        return total_cost

    def write_summaries_to_json(self, filename: str) -> None:
        summaries = self.summaries
        with open(filename, 'w') as f:
            json.dump(summaries, f, indent=4)

    def write_summaries_to_sqlite(self, filepath: str) -> None:
        """
        Write schedules as separate tables to a single SQLite DB.
        Tables: schedule_run_1, schedule_run_2, ..., and 'averages' for summary metrics.
        """
        summaries = self.summaries
        filename = f"{filepath}/{str(self).replace('/', '_')}.db"
        # Ensure directory exists
        dirpath = os.path.dirname(filename)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)
        conn = sqlite3.connect(filename)
        try:
            # write averages / metrics as two-column tables (key, value)
            pd.Series(summaries["averages"], name="value").reset_index().rename(columns={"index": "metric"}).to_sql(
                "averages", conn, index=False, if_exists="replace"
            )
            pd.Series(summaries["patient_metrics"], name="value").reset_index().rename(columns={"index": "metric"}).to_sql(
                "patient_metrics", conn, index=False, if_exists="replace"
            )
            pd.Series(summaries["system_metrics"], name="value").reset_index().rename(columns={"index": "metric"}).to_sql(
                "system_metrics", conn, index=False, if_exists="replace"
            )
            # write each schedule as its own table
            for i, df in enumerate(summaries["schedules"], start=1):
                tbl = f"schedule_run_{i}"
                df.to_sql(tbl, conn, index=False, if_exists="replace")
        finally:
            conn.close()
            print(f"{filename} written successfully.")

    def estimate_sqlite_size_quick(self) -> int:
        """
        Quick approximate estimate (bytes) of the SQLite DB that write_summaries_to_sqlite would produce.
        Uses DataFrame.memory_usage(deep=True) plus small overheads for schema and per-row storage.
        NOTE: approximate — actual SQLite file size can differ (pages, indices, encoding).
        """
        if not hasattr(self, "summaries"):
            raise RuntimeError("Call summary() first to populate self.summaries")
        total_bytes = 0

        # sizes for the small dict-like tables
        for key in ("averages", "patient_metrics", "system_metrics"):
            d = self.summaries.get(key, {})
            # rough: each key and value as text, estimate len of repr
            total_bytes += sum(len(str(k)) + len(str(v)) for k, v in d.items())

        # schedules: sum pandas memory usage
        for df in self.summaries.get("schedules", []):
            try:
                total_bytes += int(df.memory_usage(deep=True).sum())
            except Exception:
                # fallback for unexpected df-like: convert to CSV size approximation
                try:
                    csv_bytes = df.to_csv(index=False).encode("utf-8")
                    total_bytes += len(csv_bytes)
                except Exception:
                    total_bytes += 1024  # fallback small buffer

            # add per-table SQLite overhead (schema, pages): add 1 KB + 50 bytes per row
            total_bytes += 1024 + 50 * len(df)

        # Add small overhead for SQLite file header / metadata
        total_bytes += 4096
        return total_bytes
    
    def measure_sqlite_size_tempfile(self) -> int:
        """
        Create the SQLite DB in a temporary file using write_summaries_to_sqlite
        and return its exact file size in bytes. The temp file is removed afterwards.
        This is accurate but performs the full write.
        """
        if not hasattr(self, "summaries"):
            raise RuntimeError("Call summary() first to populate self.summaries")
        tmp_fd, tmp_path = tempfile.mkstemp(suffix=".db")
        os.close(tmp_fd)
        try:
            # write to temporary database file
            self.write_summaries_to_sqlite(tmp_path)
            size = os.path.getsize(tmp_path)
        finally:
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        return size

    @staticmethod
    def human_readable_size(num_bytes: float) -> str:
        """Return human readable string for bytes."""
        for unit in ("B", "KB", "MB", "GB", "TB"):
            if num_bytes < 1024.0:
                return f"{num_bytes:.1f} {unit}"
            num_bytes /= 1024.0
        return f"{num_bytes:.1f} PB"

