#contoh 4.2

inputBilangan = input("masukan bilangan: ")

try:
    bilangan = int(inputBilangan)
    
    if bilangan > 0:
        print(bilangan, "merupakan bilangan positif")
    elif bilangan < 0:
        print(bilangan, "merupakan bilangan negatif")
    else:
        print(bilangan, "bukan merupakan bilangan positif atau negatif")
        
except ValueError:
    print("nilai harus berupa angka!")