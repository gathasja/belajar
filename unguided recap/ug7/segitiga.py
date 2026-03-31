def persegi(sisi):
    if sisi < 3 or sisi % 2 == 0:
        print("Failed Prof")
    else:
        for i in range(sisi):
            for j in range(sisi):
                if ((i == 0 or i == sisi -1) and (j == 0 or j == sisi - 1)):
                    print("#", end = " ")
                elif (i == sisi // 2) and (j == sisi // 2):
                    print("#", end = " ")
                elif i == j:
                    print("#", end = " ")
                elif i + j == sisi - 1:  
                    print("#", end = " ")
                else:
                    print(" ", end = " ")
            print()

if __name__ == "__main__":
    itnsisi = int(input())
    persegi(itnsisi)