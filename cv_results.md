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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 627.50it/s]
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -13.540385
    Idle time (c*):    -0.568004
    Overtime (c*):     -0.493402

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 71.0317
    Variance:            322.2220
    Std Error:             0.5676
  With Control Variates:
    Mean:                 70.8583
    Variance:            160.0224
    Std Error:             0.4000
  Variance Reduction:       50.34%
  Efficiency Gain:           2.01x

Idle Time (minutes):
  Standard MC:
    Mean:                  9.4603
    Variance:             71.1707
    Std Error:             0.2668
  With Control Variates:
    Mean:                 12.0071
    Variance:             68.2984
    Std Error:             0.2613
  Variance Reduction:        4.04%
  Efficiency Gain:           1.04x

Overtime (minutes):
  Standard MC:
    Mean:                 10.2439
    Variance:            295.1145
    Std Error:             0.5432
  With Control Variates:
    Mean:                 10.0544
    Variance:            101.2794
    Std Error:             0.3182
  Variance Reduction:       65.68%
  Efficiency Gain:           2.91x

Total Cost ($):
  Standard MC:
    Mean:                451.0163
    Variance:          17639.3392
    Std Error:             4.1999
  With Control Variates:
    Mean:                452.2386
    Variance:           7820.0578
    Std Error:             2.7964
  Variance Reduction:       55.67%
  Efficiency Gain:           2.26x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 676.13it/s] 
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -13.039916
    Idle time (c*):    -0.221590
    Overtime (c*):     -0.529316

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 59.0583
    Variance:            298.4984
    Std Error:             0.5464
  With Control Variates:
    Mean:                 58.8914
    Variance:            148.0673
    Std Error:             0.3848
  Variance Reduction:       50.40%
  Efficiency Gain:           2.02x

Idle Time (minutes):
  Standard MC:
    Mean:                 12.8127
    Variance:             79.5919
    Std Error:             0.2821
  With Control Variates:
    Mean:                 13.8062
    Variance:             79.1548
    Std Error:             0.2813
  Variance Reduction:        0.55%
  Efficiency Gain:           1.01x

Overtime (minutes):
  Standard MC:
    Mean:                 11.4496
    Variance:            325.0872
    Std Error:             0.5702
  With Control Variates:
    Mean:                 11.2463
    Variance:            102.0076
    Std Error:             0.3194
  Variance Reduction:       68.62%
  Efficiency Gain:           3.19x

Total Cost ($):
  Standard MC:
    Mean:                384.3370
    Variance:          16703.0605
    Std Error:             4.0869
  With Control Variates:
    Mean:                384.0239
    Variance:           7327.3431
    Std Error:             2.7069
  Variance Reduction:       56.13%
  Efficiency Gain:           2.28x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 869.81it/s] 
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -12.013741
    Idle time (c*):    0.586518
    Overtime (c*):     -0.576662

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 48.3755
    Variance:            252.1316
    Std Error:             0.5021
  With Control Variates:
    Mean:                 48.2217
    Variance:            124.4453
    Std Error:             0.3528
  Variance Reduction:       50.64%
  Efficiency Gain:           2.03x

Idle Time (minutes):
  Standard MC:
    Mean:                 18.6386
    Variance:             99.3890
    Std Error:             0.3153
  With Control Variates:
    Mean:                 16.0089
    Variance:             96.3265
    Std Error:             0.3104
  Variance Reduction:        3.08%
  Efficiency Gain:           1.03x

Overtime (minutes):
  Standard MC:
    Mean:                 13.4464
    Variance:            368.1234
    Std Error:             0.6067
  With Control Variates:
    Mean:                 13.2249
    Variance:            103.3508
    Std Error:             0.3215
  Variance Reduction:       71.92%
  Efficiency Gain:           3.56x

Total Cost ($):
  Standard MC:
    Mean:                329.0613
    Variance:          14504.8807
    Std Error:             3.8085
  With Control Variates:
    Mean:                325.1765
    Variance:           6259.7150
    Std Error:             2.5019
  Variance Reduction:       56.84%
  Efficiency Gain:           2.32x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 751.24it/s] 
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -10.346425
    Idle time (c*):    2.037852
    Overtime (c*):     -0.618066

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 39.4207
    Variance:            188.0387
    Std Error:             0.4336
  With Control Variates:
    Mean:                 39.2883
    Variance:             93.3346
    Std Error:             0.3055
  Variance Reduction:       50.36%
  Efficiency Gain:           2.01x

Idle Time (minutes):
  Standard MC:
    Mean:                 28.5414
    Variance:            160.4733
    Std Error:             0.4006
  With Control Variates:
    Mean:                 19.4045
    Variance:            123.5021
    Std Error:             0.3514
  Variance Reduction:       23.04%
  Efficiency Gain:           1.30x

