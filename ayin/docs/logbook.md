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
## Full Pipeline Validation (Stadium Shock) — 2026-04-06T12:57:41Z

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 0 |
| Proposals generated | 0 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

**None.** Agent did not detect acute incoherence signature.

### Agent Statistics

- **Total proposals:** 0
- **Average confidence:** 0.000
- **By status:**
  - pending: 0
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Test Conclusion

**Result: FAIL**

Agent did not trigger investigation despite unmapped shock scenario.

## Full Pipeline Validation (Stadium Shock) — 2026-04-06T12:58:10Z

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 0 |
| Proposals generated | 0 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

**None.** Agent did not detect acute incoherence signature.

### Agent Statistics

- **Total proposals:** 0
- **Average confidence:** 0.000
- **By status:**
  - pending: 0
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Test Conclusion

**Result: FAIL**

Agent did not trigger investigation despite unmapped shock scenario.

## Full Pipeline Validation (Stadium Shock) — 2026-04-06T12:59:15Z
**Mode: MOCK Claude (deterministic, no API key required)**

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 2 |
| Proposals generated | 2 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

#### Proposal 1: prop_1

- **Source:** Stadium event discharge or major demand surge event
- **Target Node:** 2 (Approaching Traffic)
- **Direction:** +1
- **Confidence:** 0.780
- **Rationale:** The simultaneous positive incoherence across all three nodes, with no single internal node initiating the pattern, strongly suggests an external event driving approach traffic upward. This is consistent with a stadium or entertainment venue discharge pushing unplanned demand into the intersection upstream.
- **Status:** pending
- **Affected nodes:** [np.int64(0), np.int64(1), np.int64(2)]

#### Proposal 2: prop_2

- **Source:** Stadium event discharge or major demand surge event
- **Target Node:** 2 (Approaching Traffic)
- **Direction:** +1
- **Confidence:** 0.780
- **Rationale:** The simultaneous positive incoherence across all three nodes, with no single internal node initiating the pattern, strongly suggests an external event driving approach traffic upward. This is consistent with a stadium or entertainment venue discharge pushing unplanned demand into the intersection upstream.
- **Status:** pending
- **Affected nodes:** [np.int64(0), np.int64(1), np.int64(2)]

### Agent Statistics

- **Total proposals:** 1
- **Average confidence:** 0.780
- **By status:**
  - pending: 1
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Validation Results

**Result: ✓ PASS**

Evidence:
  ✓ Agent hypothesized external event/surge (not internal diffusion)
  ✓ Agent connected proposal to Node 2 (Approaching Traffic) — correct
  ✓ Agent predicted positive tension direction (demand surge) — correct

## Full Pipeline Validation (Stadium Shock) — 2026-04-06T13:17:21Z

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 0 |
| Proposals generated | 0 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

**None.** Agent did not detect acute incoherence signature.

### Agent Statistics

- **Total proposals:** 0
- **Average confidence:** 0.000
- **By status:**
  - pending: 0
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Test Conclusion

**Result: FAIL**

Agent did not trigger investigation despite unmapped shock scenario.

## Full Pipeline Validation (Stadium Shock) — 2026-04-06T13:18:32Z

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 0 |
| Proposals generated | 0 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

**None.** Agent did not detect acute incoherence signature.

### Agent Statistics

- **Total proposals:** 0
- **Average confidence:** 0.000
- **By status:**
  - pending: 0
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Test Conclusion

**Result: FAIL**

Agent did not trigger investigation despite unmapped shock scenario.

## Full Pipeline Validation (Stadium Shock) — 2026-04-06T13:19:03Z

**Test:** End-to-end validation of simulator → web → coherence → strand agent

### Pipeline Statistics

| Metric | Value |
|--------|-------|
| Total steps | 180 |
| Snapshots evaluated | 180 |
| Agent triggers | 2 |
| Proposals generated | 2 |
| Peak energy | 1.9540e+00 at step 76 |
| Final energy | 4.1555e-01 |

### Proposals Generated by Agent

#### Proposal 1: prop_1

- **Source:** Emergency vehicle convoy or major incident requiring intersection shutdown
- **Target Node:** 1 (Signal Timing)
- **Direction:** +1
- **Confidence:** 0.850
- **Rationale:** An emergency requiring immediate signal override would inject maximum tension into signal timing (forcing non-optimal patterns), which then propagates to create simultaneous unexplained deviations in throughput and approaching traffic flows that cannot be explained by normal interdependencies alone.
- **Status:** pending
- **Affected nodes:** [np.int64(0), np.int64(1), np.int64(2)]

#### Proposal 2: prop_2

- **Source:** Emergency vehicle preemption signal activation
- **Target Node:** 1 (Signal Timing)
- **Direction:** +1
- **Confidence:** 0.850
- **Rationale:** Emergency vehicle preemption overrides normal signal timing algorithms, creating sudden tension in Signal Timing (node 1) that immediately propagates through the triangle topology to affect both Intersection Throughput and Approaching Traffic simultaneously, explaining the synchronized high incoherence across all nodes.
- **Status:** pending
- **Affected nodes:** [np.int64(0), np.int64(1), np.int64(2)]

### Agent Statistics

- **Total proposals:** 2
- **Average confidence:** 0.850
- **By status:**
  - pending: 2
  - probationary: 0
  - validating: 0
  - validated: 0
  - rejected: 0
  - slack: 0

### Test Conclusion

**Result: ~ PARTIAL**

Evidence:
  ✗ Agent did not recognize event/surge pattern
  ✗ Agent did not identify Node 2 as affected
  ✓ Agent predicted positive tension direction (demand surge) — correct

## Strand Integration Validation (Phase 2) -- 2026-04-06T13:52:25Z

**Scenario:** Stadium/Event Venue probationary strand attached to Node 2 (Approaching Traffic)  
**Run timestamp:** 2026-04-06T13:52:25Z  
**Script:** run_strand_validation.py  

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength (triangle) | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| seed | 314 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| initial_strand_weight | 0.01 |
| weight_ramp | 0.01 -> 0.05 -> 0.10 -> 0.25 |

### Criterion 1: Bidirectional Propagation

| Measure | Value |
|---------|-------|
| Flux source->target | 11.982388 |
| Flux target->source | 3.585586 |
| Total flux | 15.567973 |
| Directionality ratio | 0.7697 |
| Result | PASS |

### Criterion 2: Coherence Improvement

| Measure | Value |
|---------|-------|
| Mean incoherence (baseline) | 0.0477 |
| Mean incoherence (with strand) | 0.0235 |
| Improvement | +0.0242 |
| Result | PASS |

Per-phase breakdown:

| Phase | Baseline | With Strand | Improvement |
|-------|----------|-------------|-------------|
| Pre-surge | 0.0000 | 0.0000 | +0.0000 |
| During surge | 0.2368 | 0.1388 | +0.0981 |
| Post-surge | 0.0149 | 0.0007 | +0.0142 |

### Criterion 3: Energy Convergence

