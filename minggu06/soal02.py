def ganjil():
    try:
        bawah = int(input("batas bawah: "))
        atas = int(input("batas atas: "))
        
        if bawah < atas:
            for i in range(bawah, atas + 1):
                if i % 2 != 0:
                    print(i, end=" ")
        else:
            for i in range(bawah, atas -1, -1):
                if i % 2 != 0:
                    print(i, end=" ")
    except ValueError:
        print("input harus berupa angka!")

ganjil()
        