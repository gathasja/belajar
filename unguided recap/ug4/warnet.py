def skyNet(status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda):
    # jika status pengguna 'M' jam tutup akan mundur
    # jam tutup maksimal untuk pengguna umum adalah 2 jam dan total waktu buka maksimal <= 24 jam (maks disini maksudnya untuk member)
    try:
        jam_masuk = int(jam_masuk)
        jam_keluar = int(jam_keluar)
        jam_buka = int(jam_buka)
        jam_tutup = int(jam_tutup)
        denda = int(denda)
        waktu_tambahan_member = int(waktu_tambahan_member)
        billing = int(billing)
        
        if status_pengguna != "M" and status_pengguna != "U":
            return "Status pengguna tidak valid!"
        elif billing < 0:
            return "Billing harus lebih dari 0!"
        elif jam_masuk < jam_buka:
            return "Maaf lab belum buka"
        else:
            if status_pengguna== "M":
                jam_tutup += waktu_tambahan_member
            jam_perkiraan_keluar = jam_masuk + billing
            if jam_perkiraan_keluar > jam_tutup:
                sisa = jam_perkiraan_keluar - jam_tutup
                return f"sisa waktu: {sisa} jam"
            else:
                lama_asli = jam_keluar - jam_masuk
                if lama_asli > billing:
                    denda_total = (lama_asli - billing) * denda
                    return f"Anda kena denda sebesar Rp.{denda_total}"
                else:
                    return "Terimakasih telah berkunjung ke lab"
    except:
        return "Data nya ada yang ga valid"

if __name__ == '__main__' :
    status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda = input().split()
    print(skyNet(status_pengguna, jam_buka, jam_masuk, jam_keluar, jam_tutup, waktu_tambahan_member, billing, denda))