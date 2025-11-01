from visualisation import ClinicVisualization
from optimisation import Optimisation
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # CONSTANT VARIABLES (Only modify if exploring different scenarios)
    WORKING_HOURS = 8.0  # hours
    SCHEDULED_ARRIVAL = 15 # minutes - how long the appointment slots are spaced apart
    MEAN_SERVICE_TIME = 15.5 # minutes
    NUMBER_OF_DOCTORS = 1

    # Change to 1000 if doing 2D optimisation to reduce computation time
    NUMBER_OF_RUNS = 10000

    # RANGE FOR OPTIMISATION
    # NOTE: Adjust RANGE and VARIABLE to explore different optimisation scenarios
    #       Make sure VARIABLE + RANGE make sense together (e.g., don't set negative service times)
    #       Inclusive of start and end values
    RANGE = (-3, 3)

    # Cost parameters: (idle_cost/min, waiting_cost/min/patient, overtime_cost/min, labor_cost/min/doctor)
    # Labor cost parameter currently not used, hence set to 0.0
    COST_PARAMS = (1.0, 0.2, 1.5, 0.0)  # idle, waiting, overtime, labor costs

    # TO OPTIMIZE FOR: (SELECT ONE OUT OF THREE)
    # "scheduled_arrival"
    # "mean_service_time"
    # "working_hours"
    VARIABLE = "scheduled_arrival"
    SENSITIVITY_ANALYSIS = True  # Set to True to perform sensitivity analysis around optimal value

    # SAVE TO DATABASE --- OPTIONAL ---
    # Turned off by default, change to True to enable saving
    # DB: saves summary metrics to SQLite database
    # PNG: saves visualizations as PNG files
    #
    # NOTE: Saving to DB will warn you how much space the database file takes
    #       A confirmation prompt will appear before proceeding with the save
    SAVE_TO_DB = False
    SAVE_TO_PNG = False

    # SETTING SEED FOR REPRODUCIBILITY
    # Set to None for random behavior
    SEED = 0

    # TO BE IMPLEMENTED LATER
    # QUEUE_CAPACITY = 5  # patients

    ### END OF CONSTANTS ###

    # Initialize optimisation model
    model = Optimisation(
        range=RANGE,
        working_hours=WORKING_HOURS,
        mean_service_time=MEAN_SERVICE_TIME,
        number_of_doctors=NUMBER_OF_DOCTORS,
        number_of_runs=NUMBER_OF_RUNS,
        scheduled_arrival=SCHEDULED_ARRIVAL,
        cost_params=COST_PARAMS,
        seed=SEED
    )

    # Run full optimisation to get all metrics
    # Choose between normal 1D optimisation (recommended)
    # or 
    # 2D optimisation (proceed with caution)
    # D = 1 or 2
    D = 1
    if D == 1:
        model.optimise_for(variable=VARIABLE)

        if SENSITIVITY_ANALYSIS:
            opt_sim = model.optimal_solution(variable=VARIABLE)
            analysis_results = model.sensitivity_analysis(
                optimal_solution=opt_sim,
                variable=VARIABLE
            )
            model.sensitivity_summary(analysis_results, variable=VARIABLE)

        # Save results to database if enabled
        if SAVE_TO_DB:
            model.save_summary_to_db(db_path=f"out/seed{SEED}/opt_{VARIABLE}", print_summary=False)

        # Initialize visualizations
        viz1 = ClinicVisualization(model.simulations[VARIABLE])

        # List of plots to choose from

        # 1. Cost against variable value 
        viz1.plot_cost_against_variable(variable=VARIABLE)
        #    VARIABLE and RANGE affect this plot
        #    RANGE should have a distance of at least 2 to make a meaningful comparison

        # 2. Queue evolution 
        # -> viz1.plot_queue_evolution(schedule_index=0)
        #    Choose any schedule_index from 0 to NUMBER_OF_RUNS-1
        #    RANGE doesn't affect this plot

        # 3. Schedule Gantt chart 
        # viz1.plot_schedule_gantt(schedule_index=0)
        #    Choose any schedule_index from 0 to NUMBER_OF_RUNS-1
        #    RANGE doesn't affect this plot

        # 4. Cost comparison stacked bar chart
        # viz1.plot_cost_comparison()
        #    RANGE should have a distance of at least 2 to make a meaningful comparison

        # 5. Cost breakdown pie chart
        # viz1.plot_cost_breakdown()
        #    RANGE doesn't affect this plot

        # 6. Waiting time histogram
        # viz1.plot_waiting_time_distribution()
        #    RANGE doesn't affect this plot

        # 7. Waiting time vs Utilization trade-off
        # -> viz1.plot_tradeoff_analysis()
        #    RANGE should have a distance of at least 2 to make a meaningful comparison

        # plt.show() # Uncomment to display plots interactively

        if SAVE_TO_PNG:
            viz1.save_plots(f"out/seed{SEED}/simulation_plot/img")

    elif D == 2:
        # Change the function parameters to your liking (with caution)
        FIXED_VAR = "mean_service_time"
        model.optimise_2d(fixed_var=FIXED_VAR, 
                          var_to_opt=VARIABLE, 
                          fixed_var_range=(-5, 6))

        viz2 = ClinicVisualization(model.simulations["2d"])

        ClinicVisualization.plot_2d_relationship(
            fixed_vars=model.results_2d["fixed_vars"],
            opt_vars=model.results_2d["opt_vars"],
            opt_costs=model.results_2d["opt_costs"],
            fixed_var=FIXED_VAR,
            var_to_opt=VARIABLE,
        )

        # plt.show() # Uncomment to display plots interactively

        if SAVE_TO_PNG:
            viz2.save_plots(f"out/seed{SEED}/opt_2d_{FIXED_VAR}_vs_{VARIABLE}/img")
