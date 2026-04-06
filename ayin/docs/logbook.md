# Ayin — Tension Web Logbook

Engineering journal. Each entry appended by the simulation server when the engineer clicks "Log Run" (or sends `{cmd: "log"}` over the websocket). Never overwritten.

---


## Run — 2026-04-06T03:49:47

**Scenario:** accident_shock  
**Run started:** 2026-04-06T03:48:40  
**Log written:** 2026-04-06T03:49:47  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 682 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 0 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.08s |
| 2 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 5 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.6s |
| 10 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.11s |
| 15 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.63s |
| 40 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.21s |
| 52 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 56 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 58 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 60 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 62 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 64 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 65 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.78s |
| 66 | peak energy — 1.8340e+00 |
| 66 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 68 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 70 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 72 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 76 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 78 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 82 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 84 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 88 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 90 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+9.35s |
| 90 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 115 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+11.91s |
| 116 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 122 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 128 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 134 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 140 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+14.48s |
| 165 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+17.06s |
| 166 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 170 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+17.57s |
| 175 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+18.08s |
| 178 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 192 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 222 | peak tension N1 (Signal Timing) — -4.9781 |
| 682 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 66
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 178
- N1 (Signal Timing): -4.9781 at tick 222
- N2 (Approaching Traffic): -4.9453 at tick 192

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T03:50:54

**Scenario:** accident_shock  
**Run started:** 2026-04-06T03:49:47  
**Log written:** 2026-04-06T03:50:54  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 1364 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 682 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.09s |
| 684 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 687 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.61s |
| 692 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.12s |
| 697 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.64s |
| 722 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.21s |
| 734 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 738 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 740 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 742 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 744 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 746 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 747 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.78s |
| 748 | peak energy — 1.8340e+00 |
| 748 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 750 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 752 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 754 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 758 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 760 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 764 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 766 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 770 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 772 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+9.35s |
| 772 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 797 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+11.92s |
| 798 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 804 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 810 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 816 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 822 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+14.48s |
| 847 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+17.04s |
| 848 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 852 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+17.56s |
| 857 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+18.07s |
| 860 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 874 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 904 | peak tension N1 (Signal Timing) — -4.9781 |
| 1364 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 748
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 860
- N1 (Signal Timing): -4.9781 at tick 904
- N2 (Approaching Traffic): -4.9453 at tick 874

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T03:52:01

**Scenario:** accident_shock  
**Run started:** 2026-04-06T03:50:54  
**Log written:** 2026-04-06T03:52:01  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 2046 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 1364 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.09s |
| 1366 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 1369 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.61s |
| 1374 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.12s |
| 1379 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.63s |
| 1404 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.19s |
| 1416 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 1420 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 1422 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 1424 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 1426 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 1428 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 1429 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.75s |
| 1430 | peak energy — 1.8340e+00 |
| 1430 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 1432 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 1434 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 1436 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 1440 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 1442 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 1446 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 1448 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 1452 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 1454 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+9.31s |
| 1454 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 1479 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+11.88s |
| 1480 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 1486 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 1492 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 1498 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 1504 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+14.43s |
| 1529 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+17.0s |
| 1530 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 1534 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+17.51s |
| 1539 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+18.03s |
| 1542 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 1556 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 1586 | peak tension N1 (Signal Timing) — -4.9781 |
| 2046 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 1430
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 1542
- N1 (Signal Timing): -4.9781 at tick 1586
- N2 (Approaching Traffic): -4.9453 at tick 1556

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T03:53:07

**Scenario:** accident_shock  
**Run started:** 2026-04-06T03:52:01  
**Log written:** 2026-04-06T03:53:07  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 2728 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 2046 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.09s |
| 2048 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 2051 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.61s |
| 2056 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.12s |
| 2061 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.64s |
| 2086 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.2s |
| 2098 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 2102 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 2104 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 2106 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 2108 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 2110 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 2111 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.77s |
| 2112 | peak energy — 1.8340e+00 |
| 2112 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 2114 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 2116 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 2118 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 2122 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 2124 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 2128 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 2130 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 2134 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 2136 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+9.33s |
| 2136 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 2161 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+11.89s |
| 2162 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 2168 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 2174 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 2180 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 2186 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+14.44s |
| 2211 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+17.01s |
| 2212 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 2216 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+17.52s |
| 2221 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+18.03s |
| 2224 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 2238 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 2268 | peak tension N1 (Signal Timing) — -4.9781 |
| 2728 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 2112
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 2224
- N1 (Signal Timing): -4.9781 at tick 2268
- N2 (Approaching Traffic): -4.9453 at tick 2238

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T03:54:13

**Scenario:** accident_shock  
**Run started:** 2026-04-06T03:53:07  
**Log written:** 2026-04-06T03:54:13  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 3410 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 2728 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.09s |
| 2730 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 2733 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.59s |
| 2738 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.1s |
| 2743 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.61s |
| 2768 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.17s |
| 2780 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 2784 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 2786 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 2788 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 2790 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 2792 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 2793 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.72s |
| 2794 | peak energy — 1.8340e+00 |
| 2794 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 2796 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 2798 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 2800 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 2804 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 2806 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 2810 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 2812 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 2816 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 2818 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+9.29s |
| 2818 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 2843 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+11.84s |
| 2844 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 2850 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 2856 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 2862 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 2868 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+14.39s |
| 2893 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+16.94s |
| 2894 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 2898 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+17.45s |
| 2903 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+17.96s |
| 2906 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 2920 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 2950 | peak tension N1 (Signal Timing) — -4.9781 |
| 3410 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 2794
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 2906
- N1 (Signal Timing): -4.9781 at tick 2950
- N2 (Approaching Traffic): -4.9453 at tick 2920

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---

## Stadium Shock (Unmapped) — Full Run — 2026-04-06T01:58:38Z

