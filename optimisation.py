from simulation import Simulation
from distribution import Lognormal, TruncatedNormal
from typing import Any

class Optimisation:
    def __init__(self, range: tuple[int, int]=(-5, 5), working_hours: float=10.0, mean_service_time: float=25.0, number_of_doctors: int=1, number_of_runs: int=10000, scheduled_arrival: float=17.0, cost_params: tuple[float, float, float, float]=(4.0, 0.8, 6.0, 4.0), seed: int | None = None) -> None:
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
            "working_hours": [],
            "2d": []
        }
        self.summary: dict[str, list[dict[str, Any]]] = {
            "scheduled_arrival": [],
            "mean_service_time": [],
            "working_hours": [],
            "2d": []
        }

    def optimise_for(self, variable: str) -> None:
        """
        Optimize the simulation for a specific variable by adjusting its value
        within the defined range and observing the impact on key performance metrics.
        """
        for value in range(self.range[0], self.range[1] + 1):
            sim = Simulation(
                working_hours=self.working_hours,
                scheduled_arrival=self.scheduled_arrival,
                mean_service_time=self.mean_service_time,
                doctors=self.number_of_doctors,
                iat_distr=TruncatedNormal(),
                service_distr=Lognormal(desired_mean=self.mean_service_time, desired_std=self.mean_service_time * 0.5),
                cost_params=self.cost_params,
                seed=self.seed
            )

            # Adjust the specified variable
            if variable == "scheduled_arrival":
                sim.scheduled_arrival += value
            elif variable == "mean_service_time":
                # This also affects the service distribution
                sim.mean_service_time += value
                sim.service_distribution = Lognormal(desired_mean=sim.mean_service_time, desired_std=sim.mean_service_time * 0.5)
            elif variable == "working_hours":
                sim.working_hours += value
            else:
                raise ValueError(f"Unknown variable '{variable}' for optimisation.")

            # Run the simulation
            sim.simulate(number_of_runs=self.number_of_runs)
            self.simulations[variable].append(sim)
            self.summary[variable].append(sim.summary())

            # Display progress
            print(f"Optimisation for {variable}: set to {getattr(sim, variable)} completed.")

    def optimal_value(self, variable: str) -> tuple[Any, float]:
        """
        Determine the optimal value of the specified variable that minimizes total cost.
        """
        simulations = self.simulations[variable]
        if not simulations:
            raise RuntimeError(f"No simulations found for variable '{variable}'. Run optimise_for() first.")

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

    def optimise_2d(self, fixed_var: str, var_to_opt: str, fixed_var_range: tuple[int, int]) -> None:
        """
        Perform a 2D optimisation by fixing one variable and optimising another
        across a specified range.
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
            return
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
            for sim in selected_sims:
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
                print(f"  Average server idle time:     {s['averages']['average_server_idle_time']:>12.4f} minutes")
                print(f"  Average patient waiting time: {s['averages']['average_patient_waiting_time']:>12.4f} minutes")
                print(f"  Average server overtime:      {s['averages']['average_server_overtime']:>12.4f} minutes")
                print(f"  Total Cost:                   ${s['averages']['Total Cost']:>12.2f}")

                # Print Patient Metrics Table
                print("\nPATIENT METRICS (MINUTES):")
                print(f"  Avg waiting time:             {s['patient_metrics']['avg_waiting_time']:>12.4f} minutes")
                print(f"  Max waiting time:             {s['patient_metrics']['max_waiting_time']:>12.4f} minutes")
                print(f"  Std dev waiting time:         {s['patient_metrics']['std_waiting_time']:>12.4f} minutes")
                print(f"  95th percentile:              {s['patient_metrics']['waiting_time_95th_percentile']:>12.4f} minutes")
                print(f"  Patients waiting > 15 min:    {s['patient_metrics']['patients_waiting_over_15min']:>12}")
                print(f"  Percentage waiting > 15 min:  {s['patient_metrics']['percentage_waiting_over_15min']:>12.2f}%")

                # Run control variate comparison (this will take some time)
                print(f"\n  Running control variate comparison with 1000 runs...")
                comparison = sim.compare_variance_reduction(num_runs=1000, base_seed=sim.seed)

                # Print control variate results
                print("\n  CONTROL VARIATE COMPARISON:")
                print(f"    Standard MC:")
                print(f"      Mean waiting time:          {comparison['standard_mc']['mean_waiting_time']:>12.6f} minutes")
                print(f"      Variance:                   {comparison['standard_mc']['variance']:>12.6f}")
                print(f"      Standard error:             {comparison['standard_mc']['std_error']:>12.6f}")
                print(f"\n    With Control Variates:")
                print(f"      Mean waiting time:          {comparison['control_variates']['mean_waiting_time']:>12.6f} minutes")
                print(f"      Variance:                   {comparison['control_variates']['variance']:>12.6f}")
                print(f"      Standard error:             {comparison['control_variates']['std_error']:>12.6f}")
                print(f"\n    Variance Reduction:           {comparison['variance_reduction_percent']:>12.2f}%")
                print(f"    Efficiency Gain:              {comparison['efficiency_gain']:>12.2f}x")

        print("\n" + "="*80)
        print("END OF SUMMARY")
        print("="*80 + "\n")

    def sensitivity_analysis(self, variable: str, range: tuple[float, float], decimal_places: int) -> list[dict[str, Any]]:
        """
        Perform sensitivity analysis on the specified variable by examining how changes
        in that variable affect key performance metrics across the simulations.

        Returns a list of dictionaries containing the variable value and corresponding metrics.
        """
        raise NotImplementedError("Sensitivity analysis method is not yet implemented.")