| Measure | Value |
|---------|-------|
| Peak energy | 1.9614e+00 |
| Final energy | 4.2603e-01 |
| Dissipated | 1.5354e+00 |
| Result | FAIL |

### Overall Result: FAIL

The probationary strand did not pass all criteria.
  - Energy convergence FAILED

---

## Strand Integration Validation (Phase 2) -- 2026-04-06T13:53:06Z

**Scenario:** Stadium/Event Venue probationary strand attached to Node 2 (Approaching Traffic)  
**Run timestamp:** 2026-04-06T13:53:06Z  
**Script:** run_strand_validation.py  

### Parameters

| Parameter | Value |
|-----------|-------|
| strand_strength (triangle) | 1.0 |
| propagation_rate | 1.0 |
| damping_coefficient | 0.3 |
| dt | 0.05 |
| seed | 314 |
| num_intervals | 36 |
| steps_per_interval | 5 |
| initial_strand_weight | 0.01 |
| weight_ramp | 0.01 -> 0.05 -> 0.10 -> 0.25 |

### Criterion 1: Bidirectional Propagation

| Measure | Value |
|---------|-------|
| Flux source->target | 16.671975 |
| Flux target->source | 11.835484 |
| Total flux | 28.507458 |
| Directionality ratio | 0.5848 |
| Result | PASS |

### Criterion 2: Coherence Improvement

| Measure | Value |
|---------|-------|
| Mean incoherence (baseline) | 0.0477 |
| Mean incoherence (with strand) | 0.0070 |
| Improvement | +0.0407 |
| Result | PASS |

Per-phase breakdown:

| Phase | Baseline | With Strand | Improvement |
|-------|----------|-------------|-------------|
| Pre-surge | 0.0000 | 0.0000 | +0.0000 |
| During surge | 0.2368 | 0.1388 | +0.0981 |
| Post-surge | 0.0149 | 0.0007 | +0.0142 |

### Criterion 3: Energy Convergence

| Measure | Value |
|---------|-------|
| Peak energy | 1.9614e+00 |
| Final energy | 9.9674e-05 |
| Dissipated | 1.9613e+00 |
| Result | PASS |

### Overall Result: PASS

The probationary strand earned its place. The stadium demand signal,
when fed through the fourth node and coupled to Node 2, reduced
incoherence at the target node. Tension flowed bidirectionally along
the strand, confirming it is a genuine coupling, not a sensor.
The Lyapunov function (total energy) still converged, confirming
the expanded web maintains stability.