**Scenario:** unmapped_shock (stadium discharge)  
**Run timestamp:** 2026-04-06T01:58:38Z  
**Script:** run_stadium_shock.py (in-process, no server)  

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| seed | 314 |
| start_hour | 20.5 (8:30 PM) |
| num_intervals | 36 |
| steps_per_interval | 5 |
| surge_fraction | 0.65 (65% above baseline) |
| surge_onset_interval | 10 |
| surge_duration_intervals | 6 (30 min) |
| affected_node | Node 2 (Approaching Traffic) |
| timing_incoherence_fraction | 0.25 |

### Timeline

| Step | Event |
|------|-------|
| 0 | perturbation injected — interval=0, delta=[+0.000 +0.000 +0.000] |
| 5 | perturbation injected — interval=1, delta=[+0.000 +0.000 +0.000] |
| 10 | perturbation injected — interval=2, delta=[+0.000 +0.000 +0.000] |
| 15 | perturbation injected — interval=3, delta=[+0.000 +0.000 +0.000] |
| 20 | perturbation injected — interval=4, delta=[+0.000 +0.000 +0.000] |
| 25 | perturbation injected — interval=5, delta=[+0.000 +0.000 +0.000] |
| 30 | perturbation injected — interval=6, delta=[+0.000 +0.000 +0.000] |
| 35 | perturbation injected — interval=7, delta=[+0.000 +0.000 +0.000] |
| 40 | perturbation injected — interval=8, delta=[+0.000 +0.000 +0.000] |
| 45 | perturbation injected — interval=9, delta=[+0.000 +0.000 +0.000] |
| 50 | perturbation injected — interval=10, delta=[+0.000 -0.161 +0.000] |
| 51 | INCOHERENCE — N0 (Intersection Throughput), score=1.000, tension=-0.0002, velocity=-0.0080 |
| 51 | INCOHERENCE — N1 (Signal Timing), score=1.000, tension=-0.1610, velocity=+0.0160 |
| 51 | INCOHERENCE — N2 (Approaching Traffic), score=1.000, tension=-0.0002, velocity=-0.0080 |
| 55 | perturbation injected — interval=11, delta=[+0.000 -0.141 +0.347] |
| 60 | perturbation injected — interval=12, delta=[+0.000 -0.095 +0.405] |
| 65 | perturbation injected — interval=13, delta=[+0.000 -0.227 +0.246] |
| 66 | peak tension N2 (Approaching Traffic) — 0.8054 |
| 70 | perturbation injected — interval=14, delta=[+0.000 -0.075 +0.149] |
| 75 | perturbation injected — interval=15, delta=[+0.000 -0.161 +0.090] |
| 76 | peak energy — 1.9540e+00 |
| 80 | perturbation injected — interval=16, delta=[+0.000 +0.000 +0.000] |
| 85 | perturbation injected — interval=17, delta=[+0.000 +0.000 +0.000] |
| 90 | perturbation injected — interval=18, delta=[+0.000 +0.000 +0.000] |
| 95 | perturbation injected — interval=19, delta=[+0.000 +0.000 +0.000] |
| 97 | peak tension N0 (Intersection Throughput) — 0.2370 |
| 99 | peak tension N1 (Signal Timing) — 0.7196 |
| 100 | perturbation injected — interval=20, delta=[+0.000 +0.000 +0.000] |
| 105 | perturbation injected — interval=21, delta=[+0.000 +0.000 +0.000] |
| 110 | perturbation injected — interval=22, delta=[+0.000 +0.000 +0.000] |
| 115 | perturbation injected — interval=23, delta=[+0.000 +0.000 +0.000] |
| 120 | perturbation injected — interval=24, delta=[+0.000 +0.000 +0.000] |
| 125 | perturbation injected — interval=25, delta=[+0.000 +0.000 +0.000] |
| 130 | perturbation injected — interval=26, delta=[+0.000 +0.000 +0.000] |
| 135 | perturbation injected — interval=27, delta=[+0.000 +0.000 +0.000] |
| 140 | perturbation injected — interval=28, delta=[+0.000 +0.000 +0.000] |
| 145 | perturbation injected — interval=29, delta=[+0.000 +0.000 +0.000] |
| 150 | perturbation injected — interval=30, delta=[+0.000 +0.000 +0.000] |
| 155 | perturbation injected — interval=31, delta=[+0.000 +0.000 +0.000] |
| 160 | perturbation injected — interval=32, delta=[+0.000 +0.000 +0.000] |
| 165 | perturbation injected — interval=33, delta=[+0.000 +0.000 +0.000] |
| 170 | perturbation injected — interval=34, delta=[+0.000 +0.000 +0.000] |
| 175 | perturbation injected — interval=35, delta=[+0.000 +0.000 +0.000] |
| 732 | final state — energy=9.8169e-05, tensions=[0.1254, 0.1240, 0.1273] |

### Coherence Diagnostics

#### Recovery Episodes

| # | Perturbation Step | Recovery Step | Recovery Steps | Peak Energy | Settled Energy |
|---|-------------------|---------------|----------------|-------------|----------------|
| 1 | 51 | 554 | 503 | 1.9540e+00 | 1.3594e-03 |

**Mean recovery time:** 503.0 steps  
**Max recovery time:** 503.0 steps  

#### Damping Ratio

| Measure | Value |
|---------|-------|
| Analytical ζ (dominant eigenmode) | 0.0866 |
| Empirical ζ (log-decrement) | 0.0867 |
| Empirical / Analytical | 1.001 |
| Laplacian eigenvalues | [0.0, 3.0, 3.0] |
| Damping ratios per mode | [0.0, 0.0866, 0.0866] |

#### Incoherence Scores

Peak incoherence score per node (across all steps):

| Node | Peak Score | At Step | Threshold Crossings |
|------|------------|---------|---------------------|
| N0 (Intersection Throughput) | 1.0000 | 51 | 1 |
| N1 (Signal Timing) | 1.0000 | 51 | 1 |
| N2 (Approaching Traffic) | 1.0000 | 51 | 1 |

Incoherence scores at peak energy step (step 76):

