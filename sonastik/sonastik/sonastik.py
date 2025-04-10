import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona):
    if sona in sonastik:
        print(f"Tõlge vene keelde: {sonastik[sona]}")
    else:
        print("Sõna ei leitud sõnastikust.")

def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            print(f"Tõlge eesti keelde: {est}")
            return
    print("Sõna ei leitud sõnastikust.")

def lisa_sona():
    est = input("Sisesta uus sõna eesti keeles: ")
    rus = input("Sisesta selle sõna vene tõlge: ")
    sonastik[est] = rus
    print("Sõna lisatud!")


def paranda_sona():
    est = input("Sisesta parandatav eesti sõna: ")
    if est in sonastik:
        uus_est = input(f"Uus eesti sõna (vajadusel muuda, või jäta samaks '{est}'): ") or est
        uus_rus = input(f"Uus vene tõlge (praegu '{sonastik[est]}'): ") or sonastik[est]
        
        if uus_est != est:
            del sonastik[est]
        sonastik[uus_est] = uus_rus
        print("Sõna parandatud!")
    else:
        print("Sõna ei leitud sõnastikust.")


def testi_teadmisi():
    if not sonastik:
        print("Sõnastik on tühi, testi ei saa teha.")
        return

    print("Testi teadmisi alustatakse!")
    sonad = list(sonastik.items())
    random.shuffle(sonad)
    õiged = 0
    kokku = len(sonad)

    for est, rus in sonad:
        suund = random.choice(['est_rus', 'rus_est'])
        if suund == 'est_rus':
            vastus = input(f"Sisesta vene tõlge sõnale '{est}': ")
            if vastus.strip().lower() == rus.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus on: {rus}")
        else:
            vastus = input(f"Sisesta eesti tõlge sõnale '{rus}': ")
            if vastus.strip().lower() == est.lower():
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige vastus on: {est}")

    protsent = (õiged / kokku) * 100
    print(f"Test lõppenud! Sinu tulemus: {protsent:.2f}%")


def pea_programm():
    print("Tere tulemast eesti-vene sõnastikku!")
    while True:
        print("\nValikud:")
        print("1 - Tõlgi eesti -> vene")
        print("2 - Tõlgi vene -> eesti")
        print("3 - Lisa uus sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")
        valik = input("Tee oma valik: ")

        if valik == '1':
            sona = input("Sisesta sõna eesti keeles: ")
            tolgi_est_rus(sona)
        elif valik == '2':
            sona = input("Sisesta sõna vene keeles: ")
            tolgi_rus_est(sona)
        elif valik == '3':
            lisa_sona()
        elif valik == '4':
            paranda_sona()
        elif valik == '5':
            testi_teadmisi()
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Tundmatu valik, proovi uuesti.")


pea_programm()
