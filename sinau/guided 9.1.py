#soal no. 3
import re
def ekstrakStr(teks):
    digits = re.findall(r'\d', teks)
    odd_numbers = []
    even_numbers = []
    
    for d in digits:
        num = int(d)
        if num % 2 != 0:
            odd_numbers.append(num + 9)
        else:
            even_numbers.append(num + 7)
    
    odd_numbers.sort()
    even_numbers.sort()
    
    print("=========================")
    print(f" ODD NUMBER : {' '.join(map(str, odd_numbers))}")
    print(f" EVEN NUMBER : {' '.join(map(str, even_numbers))}")
    print("=========================")

if __name__ == "__main__":
    strinput = str(input())
    ekstrakStr(strinput)