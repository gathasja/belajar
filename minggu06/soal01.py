def perkalian(x, y):
    hasil = 0
    
    for i in range(x):
        hasil += y
    return hasil

print(f"6 * 5 = 5 + 5 + 5 + 5 + 5 + 5 = {perkalian(6, 5)}")
print(f"7 * 10 = 10 + 10 + 10 + 10 + 10 + 10 + 10 = {perkalian(7, 10)}")