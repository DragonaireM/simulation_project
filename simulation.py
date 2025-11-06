from distribution import Exponential, Lognormal, TruncatedNormal
from schedule import Schedule
import pandas as pd
from typing import Any
import sqlite3
import numpy as np
import os
import tempfile
from tqdm import tqdm
from summary import Summary, Statistic, Schedules, WaitingTimes, PatientMetrics, Averages, SystemMetrics

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
        self.iat_distribution = iat_distr
        self.service_distribution = service_distr
        self.schedules: list[Schedule] = []
        self.cost_params = cost_params  # idle, waiting, overtime, labor costs
        self.seed = seed
        self.control_variate_info = {}  # Store control variate information if used
        self.setup()

    def setup(self) -> None:
        """Sets up attributes that depend on other parameters."""
        self.number_of_patients = int(self.working_hours * 60 // self.mean_service_time)
        self.service_distribution = Lognormal(desired_mean=self.mean_service_time)

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

    def summary(self, print_summary: bool = False) -> Summary:
        """
        Returns:
            A Summary object containing various metrics from the simulation.

        Args:
            print_summary: If True, prints a formatted summary to terminal
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
            total_session_time.append(markov_chain.total_time)

        # Create a Summary object
        summary = Summary()

        patient_metrics = PatientMetrics()

        patient_metrics.add_stats(Statistic("Avg Waiting Time", np.mean(waiting_times)))
        patient_metrics.add_stats(Statistic("Max Waiting Time", np.max(waiting_times)))
        patient_metrics.add_stats(Statistic("Std Waiting Time", np.std(waiting_times)))
        patient_metrics.add_stats(Statistic("Patients Waiting Over 15 Min", np.sum(np.array(waiting_times) > 15) or 0))
        patient_metrics.add_stats(Statistic("Percentage Waiting Over 15 Min", np.mean(np.array(waiting_times) > 15) * 100))
        patient_metrics.add_stats(Statistic("Waiting Time 95th Percentile", np.percentile(waiting_times, 95)))

        summary.add_section(patient_metrics)

        system_metrics = SystemMetrics()

        system_metrics.add_stats(Statistic("Doctor Utilization", np.mean(doctor_utilizations)))
        system_metrics.add_stats(Statistic("Avg Queue Length", np.mean(queue_lengths)))
        system_metrics.add_stats(Statistic("Throughput", np.mean([self.number_of_patients / total for total in total_session_time if total > 0])))

        summary.add_section(system_metrics)

        average_costs = Averages()

        self.cost = float(np.mean(idle_times) * self.cost_params[0] +
                                np.mean(waiting_times) * self.number_of_patients * self.cost_params[1] +
                                np.mean(overtime_times) * self.cost_params[2] +
                                self.doctors * self.working_hours * 60.0 * self.cost_params[3])

        average_costs.add_stats(Statistic("Avg Server Idle Time", np.mean(idle_times)))
        average_costs.add_stats(Statistic("Avg Patient Waiting Time", np.mean(waiting_times)))
        average_costs.add_stats(Statistic("Avg Server Overtime", np.mean(overtime_times)))
        average_costs.add_stats(Statistic("Total Cost", self.cost))

        summary.add_section(average_costs)

        schedules_section = Schedules()
        schedules_section.extend(schedules_dfs)
        summary.add_section(schedules_section)

        waiting_times_section = WaitingTimes()
        waiting_times_section.extend(waiting_times)
        summary.add_section(waiting_times_section)

        self.summaries = summary
        if print_summary:
            self._print_summary()

        return summary

    def _print_summary(self) -> None:
        """Print formatted summary to terminal"""
        print("\n" + "="*80)
        print("SIMULATION SUMMARY")
        print("="*80)

        if not hasattr(self, 'summaries'):
            print("No summary available. Run summary() first.")
            return

        s = self.summaries

        print(f"\nSimulation Parameters:")
        print(f"  Number of runs: {len(self.schedules)}")
        print(f"  Working hours: {self.working_hours} hours")
        print(f"  Mean service time: {self.mean_service_time} minutes")
        print(f"  Number of doctors: {self.doctors}")

        print(f"\nPatient Waiting Time Metrics (MINUTES):")
        print(f"  Average waiting time: {s['patient_metrics']['avg_waiting_time']:.4f} minutes")
        print(f"  Max waiting time: {s['patient_metrics']['max_waiting_time']:.4f} minutes")
        print(f"  Std dev waiting time: {s['patient_metrics']['std_waiting_time']:.4f} minutes")
        print(f"  95th percentile: {s['patient_metrics']['waiting_time_95th_percentile']:.4f} minutes")
        print(f"  Patients waiting > 15 min: {s['patient_metrics']['patients_waiting_over_15min']}")

        print(f"\nServer Metrics (MINUTES per session):")
        print(f"  Average idle time: {s['averages']['avg_server_idle_time']:.4f} minutes")
        print(f"  Average overtime: {s['averages']['avg_server_overtime']:.4f} minutes")

        print(f"\nSystem Metrics:")
        print(f"  Doctor utilization: {s['system_metrics']['doctor_utilization']:.2%}")
        print(f"  Average queue length: {s['system_metrics']['avg_queue_length']:.4f} patients")
        print(f"  Throughput: {s['system_metrics']['throughput']:.4f} patients/minute")

        print(f"\nTotal Cost: ${s['averages']['total_cost']:.2f}")

        # Print control variate information if available
        if self.control_variate_info:
            cv_info = self.control_variate_info
            print("\n" + "-"*80)
            print("CONTROL VARIATES VARIANCE REDUCTION")
            print("-"*80)
            print(f"  Control variable: Service Time (mean = {self.mean_service_time} minutes)")
            print(f"  Variance reduction: {cv_info.get('variance_reduction_percent', 0):.2f}%")
            print(f"  Efficiency gain: {cv_info.get('efficiency_gain', 1):.2f}x")
            print(f"  Average correlation (W,S): {cv_info.get('avg_correlation', 0):.4f}")
            print(f"  Average optimal coefficient: {cv_info.get('avg_coefficient', 0):.6f}")
            print("\n  Without Control Variates:")
            print(f"    Mean waiting time: {cv_info.get('standard_mean', 0):.4f} minutes")
            print(f"    Variance: {cv_info.get('standard_variance', 0):.6f}")
            print("\n  With Control Variates:")
            print(f"    Mean waiting time: {cv_info.get('cv_mean', 0):.4f} minutes")
            print(f"    Variance: {cv_info.get('cv_variance', 0):.6f}")

        print("="*80 + "\n")
    
    def total_cost(self) -> float:
        """
        Return the total cost of the simulation using precomputed summary metrics.
        This is faster than _total_cost().
        """
        if not hasattr(self, "summaries"):
            self.summary()
        return self.summaries["averages"]["total_cost"]

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
            summaries.averages.to_dataframe().to_sql(
                "averages", conn, index=False, if_exists="replace"
            )
            summaries.patient_metrics.to_dataframe().to_sql(
                "patient_metrics", conn, index=False, if_exists="replace"
            )
            # system_metrics is already a DataFrame; write it directly instead of trying to build a Series from a DataFrame
            summaries.system_metrics.to_dataframe().to_sql(
                "system_metrics", conn, index=False, if_exists="replace"
            )
            # write each schedule as its own table
            for i, df in enumerate(summaries.schedules.arr, start=1):
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
            d = self.summaries[key].__dict__
            # rough: each key and value as text, estimate len of repr
            total_bytes += sum(len(str(k)) + len(str(v)) for k, v in d.items())

        # schedules: sum pandas memory usage
        for df in self.summaries.schedules.arr:
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

    def simulate_single_run(self, seed: int | None = None) -> pd.DataFrame:
        """
        Run a single simulation and return results as DataFrame with columns:
        Patient_ID, Arrival_Time, Service_Time, Start_Service, End_Service, Waiting_Time
        """
        service_times = self.service_distribution.sample(size=self.number_of_patients, seed=seed)
        interarrival_deviation = self.iat_distribution.sample(size=self.number_of_patients, seed=seed)
        interarrival_times = [self.scheduled_arrival + dev for dev in interarrival_deviation]
        interarrival_times[0] -= self.scheduled_arrival

        schedule = Schedule(self.working_hours)
        schedule.setup_schedule(
            interarrival_times,
            service_times,
            servers=self.doctors,
            queue_capacity=self.queue_capacity
        )

        df = schedule.to_dataframe()
        # Rename columns to match control variate format
        df_result = pd.DataFrame({
            'Patient_ID': df['patient'],
            'Arrival_Time': df['arrival'],
            'Service_Time': df['service_time'],
            'Start_Service': df['start'],
            'End_Service': df['end'],
            'Waiting_Time': df['waiting_time']
        })

        return df_result

    def simulate_without_control_variates(self, num_runs: int = 100, base_seed: int | None = None,
                                          save_to_json: bool = True,
                                          json_filename: str = 'standard_mc_results.json') -> pd.DataFrame:
        """
        Standard Monte Carlo simulation without variance reduction
        """
        print(f"\n{'='*80}")
        print(f"STANDARD MONTE CARLO SIMULATION (No Control Variates)")
        print(f"{'='*80}")
        print(f"Number of runs: {num_runs}")

        if base_seed is None:
            base_seed = self.seed if self.seed is not None else 42

        all_results: list[pd.DataFrame] = []

        for run in tqdm(range(num_runs), desc="Standard MC Simulation"):
            seed = base_seed + run
            df = self.simulate_single_run(seed=seed)
            df['run_id'] = run
            all_results.append(df)

        combined_df = pd.concat(all_results, ignore_index=True)

        # Calculate statistics
        run_means = combined_df.groupby('run_id')['Waiting_Time'].mean()
        overall_mean = run_means.mean()
        overall_var: float = float(run_means.var(ddof=1))

        print(f"\n{'='*80}")
        print("STANDARD MC SUMMARY")
        print(f"{'='*80}")
        print(f"Mean waiting time across runs: {overall_mean:.6f} hours")
        print(f"Variance of mean waiting times: {overall_var:.6f}")
        print(f"Standard error: {np.sqrt(overall_var):.6f}")
        print(f"{'='*80}\n")

        if save_to_json:
            combined_df.to_json(json_filename, orient='records', indent=2)
            print(f"[SAVED] Results saved to: {json_filename}")

        return combined_df

    def simulate_with_control_variates(self, num_runs: int = 100, base_seed: int | None = None,
                                       save_to_json: bool = True,
                                       json_filename: str = 'control_variate_results.json') -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Simulate using Control Variates variance reduction
        Uses service time as control variable since E[Service_Time] is known
        """
        print(f"\n{'='*80}")
        print(f"CONTROL VARIATES MONTE CARLO SIMULATION")
        print(f"{'='*80}")
        print(f"Number of runs: {num_runs}")
        print(f"Control variable: Service Time (Known mean = {self.mean_service_time:.4f} hours)")

        if base_seed is None:
            base_seed = self.seed if self.seed is not None else 42

        all_results: list[pd.DataFrame] = []
        variance_reduction_info: list[dict[str, Any]] = []

        for run in tqdm(range(num_runs), desc="Control Variates Simulation"):
            # Generate SAME random sequence for fair comparison
            seed = base_seed + run

            # Simulate single run
            df = self.simulate_single_run(seed=seed)

            # Calculate control variate adjustment
            # Control variable: Service Time (S)
            # Response variable: Waiting Time (W)
            service_times = df['Service_Time'].values
            waiting_times = df['Waiting_Time'].values

            # Known theoretical mean of service time
            expected_service_time = self.mean_service_time

            # Calculate optimal coefficient: c* = -Cov(W,S) / Var(S)
            cov_ws = np.cov(waiting_times, service_times)[0, 1]
            var_s = np.var(service_times, ddof=1)

            if var_s > 0:
                c_optimal = -cov_ws / var_s
            else:
                c_optimal = 0

            # Apply control variate: W* = W - c*(S - E[S])
            controlled_waiting_times = waiting_times - c_optimal * (service_times - expected_service_time)

            # Store variance reduction info for this run
            original_var = np.var(waiting_times, ddof=1)
            controlled_var = np.var(controlled_waiting_times, ddof=1)
            var_reduction = ((original_var - controlled_var) / original_var * 100) if original_var > 0 else 0

            variance_reduction_info.append({
                'run_id': run,
                'c_optimal': c_optimal,
                'original_variance': original_var,
                'controlled_variance': controlled_var,
                'variance_reduction_percent': var_reduction,
                'correlation_ws': np.corrcoef(waiting_times, service_times)[0, 1]
            })

            # Create dataframe with controlled waiting times
            df_controlled = df.copy()
            df_controlled['Waiting_Time'] = controlled_waiting_times
            df_controlled['Waiting_Time_Original'] = waiting_times
            df_controlled['Control_Coefficient'] = c_optimal
            df_controlled['run_id'] = run

            all_results.append(df_controlled)

        # Combine all runs
        combined_df = pd.concat(all_results, ignore_index=True)

        # Print summary statistics
        print(f"\n{'='*80}")
        print("CONTROL VARIATES SUMMARY")
        print(f"{'='*80}")

        vr_df = pd.DataFrame(variance_reduction_info)
        print(f"Average optimal coefficient (c*): {vr_df['c_optimal'].mean():.6f}")
        print(f"Average W-S correlation: {vr_df['correlation_ws'].mean():.6f}")
        print(f"Average within-run variance reduction: {vr_df['variance_reduction_percent'].mean():.2f}%")
        print(f"Runs with negative correlation (good for CV): {(vr_df['correlation_ws'] < 0).sum()}/{num_runs}")

        # Calculate overall statistics
        original_waiting = combined_df.groupby('run_id')['Waiting_Time_Original'].mean()
        controlled_waiting = combined_df.groupby('run_id')['Waiting_Time'].mean()

        print(f"\nOverall Statistics Across Runs:")
        print(f"  Original MC - Mean: {original_waiting.mean():.6f}, Var: {original_waiting.var(ddof=1):.6f}")
        print(f"  Control Variates - Mean: {controlled_waiting.mean():.6f}, Var: {controlled_waiting.var(ddof=1):.6f}")
        overall_reduction = ((original_waiting.var(ddof=1) - controlled_waiting.var(ddof=1)) / original_waiting.var(ddof=1) * 100)
        print(f"  Between-run variance reduction: {overall_reduction:.2f}%")
        print(f"{'='*80}\n")

        # Save to JSON
        if save_to_json:
            combined_df.to_json(json_filename, orient='records', indent=2)
            print(f"[SAVED] Results saved to: {json_filename}")

            # Save variance reduction info separately
            vr_filename = json_filename.replace('.json', '_variance_reduction.json')
            vr_df.to_json(vr_filename, orient='records', indent=2)
            print(f"[SAVED] Variance reduction details saved to: {vr_filename}")

        return combined_df, vr_df

    def compare_variance_reduction(self, num_runs: int = 1000, base_seed: int | None = None) -> dict[str, Any]:
        """
        Compare standard MC vs control variates on the same random samples
        """
        if base_seed is None:
            base_seed = self.seed if self.seed is not None else 42

        # Run both simulations with same seeds
        print("Running comparison between Standard MC and Control Variates...")

        df_standard = self.simulate_without_control_variates(
            num_runs=num_runs,
            base_seed=base_seed,
            save_to_json=False
        )

        df_cv, vr_info = self.simulate_with_control_variates(
            num_runs=num_runs,
            base_seed=base_seed,
            save_to_json=False
        )

        # Calculate comparison statistics
        standard_means = df_standard.groupby('run_id')['Waiting_Time'].mean()
        cv_means = df_cv.groupby('run_id')['Waiting_Time'].mean()

        comparison: dict[str, Any] = {
            'num_runs': num_runs,
            'base_seed': base_seed,
            'standard_mc': {
                'mean_waiting_time': float(standard_means.mean()),
                'variance': float(standard_means.var(ddof=1)),
                'std_error': float(standard_means.std(ddof=1) / np.sqrt(num_runs))
            },
            'control_variates': {
                'mean_waiting_time': float(cv_means.mean()),
                'variance': float(cv_means.var(ddof=1)),
                'std_error': float(cv_means.std(ddof=1) / np.sqrt(num_runs))
            }
        }

        comparison['variance_reduction_percent'] = float(
            ((comparison['standard_mc']['variance'] - comparison['control_variates']['variance'])
             / comparison['standard_mc']['variance'] * 100)
        )

        comparison['efficiency_gain'] = float(
            comparison['standard_mc']['variance'] / comparison['control_variates']['variance']
        )

        # Store control variate info for summary display
        self.control_variate_info: dict[str, float] = {
            'variance_reduction_percent': comparison['variance_reduction_percent'],
            'efficiency_gain': comparison['efficiency_gain'],
            'avg_correlation': float(vr_info['correlation_ws'].mean()),
            'avg_coefficient': float(vr_info['c_optimal'].mean()),
            'standard_mean': comparison['standard_mc']['mean_waiting_time'],
            'standard_variance': comparison['standard_mc']['variance'],
            'cv_mean': comparison['control_variates']['mean_waiting_time'],
            'cv_variance': comparison['control_variates']['variance']
        }

        # Print comparison
        print(f"\n{'='*80}")
        print("VARIANCE REDUCTION COMPARISON")
        print(f"{'='*80}")
        print(f"Number of runs: {num_runs}")
        print(f"Base seed: {base_seed}")
        print(f"\nStandard Monte Carlo:")
        print(f"  Mean waiting time: {comparison['standard_mc']['mean_waiting_time']:.6f} hours")
        print(f"  Variance: {comparison['standard_mc']['variance']:.6f}")
        print(f"  Standard error: {comparison['standard_mc']['std_error']:.6f}")
        print(f"\nControl Variates:")
        print(f"  Mean waiting time: {comparison['control_variates']['mean_waiting_time']:.6f} hours")
        print(f"  Variance: {comparison['control_variates']['variance']:.6f}")
        print(f"  Standard error: {comparison['control_variates']['std_error']:.6f}")
        print(f"\nVariance Reduction: {comparison['variance_reduction_percent']:.2f}%")
        print(f"Efficiency Gain: {comparison['efficiency_gain']:.2f}x")
        print(f"  (Control variates is equivalent to {comparison['efficiency_gain']:.2f}x more standard MC runs)")
        print(f"{'='*80}\n")

        return comparison

    def __getitem__(self, key: str) -> Any:
        """
        Allow dict-like access to attributes.
        """
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"Key '{key}' not found in Simulation attributes.")
    
    def __setitem__(self, key: str, value: Any) -> None:
        """
        Allow dict-like setting of attributes.
        """
        setattr(self, key, value)
    
    def __str__(self) -> str:
        # Use notation of queueing systems (e.g., M/M/1)
        return (f"{int(self.scheduled_arrival)}/{float(self.mean_service_time)}/{int(self.doctors)}")
    
    def __repr__(self) -> str:
        # Same as __str__
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Simulation):
            return NotImplemented
        return (self.working_hours == other.working_hours and
                self.scheduled_arrival == other.scheduled_arrival and
                self.mean_service_time == other.mean_service_time and
                self.doctors == other.doctors and
                self.queue_capacity == other.queue_capacity and
                self.number_of_patients == other.number_of_patients and
                self.iat_distribution == other.iat_distribution and
                self.service_distribution == other.service_distribution and
                self.cost_params == other.cost_params and
                self.seed == other.seed)

