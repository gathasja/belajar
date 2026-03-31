def programBudi():
     print("Program Pendapatan Budi Selama Libur Musim Panas\n")
     gaji = float(input("masukan gaji per jam: Rp. "))
     jamKerja = float(input("masukan jam kerja per minggu: "))
     
     #total gaji selama liburan (5 minggu)
     totalPendapatan = gaji*jamKerja*5 #5 dari total minggu kerja
     print("\ntotal pendapatan Budi selama libur musim panas: \nRp.", format(totalPendapatan, ",.2f"))
     
     #gaji seteleh dipotong pajak 14%
     pajak = 0.14
     pendapatanSetelahPajak = totalPendapatan - (totalPendapatan*pajak)
     print("pendapatan Budi setelah dipotong pajak: \nRp.", format(pendapatanSetelahPajak, ",.2f"))
     
     #untuk beli baju+aksesoris (10%)
     ba = 0.10
     bajuAksesoris = pendapatanSetelahPajak*ba
     print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: \nRp.", format(bajuAksesoris, ",.2f"))
     
     #untuk beli alat tulis (1%)
     at = 0.01
     alatTulis = pendapatanSetelahPajak*at
     print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: \nRp.", format(alatTulis, ",.2f"))
     
     #sisa uang pendapatan
     sisa = pendapatanSetelahPajak-(bajuAksesoris+alatTulis)
     
     #untuk sedekah (25%)
     sedekah = 0.25
     uangSedekah = sisa*sedekah
     print("Jumlah uang yang akan Budi sedekahkan: \nRp.", format(uangSedekah, ",.2f"))
     
     #untuk yatim (30% dari uang sedekah)
     yatim = 0.30
     uangYatim = uangSedekah*yatim
     print("Jumlah uang yang akan diterima anak yatim: \nRp.", format(uangYatim, ",.2f"))
     
     #untuk dhuafa (70% dari uang sedekah)
     dhuafa = 0.70
     uangDhuafa = uangSedekah*dhuafa
     print("Jumlah uang yang akan diterima kaum dhuafa: \nRp.", format(uangDhuafa, ",.2f"))
     
programBudi()
