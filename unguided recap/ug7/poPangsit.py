#cara 1 pakai match case
# swap_type = input()
# ball_location = 1

# for tipe in swap_type:
#     if tipe == 'A' and ball_location == 1:
#         ball_location = 2
#     elif tipe == 'A' and ball_location == 2:
#         ball_location = 1
#     elif tipe == 'B' and ball_location == 2:
#         ball_location = 3
#     elif tipe == 'B' and ball_location == 3:
#         ball_location = 2
#     elif tipe == 'C' and ball_location == 1:
#         ball_location = 3
#     elif tipe == 'C' and ball_location == 3:
#         ball_location = 1
        
# print(ball_location)

#cara 2
pertukaran = list(input())
hasil = len(pertukaran)

kiri = 1
tengah = 0
kanan = 0

for i in range(hasil):
    if pertukaran[i] == "A":
        sementara = tengah 
        tengah = kiri
        kiri = sementara
    elif pertukaran[i] == "B":
        sementara = kanan
        kanan = tengah
        tengah = sementara
    elif pertukaran[i] == "C":
        sementara = kanan
        kanan = kiri
        kiri = sementara
if hasil > 50:
    print("karakter tidak boleh lebih dari 50")
else:
    if kiri == 1:
        print(1)
    elif tengah == 1:
        print(2)
    elif kanan == 1:
        print(3)
        
        










    