inputBilangan = input("masukan bilangan: ")

try:
    bilangan = int(inputBilangan)
    hasil = "positif" if bilangan > 0 else "negatif" if bilangan < 0 else "bukan positif atau negatif"
    print(bilangan, "merupakan bilangan", hasil)
            
except ValueError:
   print("nilai harus berupa angka!")