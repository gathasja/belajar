def deret(tinggi, lebar):
    angka = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(f"{angka} ", end="")
            angka = angka + 1
        print()
tinggi = int(input("tinggi = "))
lebar = int(input("lebar = "))
deret(tinggi, lebar)