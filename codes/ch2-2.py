import numpy as np
import matplotlib.pyplot as plt

# Buat dataset (angka sembarang antara 50-100 untuk 100 siswa)
np.random.seed(42)  # seed untuk reproduktifitas
data = np.random.randint(50, 101, 100)

plt.hist(data, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribusi Skor Ujian')
plt.xlabel('Skor')
plt.ylabel('Jumlah Siswa')
plt.show()

# Menghitung probabilitas seorang siswa mendapatkan skor di atas 85
prob_above_85 = np.sum(data > 85) / len(data)
print(f"Probabilitas siswa mendapatkan skor di atas 85: {prob_above_85:.2f}")

# Menghitung probabilitas seorang siswa mendapatkan skor antara 70 dan 80
prob_between_70_and_80 = np.sum((data >= 70) & (data <= 80)) / len(data)
print(f"Probabilitas siswa mendapatkan skor antara 70 dan 80: {prob_between_70_and_80:.2f}")


import seaborn as sns

sns.kdeplot(data, fill=True, color="r")
plt.title('Estimasi Kepadatan Kernel Skor Ujian')
plt.xlabel('Skor')
plt.ylabel('Densitas')
plt.show()



######################################

labels = ["50-59", "60-69", "70-79", "80-89", "90-100"]
freq = [np.sum((data >= 50) & (data <= 59)),
        np.sum((data >= 60) & (data <= 69)),
        np.sum((data >= 70) & (data <= 79)),
        np.sum((data >= 80) & (data <= 89)),
        np.sum(data >= 90)]
        
plt.pie(freq, labels=labels, autopct='%1.1f%%')
plt.title("Distribusi Skor Ujian dalam Pie Chart")
plt.show()

prob_below_60 = np.sum(data < 60) / len(data)
print(f"Probabilitas siswa mendapatkan skor di bawah 60: {prob_below_60:.2f}")