Overtime (minutes):
  Standard MC:
    Mean:                 18.0661
    Variance:            412.2353
    Std Error:             0.6421
  With Control Variates:
    Mean:                 17.8287
    Variance:            108.0766
    Std Error:             0.3288
  Variance Reduction:       73.78%
  Efficiency Gain:           3.81x

Total Cost ($):
  Standard MC:
    Mean:                292.1650
    Variance:          10943.1920
    Std Error:             3.3080
  With Control Variates:
    Mean:                281.8772
    Variance:           4687.7866
    Std Error:             2.1651
  Variance Reduction:       57.16%
  Efficiency Gain:           2.33x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 783.93it/s]
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -8.428158
    Idle time (c*):    3.701303
    Overtime (c*):     -0.583499

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 32.1393
    Variance:            126.2942
    Std Error:             0.3554
  With Control Variates:
    Mean:                 32.0314
    Variance:             63.4517
    Std Error:             0.2519
  Variance Reduction:       49.76%
  Efficiency Gain:           1.99x

Idle Time (minutes):
  Standard MC:
    Mean:                 43.0255
    Variance:            292.2695
    Std Error:             0.5406
  With Control Variates:
    Mean:                 26.4303
    Variance:            170.3068
    Std Error:             0.4127
  Variance Reduction:       41.73%
  Efficiency Gain:           1.72x

Overtime (minutes):
  Standard MC:
    Mean:                 29.1829
    Variance:            429.7245
    Std Error:             0.6555
  With Control Variates:
    Mean:                 28.9588
    Variance:            158.6361
    Std Error:             0.3983
  Variance Reduction:       63.08%
  Efficiency Gain:           2.71x

Total Cost ($):
  Standard MC:
    Mean:                279.6355
    Variance:           7147.8728
    Std Error:             2.6736
  With Control Variates:
    Mean:                262.0568
    Variance:           3281.6541
    Std Error:             1.8115
  Variance Reduction:       54.09%
  Efficiency Gain:           2.18x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 797.21it/s] 
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -6.710350
    Idle time (c*):    5.104981
    Overtime (c*):     -0.468521

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 26.6598
    Variance:             81.3810
    Std Error:             0.2853
  With Control Variates:
    Mean:                 26.5738
    Variance:             41.5448
    Std Error:             0.2038
  Variance Reduction:       48.95%
  Efficiency Gain:           1.96x

Idle Time (minutes):
  Standard MC:
    Mean:                 62.5507
    Variance:            449.2084
    Std Error:             0.6702
  With Control Variates:
    Mean:                 39.6620
    Variance:            217.1987
    Std Error:             0.4660
  Variance Reduction:       51.65%
  Efficiency Gain:           2.07x

Overtime (minutes):
  Standard MC:
    Mean:                 47.9464
    Variance:            398.8200
    Std Error:             0.6315
  With Control Variates:
    Mean:                 47.7664
    Variance:            224.0409
    Std Error:             0.4733
  Variance Reduction:       43.82%
  Efficiency Gain:           1.78x

Total Cost ($):
  Standard MC:
    Mean:                294.4288
    Variance:           4390.2150
    Std Error:             2.0953
  With Control Variates:
    Mean:                270.7547
    Variance:           2460.3477
    Std Error:             1.5685
  Variance Reduction:       43.96%
  Efficiency Gain:           1.78x

================================================================================


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

  Running comprehensive control variate comparison with 1000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 1000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|██████████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 905.03it/s] 
Calculating optimal control variate coefficients...
  Optimal coefficients:
    Waiting time (c*): -5.374096
    Idle time (c*):    6.015520
    Overtime (c*):     -0.368710

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  Standard MC:
    Mean:                 22.5991
    Variance:             54.4743
    Std Error:             0.2334
  With Control Variates:
    Mean:                 22.5303
    Variance:             28.9238
    Std Error:             0.1701
  Variance Reduction:       46.90%
  Efficiency Gain:           1.88x

Idle Time (minutes):
  Standard MC:
    Mean:                 85.4804
    Variance:            579.1476
    Std Error:             0.7610
  With Control Variates:
    Mean:                 58.5092
    Variance:            256.9930
    Std Error:             0.5069
  Variance Reduction:       55.63%
  Efficiency Gain:           2.25x

Overtime (minutes):
  Standard MC:
    Mean:                 70.8645
    Variance:            370.0773
    Std Error:             0.6083
  With Control Variates:
    Mean:                 70.7229
    Variance:            261.8342
    Std Error:             0.5117
  Variance Reduction:       29.25%
  Efficiency Gain:           1.41x

Total Cost ($):
  Standard MC:
    Mean:                327.3714
    Variance:           3060.5933
    Std Error:             1.7495
  With Control Variates:
    Mean:                299.7750
    Variance:           2156.3551
    Std Error:             1.4685
  Variance Reduction:       29.54%
  Efficiency Gain:           1.42x

================================================================================


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
