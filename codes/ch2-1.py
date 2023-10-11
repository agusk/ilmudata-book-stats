import numpy as np
import pandas as pd

data = [250, 300, 280, 275, 310, 320, 265]

mean = np.mean(data)
print(f"Mean: {mean:.2f}")

median = np.median(data)
print(f"Median: {median}")

(values, counts) = np.unique(data, return_counts=True)
index = np.argmax(counts)
mode = values[index]
print(f"Mode: {mode}")


range_val = np.max(data) - np.min(data)
print(f"Range: {range_val}")

variance = np.var(data, ddof=1)  # ddof=1 menunjukkan kita menggunakan sampel variansi
print(f"Variance: {variance:.2f}")

std_dev = np.std(data, ddof=1)
print(f"Standard Deviation: {std_dev:.2f}")


q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
print(f"Q1: {q1}")
print(f"Q2 (Median): {q2}")
print(f"Q3: {q3}")