def cek_digit_belakang(x, y, z):
    return (x % 10 == y % 10) or (x % 10 == z % 10) or (y % 10 == z % 10)

try:
    x = int(input("nilai x: "))
    y = int(input("nilai y: "))
    z = int(input("nilai z: "))
        
    hasil = cek_digit_belakang(x, y, z)
    print(hasil)
               
except ValueError:
        print ("input harus berupa angka!")
    