---
## Run — 2026-04-06T16:48:31

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T16:28:54  
**Log written:** 2026-04-06T16:48:31  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 927 (sim_step 736)

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
| 191 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+0.0s |
| 192 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 196 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+8.0s |
| 201 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+16.01s |
| 206 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+24.02s |
| 231 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+64.07s |
| 256 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+104.11s |
| 258 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 262 | peak energy — 1.6604e+00 |
| 281 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+144.13s |
| 282 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 290 | peak tension N1 (Signal Timing) — +0.8241 |
| 306 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+184.17s |
| 324 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 331 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+224.23s |
| 332 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 356 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+264.28s |
| 361 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+272.28s |
| 366 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+280.29s |
| 927 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 262
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 282
- N1 (Signal Timing): +0.8241 at tick 290
- N2 (Approaching Traffic): +0.8477 at tick 324

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T17:08:10

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T16:48:31  
**Log written:** 2026-04-06T17:08:10  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 1663 (sim_step 736)

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
| 927 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 928 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 932 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.6s |
| 937 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.61s |
| 942 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.61s |
| 967 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.64s |
| 992 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.68s |
| 994 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 998 | peak energy — 1.6604e+00 |
| 1017 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.69s |
| 1018 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 1026 | peak tension N1 (Signal Timing) — +0.8241 |
| 1042 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.74s |
| 1060 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 1067 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.76s |
| 1068 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 1092 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.81s |
| 1097 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.82s |
| 1102 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.82s |
| 1663 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 998
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 1018
- N1 (Signal Timing): +0.8241 at tick 1026
- N2 (Approaching Traffic): +0.8477 at tick 1060

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T17:27:45

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T17:08:10  
**Log written:** 2026-04-06T17:27:45  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 2399 (sim_step 736)

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
| 1663 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 1664 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 1668 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.6s |
| 1673 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.6s |
| 1678 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.6s |
| 1703 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.67s |
| 1728 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.73s |
| 1730 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 1734 | peak energy — 1.6604e+00 |
| 1753 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.75s |
| 1754 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 1762 | peak tension N1 (Signal Timing) — +0.8241 |
| 1778 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.77s |
| 1796 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 1803 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.85s |
| 1804 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 1828 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.87s |
| 1833 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.87s |
| 1838 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.87s |
| 2399 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 1734
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 1754
- N1 (Signal Timing): +0.8241 at tick 1762
- N2 (Approaching Traffic): +0.8477 at tick 1796

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T17:47:23

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T17:27:45  
**Log written:** 2026-04-06T17:47:23  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 3135 (sim_step 736)

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
| 2399 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 2400 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 2404 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.61s |
| 2409 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.62s |
| 2414 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.63s |
| 2439 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.68s |
| 2464 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.73s |
| 2466 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 2470 | peak energy — 1.6604e+00 |
| 2489 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.76s |
| 2490 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 2498 | peak tension N1 (Signal Timing) — +0.8241 |
| 2514 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.8s |
| 2532 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 2539 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.82s |
| 2540 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 2564 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.88s |
| 2569 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.88s |
| 2574 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.89s |
| 3135 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 2470
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 2490
- N1 (Signal Timing): +0.8241 at tick 2498
- N2 (Approaching Traffic): +0.8477 at tick 2532

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T18:06:52

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T17:47:23  
**Log written:** 2026-04-06T18:06:52  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 3871 (sim_step 736)

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
| 3135 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 3136 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 3140 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.61s |
| 3145 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.62s |
| 3150 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.63s |
| 3175 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.67s |
| 3200 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.74s |
| 3202 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 3206 | peak energy — 1.6604e+00 |
| 3225 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.79s |
| 3226 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 3234 | peak tension N1 (Signal Timing) — +0.8241 |
| 3250 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.85s |
| 3268 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 3275 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.91s |
| 3276 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 3300 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.96s |
| 3305 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.98s |
| 3310 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.99s |
| 3871 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 3206
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 3226
- N1 (Signal Timing): +0.8241 at tick 3234
- N2 (Approaching Traffic): +0.8477 at tick 3268

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T18:26:14

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T18:06:52  
**Log written:** 2026-04-06T18:26:14  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 4607 (sim_step 736)

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
| 3871 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 3872 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 3876 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 3881 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.64s |
| 3886 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.66s |
| 3911 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.77s |
| 3936 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.87s |
| 3938 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 3942 | peak energy — 1.6604e+00 |
| 3961 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.98s |
| 3962 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 3970 | peak tension N1 (Signal Timing) — +0.8241 |
| 3986 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.1s |
| 4004 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 4011 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.2s |
| 4012 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 4036 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.29s |
| 4041 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.31s |
| 4046 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.32s |
| 4607 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 3942
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 3962
- N1 (Signal Timing): +0.8241 at tick 3970
- N2 (Approaching Traffic): +0.8477 at tick 4004

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T18:45:34

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T18:26:14  
**Log written:** 2026-04-06T18:45:34  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 5343 (sim_step 736)

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
| 4607 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 4608 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 4612 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 4617 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.64s |
| 4622 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.66s |
| 4647 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.78s |
| 4672 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.89s |
| 4674 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 4678 | peak energy — 1.6604e+00 |
| 4697 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.01s |
| 4698 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 4706 | peak tension N1 (Signal Timing) — +0.8241 |
| 4722 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.13s |
| 4740 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 4747 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.21s |
| 4748 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 4772 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.33s |
| 4777 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.35s |
| 4782 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.38s |
| 5343 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 4678
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 4698
- N1 (Signal Timing): +0.8241 at tick 4706
- N2 (Approaching Traffic): +0.8477 at tick 4740

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T19:04:51

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T18:45:34  
**Log written:** 2026-04-06T19:04:51  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 6079 (sim_step 736)

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
| 5343 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.58s |
| 5344 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 5348 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.59s |
| 5353 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.61s |
| 5358 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.63s |
| 5383 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.73s |
| 5408 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.81s |
| 5410 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 5414 | peak energy — 1.6604e+00 |
| 5433 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.91s |
| 5434 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 5442 | peak tension N1 (Signal Timing) — +0.8241 |
| 5458 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.03s |
| 5476 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 5483 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.14s |
| 5484 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 5508 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.25s |
| 5513 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.27s |
| 5518 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.29s |
| 6079 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 5414
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 5434
- N1 (Signal Timing): +0.8241 at tick 5442
- N2 (Approaching Traffic): +0.8477 at tick 5476

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T19:24:08

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T19:04:51  
**Log written:** 2026-04-06T19:24:08  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 6815 (sim_step 736)

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
| 6079 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 6080 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 6084 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 6089 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.65s |
| 6094 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.68s |
| 6119 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.8s |
| 6144 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.94s |
| 6146 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 6150 | peak energy — 1.6604e+00 |
| 6169 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.08s |
| 6170 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 6178 | peak tension N1 (Signal Timing) — +0.8241 |
| 6194 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.21s |
| 6212 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 6219 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.34s |
| 6220 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 6244 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.46s |
| 6249 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.49s |
| 6254 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.51s |
| 6815 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 6150
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 6170
- N1 (Signal Timing): +0.8241 at tick 6178
- N2 (Approaching Traffic): +0.8477 at tick 6212

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T19:43:23

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T19:24:08  
**Log written:** 2026-04-06T19:43:23  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 7551 (sim_step 736)

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
| 6815 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 6816 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 6820 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.61s |
| 6825 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.63s |
| 6830 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.66s |
| 6855 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.81s |
| 6880 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.95s |
| 6882 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 6886 | peak energy — 1.6604e+00 |
| 6905 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.08s |
| 6906 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 6914 | peak tension N1 (Signal Timing) — +0.8241 |
| 6930 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.23s |
| 6948 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 6955 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.37s |
| 6956 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 6980 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.51s |
| 6985 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.54s |
| 6990 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.57s |
| 7551 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 6886
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 6906
- N1 (Signal Timing): +0.8241 at tick 6914
- N2 (Approaching Traffic): +0.8477 at tick 6948

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T20:02:37

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T19:43:23  
**Log written:** 2026-04-06T20:02:37  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 8287 (sim_step 736)

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
| 7551 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 7552 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 7556 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 7561 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.64s |
| 7566 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.65s |
| 7591 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.73s |
| 7616 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.84s |
| 7618 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 7622 | peak energy — 1.6604e+00 |
| 7641 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.96s |
| 7642 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 7650 | peak tension N1 (Signal Timing) — +0.8241 |
| 7666 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.07s |
| 7684 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 7691 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.19s |
| 7692 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 7716 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.3s |
| 7721 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.33s |
| 7726 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.35s |
| 8287 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 7622
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 7642
- N1 (Signal Timing): +0.8241 at tick 7650
- N2 (Approaching Traffic): +0.8477 at tick 7684

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T20:21:51

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T20:02:37  
**Log written:** 2026-04-06T20:21:51  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 9023 (sim_step 736)

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
| 8287 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 8288 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 8292 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 8297 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.65s |
| 8302 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.68s |
| 8327 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.83s |
| 8352 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.96s |
| 8354 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 8358 | peak energy — 1.6604e+00 |
| 8377 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.11s |
| 8378 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 8386 | peak tension N1 (Signal Timing) — +0.8241 |
| 8402 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.23s |
| 8420 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 8427 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.38s |
| 8428 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 8452 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.53s |
| 8457 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.56s |
| 8462 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.59s |
| 9023 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 8358
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 8378
- N1 (Signal Timing): +0.8241 at tick 8386
- N2 (Approaching Traffic): +0.8477 at tick 8420

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T20:41:04

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T20:21:51  
**Log written:** 2026-04-06T20:41:04  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 9759 (sim_step 736)

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
| 9023 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 9024 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 9028 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 9033 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.63s |
| 9038 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.66s |
| 9063 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.77s |
| 9088 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.92s |
| 9090 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 9094 | peak energy — 1.6604e+00 |
| 9113 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.05s |
| 9114 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 9122 | peak tension N1 (Signal Timing) — +0.8241 |
| 9138 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.17s |
| 9156 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 9163 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.29s |
| 9164 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 9188 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.38s |
| 9193 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.39s |
| 9198 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.42s |
| 9759 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 9094
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 9114
- N1 (Signal Timing): +0.8241 at tick 9122
- N2 (Approaching Traffic): +0.8477 at tick 9156

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T21:00:16

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T20:41:04  
**Log written:** 2026-04-06T21:00:16  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 10495 (sim_step 736)

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
| 9759 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 9760 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 9764 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 9769 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 9774 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.68s |
| 9799 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.8s |
| 9824 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.95s |
| 9826 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 9830 | peak energy — 1.6604e+00 |
| 9849 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.07s |
| 9850 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 9858 | peak tension N1 (Signal Timing) — +0.8241 |
| 9874 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.22s |
| 9892 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 9899 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.33s |
| 9900 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 9924 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.42s |
| 9929 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.44s |
| 9934 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.46s |
| 10495 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 9830
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 9850
- N1 (Signal Timing): +0.8241 at tick 9858
- N2 (Approaching Traffic): +0.8477 at tick 9892

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T21:19:27

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T21:00:16  
**Log written:** 2026-04-06T21:19:27  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 11231 (sim_step 736)

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
| 10495 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 10496 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 10500 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 10505 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.65s |
| 10510 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.68s |
| 10535 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.8s |
| 10560 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.95s |
| 10562 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 10566 | peak energy — 1.6604e+00 |
| 10585 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.09s |
| 10586 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 10594 | peak tension N1 (Signal Timing) — +0.8241 |
| 10610 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.25s |
| 10628 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 10635 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.4s |
| 10636 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 10660 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.56s |
| 10665 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.59s |
| 10670 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.62s |
| 11231 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 10566
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 10586
- N1 (Signal Timing): +0.8241 at tick 10594
- N2 (Approaching Traffic): +0.8477 at tick 10628

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T21:38:37

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T21:19:27  
**Log written:** 2026-04-06T21:38:37  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 11967 (sim_step 736)

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
| 11231 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 11232 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 11236 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 11241 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.64s |
| 11246 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.65s |
| 11271 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.8s |
| 11296 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.95s |
| 11298 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 11302 | peak energy — 1.6604e+00 |
| 11321 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.1s |
| 11322 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 11330 | peak tension N1 (Signal Timing) — +0.8241 |
| 11346 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.25s |
| 11364 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 11371 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.4s |
| 11372 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 11396 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.54s |
| 11401 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.57s |
| 11406 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.6s |
| 11967 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 11302
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 11322
- N1 (Signal Timing): +0.8241 at tick 11330
- N2 (Approaching Traffic): +0.8477 at tick 11364

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T21:57:46

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T21:38:37  
**Log written:** 2026-04-06T21:57:46  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 12703 (sim_step 736)

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
| 11967 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 11968 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 11972 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 11977 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 11982 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.69s |
| 12007 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.85s |
| 12032 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.03s |
| 12034 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 12038 | peak energy — 1.6604e+00 |
| 12057 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.19s |
| 12058 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 12066 | peak tension N1 (Signal Timing) — +0.8241 |
| 12082 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.36s |
| 12100 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 12107 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.52s |
| 12108 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 12132 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.67s |
| 12137 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.69s |
| 12142 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.72s |
| 12703 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 12038
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 12058
- N1 (Signal Timing): +0.8241 at tick 12066
- N2 (Approaching Traffic): +0.8477 at tick 12100

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T22:16:53

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T21:57:46  
**Log written:** 2026-04-06T22:16:53  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 13439 (sim_step 736)

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
| 12703 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 12704 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 12708 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 12713 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 12718 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.68s |
| 12743 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.82s |
| 12768 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.93s |
| 12770 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 12774 | peak energy — 1.6604e+00 |
| 12793 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.06s |
| 12794 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 12802 | peak tension N1 (Signal Timing) — +0.8241 |
| 12818 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.2s |
| 12836 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 12843 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.34s |
| 12844 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 12868 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.49s |
| 12873 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.53s |
| 12878 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.56s |
| 13439 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 12774
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 12794
- N1 (Signal Timing): +0.8241 at tick 12802
- N2 (Approaching Traffic): +0.8477 at tick 12836

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T22:36:00

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T22:16:53  
**Log written:** 2026-04-06T22:36:00  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 14175 (sim_step 736)

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
| 13439 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 13440 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 13444 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 13449 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.64s |
| 13454 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.67s |
| 13479 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.82s |
| 13504 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.98s |
| 13506 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 13510 | peak energy — 1.6604e+00 |
| 13529 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.15s |
| 13530 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 13538 | peak tension N1 (Signal Timing) — +0.8241 |
| 13554 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.3s |
| 13572 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 13579 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.49s |
| 13580 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 13604 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.65s |
| 13609 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.68s |
| 13614 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.71s |
| 14175 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 13510
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 13530
- N1 (Signal Timing): +0.8241 at tick 13538
- N2 (Approaching Traffic): +0.8477 at tick 13572

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T22:55:06

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T22:36:00  
**Log written:** 2026-04-06T22:55:06  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 14911 (sim_step 736)

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
| 14175 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 14176 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 14180 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 14185 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 14190 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.71s |
| 14215 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.85s |
| 14240 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.04s |
| 14242 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 14246 | peak energy — 1.6604e+00 |
| 14265 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.21s |
| 14266 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 14274 | peak tension N1 (Signal Timing) — +0.8241 |
| 14290 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.37s |
| 14308 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 14315 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.5s |
| 14316 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 14340 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.66s |
| 14345 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.69s |
| 14350 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.72s |
| 14911 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 14246
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 14266
- N1 (Signal Timing): +0.8241 at tick 14274
- N2 (Approaching Traffic): +0.8477 at tick 14308

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T23:14:09

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T22:55:06  
**Log written:** 2026-04-06T23:14:09  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 15647 (sim_step 736)

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
| 14911 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 14912 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 14916 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.62s |
| 14921 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 14926 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.7s |
| 14951 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.89s |
| 14976 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.06s |
| 14978 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 14982 | peak energy — 1.6604e+00 |
| 15001 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.22s |
| 15002 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 15010 | peak tension N1 (Signal Timing) — +0.8241 |
| 15026 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.39s |
| 15044 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 15051 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.57s |
| 15052 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 15076 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.75s |
| 15081 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.79s |
| 15086 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.84s |
| 15647 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 14982
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 15002
- N1 (Signal Timing): +0.8241 at tick 15010
- N2 (Approaching Traffic): +0.8477 at tick 15044

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T23:33:12

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T23:14:09  
**Log written:** 2026-04-06T23:33:12  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 16383 (sim_step 736)

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
| 15647 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 15648 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 15652 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 15657 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 15662 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.7s |
| 15687 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.85s |
| 15712 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.0s |
| 15714 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 15718 | peak energy — 1.6604e+00 |
| 15737 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.18s |
| 15738 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 15746 | peak tension N1 (Signal Timing) — +0.8241 |
| 15762 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.38s |
| 15780 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 15787 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.55s |
| 15788 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 15812 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.74s |
| 15817 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.78s |
| 15822 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.81s |
| 16383 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 15718
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 15738
- N1 (Signal Timing): +0.8241 at tick 15746
- N2 (Approaching Traffic): +0.8477 at tick 15780

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-06T23:52:15

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T23:33:12  
**Log written:** 2026-04-06T23:52:15  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 17119 (sim_step 736)

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
| 16383 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 16384 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 16388 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 16393 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 16398 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.7s |
| 16423 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.87s |
| 16448 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.04s |
| 16450 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 16454 | peak energy — 1.6604e+00 |
| 16473 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.18s |
| 16474 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 16482 | peak tension N1 (Signal Timing) — +0.8241 |
| 16498 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.32s |
| 16516 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 16523 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.5s |
| 16524 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 16548 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.67s |
| 16553 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.7s |
| 16558 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.74s |
| 17119 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 16454
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 16474
- N1 (Signal Timing): +0.8241 at tick 16482
- N2 (Approaching Traffic): +0.8477 at tick 16516

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T00:11:16

