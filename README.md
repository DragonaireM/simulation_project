# Clinic Appointment Scheduling Optimization

A Monte Carlo simulation-based optimization framework for healthcare appointment scheduling, featuring variance reduction techniques and comprehensive cost analysis.

## Overview

This project simulates and optimizes clinic appointment scheduling to minimize total operational costs while balancing:
- **Doctor idle time** (underutilization)
- **Patient waiting time** (service quality)
- **Doctor overtime** (overwork)

The system uses **Monte Carlo simulation** with **10,000 runs** to account for stochastic patient arrivals and service times, and employs **control variates** for variance reduction.

### Problem Context

Real-world clinic scheduling faces uncertainty:
- Patients may arrive early or late (unpunctuality)
- Service times vary between patients
- Balancing efficiency vs. patient satisfaction is challenging

This tool helps clinic managers find optimal scheduling parameters through simulation.

---

## Features

### Core Capabilities
- ✅ **Stochastic Simulation**: Models patient unpunctuality and variable service times
- ✅ **Optimization**: Finds optimal appointment intervals, service times, or cost parameters
- ✅ **Variance Reduction**: Control variates reduce estimation variance by 23-73%
- ✅ **Sensitivity Analysis**: Analyzes robustness to parameter changes
- ✅ **Cost Analysis**: Multi-objective cost function with configurable weights
- ✅ **Visualization**: Queue evolution, Gantt charts, cost breakdowns, trade-off curves
- ✅ **Database Export**: Saves detailed simulation results to SQLite

### Statistical Methods
- **Two-Stage Control Variates**: Unbiased variance reduction
- **Truncated Normal Distribution**: Models patient unpunctuality with realistic bounds
- **Lognormal Distribution**: Models service time variability (CV = 0.325)
- **Pilot Run Methodology**: Eliminates data snooping bias

---

## Installation

### Prerequisites
- Python 3.11+
- Required packages:
  ```bash
  pip install numpy pandas matplotlib seaborn scipy tqdm
  ```

### Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If provided
   # OR install manually:
   pip install numpy pandas matplotlib seaborn scipy tqdm
   ```
3. Run script :
   ```bash
   python main.py
   ```

---


**Last Updated**: 2025-01-08
