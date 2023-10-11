import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset
df = pd.read_csv('AAPL.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Menampilkan 5 baris pertama
print(df.head())


plt.figure(figsize=(14,7))
plt.plot(df['Close'])
plt.title('Harga Penutupan Saham Apple')
plt.xlabel('Tanggal')
plt.ylabel('Harga Penutupan')
plt.grid(True)
plt.show()



from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df['Close'], model='multiplicative', period=1)
result.plot()
plt.show()

import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_predict

# Menentukan p, d, dan q dengan plot autocorrelation
autocorrelation_plot(df['Close'])
plt.show()

# Membangun model ARIMA
model = sm.tsa.arima.ARIMA(df['Close'], order=(5,1,0))
model_fit = model.fit()

# Ringkasan dari model ARIMA
print(model_fit.summary())

# Visualisasi hasil prediksi
plot_predict(model_fit,dynamic=False)
plt.show()


forecast = model_fit.forecast(steps=10)
print(f"Prediksi harga saham Apple untuk 10 hari ke depan: {forecast}")