**Scenario:** stadium_shock  
**Run started:** 2026-04-06T23:52:15  
**Log written:** 2026-04-07T00:11:16  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 17855 (sim_step 736)

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
| 17119 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 17120 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 17124 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 17129 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 17134 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.72s |
| 17159 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.88s |
| 17184 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.05s |
| 17186 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 17190 | peak energy — 1.6604e+00 |
| 17209 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.24s |
| 17210 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 17218 | peak tension N1 (Signal Timing) — +0.8241 |
| 17234 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.43s |
| 17252 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 17259 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.58s |
| 17260 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 17284 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.73s |
| 17289 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.76s |
| 17294 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.8s |
| 17855 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 17190
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 17210
- N1 (Signal Timing): +0.8241 at tick 17218
- N2 (Approaching Traffic): +0.8477 at tick 17252

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T00:30:16

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T00:11:16  
**Log written:** 2026-04-07T00:30:16  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 18591 (sim_step 736)

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
| 17855 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 17856 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 17860 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 17865 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.66s |
| 17870 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.69s |
| 17895 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.88s |
| 17920 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.07s |
| 17922 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 17926 | peak energy — 1.6604e+00 |
| 17945 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.25s |
| 17946 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 17954 | peak tension N1 (Signal Timing) — +0.8241 |
| 17970 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.46s |
| 17988 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 17995 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.63s |
| 17996 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 18020 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.81s |
| 18025 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.85s |
| 18030 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.89s |
| 18591 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 17926
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 17946
- N1 (Signal Timing): +0.8241 at tick 17954
- N2 (Approaching Traffic): +0.8477 at tick 17988

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T00:49:14

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T00:30:16  
**Log written:** 2026-04-07T00:49:14  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 19327 (sim_step 736)

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
| 18591 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 18592 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 18596 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 18601 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.69s |
| 18606 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.72s |
| 18631 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.91s |
| 18656 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.1s |
| 18658 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 18662 | peak energy — 1.6604e+00 |
| 18681 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.33s |
| 18682 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 18690 | peak tension N1 (Signal Timing) — +0.8241 |
| 18706 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.54s |
| 18724 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 18731 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.72s |
| 18732 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 18756 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.9s |
| 18761 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.94s |
| 18766 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.98s |
| 19327 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 18662
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 18682
- N1 (Signal Timing): +0.8241 at tick 18690
- N2 (Approaching Traffic): +0.8477 at tick 18724

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T01:08:14

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T00:49:14  
**Log written:** 2026-04-07T01:08:14  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 20063 (sim_step 736)

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
| 19327 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 19328 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 19332 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 19337 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 19342 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.72s |
| 19367 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.87s |
| 19392 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.04s |
| 19394 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 19398 | peak energy — 1.6604e+00 |
| 19417 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.24s |
| 19418 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 19426 | peak tension N1 (Signal Timing) — +0.8241 |
| 19442 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.47s |
| 19460 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 19467 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.69s |
| 19468 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 19492 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.89s |
| 19497 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.94s |
| 19502 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.99s |
| 20063 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 19398
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 19418
- N1 (Signal Timing): +0.8241 at tick 19426
- N2 (Approaching Traffic): +0.8477 at tick 19460

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T01:27:11

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T01:08:14  
**Log written:** 2026-04-07T01:27:11  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 20799 (sim_step 736)

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
| 20063 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 20064 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 20068 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 20073 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.69s |
| 20078 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.73s |
| 20103 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.96s |
| 20128 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.19s |
| 20130 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 20134 | peak energy — 1.6604e+00 |
| 20153 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.41s |
| 20154 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 20162 | peak tension N1 (Signal Timing) — +0.8241 |
| 20178 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.64s |
| 20196 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 20203 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.86s |
| 20204 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 20228 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.07s |
| 20233 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.11s |
| 20238 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.14s |
| 20799 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 20134
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 20154
- N1 (Signal Timing): +0.8241 at tick 20162
- N2 (Approaching Traffic): +0.8477 at tick 20196

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T01:46:07

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T01:27:11  
**Log written:** 2026-04-07T01:46:07  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 21535 (sim_step 736)

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
| 20799 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 20800 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 20804 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 20809 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 20814 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.71s |
| 20839 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.91s |
| 20864 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.08s |
| 20866 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 20870 | peak energy — 1.6604e+00 |
| 20889 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.21s |
| 20890 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 20898 | peak tension N1 (Signal Timing) — +0.8241 |
| 20914 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.43s |
| 20932 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 20939 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.65s |
| 20940 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 20964 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.87s |
| 20969 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.91s |
| 20974 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.95s |
| 21535 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 20870
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 20890
- N1 (Signal Timing): +0.8241 at tick 20898
- N2 (Approaching Traffic): +0.8477 at tick 20932

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T02:05:01

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T01:46:07  
**Log written:** 2026-04-07T02:05:01  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 22271 (sim_step 736)

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
| 21535 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 21536 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 21540 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 21545 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.69s |
| 21550 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.73s |
| 21575 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.94s |
| 21600 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.17s |
| 21602 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 21606 | peak energy — 1.6604e+00 |
| 21625 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.36s |
| 21626 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 21634 | peak tension N1 (Signal Timing) — +0.8241 |
| 21650 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.51s |
| 21668 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 21675 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.65s |
| 21676 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 21700 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.83s |
| 21705 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.88s |
| 21710 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.92s |
| 22271 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 21606
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 21626
- N1 (Signal Timing): +0.8241 at tick 21634
- N2 (Approaching Traffic): +0.8477 at tick 21668

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T02:23:54

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T02:05:01  
**Log written:** 2026-04-07T02:23:54  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 23007 (sim_step 736)

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
| 22271 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 22272 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 22276 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 22281 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 22286 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.69s |
| 22311 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.88s |
| 22336 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.04s |
| 22338 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 22342 | peak energy — 1.6604e+00 |
| 22361 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.14s |
| 22362 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 22370 | peak tension N1 (Signal Timing) — +0.8241 |
| 22386 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.3s |
| 22404 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 22411 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.45s |
| 22412 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 22436 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.61s |
| 22441 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.63s |
| 22446 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+282.67s |
| 23007 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 22342
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 22362
- N1 (Signal Timing): +0.8241 at tick 22370
- N2 (Approaching Traffic): +0.8477 at tick 22404

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T02:42:47

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T02:23:54  
**Log written:** 2026-04-07T02:42:47  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 23743 (sim_step 736)

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
| 23007 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 23008 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 23012 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 23017 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.68s |
| 23022 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.73s |
| 23047 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.94s |
| 23072 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.21s |
| 23074 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 23078 | peak energy — 1.6604e+00 |
| 23097 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.45s |
| 23098 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 23106 | peak tension N1 (Signal Timing) — +0.8241 |
| 23122 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.7s |
| 23140 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 23147 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.9s |
| 23148 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 23172 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.11s |
| 23177 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.15s |
| 23182 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.19s |
| 23743 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 23078
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 23098
- N1 (Signal Timing): +0.8241 at tick 23106
- N2 (Approaching Traffic): +0.8477 at tick 23140

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T03:01:38

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T02:42:47  
**Log written:** 2026-04-07T03:01:38  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 24479 (sim_step 736)

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
| 23743 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 23744 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 23748 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 23753 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.69s |
| 23758 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.72s |
| 23783 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.91s |
| 23808 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.11s |
| 23810 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 23814 | peak energy — 1.6604e+00 |
| 23833 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.31s |
| 23834 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 23842 | peak tension N1 (Signal Timing) — +0.8241 |
| 23858 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.53s |
| 23876 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 23883 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.76s |
| 23884 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 23908 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.99s |
| 23913 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.04s |
| 23918 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.08s |
| 24479 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 23814
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 23834
- N1 (Signal Timing): +0.8241 at tick 23842
- N2 (Approaching Traffic): +0.8477 at tick 23876

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T03:20:31

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T03:01:38  
**Log written:** 2026-04-07T03:20:31  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 25215 (sim_step 736)

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
| 24479 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 24480 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 24484 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 24489 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.68s |
| 24494 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.74s |
| 24519 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.95s |
| 24544 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.16s |
| 24546 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 24550 | peak energy — 1.6604e+00 |
| 24569 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.36s |
| 24570 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 24578 | peak tension N1 (Signal Timing) — +0.8241 |
| 24594 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.51s |
| 24612 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 24619 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.7s |
| 24620 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 24644 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.91s |
| 24649 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+274.97s |
| 24654 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.02s |
| 25215 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 24550
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 24570
- N1 (Signal Timing): +0.8241 at tick 24578
- N2 (Approaching Traffic): +0.8477 at tick 24612

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T03:39:22

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T03:20:31  
**Log written:** 2026-04-07T03:39:22  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 25951 (sim_step 736)

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
| 25215 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 25216 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 25220 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 25225 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 25230 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.76s |
| 25255 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.99s |
| 25280 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.22s |
| 25282 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 25286 | peak energy — 1.6604e+00 |
| 25305 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.4s |
| 25306 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 25314 | peak tension N1 (Signal Timing) — +0.8241 |
| 25330 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.61s |
| 25348 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 25355 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.83s |
| 25356 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 25380 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.02s |
| 25385 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.05s |
| 25390 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.09s |
| 25951 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 25286
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 25306
- N1 (Signal Timing): +0.8241 at tick 25314
- N2 (Approaching Traffic): +0.8477 at tick 25348

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T03:58:11

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T03:39:22  
**Log written:** 2026-04-07T03:58:11  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 26687 (sim_step 736)

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
| 25951 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 25952 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 25956 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 25961 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 25966 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.76s |
| 25991 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.03s |
| 26016 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.29s |
| 26018 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 26022 | peak energy — 1.6604e+00 |
| 26041 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.51s |
| 26042 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 26050 | peak tension N1 (Signal Timing) — +0.8241 |
| 26066 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.69s |
| 26084 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 26091 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.91s |
| 26092 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 26116 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.08s |
| 26121 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.12s |
| 26126 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.16s |
| 26687 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 26022
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 26042
- N1 (Signal Timing): +0.8241 at tick 26050
- N2 (Approaching Traffic): +0.8477 at tick 26084

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T04:16:59

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T03:58:11  
**Log written:** 2026-04-07T04:16:59  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 27423 (sim_step 736)

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
| 26687 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 26688 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 26692 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 26697 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 26702 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.75s |
| 26727 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.02s |
| 26752 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.28s |
| 26754 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 26758 | peak energy — 1.6604e+00 |
| 26777 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.52s |
| 26778 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 26786 | peak tension N1 (Signal Timing) — +0.8241 |
| 26802 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.73s |
| 26820 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 26827 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.99s |
| 26828 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 26852 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.24s |
| 26857 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.28s |
| 26862 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.34s |
| 27423 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 26758
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 26778
- N1 (Signal Timing): +0.8241 at tick 26786
- N2 (Approaching Traffic): +0.8477 at tick 26820

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T04:35:46

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T04:16:59  
**Log written:** 2026-04-07T04:35:46  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 28159 (sim_step 736)

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
| 27423 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 27424 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 27428 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 27433 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.72s |
| 27438 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.78s |
| 27463 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.07s |
| 27488 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.31s |
| 27490 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 27494 | peak energy — 1.6604e+00 |
| 27513 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.58s |
| 27514 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 27522 | peak tension N1 (Signal Timing) — +0.8241 |
| 27538 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.87s |
| 27556 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 27563 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.13s |
| 27564 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 27588 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.39s |
| 27593 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.45s |
| 27598 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.5s |
| 28159 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 27494
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 27514
- N1 (Signal Timing): +0.8241 at tick 27522
- N2 (Approaching Traffic): +0.8477 at tick 27556

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T04:54:32

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T04:35:46  
**Log written:** 2026-04-07T04:54:32  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 28895 (sim_step 736)

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
| 28159 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 28160 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 28164 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 28169 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.69s |
| 28174 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.76s |
| 28199 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.99s |
| 28224 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.19s |
| 28226 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 28230 | peak energy — 1.6604e+00 |
| 28249 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.4s |
| 28250 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 28258 | peak tension N1 (Signal Timing) — +0.8241 |
| 28274 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.58s |
| 28292 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 28299 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.75s |
| 28300 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 28324 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+266.98s |
| 28329 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.03s |
| 28334 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.07s |
| 28895 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 28230
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 28250
- N1 (Signal Timing): +0.8241 at tick 28258
- N2 (Approaching Traffic): +0.8477 at tick 28292

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T05:13:18

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T04:54:32  
**Log written:** 2026-04-07T05:13:18  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 29631 (sim_step 736)

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
| 28895 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 28896 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 28900 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 28905 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.68s |
| 28910 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.73s |
| 28935 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.95s |
| 28960 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.18s |
| 28962 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 28966 | peak energy — 1.6604e+00 |
| 28985 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.44s |
| 28986 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 28994 | peak tension N1 (Signal Timing) — +0.8241 |
| 29010 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.71s |
| 29028 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 29035 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.94s |
| 29036 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 29060 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.2s |
| 29065 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.25s |
| 29070 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.3s |
| 29631 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 28966
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 28986
- N1 (Signal Timing): +0.8241 at tick 28994
- N2 (Approaching Traffic): +0.8477 at tick 29028

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T05:32:01

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T05:13:18  
**Log written:** 2026-04-07T05:32:01  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 30367 (sim_step 736)

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
| 29631 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 29632 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 29636 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 29641 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 29646 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.74s |
| 29671 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.02s |
| 29696 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.28s |
| 29698 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 29702 | peak energy — 1.6604e+00 |
| 29721 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.57s |
| 29722 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 29730 | peak tension N1 (Signal Timing) — +0.8241 |
| 29746 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.77s |
| 29764 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 29771 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.01s |
| 29772 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 29796 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.24s |
| 29801 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.27s |
| 29806 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.32s |
| 30367 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 29702
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 29722
- N1 (Signal Timing): +0.8241 at tick 29730
- N2 (Approaching Traffic): +0.8477 at tick 29764

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T05:50:45

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T05:32:01  
**Log written:** 2026-04-07T05:50:45  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 31103 (sim_step 736)

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
| 30367 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.61s |
| 30368 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 30372 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 30377 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.71s |
| 30382 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.77s |
| 30407 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.02s |
| 30432 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.24s |
| 30434 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 30438 | peak energy — 1.6604e+00 |
| 30457 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.47s |
| 30458 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 30466 | peak tension N1 (Signal Timing) — +0.8241 |
| 30482 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.72s |
| 30500 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 30507 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.93s |
| 30508 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 30532 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.12s |
| 30537 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.14s |
| 30542 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.18s |
| 31103 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 30438
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 30458
- N1 (Signal Timing): +0.8241 at tick 30466
- N2 (Approaching Traffic): +0.8477 at tick 30500

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T06:09:26

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T05:50:45  
**Log written:** 2026-04-07T06:09:26  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 31839 (sim_step 736)

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
| 31103 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 31104 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 31108 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 31113 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.72s |
| 31118 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.79s |
| 31143 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.09s |
| 31168 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.36s |
| 31170 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 31174 | peak energy — 1.6604e+00 |
| 31193 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.53s |
| 31194 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 31202 | peak tension N1 (Signal Timing) — +0.8241 |
| 31218 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.73s |
| 31236 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 31243 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.03s |
| 31244 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 31268 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.33s |
| 31273 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.38s |
| 31278 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.43s |
| 31839 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 31174
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 31194
- N1 (Signal Timing): +0.8241 at tick 31202
- N2 (Approaching Traffic): +0.8477 at tick 31236

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T06:28:07

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T06:09:26  
**Log written:** 2026-04-07T06:28:07  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 32575 (sim_step 736)

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
| 31839 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 31840 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 31844 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 31849 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.71s |
| 31854 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.75s |
| 31879 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.01s |
| 31904 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.29s |
| 31906 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 31910 | peak energy — 1.6604e+00 |
| 31929 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.56s |
| 31930 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 31938 | peak tension N1 (Signal Timing) — +0.8241 |
| 31954 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.8s |
| 31972 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 31979 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.01s |
| 31980 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 32004 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.26s |
| 32009 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.33s |
| 32014 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.38s |
| 32575 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 31910
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 31930
- N1 (Signal Timing): +0.8241 at tick 31938
- N2 (Approaching Traffic): +0.8477 at tick 31972

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T06:46:48

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T06:28:07  
**Log written:** 2026-04-07T06:46:48  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 33311 (sim_step 736)

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
| 32575 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 32576 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 32580 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 32585 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.71s |
| 32590 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.78s |
| 32615 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.05s |
| 32640 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.28s |
| 32642 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 32646 | peak energy — 1.6604e+00 |
| 32665 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.52s |
| 32666 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 32674 | peak tension N1 (Signal Timing) — +0.8241 |
| 32690 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.78s |
| 32708 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 32715 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.04s |
| 32716 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 32740 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.31s |
| 32745 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.37s |
| 32750 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.43s |
| 33311 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 32646
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 32666
- N1 (Signal Timing): +0.8241 at tick 32674
- N2 (Approaching Traffic): +0.8477 at tick 32708

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T07:05:27

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T06:46:48  
**Log written:** 2026-04-07T07:05:27  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 34047 (sim_step 736)

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
| 33311 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.61s |
| 33312 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 33316 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.68s |
| 33321 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.75s |
| 33326 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.81s |
| 33351 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.01s |
| 33376 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.35s |
| 33378 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 33382 | peak energy — 1.6604e+00 |
| 33401 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.64s |
| 33402 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 33410 | peak tension N1 (Signal Timing) — +0.8241 |
| 33426 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.92s |
| 33444 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 33451 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.14s |
| 33452 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 33476 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.37s |
| 33481 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.42s |
| 33486 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.48s |
| 34047 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 33382
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 33402
- N1 (Signal Timing): +0.8241 at tick 33410
- N2 (Approaching Traffic): +0.8477 at tick 33444

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T07:24:06

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T07:05:27  
**Log written:** 2026-04-07T07:24:06  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 34783 (sim_step 736)

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
| 34047 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 34048 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 34052 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 34057 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.67s |
| 34062 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.7s |
| 34087 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.98s |
| 34112 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.27s |
| 34114 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 34118 | peak energy — 1.6604e+00 |
| 34137 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.54s |
| 34138 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 34146 | peak tension N1 (Signal Timing) — +0.8241 |
| 34162 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.75s |
| 34180 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 34187 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.02s |
| 34188 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 34212 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.35s |
| 34217 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.41s |
| 34222 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.48s |
| 34783 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 34118
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 34138
- N1 (Signal Timing): +0.8241 at tick 34146
- N2 (Approaching Traffic): +0.8477 at tick 34180

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T07:42:43

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T07:24:06  
**Log written:** 2026-04-07T07:42:43  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 35519 (sim_step 736)

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
| 34783 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.61s |
| 34784 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 34788 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 34793 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 34798 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.76s |
| 34823 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.01s |
| 34848 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.26s |
| 34850 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 34854 | peak energy — 1.6604e+00 |
| 34873 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.5s |
| 34874 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 34882 | peak tension N1 (Signal Timing) — +0.8241 |
| 34898 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.82s |
| 34916 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 34923 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.11s |
| 34924 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 34948 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.42s |
| 34953 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.48s |
| 34958 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.55s |
| 35519 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 34854
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 34874
- N1 (Signal Timing): +0.8241 at tick 34882
- N2 (Approaching Traffic): +0.8477 at tick 34916

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T08:01:20

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T07:42:43  
**Log written:** 2026-04-07T08:01:20  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 36255 (sim_step 736)

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
| 35519 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 35520 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 35524 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.65s |
| 35529 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.72s |
| 35534 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.78s |
| 35559 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.08s |
| 35584 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.33s |
| 35586 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 35590 | peak energy — 1.6604e+00 |
| 35609 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.63s |
| 35610 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 35618 | peak tension N1 (Signal Timing) — +0.8241 |
| 35634 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.94s |
| 35652 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 35659 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.2s |
| 35660 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 35684 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.44s |
| 35689 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.47s |
| 35694 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.53s |
| 36255 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 35590
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 35610
- N1 (Signal Timing): +0.8241 at tick 35618
- N2 (Approaching Traffic): +0.8477 at tick 35652

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T08:19:55

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T08:01:20  
**Log written:** 2026-04-07T08:19:55  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 36991 (sim_step 736)

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
| 36255 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 36256 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 36260 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 36265 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.71s |
| 36270 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.78s |
| 36295 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.09s |
| 36320 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.39s |
| 36322 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 36326 | peak energy — 1.6604e+00 |
| 36345 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.68s |
| 36346 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 36354 | peak tension N1 (Signal Timing) — +0.8241 |
| 36370 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.95s |
| 36388 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 36395 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.22s |
| 36396 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 36420 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.41s |
| 36425 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.43s |
| 36430 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.47s |
| 36991 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 36326
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 36346
- N1 (Signal Timing): +0.8241 at tick 36354
- N2 (Approaching Traffic): +0.8477 at tick 36388

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T08:38:29

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T08:19:55  
**Log written:** 2026-04-07T08:38:29  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 37727 (sim_step 736)

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
| 36991 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 36992 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 36996 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.63s |
| 37001 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.68s |
| 37006 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.74s |
| 37031 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.99s |
| 37056 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.29s |
| 37058 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 37062 | peak energy — 1.6604e+00 |
| 37081 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.51s |
| 37082 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 37090 | peak tension N1 (Signal Timing) — +0.8241 |
| 37106 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.71s |
| 37124 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 37131 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.99s |
| 37132 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 37156 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.24s |
| 37161 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.29s |
| 37166 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.35s |
| 37727 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 37062
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 37082
- N1 (Signal Timing): +0.8241 at tick 37090
- N2 (Approaching Traffic): +0.8477 at tick 37124

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T08:57:02

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T08:38:29  
**Log written:** 2026-04-07T08:57:02  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 38463 (sim_step 736)

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
| 37727 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.61s |
| 37728 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 37732 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 37737 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.72s |
| 37742 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.78s |
| 37767 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.03s |
| 37792 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.28s |
| 37794 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 37798 | peak energy — 1.6604e+00 |
| 37817 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.52s |
| 37818 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 37826 | peak tension N1 (Signal Timing) — +0.8241 |
| 37842 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.75s |
| 37860 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 37867 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+226.97s |
| 37868 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 37892 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.25s |
| 37897 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.32s |
| 37902 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.36s |
| 38463 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 37798
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 37818
- N1 (Signal Timing): +0.8241 at tick 37826
- N2 (Approaching Traffic): +0.8477 at tick 37860

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T09:15:37

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T08:57:02  
**Log written:** 2026-04-07T09:15:37  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 39199 (sim_step 736)

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
| 38463 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 38464 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 38468 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.64s |
| 38473 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.7s |
| 38478 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.75s |
| 38503 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.93s |
| 38528 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.11s |
| 38530 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 38534 | peak energy — 1.6604e+00 |
| 38553 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.38s |
| 38554 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 38562 | peak tension N1 (Signal Timing) — +0.8241 |
| 38578 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+186.7s |
| 38596 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 38603 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.02s |
| 38604 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 38628 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.34s |
| 38633 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.4s |
| 38638 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.44s |
| 39199 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 38534
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 38554
- N1 (Signal Timing): +0.8241 at tick 38562
- N2 (Approaching Traffic): +0.8477 at tick 38596

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T09:34:35

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T09:15:37  
**Log written:** 2026-04-07T09:34:35  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 39935 (sim_step 736)

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
| 39199 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.6s |
| 39200 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 39204 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.66s |
| 39209 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.73s |
| 39214 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.79s |
| 39239 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+66.09s |
| 39264 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+106.4s |
| 39266 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 39270 | peak energy — 1.6604e+00 |
| 39289 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+146.69s |
| 39290 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 39298 | peak tension N1 (Signal Timing) — +0.8241 |
| 39314 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+187.0s |
| 39332 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 39339 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+227.35s |
| 39340 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 39364 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+267.66s |
| 39369 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+275.72s |
| 39374 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+283.79s |
| 39935 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 39270
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 39290
- N1 (Signal Timing): +0.8241 at tick 39298
- N2 (Approaching Traffic): +0.8477 at tick 39332

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T09:54:13

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T09:34:35  
**Log written:** 2026-04-07T09:54:13  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 40671 (sim_step 736)

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
| 39935 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 39936 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 39940 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.6s |
| 39945 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.61s |
| 39950 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.62s |
| 39975 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.64s |
| 40000 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.67s |
| 40002 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 40006 | peak energy — 1.6604e+00 |
| 40025 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.7s |
| 40026 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 40034 | peak tension N1 (Signal Timing) — +0.8241 |
| 40050 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.72s |
| 40068 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 40075 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.76s |
| 40076 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 40100 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.78s |
| 40105 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.79s |
| 40110 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.8s |
| 40671 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 40006
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 40026
- N1 (Signal Timing): +0.8241 at tick 40034
- N2 (Approaching Traffic): +0.8477 at tick 40068

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
## Run — 2026-04-07T10:13:52

