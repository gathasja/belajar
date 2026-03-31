def bioskopAlPro(jumlahTiket, jumlahPopcorn, jumlahSoda, hari):
    try:
        # Validasi input hari
        try:
            hari_int = int(hari)
        except ValueError:
            raise ValueError("invalid literal for int() with base 10: '{}'".format(hari))
        
        if hari_int < 0 or hari_int > 6:
            print("pilihan hari hanya 0-6")
            return
        
        # Daftar harga berdasarkan hari
        if hari_int in [0, 1, 2, 3]:  # Senin-Kamis
            harga_tiket = 40000
            harga_popcorn = 35000
            harga_soda = 20000
        elif hari_int == 4:  # Jumat
            harga_tiket = 45000
            harga_popcorn = 30000
            harga_soda = 15000
        else:  # Sabtu-Minggu (5-6)
            harga_tiket = 50000
            harga_popcorn = 40000
            harga_soda = 25000
        
        # Hitung harga normal
        total_tiket = jumlahTiket * harga_tiket
        total_popcorn = jumlahPopcorn * harga_popcorn
        total_soda = jumlahSoda * harga_soda
        
        # Cek promo
        diskon = 0
        if jumlahTiket > 0:
            # Cek promo 25% (beli tiket+popcorn+soda untuk setiap tiket)
            if jumlahPopcorn >= jumlahTiket and jumlahSoda >= jumlahTiket:
                diskon = 0.25
            # Cek promo 10% (beli tiket+popcorn ATAU tiket+soda untuk setiap tiket)
            elif (jumlahPopcorn >= jumlahTiket) or (jumlahSoda >= jumlahTiket):
                diskon = 0.10
        
        # Hitung harga setelah diskon
        total_tiket_diskon = total_tiket * (1 - diskon)
        harga_akhir = total_tiket_diskon + total_popcorn + total_soda
        
        # Print hasil
        print("Harga Tiket : {:.1f}".format(total_tiket_diskon))
        print("Harga Popcorn : {:.1f}".format(total_popcorn))
        print("Harga Soda : {:.1f}".format(total_soda))
        print("Harga Akhir : {:.1f}".format(harga_akhir))
        
    except Exception as e:
        print(str(e))
        
print(bioskopAlPro(2,0,0,89))