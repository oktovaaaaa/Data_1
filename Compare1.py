import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



train = pd.read_csv("KelulusanTepatWaktu_Train.csv")
test = pd.read_csv("KelulusanTepatWaktu_Test.csv")

print(train.head()) # Untuk menampilkan 5 data teratas
print("\n\n")

print("=================  Menampilkan statstik  ==================\n\n")

print(train.describe()) # Untuk menampilkan statstik 
print("\n\n")

print("=================  Menampilkan Kelulusan Balance atau tidak  ==================\n\n")

print(train['kelulusan_tepat_waktu'].value_counts())
print("\n\n")

print("=================  Menampilkan jumlah value yang duplicate  ==================\n")
print("Jumlah data yang duplicate = ",train.duplicated().sum())

sns.histplot(data=train, x="IPK", kde=True)
plt.title("Distribusi IPK Mahasiswa")
plt.xlabel("IPK")
plt.ylabel("Jumlah")
plt.show()


train.dropna()
print(train.isnull().sum())




