def tower_defense(n):
    if n <= 0:
        print("AREA TIDAK VALID")
        return
    if n > 50:
        print("AREA TERLALU LUAS")
        return
    if n % 2 == 0:
        print("AREA TIDAK PAS")
        return

    tengah = (n // 2) + 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            if n % 2 != 0 and i == tengah and j == tengah:
                print("T", end=" ")
            elif i == j or i + j == n + 1:
                print("X", end=" ")
            elif i % 2 == 0 and j % 2 != 0:
                print(i + j, end=" ")
            else:
                print(".", end=" ")
        print()

n = int(input())
tower_defense(n)