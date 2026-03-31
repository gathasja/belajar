def Pertambahan(angka):
    total = 0
    for i in range(1, angka + 1):
        total += i
    return total

def Pengurangan(angka):
    total = angka
    for i in range(angka - 1, 0, -1):
        total -= i
    return total
    
def Pembagian(angka):
    return 100 // angka

def Perkalian(angka):
    return angka ** angka

def Main(angka,pilihan):
    hasil = 0
    if pilihan == "Pertambahan":
        hasil = Pertambahan(angka)
    elif pilihan == "Pengurangan":
        hasil = Pengurangan(angka)
    elif pilihan == "Perkalian":
        hasil = Perkalian(angka)
    elif pilihan == "Pembagian":
        hasil = Pembagian(angka)
    else:
        return "Mbok seng bener to"
    
    return f"Hasil Program : {hasil}"

if __name__ == "__main__":
    angka = int(input())
    pilihan = str(input())
    print(Main(angka, pilihan))