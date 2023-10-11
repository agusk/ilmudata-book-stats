versi_A = {"pengunjung": 1000, "konversi": 120}
versi_B = {"pengunjung": 980, "konversi": 145}
tingkat_konversi_A = versi_A["konversi"] / versi_A["pengunjung"]
tingkat_konversi_B = versi_B["konversi"] / versi_B["pengunjung"]

print(f"Tingkat Konversi A: {tingkat_konversi_A:.2%}")
print(f"Tingkat Konversi B: {tingkat_konversi_B:.2%}")


from statsmodels.stats.proportion import proportions_ztest

hitung = [versi_A["konversi"], versi_B["konversi"]]
n_obs = [versi_A["pengunjung"], versi_B["pengunjung"]]

z_stat, p_val = proportions_ztest(hitung, n_obs)
print(f"Nilai z: {z_stat:.2f}")
print(f"p-value: {p_val:.4f}")

alpha = 0.05
if p_val < alpha:
    print("Tolak hipotesis nol. Ada perbedaan signifikan antara tingkat konversi Versi A dan Versi B!")
else:
    print("Terima hipotesis nol. Tidak ada perbedaan signifikan antara tingkat konversi Versi A dan Versi B.")


import matplotlib.pyplot as plt

labels = ['Versi A', 'Versi B']
konversi_rates = [tingkat_konversi_A, tingkat_konversi_B]

plt.bar(labels, konversi_rates, color=['blue', 'green'])
plt.ylabel('Tingkat Konversi')
plt.title('Perbandingan Tingkat Konversi Versi A dan Versi B')
plt.ylim([0, max(konversi_rates) + 0.05])
for i, v in enumerate(konversi_rates):
    plt.text(i, v + 0.01, f"{v:.2%}", ha='center')
plt.show()    