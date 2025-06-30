import pandas as pd
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