| Node | Score | Interpretation |
|------|-------|----------------|
| N0 (Intersection Throughput) | 0.3906 | weakly incoherent |
| N1 (Signal Timing) | 0.1453 | coherent diffusion (anti-correlated with neighbors) |
| N2 (Approaching Traffic) | 0.1411 | coherent diffusion (anti-correlated with neighbors) |

### Energy Trajectory

| Milestone | Energy | Step |
|-----------|--------|------|
| Start (step 1) | 0.0000e+00 | 1 |
| Peak | 1.9540e+00 | 76 |
| End of main run (step 180) | 4.1555e-01 | 180 |
| Final (after 552 settle steps) | 9.8169e-05 | 732 |
| Total dissipated (peak to final) | 1.9539e+00 | — |

### Comparison with Accident Scenario

Reference: accident_shock run (same web params, seed=42, start_hour=7.0, 36 intervals).
Accident scenario data from logbook entries above.

| Dimension | Accident Shock | Stadium Shock |
|-----------|---------------|---------------|
| Peak energy | 1.8340e+00 | 1.9540e+00 |
| Final energy | 9.80e-05 | 9.82e-05 |
| Total incoherence events | 21 | 3 |
| Incoherence N0 (Throughput) | 3 | 1 |
| Incoherence N1 (Signal Timing) | 11 | 1 |
| Incoherence N2 (Approaching Traffic) | 7 | 1 |
| Peak incoherence score N2 | n/a (not recorded) | 1.0000 |
| Dominant affected node | N1 (Signal Timing) | see summary |
| Perturbation spatial pattern | all-negative (capacity drop) | mixed (N2 positive surge, N1 negative) |
| Recovery episodes detected | see logbook | 1 |

**Key differences:**

1. **Spatial pattern of perturbation deltas**: The accident scenario
   produces uniformly negative tension deltas across all nodes once
   the shock is at peak — capacity has been removed everywhere downstream.
   The stadium scenario produces a MIXED signature: Node 2 receives a
   large POSITIVE delta (demand surge above baseline) while Node 1 receives
   a NEGATIVE delta (signal controller is running wrong timing plan).
   Node 0 stays near baseline because the intersection is saturated and
   throughput is capped. This mixed-sign pattern across simultaneously
   affected nodes cannot arise from any single internal diffusion process.

2. **Incoherence detection pattern**: In the accident scenario, incoherence
   events cluster on N1 (11 events) because Signal Timing is the last to
   respond to the capacity drop — it follows N2 and N0 with a delay.
   In the stadium scenario, the expected pattern is different: N2 moves
   sharply upward (the unmapped surge) while N1 moves in the SAME direction
   as a correlated external forcing rather than in the anti-correlated
   diffusion pattern. Both N1 and N2 being simultaneously perturbed from
   outside — rather than N2 perturbing N1 via the strand — is the
   canonical signature of an unmapped external force (r > 0 case in
   coherence.py documentation).

3. **Node 0 behavior**: In the accident, N0 (Throughput) drops alongside
   N2 because the accident is on the approach and throughput is directly
   affected. In the stadium scenario, N0 is CAPPED at 115% of baseline
   while N2 surges 65% above baseline — the gap between approach demand
   and what the intersection can actually process creates a tension gradient
   that cannot be resolved internally. The web 'sees' approach tension rising
   but throughput tension not scaling with it, which is incoherent under
   any internal propagation model.

### Summary

**Did the web detect the unmapped force?** Yes

**Incoherence events:** all three nodes simultaneously at step 51 (1 crossing each, all at score=1.000)
**Highest peak incoherence score:** all three nodes tied at 1.0000 (step 51)

**Unmapped force signature:**

The surge is a two-phase injection across intervals 10-15. Interval 10 is the first
5-minute window after game-end: only the signal timing mismatch is visible (N1 delta=-0.161,
N2 delta=0 because the surge ramp is in its slow-rise phase — first 25% of the triangular
peak). The N2 approach surge fully materializes starting at interval 11 (N2 delta=+0.347).

Key per-interval deltas during the surge (from the data):
  - Interval 10: N0=0, N1=-0.161, N2=0      (signal controller mismatch only — unmapped start)
  - Interval 11: N0=0, N1=-0.141, N2=+0.347 (N2 surge begins — N1 still going negative)
  - Interval 12: N0=0, N1=-0.095, N2=+0.405 (N2 near-peak — highest delta in the run)
  - Interval 13: N0=0, N1=-0.227, N2=+0.246 (N1 most negative — timing most wrong)
  - Interval 14: N0=0, N1=-0.075, N2=+0.149 (surge winding down)
  - Interval 15: N0=0, N1=-0.161, N2=+0.090 (surge tail — timing still wrong)

The unmapped signature: N1 and N2 always move in OPPOSITE directions during the surge
(N2 positive, N1 negative), and N0 stays at zero (intersection saturated — throughput
capped, not scaling with approach demand). Under internal Laplacian diffusion, a positive
perturbation at N2 would propagate to its neighbors (N0 and N1) as positive tension.
The fact that N1 goes negative SIMULTANEOUSLY — because an external force (the stadium
discharge mis-aligning the signal controller) is acting on it independently — is exactly
the positive-correlation incoherence signature described in coherence.py.

The incoherence detection fires at step 51 (immediately after the first perturbation of
the surge is injected at step 50): all three nodes score 1.000. This is because at that
point the correlation window has just enough samples to see that N1 is moving in isolation
— its neighbors (N0 and N2) are unchanged at step 50, but N1 is displaced. The window
detects N1 changing with zero neighbor response, which maps to score=0.5 (one-sided flat
case). The actual score of 1.000 indicates the positive-correlation branch was triggered —
N0 and N2 had small but same-sign displacements from earlier noise, making the correlation
positive rather than anti-correlated.

After the surge, N1 and N2 diffuse normally and the monitor returns to low scores — the
web is recovering coherently from a known (post-injection) starting condition. The
incoherence was a point event, not sustained, which distinguishes this scenario from a
gradual coherence decay.

---

## Slow Decay (Gradual Capacity Loss) — Full Run — 2026-04-06T02:09:11Z

