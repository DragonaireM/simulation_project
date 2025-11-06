Run at 6 Nov, 2:30 p.m. 

================================================================================
SIMULATION SUMMARY - SAVED RESULTS
================================================================================

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 15/25/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          10.5034 minutes
  Average patient waiting time:      82.2370 minutes
  Average server overtime:           29.7671 minutes
  Total Cost:                   $      449.89

PATIENT METRICS (MINUTES):
  Avg waiting time:                  82.2370 minutes
  Max waiting time:                 439.8848 minutes
  Std dev waiting time:              64.5975 minutes
  95th percentile:                  203.4250 minutes
  Patients waiting > 15 min:          200140
  Percentage waiting > 15 min:         83.39%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|████████████████████████████████████████████████████████████████████| 1000/1000 [00:02<00:00, 457.53it/s]

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 81.308789 hours
Variance of mean waiting times: 1170.201110
Standard error: 34.208202
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 25.0000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 524.49it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.433624
Average W-S correlation: -0.110810
Average within-run variance reduction: -17.09%
Runs with negative correlation (good for CV): 705/1000

Overall Statistics Across Runs:
  Original MC - Mean: 81.308789, Var: 1170.201110
  Control Variates - Mean: 81.180321, Var: 1102.942313
  Between-run variance reduction: 5.75%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 81.308789 hours
  Variance: 1170.201110
  Standard error: 1.081758

Control Variates:
  Mean waiting time: 81.180321 hours
  Variance: 1102.942313
  Standard error: 1.050211

