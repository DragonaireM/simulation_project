import heapq
import bisect
from markov import MarkovChain
import pandas as pd
import numpy as np

def two_largest(values: list[float]) -> tuple[float | None, float | None]:
    if not values:
        return None, None
    if len(values) == 1:
        return values[0], None
    max1 = float("-inf")
    max2 = float("-inf")
    for v in values:
        if v > max1:
            max2 = max1
            max1 = v
        elif v > max2:
            max2 = v
    return (max1, max2 if max2 != float("-inf") else None)

class Schedule:
    """
    Represents the schedule of a clinic's queueing system.
    """

    def __init__(self, working_hours: float=10.0, scheduled_arrival: float=16.0):
        self.working_hours = working_hours  # hours
        self.scheduled_arrival = scheduled_arrival  # minutes
        self.arrival_times: list[float] = []
        self.service_start_times: list[float] = []
        self.service_end_times: list[float] = []
        self.markov_chain: MarkovChain | None = None
        self.idle_time = 0.0
        self.waiting_times: list[float] = []
        self.overtime_time = 0.0

    def setup_schedule(self, arrival_times: list[float], service_times: np.ndarray, servers: int=1, queue_capacity: float=float('inf')):
        """Sets up the schedule for potentially multiple servers.

        Approach:
        - Keep a min-heap `busy` of service end times for busy servers.
        - For each arrival:
          * pop all busy servers that finished <= arrival (they become free)
          * compute current waiting size with bisect on non-decreasing service_start_times
          * if total in system >= servers + queue_capacity -> drop arrival
          * if free server exists -> start at arrival
          * else -> pop earliest end, start at that time (customer waits)
          * push new end time into heap
        This avoids sorting all end times each iteration.
        """
        # save the variables (for potential future use)
        # Ensure all arrival_times are positive
        self.arrival_times = [max(0.0, t) for t in arrival_times]
        # Sort arrival times to ensure non-decreasing order
        self.arrival_times.sort()
        self.service_times = service_times
        self.servers = servers
        self.queue_capacity = queue_capacity

        # min-heap of end times for busy servers
        busy: list[float] = []

        for i, arrival in enumerate(self.arrival_times):
            # free servers that finished before or at arrival
            while busy and busy[0] <= arrival:
                heapq.heappop(busy)

            # number of previously scheduled starts that are still in the waiting line
            # service_start_times is non-decreasing, so bisect_right gives count of starts <= arrival
            started_by_arrival = bisect.bisect_right(self.service_start_times, arrival)
            waiting_count = len(self.service_start_times) - started_by_arrival

            total_in_system = len(busy) + waiting_count
            # if capacity is finite and the system is full, drop this arrival
            if total_in_system >= servers + queue_capacity:
                # drop / reject arrival: do not create start/end for this customer
                continue

            if len(busy) < servers:
                # free server available right now
                # also means server was idle
                num_idle = servers - len(busy)
                if num_idle > 0:
                    idle_time = arrival - (self.service_end_times[-1] if self.service_end_times else 0.0)
                    self.idle_time += idle_time * num_idle
                start_time = arrival
            else:
                # all servers busy -> wait until the earliest one finishes
                earliest_end = heapq.heappop(busy)
                start_time = earliest_end

            end_time = start_time + service_times[i]
            self.service_start_times.append(start_time)
            self.service_end_times.append(end_time)
            heapq.heappush(busy, end_time)

        max1, max2 = two_largest(self.service_end_times)
        if max2 is not None and self.servers > 1:
            self.overtime_time += max(0.0, max2 - self.working_hours * 60.0)
        if max1 is not None:
            self.overtime_time += max(0.0, max1 - self.working_hours * 60.0)

    def get_schedule(self) -> list[tuple[int, float, float, float, float]]:
        return [
            (i, self.arrival_times[i], self.service_start_times[i], self.service_end_times[i], self.service_end_times[i] - self.service_start_times[i])
            for i in range(len(self.arrival_times))
        ]
    
    def to_markov_chain(self) -> MarkovChain:
        """
        Converts the schedule to a Markov chain representation.
        - states: list of number of patients in the system at each event time
        - staying_times: list of times spent in each state
        """
        states: list[int] = []
        staying_times: list[float] = []

        # Logic:
        # Use two pointers to traverse arrival_times and service_end_times
        # Increment num_in_system on arrival, decrement on service end
        arrival_ptr = 0
        end_ptr = 0
        current_time = 0.0
        num_in_system = 0

        # Modify list to account for servers > 1
        at = self.arrival_times
        et = sorted(self.service_end_times)

        # Traverse until both lists are fully processed
        while arrival_ptr < len(at) or end_ptr < len(et):
            # Get the next arrival and service end times
            # as long as pointers are within bounds
            # or else set to infinity (to ensure the other event is chosen)
            next_arrival = at[arrival_ptr] if arrival_ptr < len(at) else float('inf')
            next_end = et[end_ptr] if end_ptr < len(et) else float('inf')

            # Similar to exponential race
            # If next arrival is earlier, 
            # it means next patient arrives before current patient's service ends
            # else it's a service end event
            if next_arrival <= next_end:
                # Arrival event
                if current_time < next_arrival:
                    states.append(num_in_system)
                    staying_times.append(next_arrival - current_time)
                    current_time = next_arrival
                num_in_system += 1
                arrival_ptr += 1
            else:
                # Service end event
                if current_time < next_end:
                    states.append(num_in_system)
                    staying_times.append(next_end - current_time)
                    current_time = next_end
                num_in_system -= 1
                end_ptr += 1

        self.markov_chain = MarkovChain(states, staying_times)
        return self.markov_chain

    def to_dataframe(self) -> pd.DataFrame:
        """Converts the schedule to a pandas DataFrame."""
        data: dict[str, list[float]] = {
            "patient": list(range(len(self.arrival_times))),
            "arrival": self.arrival_times,
            "start": self.service_start_times,
            "end": self.service_end_times,
            "service_time": [end - start for start, end in zip(self.service_start_times, self.service_end_times)],
            # "waiting_time": [start - arrival for arrival, start in zip(self.arrival_times, self.service_start_times)]
            "waiting_time": [max(0.0, start - i * self.scheduled_arrival) for i, start in enumerate(self.service_start_times)]
        }
        return pd.DataFrame(data)