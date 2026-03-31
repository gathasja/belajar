def kalkulatorRusak(angka1, angka2, angka3):
    try:
        # Konversi angka ke string dan hilangkan tanda minus jika ada
        str1 = str(angka1).lstrip('-')
        str2 = str(angka2).lstrip('-')
        str3 = str(angka3).lstrip('-')
        
        # Ambil digit paling kiri
        digit1 = int(str1[0])
        digit2 = int(str2[0])
        digit3 = int(str3[0])
        
        # Cek jika ada digit yang 0
        if digit1 == 0 or digit2 == 0 or digit3 == 0:
            print("Error, angka tidak boleh 0")
            return
        
        # Hitung hasil perkalian
        hasil = digit1 * digit2 * digit3
        
        # Cetak output sesuai format
        print("Digit Kiri Angka1 :", digit1)
        print("Digit Kiri Angka2 :", digit2)
        print("Digit Kiri Angka3 :", digit3)
        print("Hasil :", hasil)
        
    except Exception as e:
        print("Error:", e)


# Contoh penggunaan
kalkulatorRusak(3214, 12, 8235)  # Output: 24
kalkulatorRusak(3214, 0, 8235)   # Output: Error, angka tidak boleh 0

# kalkulatorRusak(3214, 12, 8235)  # Output sesuai contoh pertama
# kalkulatorRusak(42, 145, 236)    # Output sesuai contoh kedua
# kalkulatorRusak(0, 123, 456)     # Output: "Error, angka tidak boleh 0"
# kalkulatorRusak(-123, 45, 678)   # Output: Digit Kirl Angkai : 1, dst.