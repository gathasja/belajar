def PetaMampus(n):
    size = 2 * n - 1  # Ukuran matriks
    for i in range(size):
        for j in range(size):
            # Ambil nilai maksimum dari seberapa jauh posisi i, j dari sisi luar
            value = n - min(i, j, size - 1 - i, size - 1 - j)
            print(value, end=' ')
        print()
PetaMampus(5)