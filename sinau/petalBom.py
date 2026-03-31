def petak_bom(baris, kolom, angkaBom, kataBom):
    nomor_sekarang = 1
    for indeks_baris in range(baris):
        deretan_sel = []
        for indeks_kolom in range(kolom):
            # Cek apakah angka harus diganti dengan bom
            if (nomor_sekarang % angkaBom == 0) or (str(angkaBom) in str(nomor_sekarang)):
                tampilan = kataBom
            else:
                tampilan = str(nomor_sekarang)
            
            # Format output berdasarkan posisi kolom
            if indeks_kolom == 0:  # Kolom paling kiri
                sel = f"{tampilan}-"
            elif indeks_kolom == kolom - 1:  # Kolom paling kanan
                sel = f"-{tampilan}"
            else:  # Kolom tengah
                sel = f"-{tampilan}-"
            
            deretan_sel.append(sel)
            nomor_sekarang += 1
        
        # Gabungkan semua sel dengan tab sebagai pemisah
        print("\t".join(deretan_sel))

# Contoh pemanggilan fungsi
# petak_bom(5, 5, 3, "bom")
petak_bom(2, 10, 5, "EXPLODE")