import math

def hitung_status(level):
    nyawa = 10000
    atk = 1000
    for _ in range(level):
        nyawa = math.floor(nyawa * 1.05)
        atk = math.floor(atk * 1.10)
    return nyawa, atk

def bergelutSamaNicho(lvlNicho, cooldownSkillNicho, namaMusuh, lvlMusuh, cooldownSkillMusuh):
    # Hitung status awal
    nyawa_nicho, atk_nicho = hitung_status(lvlNicho)
    nyawa_musuh, atk_musuh = hitung_status(lvlMusuh)
    max_nyawa_nicho = nyawa_nicho
    max_nyawa_musuh = nyawa_musuh

    # Cetak status Nicho
    print("Status Nicho")
    print(f"Nyawa: {nyawa_nicho}")
    print(f"Kekuatan: {atk_nicho}")
    print()
    # Cetak status Musuh
    print(f"Status {namaMusuh}")
    print(f"Nyawa: {nyawa_musuh}")
    print(f"Kekuatan: {atk_musuh}")
    print()

    ronde = 1
    while True:
        # Giliran Nicho
        if ronde % cooldownSkillNicho == 0:
            damage = atk_nicho + math.floor(0.15 * max_nyawa_musuh)
            nyawa_musuh -= damage
            if nyawa_musuh <= 0:
                print(f"{namaMusuh} kalah karena skill Nicho di ronde ke {ronde}")
                break
        else:
            nyawa_musuh -= atk_nicho
            if nyawa_musuh <= 0:
                print(f"{namaMusuh} kalah karena serangan Nicho di ronde ke {ronde}")
                break

        # Giliran Musuh
        if ronde % cooldownSkillMusuh == 0:
            damage = atk_musuh + math.floor(0.15 * max_nyawa_nicho)
            nyawa_nicho -= damage
            if nyawa_nicho <= 0:
                print(f"Nicho kalah karena skill {namaMusuh} di ronde ke {ronde}")
                break
        else:
            nyawa_nicho -= atk_musuh
            if nyawa_nicho <= 0:
                print(f"Nicho kalah karena serangan {namaMusuh} di ronde ke {ronde}")
                break

        ronde += 1


bergelutSamaNicho(lvlNicho=10, cooldownSkillNicho=3, namaMusuh="Dunia", lvlMusuh=10, cooldownSkillMusuh=3)
