def nilaiIps():
    print("Program penghitung IPS Mahasiswa")
    
    try:
        jumlah = int(input("Berapa jumlah mata kuliah? "))
        total = 0
        sks = 3
        
        for i in range(1, jumlah + 1):
            nilai = input(f"Nilai MK {i}: ").upper()
            
            if nilai == "A":
                total += 4 * sks
            elif nilai == "B":
                total += 3 * sks
            elif nilai == "C":
                total += 2 * sks
            elif nilai == "D":
                total += 1 * sks
        
        ips = total / (jumlah * sks)
        print(f"Nilai IPS anda semester ini {ips:.2f}")
          
    except ValueError:
        print("input harus berupa angka!")
nilaiIps()
