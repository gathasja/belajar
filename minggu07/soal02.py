def deret(n):
    for i in range(n, 0, -1):
        faktorial = 1
        for j in range(i, 0, -1):
            faktorial = faktorial * j
        print(f"{faktorial} ", end="")
        for k in range(i, 0, -1):
            print(f"{k}", end=" ")
        print()
n = int(input("n = "))
deret(n)
