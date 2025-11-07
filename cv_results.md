Run at 7 Nov, 2:55 p.m. 
Simulating progress: 100%|██████████████████████████████████████████████████████████████████████████████| 7/7 [00:35<00:00,  5.00s/it]

================================================================================
SIMULATION SUMMARY - SAVED RESULTS
================================================================================

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 12/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:           9.5447 minutes
  Average patient waiting time:      71.2485 minutes
  Average server overtime:            9.7875 minutes
  Total Cost:                   $      451.72

PATIENT METRICS (MINUTES):
  Avg waiting time:                  71.2485 minutes
  Max waiting time:                 268.0984 minutes
  Std dev waiting time:              42.7844 minutes
  95th percentile:                  144.2056 minutes
  Patients waiting > 15 min:        266954.0
  Percentage waiting > 15 min:         88.98%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1009.97it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 71.031672 hours
Variance of mean waiting times: 322.222027
Standard error: 17.950544
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 534.32it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 3.441893
Average W-S correlation: -0.441759
Average within-run variance reduction: -66.27%
Runs with negative correlation (good for CV): 993/1000

Overall Statistics Across Runs:
  Original MC - Mean: 71.031672, Var: 322.222027
  Control Variates - Mean: 71.043144, Var: 248.933783
  Between-run variance reduction: 22.74%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 71.031672 hours
  Variance: 322.222027
  Standard error: 0.567646

Control Variates:
  Mean waiting time: 71.043144 hours
  Variance: 248.933783
  Standard error: 0.498933

