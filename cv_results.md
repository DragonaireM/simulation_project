================================================================================
SIMPLE COMPARISON: Control Variates vs Standard Monte Carlo
================================================================================

Running comparison with 100 simulation runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)

STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 21.994907 hours
Variance of mean waiting times: 431.091438
Standard error: 20.762742
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.122836
Average W-S correlation: -0.079274
Average within-run variance reduction: -7.56%
Runs with negative correlation (good for CV): 71/100

Overall Statistics Across Runs:
  Original MC - Mean: 21.994907, Var: 431.091438
  Control Variates - Mean: 21.804865, Var: 413.603421
  Between-run variance reduction: 4.06%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 100
Base seed: 42

Standard Monte Carlo:
  Mean waiting time: 21.994907 hours
  Variance: 431.091438
  Standard error: 2.076274

Control Variates:
  Mean waiting time: 21.804865 hours
  Variance: 413.603421
  Standard error: 2.033724

Variance Reduction: 4.06%
Efficiency Gain: 1.04x
  (Control variates is equivalent to 1.04x more standard MC runs)
================================================================================


================================================================================
CHECKING RESULTS IN TERMINAL:
================================================================================

================================================================================
SIMULATION SUMMARY
================================================================================

Simulation Parameters:
  Number of runs: 10
  Working hours: 8.0 hours
  Mean service time: 12.0 minutes
  Number of doctors: 1

Patient Waiting Time Metrics (MINUTES):
  Average waiting time: 18.1593 minutes
  Max waiting time: 116.0689 minutes
  Std dev waiting time: 25.4460 minutes
  95th percentile: 73.3952 minutes
  Patients waiting > 15 min: 145

Server Metrics (MINUTES per session):
  Average idle time: 181.5808 minutes
  Average overtime: 139.7675 minutes

System Metrics:
  Doctor utilization: 7104.16%
  Average queue length: 1151.7944 patients
  Throughput: 0.0654 patients/minute

Total Cost: $3630.20

--------------------------------------------------------------------------------
CONTROL VARIATES VARIANCE REDUCTION
--------------------------------------------------------------------------------
  Control variable: Service Time (mean = 12.0 minutes)
  Variance reduction: 4.06%
  Efficiency gain: 1.04x
  Average correlation (W,S): -0.0793
  Average optimal coefficient: 0.122836

  Without Control Variates:
    Mean waiting time: 21.9949 minutes
    Variance: 431.091438

  With Control Variates:
    Mean waiting time: 21.8049 minutes
    Variance: 413.603421
================================================================================


================================================================================
KEY TAKEAWAYS:
================================================================================
Average Patient Waiting Time: 18.1593 minutes

Control Variate Results:
  Without CV: 21.9949 minutes (variance: 431.0914)
  With CV:    21.8049 minutes (variance: 413.6034)
  Variance Reduction: 4.06%
  Efficiency Gain: 1.04x