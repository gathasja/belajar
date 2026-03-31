def UlarTangga(angkaUlar, angkaTangga, kataUlar, kataTangga, n, x):
    if n not in [10, 100]:
        print("Pilih 10 atau 100")
        return
    
    nomor_sekarang = x  # Mulai dari kelipatan pertama
    ukuran = n
    
    for baris in range(ukuran):
        deretan = []
        for kolom in range(ukuran):
            # Cek kondisi untuk kedua kata
            adalah_ular = (nomor_sekarang % angkaUlar == 0)
            adalah_tangga = (nomor_sekarang % angkaTangga == 0)
            
            if adalah_ular and adalah_tangga:
                tampilan = f"{kataUlar}_{kataTangga}"
            elif adalah_ular:
                tampilan = kataUlar
            elif adalah_tangga:
                tampilan = kataTangga
            else:
                tampilan = str(nomor_sekarang)
            
            deretan.append(tampilan)
            nomor_sekarang += x  # Loncat sesuai kelipatan x
        
        # Cetak baris dengan spasi sebagai pemisah
        print(" ".join(deretan))

# Contoh Penggunaan 1
print("Contoh Penggunaan 1:")
UlarTangga(3, 5, "ULAR", "TANGGA", 10, 2)

# Contoh Penggunaan 2
# print("\nContoh Penggunaan 2:")
# UlarTangga(4, 6, "SNAKE", "LADDER", 10, 3)