**Scenario:** stadium_shock  
**Run started:** 2026-04-07T09:54:13  
**Log written:** 2026-04-07T10:13:52  
**Duration:** 736 ticks (73.6s wall at 1x speed)  
**Ticks at log time:** 41407 (sim_step 736)

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
| 40671 | perturbation injected — sim_step=0, delta=[-0.065 -0.035 -0.001], t+1.59s |
| 40672 | run start — energy=3.0710e-03, tensions=[-0.0648, -0.0352, -0.0011] |
| 40676 | perturbation injected — sim_step=5, delta=[+0.099 -0.001 +0.024], t+9.6s |
| 40681 | perturbation injected — sim_step=10, delta=[+0.008 +0.006 -0.016], t+17.61s |
| 40686 | perturbation injected — sim_step=15, delta=[-0.011 -0.103 -0.045], t+25.62s |
| 40711 | perturbation injected — sim_step=40, delta=[+0.070 -0.033 +0.133], t+65.65s |
| 40736 | perturbation injected — sim_step=65, delta=[+0.016 -0.231 +0.392], t+105.68s |
| 40738 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8027, velocity=-0.8068 |
| 40742 | peak energy — 1.6604e+00 |
| 40761 | perturbation injected — sim_step=90, delta=[+0.131 -0.053 -0.055], t+145.72s |
| 40762 | peak tension N0 (Intersection Throughput) — +0.5543 |
| 40770 | peak tension N1 (Signal Timing) — +0.8241 |
| 40786 | perturbation injected — sim_step=115, delta=[+0.131 -0.061 -0.056], t+185.75s |
| 40804 | peak tension N2 (Approaching Traffic) — +0.8477 |
| 40811 | perturbation injected — sim_step=140, delta=[+0.034 -0.023 +0.138], t+225.77s |
| 40812 | INCOHERENCE — N2 (Approaching Traffic), tension=+0.8357, velocity=-0.6282 |
| 40836 | perturbation injected — sim_step=165, delta=[-0.020 -0.026 +0.081], t+265.81s |
| 40841 | perturbation injected — sim_step=170, delta=[+0.030 -0.000 +0.071], t+273.82s |
| 40846 | perturbation injected — sim_step=175, delta=[-0.087 +0.051 +0.003], t+281.83s |
| 41407 | snapshot — energy=1.0000e-04, total_tension=0.6157, tensions=[0.2051, 0.205, 0.2055] |

### Summary Statistics

**Energy trajectory:**
- Start: 3.0710e-03
- Peak: 1.6604e+00 at tick 40742
- Final: 1.0000e-04
- Total dissipated (peak -> final): 1.6603e+00

**Peak tension per node:**
- N0 (Intersection Throughput): +0.5543 at tick 40762
- N1 (Signal Timing): +0.8241 at tick 40770
- N2 (Approaching Traffic): +0.8477 at tick 40804

**Perturbations injected:** 36 (across 736 sim steps)

**Incoherence events:** 2 total (N2=2)

**Recovery (energy to 1% of peak):** ~332 ticks (33.2s at 1x speed)

### Qualitative Assessment

_(Fill in manually after observation.)_

- Wave propagation character:
- Damping behavior observed:
- Node most affected:
- Recovery quality:
- Notes:

---