Variance Reduction: 5.75%
Efficiency Gain: 1.06x
  (Control variates is equivalent to 1.06x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             81.308789 minutes
      Variance:                    1170.201110
      Standard error:                 1.081758

    With Control Variates:
      Mean waiting time:             81.180321 minutes
      Variance:                    1102.942313
      Standard error:                 1.050211

    Variance Reduction:                   5.75%
    Efficiency Gain:                      1.06x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 16/25/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          13.8847 minutes
  Average patient waiting time:      70.4576 minutes
  Average server overtime:           31.2002 minutes
  Total Cost:                   $      398.88

PATIENT METRICS (MINUTES):
  Avg waiting time:                  70.4576 minutes
  Max waiting time:                 412.7041 minutes
  Std dev waiting time:              58.5066 minutes
  95th percentile:                  182.1403 minutes
  Patients waiting > 15 min:          192566
  Percentage waiting > 15 min:         80.24%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1749.48it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 69.499076 hours
Variance of mean waiting times: 1097.252691
Standard error: 33.124805
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 25.0000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 809.75it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.416935
Average W-S correlation: -0.126596
Average within-run variance reduction: -18.14%
Runs with negative correlation (good for CV): 730/1000

Overall Statistics Across Runs:
  Original MC - Mean: 69.499076, Var: 1097.252691
  Control Variates - Mean: 69.336117, Var: 1034.597597
  Between-run variance reduction: 5.71%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 69.499076 hours
  Variance: 1097.252691
  Standard error: 1.047498

Control Variates:
  Mean waiting time: 69.336117 hours
  Variance: 1034.597597
  Standard error: 1.017152

Variance Reduction: 5.71%
Efficiency Gain: 1.06x
  (Control variates is equivalent to 1.06x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             69.499076 minutes
      Variance:                    1097.252691
      Standard error:                 1.047498

    With Control Variates:
      Mean waiting time:             69.336117 minutes
      Variance:                    1034.597597
      Standard error:                 1.017152

    Variance Reduction:                   5.71%
    Efficiency Gain:                      1.06x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 17/25/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          18.7763 minutes
  Average patient waiting time:      59.5086 minutes
  Average server overtime:           33.4064 minutes
  Total Cost:                   $      354.53

PATIENT METRICS (MINUTES):
  Avg waiting time:                  59.5086 minutes
  Max waiting time:                 385.5234 minutes
  Std dev waiting time:              52.7060 minutes
  95th percentile:                  162.0935 minutes
  Patients waiting > 15 min:          182579
  Percentage waiting > 15 min:         76.07%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1800.38it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 58.515568 hours
Variance of mean waiting times: 995.928825
Standard error: 31.558340
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 25.0000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 710.43it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.393981
Average W-S correlation: -0.141864
Average within-run variance reduction: -19.28%
Runs with negative correlation (good for CV): 763/1000

Overall Statistics Across Runs:
  Original MC - Mean: 58.515568, Var: 995.928825
  Control Variates - Mean: 58.319327, Var: 939.048955
  Between-run variance reduction: 5.71%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 58.515568 hours
  Variance: 995.928825
  Standard error: 0.997962

Control Variates:
  Mean waiting time: 58.319327 hours
  Variance: 939.048955
  Standard error: 0.969045

Variance Reduction: 5.71%
Efficiency Gain: 1.06x
  (Control variates is equivalent to 1.06x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             58.515568 minutes
      Variance:                     995.928825
      Standard error:                 0.997962

    With Control Variates:
      Mean waiting time:             58.319327 minutes
      Variance:                     939.048955
      Standard error:                 0.969045

    Variance Reduction:                   5.71%
    Efficiency Gain:                      1.06x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 18/25/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          25.7018 minutes
  Average patient waiting time:      49.5671 minutes
  Average server overtime:           36.9074 minutes
  Total Cost:                   $      318.99

PATIENT METRICS (MINUTES):
  Avg waiting time:                  49.5671 minutes
  Max waiting time:                 358.3427 minutes
  Std dev waiting time:              47.2062 minutes
  95th percentile:                  143.0413 minutes
  Patients waiting > 15 min:          170291
  Percentage waiting > 15 min:         70.95%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1817.70it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 48.588004 hours
Variance of mean waiting times: 867.764559
Standard error: 29.457844
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 25.0000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 607.81it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.362208
Average W-S correlation: -0.153577
Average within-run variance reduction: -20.31%
Runs with negative correlation (good for CV): 778/1000

Overall Statistics Across Runs:
  Original MC - Mean: 48.588004, Var: 867.764559
  Control Variates - Mean: 48.358419, Var: 817.865436
  Between-run variance reduction: 5.75%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 48.588004 hours
  Variance: 867.764559
  Standard error: 0.931539

Control Variates:
  Mean waiting time: 48.358419 hours
  Variance: 817.865436
  Standard error: 0.904359

Variance Reduction: 5.75%
Efficiency Gain: 1.06x
  (Control variates is equivalent to 1.06x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             48.588004 minutes
      Variance:                     867.764559
      Standard error:                 0.931539

    With Control Variates:
      Mean waiting time:             48.358419 minutes
      Variance:                     817.865436
      Standard error:                 0.904359

    Variance Reduction:                   5.75%
    Efficiency Gain:                      1.06x

--------------------------------------------------------------------------------
Variable: scheduled_arrival | Configuration: 19/25/1
--------------------------------------------------------------------------------

AVERAGES TABLE (MINUTES):
  Average server idle time:          35.1836 minutes
  Average patient waiting time:      40.7683 minutes
  Average server overtime:           42.7752 minutes
  Total Cost:                   $      295.03

PATIENT METRICS (MINUTES):
  Avg waiting time:                  40.7683 minutes
  Max waiting time:                 331.1620 minutes
  Std dev waiting time:              42.0136 minutes
  95th percentile:                  125.2405 minutes
  Patients waiting > 15 min:          155402
  Percentage waiting > 15 min:         64.75%

  Running control variate comparison with 1000 runs...
Running comparison between Standard MC and Control Variates...

================================================================================
STANDARD MONTE CARLO SIMULATION (No Control Variates)
================================================================================
Number of runs: 1000
Standard MC Simulation: 100%|███████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 1258.94it/s] 

================================================================================
STANDARD MC SUMMARY
================================================================================
Mean waiting time across runs: 39.844461 hours
Variance of mean waiting times: 721.331963
Standard error: 26.857624
================================================================================


================================================================================
CONTROL VARIATES MONTE CARLO SIMULATION
================================================================================
Number of runs: 1000
Control variable: Service Time (Known mean = 25.0000 hours)
Control Variates Simulation: 100%|███████████████████████████████████████████████████████████████| 1000/1000 [00:01<00:00, 846.85it/s] 

================================================================================
CONTROL VARIATES SUMMARY
================================================================================
Average optimal coefficient (c*): 0.322948
Average W-S correlation: -0.158980
Average within-run variance reduction: -20.39%
Runs with negative correlation (good for CV): 790/1000

Overall Statistics Across Runs:
  Original MC - Mean: 39.844461, Var: 721.331963
  Control Variates - Mean: 39.589384, Var: 678.905387
  Between-run variance reduction: 5.88%
================================================================================


================================================================================
VARIANCE REDUCTION COMPARISON
================================================================================
Number of runs: 1000
Base seed: 0

Standard Monte Carlo:
  Mean waiting time: 39.844461 hours
  Variance: 721.331963
  Standard error: 0.849313

Control Variates:
  Mean waiting time: 39.589384 hours
  Variance: 678.905387
  Standard error: 0.823957

Variance Reduction: 5.88%
Efficiency Gain: 1.06x
  (Control variates is equivalent to 1.06x more standard MC runs)
================================================================================


  CONTROL VARIATE COMPARISON:
    Standard MC:
      Mean waiting time:             39.844461 minutes
      Variance:                     721.331963
      Standard error:                 0.849313

    With Control Variates:
      Mean waiting time:             39.589384 minutes
      Variance:                     678.905387
      Standard error:                 0.823957

    Variance Reduction:                   5.88%
    Efficiency Gain:                      1.06x

================================================================================
END OF SUMMARY
================================================================================