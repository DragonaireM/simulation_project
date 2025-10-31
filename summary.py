from typing import Any
import pandas as pd

class Statistic:
    """
    The smallest unit in a Summary.
    """

    def __init__(self, header: str, content: Any):
        self.header = header.replace(" ", "_").lower()
        self.content = float(content)

    def __str__(self):
        return f"{self.header}: {str(self.content)}"

class Section:
    """
    A section in a Summary, containing multiple Statements.
    """

    def __init__(self, title: str):
        self.title = title.replace(" ", "_").lower()

    def add_stats(self, statistic: Statistic):
        self.__setattr__(statistic.header, statistic.content)

    def __str__(self):
        section_str = f"--- {self.title} ---\n"
        for attr, value in self.__dict__.items():
            if attr != "title":
                section_str += f"{attr}: {value}\n"
        return section_str

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]
    
    def to_dataframe(self) -> pd.DataFrame:
        """
        Returns the section as a pandas DataFrame with two columns: 'metric' and 'value'.
        """
        data: dict[str, list[Any]] = {
            "metric": [],
            "value": []
        }
        for attr, value in self.__dict__.items():
            if attr != "title":
                data["metric"].append(attr)
                data["value"].append(value)
        return pd.DataFrame(data)
    
class Averages(Section):
    """
    A section specifically for holding average metrics.
    """

    def __init__(self):
        super().__init__(title="Averages")
        self.avg_server_idle_time: float = 0.0
        self.avg_patient_waiting_time: float = 0.0
        self.avg_server_overtime: float = 0.0
        self.total_cost: float = 0.0

class PatientMetrics(Section):
    """
    A section specifically for holding patient metrics.
    """

    def __init__(self):
        super().__init__(title="Patient Metrics")
        self.avg_waiting_time: float = 0.0
        self.max_waiting_time: float = 0.0
        self.std_waiting_time: float = 0.0
        self.patients_waiting_over_15_min: int = 0
        self.percentage_waiting_over_15_min: float = 0.0
        self.waiting_time_95th_percentile: float = 0.0

class SystemMetrics(Section):
    """
    A section specifically for holding system metrics.
    """

    def __init__(self):
        super().__init__(title="System Metrics")
        self.doctor_utilization: float = 0.0
        self.avg_queue_length: float = 0.0
        self.throughput: float = 0.0

class Schedules(Section):
    """
    A section specifically for holding multiple schedules.
    Each schedule is stored as a Statement with the schedule index as header.
    """

    def __init__(self):
        super().__init__(title="Schedules")
        self.arr: list[pd.DataFrame] = []

    def append(self, schedule_df: pd.DataFrame):
        self.arr.append(schedule_df)

    def extend(self, schedule_dfs: list[pd.DataFrame]):
        self.arr.extend(schedule_dfs)

class WaitingTimes(Section):
    """
    A section specifically for holding waiting times.
    """

    def __init__(self):
        super().__init__(title="Waiting Times")
        self.arr: list[float] = []

    def append(self, waiting_time: float):
        self.arr.append(waiting_time)

    def extend(self, waiting_times: list[float]):
        self.arr.extend(waiting_times)

class Summary:
    """
    A summary report consisting of multiple Sections.
    """

    def __init__(self):
        self.averages = Averages()
        self.patient_metrics = PatientMetrics()
        self.system_metrics = SystemMetrics()
        self.schedules = Schedules()
        self.waiting_times = WaitingTimes()

    def add_section(self, section: Section):
        self.__setattr__(section.title.replace(" ", "_").lower(), section)

    def __str__(self):
        summary_str = "Summary Report\n\n"
        for sec in self.__dict__.values():
            if isinstance(sec, Section):
                summary_str += str(sec) + "\n"
        return summary_str
    
    def __getitem__(self, key: str) -> Section:
        return self.__dict__[key]