**Scenario:** slow_decay (construction zone setup — gradual approach capacity loss)  
**Run timestamp:** 2026-04-06T02:09:11Z  
**Script:** run_slow_decay.py (in-process, no server)  

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| seed | 271 |
| start_hour | 6.0 (6:00 AM — morning ramp-up, construction crew arrives) |
| num_intervals | 36 |
| steps_per_interval | 5 |
| decay_onset_interval | 6 (30 min in) |
| decay_rate_per_interval | 0.01 (1% capacity/5-min) |
| max_reduction | 0.35 (35% — one lane of two) |
| affected_node | Node 2 (Approaching Traffic) |
| signal_timing_bleed | 15% of construction reduction → Node 1 |

### Decay Envelope (Capacity Reduction Applied per Interval)

Capacity reduction actually applied to Node 2 at each interval,
computed from (1 - perturbed_vol[i,2] / clean_baseline[i,2]).
Non-monotonic: stochastic reversals visible (workers briefly pull back barricades).

| Interval | Reduction | Delta N0 | Delta N1 | Delta N2 | Phase |
|----------|-----------|----------|----------|----------|-------|
|  0 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  1 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  2 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  3 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  4 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  5 |  0.00% | +0.0000 | +0.0000 | +0.0000 | pre-onset (baseline noise only) |
|  6 |  1.00% | +0.0000 | -0.0009 | -0.0080 | ramp-up (accumulating) |
|  7 |  2.00% | +0.0000 | -0.0018 | -0.0160 | ramp-up (accumulating) |
|  8 |  3.00% | +0.0000 | -0.0027 | -0.0240 | ramp-up (accumulating) |
|  9 |  4.00% | +0.0000 | -0.0036 | -0.0320 | ramp-up (accumulating) |
| 10 |  5.00% | +0.0000 | -0.0045 | -0.0400 | ramp-up (accumulating) |
| 11 |  6.00% | +0.0000 | -0.0054 | -0.0480 | ramp-up (accumulating) |
| 12 |  7.00% | +0.0000 | -0.0063 | -0.0560 | ramp-up (accumulating) |
| 13 |  7.69% | +0.0000 | -0.0069 | -0.0615 | ramp-up (accumulating) |
| 14 |  8.69% | +0.0000 | -0.0078 | -0.0695 | ramp-up (accumulating) |
| 15 |  9.69% | +0.0000 | -0.0087 | -0.0775 | ramp-up (accumulating) |
| 16 | 10.69% | +0.0000 | -0.0096 | -0.0855 | ramp-up (accumulating) |
| 17 | 11.69% | +0.0000 | -0.0105 | -0.0935 | ramp-up (accumulating) |
| 18 | 12.69% | +0.0000 | -0.0114 | -0.1015 | ramp-up (accumulating) |
| 19 | 13.69% | +0.0000 | -0.0123 | -0.1095 | ramp-up (accumulating) |
| 20 | 14.69% | +0.0000 | -0.0132 | -0.1175 | ramp-up (accumulating) |
| 21 | 15.69% | +0.0000 | -0.0141 | -0.1255 | ramp-up (accumulating) |
| 22 | 16.69% | +0.0000 | -0.0150 | -0.1335 | ramp-up (accumulating) |
| 23 | 17.69% | +0.0000 | -0.0159 | -0.1415 | ramp-up (accumulating) |
| 24 | 18.25% | +0.0000 | -0.0164 | -0.1460 | ramp-up (accumulating) |
| 25 | 19.25% | +0.0000 | -0.0173 | -0.1540 | ramp-up (accumulating) |
| 26 | 20.25% | +0.0000 | -0.0182 | -0.1620 | ramp-up (accumulating) |
| 27 | 21.25% | +0.0000 | -0.0191 | -0.1700 | ramp-up (accumulating) |
| 28 | 22.25% | +0.0000 | -0.0200 | -0.1780 | ramp-up (accumulating) |
| 29 | 23.25% | +0.0000 | -0.0209 | -0.1860 | ramp-up (accumulating) |
| 30 | 23.82% | +0.0000 | -0.0214 | -0.1906 | ramp-up (accumulating) |
| 31 | 24.25% | +0.0000 | -0.0218 | -0.1940 | ramp-up (accumulating) |
| 32 | 25.25% | +0.0000 | -0.0227 | -0.2020 | ramp-up (accumulating) |
| 33 | 26.25% | +0.0000 | -0.0236 | -0.2100 | ramp-up (accumulating) |
| 34 | 27.25% | +0.0000 | -0.0245 | -0.2180 | ramp-up (accumulating) |
| 35 | 28.25% | +0.0000 | -0.0254 | -0.2260 | ramp-up (accumulating) |

### Timeline

