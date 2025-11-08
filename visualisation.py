import matplotlib.pyplot as plt
import numpy as np
from typing import Any, Optional
from optimisation import Optimisation
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import os

class ClinicVisualization:
    """
    A comprehensive visualization class for clinic simulation results.
    Initialize with raw data, then call individual plot methods.
    """

    def __init__(self, model: Optimisation, variable: str, config: Optional[dict[str, Any]] = None):
        """
        Initialize with simulation results.
        
        Parameters:
        - simulation_data: Simulation object containing all simulation results
        - config: Optional configuration for plot styling
        """
        self.model = model
        self.data = self.model.simulations[variable]
        self.config = config or self._default_config()
        self.opt_sim = self.model.optimal_solution(variable=variable)
        
        # Set style
        plt.style.use('seaborn-v0_8')
        self.colors = ['#2E86AB', '#A23B72', "#F89705", '#C73E1D', '#3F7CAC']
        
    def _default_config(self) -> dict[str, Any]:
        """Default configuration for plots"""
        return {
            'figsize': (10, 6),
            'dpi': 100,
            'fontsize': 12,
            'style': 'seaborn-v0_8',
            'save_format': 'png',
            'save_dpi': 300,
            'save_pad_inches': 0.1
        }

    def plot_cost_against_variable(self, ax: Optional[Axes] = None, variable: str = "scheduled_arrival") -> Axes:
        """
        Plot total cost vs variable with optimal point highlighted.

        Minimum Obj[Simulations] required: 2 (different scheduled arrivals)
        """
        if ax is None:
            _, ax = plt.subplots(figsize=self.config['figsize'])

        title = f"Total Cost vs {variable.replace('_', ' ').title()}"

        manipulated_var = [data[variable] for data in self.data]
        total_costs = [round(data.summaries.averages.total_cost, 2) for data in self.data]
        optimal_cost = min(total_costs)

        ax.plot(manipulated_var, total_costs, 'o-', linewidth=2, markersize=8, color=self.colors[0], label='Total Cost')
        
        optimal_idx = total_costs.index(optimal_cost)
        ax.plot(manipulated_var[optimal_idx], total_costs[optimal_idx], 'ro', markersize=12, label=f'Optimal: {manipulated_var[optimal_idx]} min')

        ax.set_xlabel(f"{variable.title()}", fontsize=self.config['fontsize'])
        ax.set_ylabel('Total Cost ($)', fontsize=self.config['fontsize'])
        for i in range(len(manipulated_var)):
            ax.annotate(f"{total_costs[i]:.2f}", (manipulated_var[i], total_costs[i]), textcoords="offset points", xytext=(0,10), ha='center', clip_on=False)
        ax.set_title(title, fontsize=self.config['fontsize'] + 2)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        return ax

    def plot_tradeoff_analysis(self, ax1: Optional[Axes] = None, ax2: Optional[Axes] = None) -> tuple[Axes, Axes]:
        """
        Plot waiting time vs utilization trade-off on dual axes.

        Minimum Obj[Simulations] required: 2 (different scheduled arrivals)

        Returns:
        - ax1: Matplotlib Axes object for waiting time
        - ax2: Matplotlib Axes object for doctor utilization
        """
        if ax1 is None or ax2 is None:
            _, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        assert ax1 is not None and ax2 is not None
        
        scheduled_arrivals = [data.scheduled_arrival for data in self.data]
        avg_waiting_times = [data.summaries.patient_metrics.avg_waiting_time for data in self.data]
        doctor_utilizations = [data.summaries.system_metrics.doctor_utilization for data in self.data]

        # Left: Waiting times
        ax1.plot(scheduled_arrivals, avg_waiting_times, 'ro-', linewidth=2, markersize=6, label='Avg Waiting Time')
        ax1.set_xlabel('Scheduled Arrival Time (min)')
        ax1.set_ylabel('Average Waiting Time (min)', color='red')
        ax1.tick_params(axis='y', labelcolor='red')
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Patient Waiting Time')
        
        # Right: Doctor utilization
        ax2.plot(scheduled_arrivals, doctor_utilizations, 'bo-', linewidth=2, markersize=6, label='Doctor Utilization')
        ax2.set_xlabel('Scheduled Arrival Time (min)')
        ax2.set_ylabel('Doctor Utilization (%)', color='blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Doctor Utilization')
        
        plt.tight_layout()
        return (ax1, ax2)
    
    def plot_waiting_time_distribution(self, ax: Optional[Axes] = None,
                                     bins: int = 100,
                                     title: str = "Patient Waiting Time Distribution") -> Axes:
        """
        Plot histogram of waiting times with statistical annotations.

        Minimum Obj[Simulations] required: 1

        Returns:
        - ax: Matplotlib Axes object with the histogram

        Note: Picks the first Simulation, and uses the individual waiting times of all runs for the histogram.
        """
        if ax is None:
            _fig, ax = plt.subplots(figsize=self.config['figsize'])

        waiting_times: list[float] = self.opt_sim.summaries.waiting_times.arr

        _n, bins, _patches = ax.hist(waiting_times, bins=bins, alpha=0.7, color=self.colors[0], edgecolor='black', density=True)
        
        # Add statistical lines
        mean_wait = float(np.mean(waiting_times))
        percentile_95 = float(np.percentile(waiting_times, 95))
        percentile_100 = float(np.max(waiting_times))

        ax.axvline(mean_wait, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_wait:.1f} min')
        ax.axvline(percentile_95, color='orange', linestyle='--', linewidth=2, label=f'95th %ile: {percentile_95:.1f} min')
        ax.axvline(percentile_100, color='yellow', linestyle='--', linewidth=2, label=f'100th %ile: {percentile_100:.1f} min')

        ax.set_xlabel('Waiting Time (minutes)')
        ax.set_ylabel('Density')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        return ax

    def plot_cost_breakdown(self, ax: Optional[Axes] = None) -> Axes:
        """
        Plot cost component breakdown for a specific scheduled arrival time.

        Minimum Obj[Simulations] required: 1

        Returns:
        - ax: Matplotlib Axes object with the pie chart

        Note: Picks the first Simulation, then takes the cost statistics averaged over all runs. 
        """
        if ax is None:
            _fig, ax = plt.subplots(figsize=self.config['figsize'])

        sim = self.opt_sim
        scheduled_arrival = sim.scheduled_arrival

        # Get costs for this inter-arrival time
        costs = [
            float(sim.summaries["averages"]["avg_patient_waiting_time"] * sim.number_of_patients * sim.cost_params[1]),
            float(sim.summaries["averages"]["avg_server_idle_time"] * sim.cost_params[0]),
            float(sim.summaries["averages"]["avg_server_overtime"] * sim.cost_params[2])
        ]
        labels = ['Waiting', 'Idle', 'Overtime']

        pie_result = ax.pie(costs, labels=labels, autopct='%1.1f%%', colors=self.colors[:4], startangle=140)
        # ax.pie may return (wedges, texts) or (wedges, texts, autotexts) depending on autopct;
        # handle both shapes safely.
        if len(pie_result) == 3:
            _wedges, _texts, autotexts = pie_result
        else:
            _wedges, _texts = pie_result
            autotexts = []
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax.set_title(f'Cost Breakdown ({scheduled_arrival} min intervals)', fontsize=self.config['fontsize'])
        return ax
    
    def plot_cost_comparison(self, ax: Optional[Axes] = None) -> Axes:
        """
        Stacked bar chart comparing costs across different scheduled arrival times.

        Minimum Obj[Simulations] required: 2 (different scheduled arrivals)
        """
        if ax is None:
            _fig, ax = plt.subplots(figsize=self.config['figsize'])
        
        scheduled_arrivals = [data.scheduled_arrival for data in self.data]
        waiting_costs = [data.summaries['averages']['avg_patient_waiting_time'] * data.number_of_patients * data.cost_params[1] for data in self.data]
        idle_costs = [data.summaries['averages']['avg_server_idle_time'] * data.cost_params[0] for data in self.data]
        overtime_costs = [data.summaries['averages']['avg_server_overtime'] * data.cost_params[2] for data in self.data]

        bar_width = 0.8
        x_pos = np.arange(len(scheduled_arrivals))
        
        ax.bar(x_pos, waiting_costs, bar_width, label='Waiting Cost', color=self.colors[0])
        ax.bar(x_pos, idle_costs, bar_width, bottom=waiting_costs, label='Idle Cost', color=self.colors[1])
        ax.bar(x_pos, overtime_costs, bar_width, bottom=np.array(waiting_costs) + np.array(idle_costs), 
               label='Overtime Cost', color=self.colors[2])
        ax.set_xlabel('Scheduled Arrival Time (minutes)')
        ax.set_ylabel('Total Cost ($)')
        ax.set_title('Cost Component Comparison')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(scheduled_arrivals)
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)
        # make room on the right for the legend
        try:
            _fig.subplots_adjust(right=0.75)
        except Exception:
            plt.tight_layout()
        ax.grid(True, alpha=0.3, axis='y')
        
        return ax

    def plot_queue_evolution(self, schedule_index: int=0, ax: Optional[Axes] = None) -> Axes:
        """
        Plot queue length over time throughout the simulation.

        Minimum Obj[Simulations] required: 1
        """
        if ax is None:
            _fig, ax = plt.subplots(figsize=self.config['figsize'])

        schedule = self.opt_sim.schedules[schedule_index]  # Get specific schedule
        markov_chain = schedule.to_markov_chain()
        time_points = [sum(markov_chain.staying_times[:i+1]) for i in range(len(markov_chain.staying_times))]
        queue_lengths = markov_chain.states
        
        ax.plot(time_points, queue_lengths, color=self.colors[2], linewidth=1.5)
        
        ax.set_xlabel('Time (minutes)')
        ax.set_ylabel('Number of Patients in System')
        ax.set_title('Queue Evolution Throughout the Day')
        ax.grid(True, alpha=0.3)
        ax.fill_between(time_points, queue_lengths, alpha=0.3, color=self.colors[2])
        
        return ax
    
    def plot_schedule_gantt(self, schedule_index: int=0, ax: Optional[Axes] = None) -> Axes:
        """
        Plot Gantt chart of patient schedules.

        Minimum Obj[Simulations] required: 1
        """
        if ax is None:
            _fig, ax = plt.subplots(figsize=self.config['figsize'])

        schedule = self.opt_sim.schedules[schedule_index]  # Get specific schedule

        for i in range(len(schedule.arrival_times)):
            ax.broken_barh(
                [(schedule.service_start_times[i], schedule.service_end_times[i] - schedule.service_start_times[i])],
                (i - 0.4, 0.8),
                facecolors=(self.colors[0])
            )
            ax.broken_barh(
                [(schedule.arrival_times[i], schedule.service_start_times[i] - schedule.arrival_times[i])],
                (i - 0.4, 0.8),
                facecolors=(self.colors[1],), alpha=0.5
            )
            ax.text(
                schedule.service_start_times[i] + (schedule.service_end_times[i] - schedule.service_start_times[i]) / 2,
                i,
                f'{int(schedule.service_end_times[i] - schedule.service_start_times[i])}',
                va='center',
                ha='center',
                color='black'
            )
            # If no waiting time, skip waiting time label
            if schedule.service_start_times[i] > schedule.arrival_times[i]:
                ax.text(
                    schedule.arrival_times[i] + (schedule.service_start_times[i] - schedule.arrival_times[i]) / 2,
                    i,
                    f'{int(schedule.service_start_times[i] - schedule.arrival_times[i])}',
                    va='center',
                    ha='center',
                    color='black'
                )

        ax.set_xlabel('Time (minutes)')
        ax.set_xticks(np.arange(0, max(schedule.service_end_times) + 10, 50))
        ax.set_ylabel('Patients')
        ax.set_yticks(range(len(schedule.arrival_times)))
        ax.set_yticklabels([f'P{i}' for i in range(len(schedule.arrival_times))])
        ax.set_title('Clinic Schedule Gantt Chart')
        ax.legend(['Service Time', 'Waiting Time'], loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)
        # make room on the right for the legend
        try:
            _fig.subplots_adjust(right=0.75)
        except Exception:
            plt.tight_layout()
        ax.grid(True, alpha=0.3)
        
        return ax
    
    @staticmethod
    def plot_2d_relationship(fixed_vars: list[float], opt_vars: list[float], opt_costs: list[float],
                         fixed_var: str, var_to_opt: str,
                         ax: Optional[Axes] = None) -> Axes:
        if ax is None:
            _fig, ax = plt.subplots(figsize=(10, 6))

        ax.plot(fixed_vars, opt_vars, 'o-', linewidth=2, markersize=8, color='#2E86AB')
        ax.set_xlabel(f"Fixed {fixed_var.replace('_', ' ').title()}", fontsize=12)
        ax.set_xticks(fixed_vars)
        ax.set_xticklabels([f"{x:.1f}" for x in fixed_vars])
        ax.set_ylabel(f"Optimal {var_to_opt.replace('_', ' ').title()}", fontsize=12)
        ax.set_title(f"Optimal {var_to_opt.replace('_', ' ').title()} vs Fixed {fixed_var.replace('_', ' ').title()}", fontsize=14)
        for i, txt in enumerate(opt_costs):
            ax.annotate(f"{txt:.1f}", (fixed_vars[i], opt_vars[i]), textcoords="offset points", xytext=(0,10), ha='center', clip_on=False)
        ax.grid(True, alpha=0.3)

        return ax

    def save_figure(self, fig: Figure, filename: str) -> None:
        """Save one Figure to filename. Creates directories as needed."""
        dirname = os.path.dirname(filename)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        fig.savefig(filename, dpi=self.config.get("dpi", 300), bbox_inches="tight", pad_inches=self.config.get("save_pad_inches", 0.1))

    def save_plots(self, base_filename: str) -> None:
        """Save all open figures to files named {base_filename}_{n}.png."""
        dirname = os.path.dirname(base_filename)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        for i, num in enumerate(plt.get_fignums(), start=1):
            fig = plt.figure(num)
            filename = f"{base_filename}_{i}.png"
            self.save_figure(fig, filename)
