import pandas as pd

# Membuat data frame
data = {'Harga': [5000, 6000, 5500, 6500, 5200],
        'Jumlah_Penjualan': [50, 45, 53, 40, 48]}
df = pd.DataFrame(data)

# Deskripsi statistik dasar
print(df.describe())


# Menambahkan data hilang
df.at[2, 'Harga'] = None

# Mengganti data hilang dengan rata-rata
df['Harga'].fillna(df['Harga'].mean(), inplace=True)
print(df)


import matplotlib.pyplot as plt
import seaborn as sns

# Visualisasi dengan histogram
sns.histplot(df['Harga'], kde=True)
plt.show()