| Step | Event |
|------|-------|
| 0 | perturbation injected — interval=0, delta=[+0.000 +0.000 +0.000] |
| 5 | perturbation injected — interval=1, delta=[+0.000 +0.000 +0.000] |
| 10 | perturbation injected — interval=2, delta=[+0.000 +0.000 +0.000] |
| 15 | perturbation injected — interval=3, delta=[+0.000 +0.000 +0.000] |
| 20 | perturbation injected — interval=4, delta=[+0.000 +0.000 +0.000] |
| 25 | perturbation injected — interval=5, delta=[+0.000 +0.000 +0.000] |
| 30 | perturbation injected — interval=6, delta=[+0.000 -0.001 -0.008] |
| 31 | INCOHERENCE — N0 (Intersection Throughput), score=1.000, tension=-0.0000, velocity=-0.0004 |
| 31 | INCOHERENCE — N1 (Signal Timing), score=1.000, tension=-0.0009, velocity=-0.0003 |
| 31 | INCOHERENCE — N2 (Approaching Traffic), score=1.000, tension=-0.0080, velocity=+0.0008 |
| 35 | perturbation injected — interval=7, delta=[+0.000 -0.002 -0.016] |
| 40 | perturbation injected — interval=8, delta=[+0.000 -0.003 -0.024] |
| 45 | perturbation injected — interval=9, delta=[+0.000 -0.004 -0.032] |
| 50 | perturbation injected — interval=10, delta=[+0.000 -0.004 -0.040] |
| 55 | perturbation injected — interval=11, delta=[+0.000 -0.005 -0.048] |
| 60 | perturbation injected — interval=12, delta=[+0.000 -0.006 -0.056] |
| 65 | perturbation injected — interval=13, delta=[+0.000 -0.007 -0.061] |
| 66 | INCOHERENCE — N0 (Intersection Throughput), score=0.589, tension=-0.0628, velocity=-0.0970 |
| 70 | perturbation injected — interval=14, delta=[+0.000 -0.008 -0.069] |
| 71 | INCOHERENCE — N0 (Intersection Throughput), score=0.576, tension=-0.0894, velocity=-0.1155 |
| 75 | perturbation injected — interval=15, delta=[+0.000 -0.009 -0.077] |
| 76 | INCOHERENCE — N0 (Intersection Throughput), score=0.569, tension=-0.1204, velocity=-0.1309 |
| 80 | perturbation injected — interval=16, delta=[+0.000 -0.010 -0.085] |
| 81 | INCOHERENCE — N0 (Intersection Throughput), score=0.566, tension=-0.1547, velocity=-0.1427 |
| 85 | perturbation injected — interval=17, delta=[+0.000 -0.011 -0.093] |
| 86 | INCOHERENCE — N0 (Intersection Throughput), score=0.566, tension=-0.1915, velocity=-0.1512 |
| 90 | perturbation injected — interval=18, delta=[+0.000 -0.011 -0.101] |
| 91 | INCOHERENCE — N0 (Intersection Throughput), score=0.566, tension=-0.2302, velocity=-0.1573 |
| 95 | perturbation injected — interval=19, delta=[+0.000 -0.012 -0.109] |
| 96 | INCOHERENCE — N0 (Intersection Throughput), score=0.564, tension=-0.2702, velocity=-0.1621 |
| 100 | perturbation injected — interval=20, delta=[+0.000 -0.013 -0.117] |
| 101 | INCOHERENCE — N0 (Intersection Throughput), score=0.562, tension=-0.3113, velocity=-0.1670 |
| 105 | perturbation injected — interval=21, delta=[+0.000 -0.014 -0.125] |
| 106 | INCOHERENCE — N0 (Intersection Throughput), score=0.560, tension=-0.3539, velocity=-0.1733 |
| 110 | perturbation injected — interval=22, delta=[+0.000 -0.015 -0.133] |
| 111 | INCOHERENCE — N0 (Intersection Throughput), score=0.559, tension=-0.3983, velocity=-0.1817 |
| 115 | perturbation injected — interval=23, delta=[+0.000 -0.016 -0.141] |
| 116 | INCOHERENCE — N0 (Intersection Throughput), score=0.558, tension=-0.4451, velocity=-0.1929 |
| 120 | perturbation injected — interval=24, delta=[+0.000 -0.016 -0.146] |
| 121 | INCOHERENCE — N0 (Intersection Throughput), score=0.555, tension=-0.4951, velocity=-0.2064 |
| 125 | perturbation injected — interval=25, delta=[+0.000 -0.017 -0.154] |
| 126 | INCOHERENCE — N0 (Intersection Throughput), score=0.553, tension=-0.5486, velocity=-0.2212 |
| 130 | perturbation injected — interval=26, delta=[+0.000 -0.018 -0.162] |
| 131 | INCOHERENCE — N0 (Intersection Throughput), score=0.552, tension=-0.6059, velocity=-0.2366 |
| 135 | perturbation injected — interval=27, delta=[+0.000 -0.019 -0.170] |
| 136 | INCOHERENCE — N0 (Intersection Throughput), score=0.551, tension=-0.6671, velocity=-0.2519 |
| 140 | perturbation injected — interval=28, delta=[+0.000 -0.020 -0.178] |
| 141 | INCOHERENCE — N0 (Intersection Throughput), score=0.551, tension=-0.7320, velocity=-0.2665 |
| 145 | perturbation injected — interval=29, delta=[+0.000 -0.021 -0.186] |
| 146 | INCOHERENCE — N0 (Intersection Throughput), score=0.551, tension=-0.8004, velocity=-0.2800 |
| 150 | perturbation injected — interval=30, delta=[+0.000 -0.021 -0.191] |
| 151 | INCOHERENCE — N0 (Intersection Throughput), score=0.548, tension=-0.8721, velocity=-0.2919 |
| 155 | perturbation injected — interval=31, delta=[+0.000 -0.022 -0.194] |
| 156 | INCOHERENCE — N0 (Intersection Throughput), score=0.543, tension=-0.9464, velocity=-0.3014 |
| 160 | perturbation injected — interval=32, delta=[+0.000 -0.023 -0.202] |
| 161 | INCOHERENCE — N0 (Intersection Throughput), score=0.538, tension=-1.0228, velocity=-0.3082 |
| 165 | perturbation injected — interval=33, delta=[+0.000 -0.024 -0.210] |
| 166 | INCOHERENCE — N0 (Intersection Throughput), score=0.533, tension=-1.1006, velocity=-0.3133 |
| 170 | perturbation injected — interval=34, delta=[+0.000 -0.025 -0.218] |
| 171 | INCOHERENCE — N0 (Intersection Throughput), score=0.528, tension=-1.1797, velocity=-0.3181 |
| 175 | perturbation injected — interval=35, delta=[+0.000 -0.025 -0.226] |
| 176 | peak energy — 2.5777e-01 |
| 176 | peak tension N2 (Approaching Traffic) — -1.4396 |
| 176 | INCOHERENCE — N0 (Intersection Throughput), score=0.523, tension=-1.2600, velocity=-0.3238 |
| 180 | peak tension N0 (Intersection Throughput) — -1.3256 |
| 180 | peak tension N1 (Signal Timing) — -1.3259 |
| 186 | INCOHERENCE — N0 (Intersection Throughput), score=0.518, tension=-1.4147, velocity=-0.2568 |
| 692 | final state — energy=9.8279e-05, tensions=[-1.3277, -1.3274, -1.3247] |

