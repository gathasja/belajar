usd = 20000
i = int(input())
g = 10000000
pajak = 0.1
kontrakan = 1500000
makanan = 2500000
ho = 1000000
sumbangan = 0.17

konversi = i*usd
pengeluaran = kontrakan+makanan+ho
gaji = g-(g*pajak)
tabunganTotal = konversi+gaji-pengeluaran
tabunganAkhir = tabunganTotal - (sumbangan*tabunganTotal)

print(tabunganAkhir)

