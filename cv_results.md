================================================================================
SIMULATION SUMMARY - SAVED RESULTS
================================================================================

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 13/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:           2.6222 minutes
  Average patient waiting time:      38.8084 minutes
  Average server overtime:            6.4407 minutes
  Total Cost:                   $      245.13

PATIENT METRICS (MINUTES):
  Avg waiting time:                  38.8084 minutes
  Max waiting time:                 192.1901 minutes
  Std dev waiting time:              29.6960 minutes
  95th percentile:                   93.3680 minutes
  Patients waiting > 15 min:        221743.0
  Percentage waiting > 15 min:         73.91%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:21<00:00, 466.27it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -14.429551
    Idle time (c*):    -0.073829
    Overtime (c*):     -0.367430

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 38.8070
    Variance:            267.0767
    Std Error:             0.1827
  With Control Variates:
    Mean:                 38.6986
    Variance:             81.8731
    Std Error:             0.1012
  Variance Reduction:       69.34%
  Efficiency Gain:           3.26x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  2.5867
    Variance:             21.5729
    Std Error:             0.0519
  With Control Variates:
    Mean:                  2.5861
    Variance:             21.5520
    Std Error:             0.0519
  Variance Reduction:        0.10%
  Efficiency Gain:           1.00x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  6.4283
    Variance:            178.1847
    Std Error:             0.1492
  With Control Variates:
    Mean:                  6.3455
    Variance:             73.4908
    Std Error:             0.0958
  Variance Reduction:       58.76%
  Efficiency Gain:           2.42x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                245.0712
    Variance:          13051.5483
    Std Error:             1.2773
  With Control Variates:
    Mean:                244.2962
    Variance:           3621.3764
    Std Error:             0.6728
  Variance Reduction:       72.25%
  Efficiency Gain:           3.60x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 14/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:           6.6304 minutes
  Average patient waiting time:      27.1354 minutes
  Average server overtime:            7.4198 minutes
  Total Cost:                   $      180.57

PATIENT METRICS (MINUTES):
  Avg waiting time:                  27.1354 minutes
  Max waiting time:                 163.1901 minutes
  Std dev waiting time:              23.8156 minutes
  95th percentile:                   72.5328 minutes
  Patients waiting > 15 min:        185283.0
  Percentage waiting > 15 min:         61.76%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:23<00:00, 426.93it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -13.407883
    Idle time (c*):    0.549642
    Overtime (c*):     -0.399860

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 27.1573
    Variance:            236.3053
    Std Error:             0.1719
  With Control Variates:
    Mean:                 27.0566
    Variance:             78.3392
    Std Error:             0.0990
  Variance Reduction:       66.85%
  Efficiency Gain:           3.02x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  6.6275
    Variance:             60.9031
    Std Error:             0.0873
  With Control Variates:
    Mean:                  6.6318
    Variance:             57.6920
    Std Error:             0.0849
  Variance Reduction:        5.27%
  Efficiency Gain:           1.06x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  7.4047
    Variance:            203.0944
    Std Error:             0.1593
  With Control Variates:
    Mean:                  7.3146
    Variance:             80.1701
    Std Error:             0.1001
  Variance Reduction:       60.53%
  Efficiency Gain:           2.53x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                180.6785
    Variance:          11941.0892
    Std Error:             1.2217
  With Control Variates:
    Mean:                179.9435
    Variance:           3808.4210
    Std Error:             0.6900
  Variance Reduction:       68.11%
  Efficiency Gain:           3.14x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 15/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          15.9711 minutes
  Average patient waiting time:      18.2558 minutes
  Average server overtime:           10.2096 minutes
  Total Cost:                   $      140.82

PATIENT METRICS (MINUTES):
  Avg waiting time:                  18.2558 minutes
  Max waiting time:                 138.8081 minutes
  Std dev waiting time:              18.8326 minutes
  95th percentile:                   55.3299 minutes
  Patients waiting > 15 min:        140195.0
  Percentage waiting > 15 min:         46.73%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:24<00:00, 405.28it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -11.205598
    Idle time (c*):    1.993779
    Overtime (c*):     -0.456201

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 18.3052
    Variance:            174.1276
    Std Error:             0.1475
  With Control Variates:
    Mean:                 18.2210
    Variance:             65.6646
    Std Error:             0.0906
  Variance Reduction:       62.29%
  Efficiency Gain:           2.65x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 16.0148
    Variance:            161.5136
    Std Error:             0.1421
  With Control Variates:
    Mean:                 16.0304
    Variance:            122.2005
    Std Error:             0.1236
  Variance Reduction:       24.34%
  Efficiency Gain:           1.32x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 10.2157
    Variance:            251.4270
    Std Error:             0.1773
  With Control Variates:
    Mean:                 10.1129
    Variance:             92.8102
    Std Error:             0.1077
  Variance Reduction:       63.09%
  Efficiency Gain:           2.71x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                141.1695
    Variance:           9300.6735
    Std Error:             1.0782
  With Control Variates:
    Mean:                140.5260
    Variance:           3669.8628
    Std Error:             0.6773
  Variance Reduction:       60.54%
  Efficiency Gain:           2.53x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 16/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          31.7908 minutes
  Average patient waiting time:      12.4038 minutes
  Average server overtime:           19.1886 minutes
  Total Cost:                   $      135.00