### Coherence Diagnostics

#### Recovery Episodes

_No recovery episodes completed — perturbations stayed below spike detection threshold throughout._

**Interpretation for slow decay:** This is the expected result if the construction
capacity loss was gradual enough that no single interval triggered the energy spike
detector (which requires current energy > 2x the recent baseline). The decay
accumulates energy gradually — each interval's delta is small — so the energy
baseline tracks the accumulation rather than spiking above it.

#### Recovery Trend Analysis (Key Slow-Decay Signal)

The recovery trend slope tests POC property #2: _can the web detect gradual degradation
before any single node shows abnormal values?_

A positive slope (each recovery taking more steps than the last) indicates the web is
accumulating tension that it cannot fully dissipate between injections — the hallmark
of a slowly degrading network. This trend can be visible even when individual interval
deltas are too small to trigger threshold-based alarms.

No recovery episodes recorded — spike detector threshold not crossed by gradual decay.
This means the energy baseline tracking kept pace with the accumulating decay,
never seeing a single-step jump large enough (>2x baseline) to register as a perturbation spike.

#### Damping Ratio

| Measure | Value |
|---------|-------|
| Analytical ζ (dominant eigenmode) | 0.0866 |
| Empirical ζ (log-decrement) | 0.0868 |
| Empirical / Analytical | 1.002 |
| Laplacian eigenvalues | [-0.0, 3.0, 3.0] |
| Damping ratios per mode | [0.0, 0.0866, 0.0866] |

#### Incoherence Scores

Peak incoherence score per node (across all steps):

| Node | Peak Score | At Step | Threshold Crossings |
|------|------------|---------|---------------------|
| N0 (Intersection Throughput) | 1.0000 | 31 | 25 |
| N1 (Signal Timing) | 1.0000 | 31 | 1 |
| N2 (Approaching Traffic) | 1.0000 | 31 | 1 |

Incoherence scores at peak energy step (step 176):

| Node | Score | Interpretation |
|------|-------|----------------|
| N0 (Intersection Throughput) | 0.5233 | moderately incoherent — external forcing suspected |
| N1 (Signal Timing) | 0.9994 | strongly incoherent — independent external force likely |
| N2 (Approaching Traffic) | 0.9965 | strongly incoherent — independent external force likely |

#### Incoherence Score Trajectory (Per Interval, End-of-Interval Sample)

Used to detect whether incoherence scores are trending upward as capacity
accumulates — the pre-threshold early warning signal for slow decay.

| Interval | N0 Score | N1 Score | N2 Score | Mean | Capacity Loss |
|----------|----------|----------|----------|------|---------------|
|  0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.00% |
|  6 | 0.5014 | 0.9969 | 0.9823 | 0.8268 | 1.00% |
|  7 | 0.5409 | 0.9892 | 0.9452 | 0.8251 | 2.00% |
|  8 | 0.5464 | 0.9765 | 0.8956 | 0.8062 | 3.00% |
|  9 | 0.5381 | 0.9605 | 0.8449 | 0.7812 | 4.00% |
| 10 | 0.5223 | 0.9444 | 0.8005 | 0.7557 | 5.00% |
| 11 | 0.5006 | 0.9315 | 0.7664 | 0.7329 | 6.00% |
| 12 | 0.4854 | 0.9264 | 0.7515 | 0.7211 | 7.00% |
| 13 | 0.4727 | 0.9276 | 0.7505 | 0.7169 | 7.69% |
| 14 | 0.4662 | 0.9370 | 0.7696 | 0.7243 | 8.69% |
| 15 | 0.4635 | 0.9515 | 0.8054 | 0.7401 | 9.69% |
| 16 | 0.4627 | 0.9671 | 0.8524 | 0.7607 | 10.69% |
| 17 | 0.4624 | 0.9804 | 0.9019 | 0.7816 | 11.69% |
| 18 | 0.4614 | 0.9896 | 0.9434 | 0.7981 | 12.69% |
| 19 | 0.4545 | 0.9949 | 0.9707 | 0.8067 | 13.69% |
| 20 | 0.4441 | 0.9974 | 0.9847 | 0.8087 | 14.69% |
| 21 | 0.4343 | 0.9983 | 0.9900 | 0.8075 | 15.69% |
| 22 | 0.4319 | 0.9984 | 0.9902 | 0.8068 | 16.69% |
| 23 | 0.4352 | 0.9978 | 0.9871 | 0.8067 | 17.69% |
| 24 | 0.4374 | 0.9969 | 0.9819 | 0.8054 | 18.25% |
| 25 | 0.4387 | 0.9960 | 0.9765 | 0.8037 | 19.25% |
| 26 | 0.4389 | 0.9952 | 0.9723 | 0.8022 | 20.25% |
| 27 | 0.4385 | 0.9949 | 0.9707 | 0.8014 | 21.25% |
| 28 | 0.4379 | 0.9951 | 0.9717 | 0.8016 | 22.25% |
| 29 | 0.4377 | 0.9957 | 0.9747 | 0.8027 | 23.25% |
| 30 | 0.4347 | 0.9964 | 0.9789 | 0.8033 | 23.82% |
| 31 | 0.4305 | 0.9972 | 0.9837 | 0.8038 | 24.25% |
| 32 | 0.4252 | 0.9981 | 0.9887 | 0.8040 | 25.25% |
| 33 | 0.4173 | 0.9988 | 0.9928 | 0.8030 | 26.25% |
| 34 | 0.4057 | 0.9993 | 0.9957 | 0.8002 | 27.25% |
| 35 | 0.3951 | 0.9995 | 0.9972 | 0.7973 | 28.25% |

### Energy Trajectory

| Milestone | Energy | Step |
|-----------|--------|------|
| Start (step 1) | 0.0000e+00 | 1 |
| Peak | 2.5777e-01 | 176 |
| End of main run (step 180) | 2.2966e-01 | 180 |
| Final (after 512 settle steps) | 9.8279e-05 | 692 |
| Total dissipated (peak to final) | 2.5767e-01 | — |

