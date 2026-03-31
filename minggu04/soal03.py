try:
    bulan = int(input("masukan bulan (1-12): "))
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print("jumlah hari: ", 31)
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print("jumlah hari: ", 30)
    elif bulan == 2:
        print("jumlah hari: ", 29)
    else:
        print("bulan harus antara 1-12")

except ValueError:
    print("bulan harus berupa angka!")
    