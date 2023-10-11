x = [2, 3, 1, 4, 3, 5, 2, 6, 3, 4]
y = [50, 55, 48, 62, 58, 68, 52, 72, 54, 60]


import numpy as np
import matplotlib.pyplot as plt

# Data
x = [2, 3, 1, 4, 3, 5, 2, 6, 3, 4]
y = [50, 55, 48, 62, 58, 68, 52, 72, 54, 60]

# Menghitung koefisien korelasi
r = np.corrcoef(x, y)[0, 1]
print(f"Koefisien Korelasi: {r:.2f}")

# Menghitung koefisien regresi linier
b = r * (np.std(y) / np.std(x))
a = np.mean(y) - b * np.mean(x)
print(f"Koefisien a: {a:.2f}, Koefisien b: {b:.2f}")

# Visualisasi
plt.scatter(x, y, color='blue')
plt.plot(x, a + b * np.array(x), color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresi Linier Sederhana')
plt.savefig('regresi.png')
plt.show()