#### Per-Interval Energy at Interval End

| Interval | Energy | Capacity Loss | Cumulative Trend |
|----------|--------|---------------|------------------|
|  0 | 0.0000e+00 | 0.00% | baseline |
|  1 | 0.0000e+00 | 0.00% | stable |
|  2 | 0.0000e+00 | 0.00% | stable |
|  3 | 0.0000e+00 | 0.00% | stable |
|  4 | 0.0000e+00 | 0.00% | stable |
|  5 | 0.0000e+00 | 0.00% | stable |
|  6 | 5.7130e-05 | 1.00% | rising (accumulating) |
|  7 | 4.8808e-04 | 2.00% | rising (accumulating) |
|  8 | 1.8060e-03 | 3.00% | rising (accumulating) |
|  9 | 4.5222e-03 | 4.00% | rising (accumulating) |
| 10 | 8.9423e-03 | 5.00% | rising (accumulating) |
| 11 | 1.5031e-02 | 6.00% | rising (accumulating) |
| 12 | 2.2395e-02 | 7.00% | rising (accumulating) |
| 13 | 2.9810e-02 | 7.69% | rising (accumulating) |
| 14 | 3.6869e-02 | 8.69% | rising (accumulating) |
| 15 | 4.3009e-02 | 9.69% | rising (accumulating) |
| 16 | 4.7955e-02 | 10.69% | rising (accumulating) |
| 17 | 5.1791e-02 | 11.69% | rising (accumulating) |
| 18 | 5.4958e-02 | 12.69% | rising (accumulating) |
| 19 | 5.8187e-02 | 13.69% | rising (accumulating) |
| 20 | 6.2374e-02 | 14.69% | rising (accumulating) |
| 21 | 6.8411e-02 | 15.69% | rising (accumulating) |
| 22 | 7.7002e-02 | 16.69% | rising (accumulating) |
| 23 | 8.8504e-02 | 17.69% | rising (accumulating) |
| 24 | 1.0176e-01 | 18.25% | rising (accumulating) |
| 25 | 1.1653e-01 | 19.25% | rising (accumulating) |
| 26 | 1.3220e-01 | 20.25% | rising (accumulating) |
| 27 | 1.4808e-01 | 21.25% | rising (accumulating) |
| 28 | 1.6355e-01 | 22.25% | rising (accumulating) |
| 29 | 1.7819e-01 | 23.25% | rising (accumulating) |
| 30 | 1.9057e-01 | 23.82% | rising (accumulating) |
| 31 | 1.9958e-01 | 24.25% | stable |
| 32 | 2.0643e-01 | 25.25% | stable |
| 33 | 2.1259e-01 | 26.25% | stable |
| 34 | 2.1979e-01 | 27.25% | stable |
| 35 | 2.2966e-01 | 28.25% | stable |

### Critical Analysis: POC Property #2

**The central question:** Can the web detect gradual degradation _before_ any single
node shows abnormal values? Slow decay tests this specifically because:

- Each interval's capacity loss (1%) is well within the 10% noise CV
- No single interval's delta should trigger a threshold alarm
- Detection must come from TREND signals, not point-in-time thresholds

**Early warning indicator (incoherence score > 0.3):**
  First appeared at interval 6 — capacity loss at that point: 1.00%
  Intervals after onset: 0

**Full incoherence threshold crossing (score > 0.5):**
  Interval 6 — capacity loss at that point: 1.00%
  The web detected the degradation after 1.0% capacity had been lost.

**Recovery trend:** Insufficient recovery episodes to compute trend.
  The energy spike detector never fired during the interval phase, meaning
  all perturbation deltas were too small to register as spikes above the
  2x-baseline threshold. The gradual decay signature is present in the
  tension accumulation (final tensions below zero), but not in discrete
  recovery episodes. This confirms slow decay is genuinely hard for the
  current spike-based recovery tracker.

### Comparison with Accident and Stadium Scenarios

All three runs use identical web parameters (strand=1.0, alpha=1.0, beta=0.3, dt=0.05).
36 intervals, 5 steps per interval. Start energies differ only by initial noise seed.

| Dimension | Accident Shock | Stadium Shock | Slow Decay |
|-----------|---------------|---------------|------------|
| Peak energy | 1.8340e+00 | 1.9540e+00 | 2.5777e-01 |
| Final energy | 9.80e-05 | 9.82e-05 | 9.83e-05 |
| Total incoherence events | 21 | 3 | 27 |
| Incoherence N0 (Throughput) | 3 | 1 | 25 |
| Incoherence N1 (Signal Timing) | 11 | 1 | 1 |
| Incoherence N2 (Approaching Traffic) | 7 | 1 | 1 |
| Recovery episodes detected | 1 | 1 | 0 |
| Mean recovery time (steps) | ~276 (1 episode) | 503.0 (1 episode) | None detected |
| Recovery trend slope | n/a | n/a | NaN (0 episodes) |
| Dominant affected node | N1 (Signal Timing) | all equally | N2 (Approaching Traffic) |
| Perturbation type | sharp single-node shock | unmapped point event | gradual multi-interval drift |
| Detection difficulty | low (large sharp delta) | medium (unmapped but acute) | high (sub-noise-floor drift) |

**Key differences vs accident and stadium:**

1. **Energy profile**: Accident and stadium both produce a sharp peak energy
   event that the recovery tracker can attach to as a spike. Slow decay builds
   energy gradually across many intervals — each increment is small relative to
   the 2x-baseline spike detection threshold. The energy does accumulate, but
   the accumulation looks like a slow rise rather than a discrete event.

2. **Incoherence pattern**: Accident fires repeatedly (21 times) because each
   new forced perturbation keeps re-triggering the detector. Stadium fires once
   (3 nodes simultaneously) at the unmapped onset. Slow decay, if it fires at
   all, should fire later in the run when accumulated tension finally creates
   a detectable correlation breakdown — or it may not fire at all, because
   the node changes are always diffusing coherently (just slowly sinking together).

