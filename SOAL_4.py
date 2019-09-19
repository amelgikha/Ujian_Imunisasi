import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BCG = pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv',na_values='n.a')
Campak = pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv',na_values='n.a')
DPT = pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv',na_values='n.a')
Polio = pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv',na_values='n.a')

BCG = BCG.interpolate()
Campak = Campak.interpolate()
DPT = DPT.interpolate()
Polio = Polio.interpolate()
# print(BCG.head(10))
# print(Campak.head(10))
# print(DPT.head(10))
# print(Polio.head(10))

plt.figure('Persentase Balita Terimunisasi 1995-2017', figsize=(15,9))
plt.subplot(221)
plt.bar(BCG['Tahun'], BCG['% Balita yang pernah mendapat imunisasi BCG'], color='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(222)
plt.bar(Campak['Tahun'], Campak['% Balita yang pernah mendapat imunisasi Campak'], color='green')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(223)
plt.bar(DPT['Tahun'], DPT['% Balita yang pernah mendapat imunisasi DPT'], color='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(224)
plt.bar(Polio['Tahun'], Polio['% Balita yang pernah mendapat imunisasi Polio'], color='blue')
plt.title('Polio')
plt.xticks(Polio['Tahun'],np.arange(1995,2018),rotation=90)
plt.show()

plt.figure('Persentase Balita Tak Terimunisasi 1995-2017', figsize=(15,9))
plt.subplot(221)
plt.bar(BCG['Tahun'], 100-BCG['% Balita yang pernah mendapat imunisasi BCG'], color='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(222)
plt.bar(Campak['Tahun'], 100-Campak['% Balita yang pernah mendapat imunisasi Campak'], color='green')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(223)
plt.bar(DPT['Tahun'], 100-DPT['% Balita yang pernah mendapat imunisasi DPT'], color='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation=90)

plt.subplot(224)
plt.bar(Polio['Tahun'], 100-Polio['% Balita yang pernah mendapat imunisasi Polio'], color='blue')
plt.title('Polio')
plt.xticks(Polio['Tahun'],np.arange(1995,2018),rotation=90)
plt.show()