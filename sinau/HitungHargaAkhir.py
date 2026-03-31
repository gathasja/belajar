def hitung_harga(harga_awal, jumlah):
    if jumlah <= 0:
        return 0  # Jumlah negatif atau nol, kembalikan 0
    
    total = 0
    for i in range(1, jumlah + 1):
        if i == 1:
            diskon = 0.10  # Barang pertama
        else:
            diskon = 0.15  # Barang kedua dan seterusnya
        harga_setelah_diskon = harga_awal * (1 - diskon)
        total += harga_setelah_diskon
    return total
print(hitung_harga(100000, 1))
print(hitung_harga(100000, 3))
print(hitung_harga(47295, 50))