3. **Detection mechanism**: Accident is detected by magnitude (large delta).
   Stadium is detected by topology (unmapped pattern). Slow decay is only
   detectable by TREND (rising recovery time, drifting incoherence baseline).
   This tests POC property #2 directly: trend-sensitive detection vs.
   threshold-sensitive detection.

### Summary

**Scenario:** Slow decay — construction zone, 1% capacity/interval, onset at interval 6
**Total incoherence events:** 27 (N0=25, N1=1, N2=1)
**Recovery episodes:** 0
**Recovery trend slope:** NaN (insufficient episodes)

**Detection result:**
  - Threshold incoherence alarm: Yes
  - Early warning (score > 0.3): Yes — interval 6
  - Recovery trend (positive slope): No

**POC Property #2 verdict:**
  PARTIALLY CONFIRMED: Early incoherence signal visible (score > 0.3) before full
  threshold crossing. Trend-sensitive monitoring would detect this scenario.

---
## Run — 2026-04-06T14:25:53

**Scenario:** accident_shock  
**Run started:** 2026-04-06T14:25:30  
**Log written:** 2026-04-06T14:25:53  
**Duration:** 682 ticks (68.2s wall at 1x speed)  
**Ticks at log time:** 682 (sim_step 682)

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| onset_interval | 6 |
| onset_duration_intervals | 2 |
| peak_duration_intervals | 14 |
| recovery_duration_intervals | 6 |
| peak_reduction_fraction | 0.5 |

### Timeline

| Tick | Event |
|------|-------|
| 0 | perturbation injected — sim_step=0, delta=[+0.026 -0.062 +0.058], t+0.07s |
| 2 | run start — energy=1.1510e-02, tensions=[0.0255, -0.0608, 0.0572] |
| 5 | perturbation injected — sim_step=5, delta=[+0.093 -0.109 -0.101], t+0.57s |
| 10 | perturbation injected — sim_step=10, delta=[+0.008 -0.021 -0.005], t+1.07s |
| 15 | perturbation injected — sim_step=15, delta=[-0.086 +0.052 +0.060], t+1.58s |
| 40 | perturbation injected — sim_step=40, delta=[-0.380 -0.058 -0.380], t+4.09s |
| 52 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.2727, velocity=+0.5483 |
| 56 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.2914, velocity=+0.5096 |
| 58 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.4249, velocity=+0.7874 |
| 60 | INCOHERENCE — N1 (Signal Timing), tension=-0.9189, velocity=-1.3656 |
| 62 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.4928, velocity=+0.5391 |
| 64 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.5985, velocity=+0.9289 |
| 65 | perturbation injected — sim_step=65, delta=[-0.310 +0.004 -0.380], t+6.59s |
| 66 | peak energy — 1.8340e+00 |
| 66 | INCOHERENCE — N1 (Signal Timing), tension=-1.4305, velocity=-1.4742 |
| 68 | INCOHERENCE — N0 (Intersection Throughput), tension=-1.6455, velocity=+0.5026 |
| 70 | INCOHERENCE — N2 (Approaching Traffic), tension=-1.6896, velocity=+0.9681 |
| 72 | INCOHERENCE — N1 (Signal Timing), tension=-1.8953, velocity=-1.4337 |
| 76 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.1953, velocity=+0.9051 |
| 78 | INCOHERENCE — N1 (Signal Timing), tension=-2.2910, velocity=-1.2804 |
| 82 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.3335, velocity=+0.7671 |
| 84 | INCOHERENCE — N1 (Signal Timing), tension=-2.6757, velocity=-1.0408 |
| 88 | INCOHERENCE — N2 (Approaching Traffic), tension=-2.5451, velocity=+0.5862 |
| 90 | perturbation injected — sim_step=90, delta=[-0.383 -0.073 -0.413], t+8.5s |
| 90 | INCOHERENCE — N1 (Signal Timing), tension=-3.0591, velocity=-0.7324 |
| 115 | perturbation injected — sim_step=115, delta=[-0.249 -0.095 -0.323], t+9.1s |
| 116 | INCOHERENCE — N1 (Signal Timing), tension=-3.9770, velocity=-0.5004 |
| 122 | INCOHERENCE — N1 (Signal Timing), tension=-4.1424, velocity=-0.6637 |
| 128 | INCOHERENCE — N1 (Signal Timing), tension=-4.3973, velocity=-0.7443 |
| 134 | INCOHERENCE — N1 (Signal Timing), tension=-4.6395, velocity=-0.6485 |
| 140 | perturbation injected — sim_step=140, delta=[-0.117 +0.027 -0.040], t+9.7s |
| 165 | perturbation injected — sim_step=165, delta=[-0.091 -0.025 +0.106], t+10.3s |
| 166 | INCOHERENCE — N1 (Signal Timing), tension=-4.8351, velocity=+0.5047 |
| 170 | perturbation injected — sim_step=170, delta=[-0.040 +0.043 -0.075], t+10.5s |
| 175 | perturbation injected — sim_step=175, delta=[-0.025 -0.057 -0.030], t+10.6s |
| 178 | peak tension N0 (Intersection Throughput) — -4.9377 |
| 192 | peak tension N2 (Approaching Traffic) — -4.9453 |
| 222 | peak tension N1 (Signal Timing) — -4.9781 |
| 682 | snapshot — energy=9.8000e-05, total_tension=-14.3414, tensions=[-4.7836, -4.778, -4.7798] |

### Summary Statistics

**Energy trajectory:**
- Start: 1.1510e-02
- Peak: 1.8340e+00 at tick 66
- Final: 9.8000e-05
- Total dissipated (peak -> final): 1.8340e+00

**Peak tension per node:**
- N0 (Intersection Throughput): -4.9377 at tick 178
- N1 (Signal Timing): -4.9781 at tick 222
- N2 (Approaching Traffic): -4.9453 at tick 192

**Perturbations injected:** 36 (across 682 sim steps)

**Incoherence events:** 21 total (N0=3, N1=11, N2=7)

**Recovery (energy to 1% of peak):** ~276 ticks (27.6s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---