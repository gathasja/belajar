def tabel_perkalian_nggak_jelas(baris, kolom):
    # Cek apakah baris dan kolom valid
    if type(baris) != int or type(kolom) != int:
        print("TIDAK VALID")
        return
    if baris <= 0 or kolom <= 0 or baris >= 25 or kolom >= 25:
        print("TIDAK VALID")
        return

    total = baris + kolom  # Jumlahkan baris dan kolom

    # Tentukan baris yang ditampilkan: ganjil atau genap
    if total % 2 == 0:
        # Kalau genap, pakai baris ganjil saja
        baris_ditampilkan = range(1, baris + 1, 2)
    else:
        # Kalau ganjil, pakai baris genap saja
        baris_ditampilkan = range(2, baris + 1, 2)

    # Cetak isi tabel
    for i in baris_ditampilkan:
        for j in range(1, kolom + 1):
            if i == j:
                print("miau", end="\t")
            else:
                print(i * j, end="\t")
        print()  # Ganti baris




tabel_perkalian_nggak_jelas(10,10)
