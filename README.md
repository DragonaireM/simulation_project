# simulation_project

Brief: simulation code and optimisation tools for clinic scheduling experiments (queueing + variance reduction + simple visualisation).  
This README explains how to set up a reproducible environment, run the code, change parameters, save results and use the visualisations.

---

## Contents
- `main.py` — example entrypoint that runs optimisation and optionally saves results / plots.  
- `simulation.py` — Simulation class + CV experiments, DB export helpers.  
- `optimisation.py` — Optimisation wrapper (runs `Simulation` over parameter ranges).  
- `schedule.py` / `markov.py` — schedule construction and Markov-chain helpers.  
- `distribution.py` — distribution classes (Lognormal, TruncatedNormal, etc.).  
- `visualisation.py` — plotting helpers using matplotlib.  
- `summary.py` — lightweight summary object used for storing metrics and DataFrames.  
- `requirements.txt` — pinned Python dependencies.  
- `out/` — output directory (not committed) where DB and PNGs are written by default.

---

## Quick start (macOS)
1. Clone the repo (or pull from GitHub):

`git clone https://github.com/DragonaireM/simulation_project.git`

`cd simulation_project`

2. Create & activate a virtualenv:

`python3 -m venv .venv`

`source .venv/bin/activate`

3. Install dependencies (from `requirements.txt`):

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

4. Run the example entrypoint:

`python main.py`

`main.py` runs the optimisation configured in the constants at the top of the file. It prints summaries and (optionally) writes a SQLite DB + PNGs under `out/`.

---

## Quick start (Windows)
1. Clone the repo:

`git clone https://github.com/DragonaireM/simulation_project.git`

`cd simulation project`

2. Create and activate a virtualenv:
`py -3 -m venv .venv` or 
`python -m venv .venv`

3. Activate the venv (pick one):
- PowerShell (preferred):
    - `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force`
    - `.venv\Scripts\Activate.ps1`

- Command prompt (cmd.exe):
`.venv\Scripts\activate.bat`

- Git Bash:
`source .venv/Scripts/activate`

4. Install dependencies:
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`

or if you prefer the py launcher:
`py -3 -m pip install - r requirements.txt`

5. Run the project
`python main.py` or `py -3 main.py`

## Key configurable parameters
Open `main.py` and edit the constants near top:

- `WORKING_HOURS` (float) — session length in hours (default `8.0`).
- `SCHEDULED_ARRIVAL` (int/float) — minutes between scheduled appointments (default `15`).
- `MEAN_SERVICE_TIME` (float) — mean service duration in minutes (default `15.5`).
- `NUMBER_OF_DOCTORS` (int) — number of parallel servers (default `1`).
- `NUMBER_OF_RUNS` (int) — simulation repetitions per configuration (large values -> long runtime).
- `RANGE` (tuple) — integer offsets used by `Optimisation.optimise_for`.
- `COST_PARAMS` (tuple) — (idle_cost_per_min, waiting_cost_per_min_per_patient, overtime_cost_per_min).
- `VARIABLE` — which variable to optimise: `"scheduled_arrival"`, `"mean_service_time"`, or `"cost_params"`.
- `SAVE_TO_DB`, `SAVE_TO_PNG` — toggles for outputs.
- `SEED` — integer or `None` for reproducibility.

You can also call the classes directly from a Python REPL / notebook:
```python
from optimisation import Optimisation
model = Optimisation(range=(-3,3), number_of_runs=1000, ...)
model.optimise_for("scheduled_arrival")
best_sim = model.optimal_solution("scheduled_arrival")
```
---

## Running faster / scaling tips
- Reduce `NUMBER_OF_RUNS` for quick tests. Use larger values for final results.
- Consider reducing `number_of_runs` during development, then scale up for submission.
- Use `tqdm` progress bars are present for long loops.

---

## Saving outputs & file layout
When `save_summary_to_db` / `write_summaries_to_sqlite` is used, DB files are written under the `out/` path you pass, e.g.:
`out/seed0/opt_scheduled_arrival/<simulation_identifier>.db`

Each DB contains:
- `averages` (table of average metrics)
- `patient_metrics`
- `system_metrics`
- `schedule_run_1`, `schedule_run_2`, ... (one table per saved schedule run)

PNG visualisations are saved to:
`out/seed{SEED}/simulation_plot/{VARIABLE}/img_<n>.png`

---

## Formatting, rounding & presentation
Internal computations keep full float precision; many outputs and DataFrames are rounded to 6 decimals before saving to DB and formatted for printing (see `Schedule.to_dataframe()` and `Simulation.write_summaries_to_sqlite()`).
For display only, use pandas `.style.format(...)` or Python format strings (e.g. `f"${value:,.2f}"`).