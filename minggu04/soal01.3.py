#contoh 4.3
try: 
    x = int(input("masukan bilangan pertama: "))
    y = int(input("masukan bilangan kedua: "))
    z = int(input("masukan bilangan ketiga: "))

    if x > y and x > z:
        print("bilangan terbesar:", x)
    elif y > x and y > z:
        print("bilangan terbesar:", y)
    else:
        print("bilangan terbesar:", z)
        
except ValueError:
    print("nilai harus berupa angka!")