def kalkulator(angka1,angka2,angka3,angka4,angka5,angka6,angka7,angka8):
    
    
    try:
        a1 = int(angka1)
        a2 = int(angka2)
        a3 = int(angka3)
        a4 = int(angka4)
        a5 = int(angka5)
        a6 = int(angka6)
        a7 = int(angka7)
        a8 = int(angka8)
        
        jumlah = a1 + a2
        kurang = a3 - a4
        kali = a5 * a6
        
        print ("=== KALKULATOR WISNU ===\n")
        
        print(f"{a1} {a2} {a3} {a4} {a5} {a6} {a7} {a8}")
        print(f"Hasil Penjumlahan :  {jumlah}")    
        print(f"Hasil Pengurangan :  {kurang}")
        print(f"Hasil Perkalian :  {kali}")
        
        if a8 == 0:
            print("Angka ke 8 mu nilainya kosong / division by Zero")
        else:
            bagi = a7 / a8
            print(f"Hasil Pembagian :  {bagi}")
        
        hasilGabung = (a1 + a2) + (a3 - a4) + (a5 * a6) + (a7 / 10)
        print(f"Hasil Gabungan :  {hasilGabung}")
        
        print("\n========================") 
    
    except ValueError:
        print("Maaf Koh Wisnu tidak menerima number selain angka INTEGER")


#Jangan dirubah
if __name__ == "__main__":
    number1 = input()
    number2 = input()
    number3 = input()
    number4 = input()
    number5 = input()
    number6 = input()
    number7 = input()
    number8 = input()
    kalkulator(number1,number2,number3,number4,number5,number6,number7,number8)