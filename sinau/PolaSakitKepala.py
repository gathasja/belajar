def pola(panjang,lebar):
    panjang,lebar = panjang % 10,lebar % 10
    
    midLebar = lebar//2+1
    temp = panjang
    maju = True
    stop = 0
    ulang = False
    for i in range(lebar):
        for j in range(panjang):
            print(temp,end=" ")
            if temp == midLebar:
                maju = False
            if maju == True:
                temp -= 1
            if maju == False:
                temp += 1
            if maju == False and temp == panjang-stop:
                print(temp,end=" ")
                break
        print()
        if midLebar == 1:
            ulang = True
        if ulang == False:
            midLebar -= 1
            temp -= 1
            stop += 1
        else:
            midLebar += 1
            temp += 1
            stop -= 1
        maju = True

    return ""

# print(pola(999999,99999))
print(pola(7,7))
# print(pola(5,5))