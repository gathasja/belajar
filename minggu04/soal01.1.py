#contoh 4.1

inputSuhu = input("masukan suhu tubuh: ")
try:
    suhu = int(inputSuhu)
    
    if suhu >=38:
        print("anda demam")
    else:
        print("anda tidak demam")
        
except ValueError:
    print("suhu harus berupa angka!") 