PATIENT METRICS (MINUTES):
  Avg waiting time:                  12.4038 minutes
  Max waiting time:                 119.8081 minutes
  Std dev waiting time:              14.8854 minutes
  95th percentile:                   42.5693 minutes
  Patients waiting > 15 min:        100025.0
  Percentage waiting > 15 min:         33.34%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:22<00:00, 441.44it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -8.516888
    Idle time (c*):    3.809112
    Overtime (c*):     -0.499003

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 12.4484
    Variance:            108.4260
    Std Error:             0.1164
  With Control Variates:
    Mean:                 12.3845
    Variance:             45.8900
    Std Error:             0.0757
  Variance Reduction:       57.68%
  Efficiency Gain:           2.36x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 31.8005
    Variance:            321.9261
    Std Error:             0.2006
  With Control Variates:
    Mean:                 31.8303
    Variance:            186.9500
    Std Error:             0.1529
  Variance Reduction:       41.93%
  Efficiency Gain:           1.72x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 19.2054
    Variance:            336.1532
    Std Error:             0.2050
  With Control Variates:
    Mean:                 19.0930
    Variance:            147.2305
    Std Error:             0.1357
  Variance Reduction:       56.20%
  Efficiency Gain:           2.28x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                135.2994
    Variance:           6291.7539
    Std Error:             0.8868
  With Control Variates:
    Mean:                134.7767
    Variance:           3110.7211
    Std Error:             0.6236
  Variance Reduction:       50.56%
  Efficiency Gain:           2.02x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 17/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          52.9468 minutes
  Average patient waiting time:       8.8485 minutes
  Average server overtime:           38.3287 minutes
  Total Cost:                   $      163.53

PATIENT METRICS (MINUTES):
  Avg waiting time:                   8.8485 minutes
  Max waiting time:                 100.8081 minutes
  Std dev waiting time:              12.0731 minutes
  95th percentile:                   33.9929 minutes
  Patients waiting > 15 min:         71248.0
  Percentage waiting > 15 min:         23.75%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:23<00:00, 421.64it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -6.236388
    Idle time (c*):    5.200013
    Overtime (c*):     -0.439774

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  8.8693
    Variance:             61.6957
    Std Error:             0.0878
  With Control Variates:
    Mean:                  8.8224
    Variance:             28.3620
    Std Error:             0.0595
  Variance Reduction:       54.03%
  Efficiency Gain:           2.18x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 52.9074
    Variance:            487.3711
    Std Error:             0.2468
  With Control Variates:
    Mean:                 52.9480
    Variance:            236.4728
    Std Error:             0.1719
  Variance Reduction:       51.48%
  Efficiency Gain:           2.06x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 38.3312
    Variance:            362.1566
    Std Error:             0.2128
  With Control Variates:
    Mean:                 38.2321
    Variance:            226.8728
    Std Error:             0.1684
  Variance Reduction:       37.36%
  Efficiency Gain:           1.60x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                163.6197
    Variance:           3883.9889
    Std Error:             0.6968
  With Control Variates:
    Mean:                163.2307
    Variance:           2576.7095
    Std Error:             0.5675
  Variance Reduction:       33.66%
  Efficiency Gain:           1.51x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 18/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          77.4245 minutes
  Average patient waiting time:       6.7526 minutes
  Average server overtime:           62.7658 minutes
  Total Cost:                   $      212.09

PATIENT METRICS (MINUTES):
  Avg waiting time:                   6.7526 minutes
  Max waiting time:                  85.9912 minutes
  Std dev waiting time:              10.2409 minutes
  95th percentile:                   28.5496 minutes
  Patients waiting > 15 min:         52516.0
  Percentage waiting > 15 min:         17.51%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:23<00:00, 420.44it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -4.635642
    Idle time (c*):    6.060678
    Overtime (c*):     -0.347418

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  6.7647
    Variance:             35.6002
    Std Error:             0.0667
  With Control Variates:
    Mean:                  6.7299
    Variance:             17.1611
    Std Error:             0.0463
  Variance Reduction:       51.79%
  Efficiency Gain:           2.07x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 77.3958
    Variance:            607.0056
    Std Error:             0.2755
  With Control Variates:
    Mean:                 77.4432
    Variance:            272.7533
    Std Error:             0.1846
  Variance Reduction:       55.07%
  Efficiency Gain:           2.23x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 62.7822
    Variance:            343.3800
    Std Error:             0.2072
  With Control Variates:
    Mean:                 62.7039
    Variance:            260.0659
    Std Error:             0.1803
  Variance Reduction:       24.26%
  Efficiency Gain:           1.32x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                212.1572
    Variance:           2676.1922
    Std Error:             0.5784
  With Control Variates:
    Mean:                211.8783
    Variance:           2234.9602
    Std Error:             0.5286
  Variance Reduction:       16.49%
  Efficiency Gain:           1.20x