Variance Reduction: 22.74%
Efficiency Gain: 1.29x
  (Control variates is equivalent to 1.29x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             71.031672 minutes
      Variance:                     322.222027
      Standard error:                 0.567646

    With Control Variates:
      Mean waiting time:             71.043144 minutes
      Variance:                     248.933783
      Standard error:                 0.498933

    Variance Reduction:                  22.74%
    Efficiency Gain:                      1.29x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 13/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          13.0015 minutes
  Average patient waiting time:      59.3488 minutes
  Average server overtime:           11.0164 minutes
  Total Cost:                   $      385.62

PATIENT METRICS (MINUTES):
  Avg waiting time:                  59.3488 minutes
  Max waiting time:                 239.0984 minutes
  Std dev waiting time:              36.8078 minutes
  95th percentile:                  122.6694 minutes
  Patients waiting > 15 min:        259830.0
  Percentage waiting > 15 min:         86.61%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1022.85it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 59.058320 hours
Variance of mean waiting times: 298.498355
Standard error: 17.277105
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 530.03it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 3.390432
Average W-S correlation: -0.531131
Average within-run variance reduction: -93.07%
Runs with negative correlation (good for CV): 997/1000

Overall Statistics Across Runs:
  Original MC - Mean: 59.058320, Var: 298.498355
  Control Variates - Mean: 59.042000, Var: 229.090615
  Between-run variance reduction: 23.25%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 59.058320 hours
  Variance: 298.498355
  Standard error: 0.546350

Control Variates:
  Mean waiting time: 59.042000 hours
  Variance: 229.090615
  Standard error: 0.478634

Variance Reduction: 23.25%
Efficiency Gain: 1.30x
  (Control variates is equivalent to 1.30x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             59.058320 minutes
      Variance:                     298.498355
      Standard error:                 0.546350

    With Control Variates:
      Mean waiting time:             59.042000 minutes
      Variance:                     229.090615
      Standard error:                 0.478634

    Variance Reduction:                  23.25%
    Efficiency Gain:                      1.30x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 14/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          18.8297 minutes
  Average patient waiting time:      48.7013 minutes
  Average server overtime:           13.1387 minutes
  Total Cost:                   $      330.75

PATIENT METRICS (MINUTES):
  Avg waiting time:                  48.7013 minutes
  Max waiting time:                 210.0984 minutes
  Std dev waiting time:              31.6488 minutes
  95th percentile:                  103.1356 minutes
  Patients waiting > 15 min:        248951.0
  Percentage waiting > 15 min:         82.98%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1067.90it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 48.375510 hours
Variance of mean waiting times: 252.131643
Standard error: 15.878654
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 522.94it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 3.286178
Average W-S correlation: -0.615925
Average within-run variance reduction: -123.06%
Runs with negative correlation (good for CV): 999/1000

Overall Statistics Across Runs:
  Original MC - Mean: 48.375510, Var: 252.131643
  Control Variates - Mean: 48.306736, Var: 190.937275
  Between-run variance reduction: 24.27%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 48.375510 hours
  Variance: 252.131643
  Standard error: 0.502127

Control Variates:
  Mean waiting time: 48.306736 hours
  Variance: 190.937275
  Standard error: 0.436964

Variance Reduction: 24.27%
Efficiency Gain: 1.32x
  (Control variates is equivalent to 1.32x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             48.375510 minutes
      Variance:                     252.131643
      Standard error:                 0.502127

    With Control Variates:
      Mean waiting time:             48.306736 minutes
      Variance:                     190.937275
      Standard error:                 0.436964

    Variance Reduction:                  24.27%
    Efficiency Gain:                      1.32x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 15/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          28.3802 minutes
  Average patient waiting time:      39.6290 minutes
  Average server overtime:           17.8368 minutes
  Total Cost:                   $      292.91

PATIENT METRICS (MINUTES):
  Avg waiting time:                  39.6290 minutes
  Max waiting time:                 188.1913 minutes
  Std dev waiting time:              27.4325 minutes
  95th percentile:                   86.6751 minutes
  Patients waiting > 15 min:        233362.0
  Percentage waiting > 15 min:         77.79%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|████████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 970.98it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 39.420733 hours
Variance of mean waiting times: 188.038680
Standard error: 13.712720
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 533.56it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 3.114833
Average W-S correlation: -0.667736
Average within-run variance reduction: -142.60%
Runs with negative correlation (good for CV): 999/1000

Overall Statistics Across Runs:
  Original MC - Mean: 39.420733, Var: 188.038680
  Control Variates - Mean: 39.278790, Var: 139.487282
  Between-run variance reduction: 25.82%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 39.420733 hours
  Variance: 188.038680
  Standard error: 0.433634

Control Variates:
  Mean waiting time: 39.278790 hours
  Variance: 139.487282
  Standard error: 0.373480

Variance Reduction: 25.82%
Efficiency Gain: 1.35x
  (Control variates is equivalent to 1.35x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             39.420733 minutes
      Variance:                     188.038680
      Standard error:                 0.433634

    With Control Variates:
      Mean waiting time:             39.278790 minutes
      Variance:                     139.487282
      Standard error:                 0.373480

    Variance Reduction:                  25.82%
    Efficiency Gain:                      1.35x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 16/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          42.8146 minutes
  Average patient waiting time:      32.3341 minutes
  Average server overtime:           28.8831 minutes
  Total Cost:                   $      280.14

PATIENT METRICS (MINUTES):
  Avg waiting time:                  32.3341 minutes
  Max waiting time:                 167.1913 minutes
  Std dev waiting time:              24.2408 minutes
  95th percentile:                   74.6211 minutes
  Patients waiting > 15 min:        213767.0
  Percentage waiting > 15 min:         71.26%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1011.19it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 32.139280 hours
Variance of mean waiting times: 126.294219
Standard error: 11.238070
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 506.55it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 2.887460
Average W-S correlation: -0.677512
Average within-run variance reduction: -145.51%
Runs with negative correlation (good for CV): 1000/1000

Overall Statistics Across Runs:
  Original MC - Mean: 32.139280, Var: 126.294219
  Control Variates - Mean: 31.936012, Var: 91.052792
  Between-run variance reduction: 27.90%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 32.139280 hours
  Variance: 126.294219
  Standard error: 0.355379

Control Variates:
  Mean waiting time: 31.936012 hours
  Variance: 91.052792
  Standard error: 0.301750

Variance Reduction: 27.90%
Efficiency Gain: 1.39x
  (Control variates is equivalent to 1.39x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             32.139280 minutes
      Variance:                     126.294219
      Standard error:                 0.355379

    With Control Variates:
      Mean waiting time:             31.936012 minutes
      Variance:                      91.052792
      Standard error:                 0.301750

    Variance Reduction:                  27.90%
    Efficiency Gain:                      1.39x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 17/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          62.1483 minutes
  Average patient waiting time:      26.8225 minutes
  Average server overtime:           47.5030 minutes
  Total Cost:                   $      294.34

PATIENT METRICS (MINUTES):
  Avg waiting time:                  26.8225 minutes
  Max waiting time:                 146.1913 minutes
  Std dev waiting time:              21.9932 minutes
  95th percentile:                   66.3740 minutes
  Patients waiting > 15 min:        192282.0
  Percentage waiting > 15 min:         64.09%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1032.19it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 26.659757 hours
Variance of mean waiting times: 81.381024
Standard error: 9.021143
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:02<00:00, 488.80it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 2.639033
Average W-S correlation: -0.658880
Average within-run variance reduction: -137.12%
Runs with negative correlation (good for CV): 1000/1000

Overall Statistics Across Runs:
  Original MC - Mean: 26.659757, Var: 81.381024
  Control Variates - Mean: 26.429589, Var: 56.815310
  Between-run variance reduction: 30.19%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 26.659757 hours
  Variance: 81.381024
  Standard error: 0.285274

Control Variates:
  Mean waiting time: 26.429589 hours
  Variance: 56.815310
  Standard error: 0.238360

Variance Reduction: 30.19%
Efficiency Gain: 1.43x
  (Control variates is equivalent to 1.43x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             26.659757 minutes
      Variance:                      81.381024
      Standard error:                 0.285274

    With Control Variates:
      Mean waiting time:             26.429589 minutes
      Variance:                      56.815310
      Standard error:                 0.238360

    Variance Reduction:                  30.19%
    Efficiency Gain:                      1.43x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 18/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          85.0993 minutes
  Average patient waiting time:      22.7635 minutes
  Average server overtime:           70.4406 minutes
  Total Cost:                   $      327.34

PATIENT METRICS (MINUTES):
  Avg waiting time:                  22.7635 minutes
  Max waiting time:                 126.6038 minutes
  Std dev waiting time:              20.4120 minutes
  95th percentile:                   60.5538 minutes
  Patients waiting > 15 min:        172104.0
  Percentage waiting > 15 min:         57.37%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1037.94it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 22.599057 hours
Variance of mean waiting times: 54.474277
Standard error: 7.380669
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 15.5000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 573.37it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 2.404691
Average W-S correlation: -0.631042
Average within-run variance reduction: -125.79%
Runs with negative correlation (good for CV): 1000/1000

Overall Statistics Across Runs:
  Original MC - Mean: 22.599057, Var: 54.474277
  Control Variates - Mean: 22.366224, Var: 37.372434
  Between-run variance reduction: 31.39%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 22.599057 hours
  Variance: 54.474277
  Standard error: 0.233397

Control Variates:
  Mean waiting time: 22.366224 hours
  Variance: 37.372434
  Standard error: 0.193320

Variance Reduction: 31.39%
Efficiency Gain: 1.46x
  (Control variates is equivalent to 1.46x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             22.599057 minutes
      Variance:                      54.474277
      Standard error:                 0.233397

    With Control Variates:
      Mean waiting time:             22.366224 minutes
      Variance:                      37.372434
      Standard error:                 0.193320

    Variance Reduction:                  31.39%
    Efficiency Gain:                      1.46x

================================================================================
END OF SUMMARY
================================================================================


================================================================================
               SENSITIVITY ANALYSIS SUMMARY FOR SCHEDULED_ARRIVAL
================================================================================

--- Below Optimal Scheduled Arrival ---
                           metric delta_minus          minus           self           plus delta_plus
0               scheduled_arrival          -1      13.000000      14.000000      15.000000         +1
1            avg_server_idle_time   -5.828137      13.001531      18.829668      28.380247   9.550579
2        avg_patient_waiting_time   10.647514      59.348765      48.701252      39.628968  -9.072284
3             avg_server_overtime    -2.12229      11.016418      13.138707      17.836825   4.698118
4                      total_cost    54.87351     385.618751     330.745241     292.909294 -37.835947
5                avg_waiting_time   10.647514      59.348765      48.701252      39.628968  -9.072284
6                max_waiting_time        29.0     239.098378     210.098378     188.191322 -21.907057
7                std_waiting_time    5.158939      36.807758      31.648819      27.432483  -4.216336
8     patients_waiting_over_15min     10879.0  259830.000000  248951.000000  233362.000000   -15589.0
9   percentage_waiting_over_15min    3.626333      86.610000      82.983667      77.787333  -5.196333
10   waiting_time_95th_percentile   19.533762     122.669403     103.135641      86.675107 -16.460534
11             doctor_utilization    1.192645      97.310316      96.117671      94.237666  -1.880004
12               avg_queue_length    0.678806       4.353405       3.674599       3.085767  -0.588831
13                     throughput    0.000793       0.062954       0.062161       0.060912  -0.001249

--- At Optimal Scheduled Arrival ---
                           metric delta_minus          minus           self           plus delta_plus
0               scheduled_arrival          -1      15.000000      16.000000      17.000000         +1
1            avg_server_idle_time  -14.434317      28.380247      42.814564      62.148339  19.333775
2        avg_patient_waiting_time    7.294819      39.628968      32.334149      26.822499  -5.511651
3             avg_server_overtime  -11.046293      17.836825      28.883119      47.503022  18.619903
4                      total_cost   12.765157     292.909294     280.144137     294.337863  14.193726
5                avg_waiting_time    7.294819      39.628968      32.334149      26.822499  -5.511651
6                max_waiting_time        21.0     188.191322     167.191322     146.191322      -21.0
7                std_waiting_time    3.191731      27.432483      24.240751      21.993181   -2.24757
8     patients_waiting_over_15min     19595.0  233362.000000  213767.000000  192282.000000   -21485.0
9   percentage_waiting_over_15min    6.531667      77.787333      71.255667      64.094000  -7.161667
10   waiting_time_95th_percentile   12.053966      86.675107      74.621141      66.374045  -8.247096
11             doctor_utilization    2.680191      94.237666      91.557476      88.213616   -3.34386
12               avg_queue_length    0.487559       3.085767       2.598208       2.214337  -0.383871
13                     throughput     0.00177       0.060912       0.059143       0.056952  -0.002191

--- Above Optimal Scheduled Arrival ---
                           metric delta_minus          minus           self           plus delta_plus
0               scheduled_arrival          -1      17.000000      18.000000      19.000000         +1
1            avg_server_idle_time  -22.950913      62.148339      85.099252     110.148151  25.048899
2        avg_patient_waiting_time     4.05898      26.822499      22.763519      19.724581  -3.038937
3             avg_server_overtime  -22.937553      47.503022      70.440574      95.489474  25.048899
4                      total_cost  -33.003362     294.337863     327.341225     371.729850  44.388625
5                avg_waiting_time     4.05898      26.822499      22.763519      19.724581  -3.038937
6                max_waiting_time   19.587516     146.191322     126.603805     111.775033 -14.828772
7                std_waiting_time    1.581198      21.993181      20.411983      19.226803   -1.18518
8     patients_waiting_over_15min     20178.0  192282.000000  172104.000000  154183.000000   -17921.0
9   percentage_waiting_over_15min       6.726      64.094000      57.368000      51.394333  -5.973667
10   waiting_time_95th_percentile    5.820262      66.374045      60.553782      56.347173   -4.20661
11             doctor_utilization    3.665397      88.213616      84.548219      80.875266  -3.672953
12               avg_queue_length    0.294369       2.214337       1.919968       1.693244  -0.226724
13                     throughput    0.002385       0.056952       0.054566       0.052186  -0.002381

================================================================================
                      END OF SENSITIVITY ANALYSIS SUMMARY
================================================================================