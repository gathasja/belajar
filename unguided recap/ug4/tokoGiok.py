def Giokstore(Member : bool, Harga_barang : int, Jenis_Kemasan : str, Metode_Pembayaran : str) -> int:
    sementara = 0
    final = 0
    if(Metode_Pembayaran == "Kasbon"):
        return "Maaf Toko ini tidak menerima pinjaman"
    else:
        if(Member == True):
            if(Harga_barang > 500000):
                diskon = 0.5
                sementara = Harga_barang - (diskon * Harga_barang)
            elif(Harga_barang >= 250000 and Harga_barang <= 500000):
                diskon = 0.35
                sementara = Harga_barang - (diskon * Harga_barang)
            elif(Harga_barang >= 100000 and Harga_barang <= 249999):
                diskon = 0.15
                sementara = Harga_barang - (diskon * Harga_barang)
            else:
                sementara = Harga_barang
            if(Jenis_Kemasan == "Plastik"):
                sementara = sementara + 15000
            elif(Jenis_Kemasan == "Kardus"):
                sementara = sementara + 20000
            if(Metode_Pembayaran == "Cash"):
                total = sementara
            elif(Metode_Pembayaran == "Kredit / QRIS"):
                pajak = 0.02
                total = sementara + (pajak * sementara)
        else:
            if(Harga_barang > 750000):
                diskon = 0.5
                sementara = Harga_barang - (diskon * Harga_barang)
            elif(Harga_barang >= 350000 and Harga_barang <= 750000):
                diskon = 0.35
                sementara = Harga_barang - (diskon * Harga_barang)
            elif(Harga_barang >= 150000 and Harga_barang <= 349999):
                diskon = 0.15
                sementara = Harga_barang - (diskon * Harga_barang)
            else:
                sementara = Harga_barang
            if(Jenis_Kemasan == "Plastik"):
                sementara = sementara + 17500
            elif(Jenis_Kemasan == "Kardus"):
                sementara = sementara + 30000
            if(Metode_Pembayaran == "Cash"):
                total = sementara
            elif(Metode_Pembayaran == "Kredit / QRIS"):
                pajak = 0.05
                total = sementara + (pajak * sementara)
    return int(total)
# #Bagian ini jangan dirubah
if __name__ == "__main__":
    member_str = input()
    member = True if member_str == "True" else False
    harga = int(input())
    kemasan = str(input())
    metode = str(input())
    print(Giokstore(member,harga,kemasan,metode))