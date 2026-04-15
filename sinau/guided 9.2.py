#soal no. 1
import re

def sorting_string(stript):
    besar = "".join(re.findall(r"[A-Z]", stript))
    kecil = "".join(re.findall(r"[a-z]", stript))
    angka = "".join(re.findall(r"\d", stript))
    
    return f"{kecil}{besar}{angka}"

if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))