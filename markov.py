import pandas as pd

class MarkovChain:
    """
    Represents a Markov chain with states and staying times.
    """
    def __init__(self, states: list[int], staying_times: list[float]):
        self.states = states
        self.staying_times = staying_times

    # Note this is equal to L in little's formula
    def get_average_queue_length(self) -> float:
        weighted_sum = sum(s * t for s, t in zip(self.states, self.staying_times))
        return weighted_sum
    
    def get_server_idle_time(self, servers: int=1) -> float:
        idle_time = 0.0
        for state, time in zip(self.states, self.staying_times):
            if state < servers:
                idle_time += (servers - state) * time
        return idle_time
    
    def get_patient_waiting_time(self, servers: int=1) -> float:
        total_waiting_time = 0.0
        for state, time in zip(self.states, self.staying_times):
            if state > servers:
                total_waiting_time += (state - servers) * time
        return total_waiting_time
    
    def list_waiting_times(self, servers: int=1) -> list[float]:
        waiting_times: list[float] = []
        for state, time in zip(self.states, self.staying_times):
            if state > servers:
                waiting_times.append((state - servers) * time)
            else:
                waiting_times.append(0.0)
        return waiting_times

    def get_server_overtime(self, working_hours: float, servers: int=1) -> float:
        total_time = sum(self.staying_times)
        overtime = 0.0
        for i in range(servers):
            overtime += max(0.0, total_time - working_hours * 60.0)
            total_time -= self.staying_times[-1 - i]
        return overtime
    
    def get_doctor_utilization(self) -> float:
        busy_time = 0.0
        total_time = sum(self.staying_times)
        for state, time in zip(self.states, self.staying_times):
            if state > 0:
                busy_time += time
        return (busy_time / total_time) * 100  # percentage
    
    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({
            "state": self.states,
            "staying_time": self.staying_times
        })
                