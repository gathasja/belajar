def olah_suhu(nilai, dari, ke):
    try:
        nilai = float(nilai)
    except:
        return "Input nilai suhu invalid"

    if dari in ("C", "F", "K") and ke in ("C", "F", "K"):
        celcius = ke_celcius(nilai, dari)
        hasil = dari_celcius(celcius, ke)
        return round(hasil, 2)
    else:
        return "Input konversi suhu invalid"

def ke_celcius(nilai, dari):
    if dari == "C":
        return nilai
    elif dari == "F":
        return (nilai - 32) * 5/9
    elif dari == "K":
        return nilai - 273.15
    else:
        return None

def dari_celcius(celcius, ke):
    if ke == "C":
        return celcius
    elif ke == "F":
        return (celcius * 9/5) + 32
    elif ke == "K":
        return celcius + 273.15
    else:
        return None

if __name__ == "__main__":
    nilai, dari, ke = input().split()
    print(olah_suhu(nilai, dari, ke))