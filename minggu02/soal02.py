def programFungsi():
    try:
        print("Program Menghitung Fungsi\n")
        x = int(input("Masukan nilai x (bil. bulat)= "))
        
        if x == 0:
            print("input tidak boleh nol!") #pembagian tidak boleh dengan 0
            return
        
        fungsi = 2*x**3+2*x+15/x
        print("hasil dari fungsi f("+ str(x) + ") =", round(fungsi, 2))
        
    except ValueError:
        print("input harus bilangan bulat!")
    
programFungsi()