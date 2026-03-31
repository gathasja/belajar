def programBMI():
    try: 
        print("Program Menghitung BMI")
        berat = float(input("Masukan berat badan anda (kg): ")) #dalam kilogram
        tinggi = float(input("Masukan tinggi badan anda (m): ")) #dalam meter
        
        rumusBMI = berat/tinggi**2
        print("BMI anda adalah: ", round(rumusBMI, 2))
        
    except ValueError:
        print("--- Input harus berupa angka! ---") #yang terjadi kalau input bukan dalam bentuk angka
        
programBMI() #untuk manggil fungsi program_BMI()