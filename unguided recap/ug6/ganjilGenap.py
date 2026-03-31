def pakarai(n):
    try:
        intn = int(n)
        if intn == 0:
            print("Endog")
        elif intn > 0:
            for i in range(1, intn + 1):
                if i % 3 == 0 and i % 5 == 0:
                    print("Ayoyoyo")
                elif i % 2 != 0:
                    print("Ganjil Cokk")
                else:
                    print("Genap Cokk")
        else:
            print("Negatif Cokk")
        
    except:
        print("Apehal ni Prof")

if __name__ == "__main__":
    userint = input()
    pakarai(userint)