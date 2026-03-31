def cek_angka(x, y, z):
    if x == y or x == z or y == z:
        return False
    else:
       return (x + y == z) or (x + z == y) or (y + z == x)
   
print(cek_angka(6, 7, 8))
print(cek_angka(6, 7, 13))
print(cek_angka(6, 6, 7))