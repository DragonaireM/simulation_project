from simulation import Simulation
from distribution import Lognormal, TruncatedNormal
from typing import Any
from summary import Summary
from tqdm import tqdm
import pandas as pd

class Optimisation:
    def __init__(self, range: tuple[int, int]=(-5, 5), working_hours: float=8.0, mean_service_time: float=15.5, number_of_doctors: int=1, number_of_runs: int=10000, scheduled_arrival: float=15.0, cost_params: tuple[float, float, float]=(1.0, 0.2, 1.5), seed: int | None = None) -> None:
        self.working_hours = working_hours  # hours
        self.mean_service_time = mean_service_time   # minutes
        self.number_of_doctors = number_of_doctors
        self.number_of_runs = number_of_runs
        self.scheduled_arrival = scheduled_arrival # minutes
        self.range = range
        self.cost_params = cost_params
        self.seed = seed
        self.simulations: dict[str, list[Simulation]] = {
            "scheduled_arrival": [],
            "mean_service_time": [],
            "cost_params": [],
            "2d": []
        }
        self.summary: dict[str, list[Summary]] = {
            "scheduled_arrival": [],
            "mean_service_time": [],
            "cost_params": [],
            "2d": []
        }

    def optimise_for(self, variable: str) -> None:
        """
        Optimize the simulation for a specific variable by adjusting its value
        within the defined range and observing the impact on key performance metrics.
        """
        for value in tqdm(range(self.range[0], self.range[1] + 1), desc="Simulating progress: "):
            # Initialize a new simulation instance with base parameters
            sim = Simulation(
                working_hours=self.working_hours,
                scheduled_arrival=self.scheduled_arrival,
                mean_service_time=self.mean_service_time,
                doctors=self.number_of_doctors,
                iat_distr=TruncatedNormal(),
                service_distr=Lognormal(desired_mean=self.mean_service_time),
                cost_params=self.cost_params,
                seed=self.seed
            )
            # Adjust the specified variable
            if variable == "scheduled_arrival":
                sim.scheduled_arrival += value
            elif variable == "mean_service_time":
                sim.mean_service_time += value
            elif variable == "working_hours":
                sim.working_hours += value
            elif variable == "cost_params":
                # Not applicable here
                pass
            else:
                raise ValueError(f"Unknown variable '{variable}' for optimisation.")

            sim.setup()
            # Run the simulation
            if self.simulations[variable] and sim in self.simulations[variable]:
                # Skip existing simulation if already run
                continue
            sim.simulate(number_of_runs=self.number_of_runs)
            self.simulations[variable].append(sim)
            self.summary[variable].append(sim.summary())

    def optimal_value(self, variable: str) -> tuple[Any, float]:
        """
        Determine the optimal value of the specified variable that minimizes total cost.
        """
        simulations = self.simulations[variable]
        if not simulations:
            raise RuntimeError(f"No simulations found for variable '{variable}'. Run optimise_for() first.")

        if len(simulations) == 1:
            # Only one simulation exists (e.g., for cost_params), return it directly
            sim = simulations[0]
            return getattr(sim, variable), sim.total_cost()

        min_cost = float('inf')
        optimal_value = None
        optimal_cost = 0.0
        for sim in simulations:
            total_cost = sim.total_cost()
            if total_cost < min_cost:
                min_cost = total_cost
                optimal_cost = total_cost
                optimal_value = getattr(sim, variable)

        return optimal_value, optimal_cost
    
    def optimal_solution(self, variable: str) -> Simulation:
        """
        Retrieve the simulation instance corresponding to the optimal value
        of the specified variable.
        """
        simulations = self.simulations[variable]
        if not simulations:
            raise RuntimeError(f"No simulations found for variable '{variable}'. Run optimise_for() first.")
        
        if len(simulations) == 1:
            # Only one simulation exists (e.g., for cost_params), return it directly
            return simulations[0]

        min_cost = float('inf')
        optimal_simulation = None
        for sim in simulations:
            total_cost = sim.total_cost()
            if total_cost < min_cost:
                min_cost = total_cost
                optimal_simulation = sim

        if optimal_simulation is None:
            raise RuntimeError(f"Could not determine optimal simulation for variable '{variable}'.")

        return optimal_simulation

    def _optimise_2d(self, fixed_var: str, var_to_opt: str, fixed_var_range: tuple[int, int]) -> None:
        """
        Perform a 2D optimisation by fixing one variable and optimising another
        across a specified range.

        DISCONTINUED.
        """
        # Make sure variables are valid
        if fixed_var not in ["scheduled_arrival", "mean_service_time", "working_hours"]:
            raise ValueError(f"Unknown fixed variable '{fixed_var}' for 2D optimisation.")
        if var_to_opt not in ["scheduled_arrival", "mean_service_time", "working_hours"]:
            raise ValueError(f"Unknown variable to optimise '{var_to_opt}' for 2D optimisation.")
        if fixed_var == var_to_opt:
            raise ValueError("Fixed variable and variable to optimise must be different.")

        fixed_vars: list[float] = []
        opt_vars: list[float] = []
        opt_costs: list[float] = []
        for fixed_value in range(fixed_var_range[0], fixed_var_range[1] + 1):
            # Create a new optimisation instance with the fixed variable set
            if fixed_var == "scheduled_arrival":
                opt = Optimisation(
                    range=self.range,
                    working_hours=self.working_hours,
                    mean_service_time=self.mean_service_time,
                    number_of_doctors=self.number_of_doctors,
                    number_of_runs=self.number_of_runs,
                    scheduled_arrival=self.scheduled_arrival + fixed_value,
                    cost_params=self.cost_params,
                    seed=self.seed
                )
            elif fixed_var == "mean_service_time":
                opt = Optimisation(
                    range=self.range,
                    working_hours=self.working_hours,
                    mean_service_time=self.mean_service_time + fixed_value,
                    number_of_doctors=self.number_of_doctors,
                    number_of_runs=self.number_of_runs,
                    scheduled_arrival=self.scheduled_arrival,
                    cost_params=self.cost_params,
                    seed=self.seed
                )
            elif fixed_var == "working_hours":
                opt = Optimisation(
                    range=self.range,
                    working_hours=self.working_hours + fixed_value,
                    mean_service_time=self.mean_service_time,
                    number_of_doctors=self.number_of_doctors,
                    number_of_runs=self.number_of_runs,
                    scheduled_arrival=self.scheduled_arrival,
                    cost_params=self.cost_params,
                    seed=self.seed
                )
            else:
                raise ValueError(f"Unknown fixed variable '{fixed_var}' for 2D optimisation.")

            # Optimise the other variable
            print(f"Performing 2D optimisation for {var_to_opt} with {fixed_var} = {getattr(opt, fixed_var)}.")
            opt.optimise_for(variable=var_to_opt)
            optimal_value, optimal_cost = opt.optimal_value(variable=var_to_opt)
            fixed_vars.append(getattr(opt, fixed_var))
            opt_vars.append(optimal_value)
            opt_costs.append(optimal_cost)
            # Store results
            self.simulations["2d"].extend(opt.simulations[var_to_opt])
            self.summary["2d"].extend(opt.summary[var_to_opt])
        
        self.results_2d = {
            "fixed_vars": fixed_vars,
            "opt_vars": opt_vars,
            "opt_costs": opt_costs
        }

    def save_summary_to_db(self, db_path: str, print_summary: bool = True) -> None:
        # Before saving, list all summaries and their respective file sizes
        print("Following sizes are estimated (actual sizes may usually be larger.)")
        for var, simulations in self.simulations.items():
            if not simulations:
                continue
            print(f"Manipulated variable: {var}")
            for i, sim in enumerate(simulations):
                approx_size = sim.estimate_sqlite_size_quick()
                # exact_size = sim.measure_sqlite_size_tempfile()
                print(f"({i}) {sim}: {sim.human_readable_size(approx_size)}")

        # Let user choose which simulations to save
        to_save = input("Which simulations do you want to save? \n(e.g., 'scheduled_arrival:0,2;mean_service_time:1;working_hours:all' \nOR 'all' to save everything \nOR 'none' to save nothing): ")
        selections: dict[str, Any] = {}
        if to_save.strip().lower() == "all":
            for var in self.simulations.keys():
                selections[var] = "all"
        elif to_save.strip().lower() == "none":
            # Do nothing, but not return because we want to print summary
            pass
        else:
            entries = to_save.split(";")
            for entry in entries:
                var, indices = entry.split(":")
                var = var.strip()
                if indices.strip().lower() == "all":
                    selections[var] = "all"
                else:
                    selections[var] = [int(idx) for idx in indices.split(",")]

        # Save selected simulations to the database
        for var, indices in selections.items():
            sims = self.simulations[var]
            if indices == "all":
                selected_sims = sims
            else:
                selected_sims = [sims[int(i)] for i in indices if int(i) < len(sims)]
            for sim in tqdm(selected_sims, desc=f"Saving simulations for variable '{var}'"):
                sim.write_summaries_to_sqlite(db_path)

        # Print summary after saving
        if print_summary:
            self.print_summary_to_console(selections)

    def print_summary_to_console(self, selections: dict[str, Any]) -> None:
        """
        Print summary of averages and patient_metrics to console for selected simulations.
        Includes both standard and control variate results.
        """
        print("\n" + "="*80)
        print("SIMULATION SUMMARY - SAVED RESULTS")
        print("="*80)

        for var, indices in selections.items():
            sims = self.simulations[var]
            if indices == "all":
                selected_sims = sims
            else:
                selected_sims = [sims[int(i)] for i in indices if int(i) < len(sims)]

            for sim in selected_sims:
                print(f"\n{'-'*80}")
                print(f"Variable: {var} | Configuration: {sim}")
                print(f"{'-'*80}")

                # Get the summary (already computed)
                if not hasattr(sim, 'summaries'):
                    sim.summary()

                s = sim.summaries

                # Print Averages Table
                print("\nAVERAGES TABLE (MINUTES):")
                print(f"  Average server idle time:     {s['averages']['avg_server_idle_time']:>12.4f} minutes")
                print(f"  Average patient waiting time: {s['averages']['avg_patient_waiting_time']:>12.4f} minutes")
                print(f"  Average server overtime:      {s['averages']['avg_server_overtime']:>12.4f} minutes")
                print(f"  Total Cost:                   ${s['averages']['total_cost']:>12.2f}")

                # Print Patient Metrics Table
                print("\nPATIENT METRICS (MINUTES):")
                print(f"  Avg waiting time:             {s['patient_metrics']['avg_waiting_time']:>12.4f} minutes")
                print(f"  Max waiting time:             {s['patient_metrics']['max_waiting_time']:>12.4f} minutes")
                print(f"  Std dev waiting time:         {s['patient_metrics']['std_waiting_time']:>12.4f} minutes")
                print(f"  95th percentile:              {s['patient_metrics']['waiting_time_95th_percentile']:>12.4f} minutes")
                print(f"  Patients waiting > 15 min:    {s['patient_metrics']['patients_waiting_over_15min']:>12}")
                print(f"  Percentage waiting > 15 min:  {s['patient_metrics']['percentage_waiting_over_15min']:>12.2f}%")

                # Run comprehensive control variate comparison (this will take some time)
                # Using same number of runs and seeds as optimization for perfect consistency
                print(f"\n  Running comprehensive control variate comparison with {self.number_of_runs} runs...")
                sim.comprehensive_control_variate_comparison(num_runs=self.number_of_runs, base_seed=sim.seed)

        print("\n" + "="*80)
        print("END OF SUMMARY")
        print("="*80 + "\n")

    def sensitivity_analysis(self, variable: str, optimal_solution: Simulation) -> list[dict[str, Any]]:
        """
        Perform sensitivity analysis on the specified variable by examining how changes
        in that variable affect key performance metrics across the simulations.

        Parameters:
        - variable: The variable to perform sensitivity analysis on.
        - optimal_solution: The simulation instance representing the optimal solution.

        Returns a list of dictionaries containing the variable value and corresponding metrics.
        """
        if variable in ["scheduled_arrival", "mean_service_time"]:
            # Perform sensitivity analysis for scheduled_arrival
            # Change the scheduled arrival time around the optimal solution
            analysis_results: list[dict[str, Any]] = []
            for delta in tqdm(range(-3, 4), desc="Sensitivity Analysis Progress"):  # from -3 to +3 minutes
                adjusted_value = optimal_solution[variable] + delta
                # Initialize a new simulation
                sim = Simulation(
                    working_hours=optimal_solution.working_hours,
                    scheduled_arrival=optimal_solution.scheduled_arrival,
                    mean_service_time=optimal_solution.mean_service_time,
                    doctors=optimal_solution.doctors,
                    queue_capacity=optimal_solution.queue_capacity,
                    iat_distr=optimal_solution.iat_distribution,
                    service_distr=optimal_solution.service_distribution,
                    cost_params=optimal_solution.cost_params,
                    seed=self.seed
                )
                # Adjust the variable
                sim[variable] = adjusted_value
                sim.setup()  # Re-setup to update dependent attributes

                if sim in self.simulations[variable]:
                    # Reuse existing simulation if already run
                    existing_index = self.simulations[variable].index(sim)
                    existing_sim = self.simulations[variable][existing_index]
                    summary = self.summary[variable][existing_index]
                    analysis_results.append({
                        "id": delta + 4, # starts from 1
                        variable: adjusted_value,
                        "simulation": existing_sim,
                        "summary": summary
                    })
                    continue

                sim.simulate(number_of_runs=self.number_of_runs)
                summary = sim.summary()
                analysis_results.append({
                    "id": delta + 4, # starts from 1
                    variable: adjusted_value,
                    "simulation": sim,
                    "summary": summary
                })
            return analysis_results

        elif variable == "cost_params":
            # Perform sensitivity analysis for cost_params
            # The only metrics that change are the cost-related ones
            analysis_results: list[dict[str, Any]] = []
            base_cost_params = list(optimal_solution.cost_params)
            multipliers = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]

            # Extract base averages
            averages = self.summary["cost_params"][0].averages
            avg_idle_time = averages.avg_server_idle_time
            avg_waiting_time = averages.avg_patient_waiting_time * optimal_solution.number_of_patients
            avg_overtime = averages.avg_server_overtime

            # Each iteration, pick one cost parameter to vary
            for i in range(3):
                for mult in multipliers:
                    new_cost_params = [param for param in base_cost_params]
                    new_cost_params[i] = base_cost_params[i] * mult
                    new_cost_params_tuple = (new_cost_params[0], new_cost_params[1], new_cost_params[2])

                    # Calculate new total cost based on unchanged averages
                    total_cost = (
                        new_cost_params_tuple[0] * avg_idle_time,
                        new_cost_params_tuple[1] * avg_waiting_time,
                        new_cost_params_tuple[2] * avg_overtime
                    )

                    analysis_results.append({
                        "id": i,
                        "variable": ["Idle Cost", "Waiting Cost", "Overtime Cost"][i],
                        "multiplier": mult,
                        "variable_cost": total_cost[i],
                        "total_cost": total_cost[0] + total_cost[1] + total_cost[2]
                    })

            return analysis_results
        else:
            raise NotImplementedError(f"Sensitivity analysis for variable '{variable}' is not implemented.")

    def sensitivity_summary(self, analysis_results: list[dict[str, Any]], variable: str) -> None:
        """
        Print a summary of the sensitivity analysis results to the console.

        Parameters:
        - analysis_results: List of dictionaries containing analysis results.
        - variable: The variable that was analyzed.
        """
        width = 80 # total width for printing
        print("\n" + "="*width)
        header = f"SENSITIVITY ANALYSIS SUMMARY FOR {variable.upper()}"
        print(" " * ((width - len(header))//2) + header)
        print("="*width)

        if variable in ["scheduled_arrival", "mean_service_time"]:
            text = variable.replace("_", " ").title()
            # Split into three sections: below optimal, at optimal, above optimal
            for i in range(3):
                if i == 0:
                    # Section 1: Below optimal
                    print(f"\n--- Below Optimal {text} ---")
                elif i == 1:
                    # Section 2: At optimal
                    print(f"\n--- At Optimal {text} ---")
                else:
                    # Section 3: Above optimal
                    print(f"\n--- Above Optimal {text} ---")
                minus, zero, plus = analysis_results[2*i:2*i+3]
                minus_delta_df: pd.DataFrame = zero['summary'].compare(minus['summary'])
                plus_delta_df: pd.DataFrame = zero['summary'].compare(plus['summary'])
                minus_delta_df.rename(columns={
                    "this_summary": "self",
                    "other_summary": "minus",
                    "difference": "delta_minus"
                }, inplace=True)
                plus_delta_df.rename(columns={
                    "this_summary": "self",
                    "other_summary": "plus",
                    "difference": "delta_plus"
                }, inplace=True)
                
                # Merge the two delta dataframes
                combined_df = pd.merge(minus_delta_df, plus_delta_df, on=['section' ,'metric', 'self'])
                # Reorder columns for clarity
                combined_df = combined_df[['section', 'metric', 'delta_minus', 'minus', 'self', 'plus', 'delta_plus']]

                # Add a zero-th row for the variable change
                variable_change_row: dict[str, Any] = {
                    'section': 'variable_change',
                    'metric': variable,
                    'delta_minus': '-1',
                    'minus': minus[variable],
                    'self': zero[variable],
                    'plus': plus[variable],
                    'delta_plus': '+1'
                }
                combined_df = pd.concat([pd.DataFrame([variable_change_row]), combined_df], ignore_index=True)
                combined_df = combined_df[(combined_df['section'] == 'variable_change') | 
                                          (combined_df['metric'] == 'total_cost') | 
                                          (combined_df['metric'] == 'avg_waiting_time') |
                                          (combined_df['metric'] == 'doctor_utilization') |
                                          (combined_df['metric'] == 'patients_waiting_over_15min')]
                print(combined_df.iloc[:, 1:])

        elif variable == "cost_params":
            # Sensitivity summary for cost_params
            original_total_cost = 0.0
            for mult in [1.0, 0.5, 0.75, 1.25, 1.5, 1.75, 2.0]: # start with 1.0 for reference
                if mult == 1.0:
                    for res in analysis_results:
                        if res['multiplier'] == 1.0:
                            original_total_cost = res['total_cost']
                            break # checking once is enough
                    continue
                print(f"\n--- Multiplier: {mult} ---")
                rows = [res for res in analysis_results if res['multiplier'] == mult]
                df = pd.DataFrame(rows)
                df = df[['variable', 'variable_cost', 'total_cost']]
                df['change_in_total_cost'] = df['total_cost'] - original_total_cost
                df['change_percentage'] = df['change_in_total_cost'] / original_total_cost * 100

                # Some basic formatting
                df['variable_cost'] = [f"-${-x:,.2f}" if x < 0 else f"${x:,.2f}" for x in df['variable_cost']]
                df['total_cost'] = [f"-${-x:,.2f}" if x < 0 else f"${x:,.2f}" for x in df['total_cost']]
                df['change_in_total_cost'] = [f"-${-x:,.2f}" if x < 0 else f"${x:,.2f}" for x in df['change_in_total_cost']]
                df['change_percentage'] = [f"{x:.2f}%" if x < 0 else f"+{x:.2f}%" for x in df["change_percentage"]]
                print(df)

        print("\n" + "="*width)
        footer = "END OF SENSITIVITY ANALYSIS SUMMARY"
        print(" " * ((width - len(footer))//2) + footer)
        print("="*width + "\n")
