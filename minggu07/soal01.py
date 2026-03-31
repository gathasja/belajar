def primaTerdekat():
        n = int(input("masukan bilangan n: "))
        if n < 2:
            return "tidak ada bilangan prima kurang dari 2"
        for i in range(n-1, 1, -1):
            prima = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    prima = False
                    break
            if prima:
                return f"bilangan prima terdekat < {n} adalah {i}"          
print(primaTerdekat())
        