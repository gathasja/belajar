def panah(n):
    tengah = n // 2
    if n < 4 or n % 2 == 0:
        print("Error Prof")
    else:
        for i in range(n):
            for j in range(n):
                if i == tengah or i-j == tengah or i + j == tengah:
                    print("# ", end = "")
                else:
                    print("  ", end= "")
            print()
        
if __name__ == "__main__":
    intpanjang = int(input())
    panah(intpanjang)