================================================================================


--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 19/15.5/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:         103.6300 minutes
  Average patient waiting time:       5.4900 minutes
  Average server overtime:           88.9713 minutes
  Total Cost:                   $      270.03

PATIENT METRICS (MINUTES):
  Avg waiting time:                   5.4900 minutes
  Max waiting time:                  81.7000 minutes
  Std dev waiting time:               9.0562 minutes
  95th percentile:                   25.0495 minutes
  Patients waiting > 15 min:         41243.0
  Percentage waiting > 15 min:         13.75%

  Running comprehensive control variate comparison with 10000 runs...

================================================================================
COMPREHENSIVE CONTROL VARIATE ANALYSIS
================================================================================
Number of runs: 10000
Control variables:
  - Service Time (mean = 15.5000 minutes)
  - Unpunctuality (mean = -7.9213 minutes)
  - Total Service Time (mean = 465.0000 minutes)

Running simulations...
Control Variate Analysis: 100%|████████████████████████████████████████████████████████████████| 10000/10000 [00:24<00:00, 407.29it/s] 

Using two-stage approach for all control variates:
  Pilot runs: 2000 (for estimating coefficients)
  Main runs:  8000 (for applying coefficients)

Calculating optimal control variate coefficients from pilot runs...
  Optimal coefficients (from pilot runs):
    Waiting time (c*): -3.631000
    Idle time (c*):    6.545358
    Overtime (c*):     -0.293533

================================================================================
COMPREHENSIVE CONTROL VARIATE RESULTS
================================================================================

Waiting Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                  5.5005
    Variance:             22.2363
    Std Error:             0.0527
  With Control Variates:
    Mean:                  5.4733
    Variance:             10.9301
    Std Error:             0.0370
  Variance Reduction:       50.85%
  Efficiency Gain:           2.03x

Idle Time (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                103.6203
    Variance:            680.5332
    Std Error:             0.2917
  With Control Variates:
    Mean:                103.6715
    Variance:            298.5778
    Std Error:             0.1932
  Variance Reduction:       56.13%
  Efficiency Gain:           2.28x

Overtime (minutes):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                 89.0067
    Variance:            342.6789
    Std Error:             0.2070
  With Control Variates:
    Mean:                 88.9406
    Variance:            281.8735
    Std Error:             0.1877
  Variance Reduction:       17.74%
  Efficiency Gain:           1.22x

Total Cost ($):
  [Two-stage approach: 2000 pilot runs + 8000 main runs]
  Standard MC:
    Mean:                270.1335
    Variance:           2264.5093
    Std Error:             0.5320
  With Control Variates:
    Mean:                269.9218
    Variance:           2120.2237
    Std Error:             0.5148
  Variance Reduction:        6.37%
  Efficiency Gain:           1.07x

================================================================================


================================================================================
END OF SUMMARY
================================================================================

================================================================================
               SENSITIVITY ANALYSIS SUMMARY FOR SCHEDULED_ARRIVAL
================================================================================

--- Below Optimal Scheduled Arrival ---
                         metric delta_minus          minus           self           plus delta_plus
0             scheduled_arrival          -1      13.000000      14.000000      15.000000         +1
4                    total_cost   64.561123     245.133526     180.572403     140.820061 -39.752342
5              avg_waiting_time   11.672991      38.808377      27.135385      18.255763  -8.879623
8   patients_waiting_over_15min     36460.0  221743.000000  185283.000000  140195.000000   -45088.0
11           doctor_utilization    0.853843      99.448475      98.594632      96.668009  -1.926623

--- At Optimal Scheduled Arrival ---
                         metric delta_minus          minus           self          plus delta_plus
0             scheduled_arrival          -1      15.000000      16.000000     17.000000         +1
4                    total_cost    5.823435     140.820061     134.996627    163.530923  28.534297
5              avg_waiting_time    5.851943      18.255763      12.403820      8.848518  -3.555302
8   patients_waiting_over_15min     40170.0  140195.000000  100025.000000  71248.000000   -28777.0
11           doctor_utilization    3.075311      96.668009      93.592697     89.785552  -3.807146

--- Above Optimal Scheduled Arrival ---
                         metric delta_minus         minus          self          plus delta_plus
0             scheduled_arrival          -1     17.000000     18.000000     19.000000         +1
4                    total_cost  -48.558092    163.530923    212.089015    270.026901  57.937887
5              avg_waiting_time    2.095869      8.848518      6.752649      5.489978  -1.262672
8   patients_waiting_over_15min     18732.0  71248.000000  52516.000000  41243.000000   -11273.0
11           doctor_utilization    4.037172     89.785552     85.748380     81.805447  -3.942933

================================================================================
                      END OF SENSITIVITY ANALYSIS SUMMARY
================================================================================