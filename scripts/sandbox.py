import numpy as np
from sklearn.model_selection import KFold
from sklearn.base import clone
from sklearn.metrics import r2_score


# Count total iterations
increments=0.001
num_steps = int(1 / increments) + 1
total_iterations = (num_steps * (num_steps + 1)) // 2  # Sum of arithmetic series
iteration_count = 0
last_reported_progress = 0

for w1 in np.arange(0, 1 + increments, increments):
    for w2 in np.arange(0, 1 + increments, increments):
        w3 = 1 - w1 - w2
        if w3 < 0:
            continue
        # blend = w1 * predsA_oof + w2 * predsB_oof + w3 * predsC_oof
        # r2_ens = r2_score(y, blend)
        # if r2_ens > best_r2:
        #     best_r2 = r2_ens
        #     best_combo = (w1, w2, w3)
        # Track progress
        iteration_count += 1
        progress = (iteration_count / total_iterations) * 100
        if round(progress) > last_reported_progress:
            last_reported_progress = round(progress)
            print(f"Progress: {last_reported_progress}%")