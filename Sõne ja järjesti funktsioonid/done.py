while True:
        print("valige funktsioon 1-10")
        print("1. swapcase ")
        print("2. [::-1]")
        print("3. len")
        print("4. s.upper")
        print("5. s.lower")
        print("6. s.isdigit")
        print("7. s.isalpha")
        print("8. kui s == s[::-1]")
        print("9. word_list = s.split() ")
        print("10. s.strip")
        print("11. s.zfill")
        print("12. s.count")
        print("0. väljumine")
        
        answer = input("sisesta number: ")
        
        if answer == "1":
            s = input("Sisesta tekst: ")
            print(s.swapcase())
            print("funktsioon .swapcase muudab väiksed tähed suurteks ja suured tähed väikesteks")
        
        elif answer == "2":
            s = input("Sisesta tekst: ")
            print(s[::-1])
            print("funktsioon pöörab teksti ümber")
        
        elif answer == "3":
            s = input("Sisesta tekst: ")
            print(len(s))
            print("funktsioon tagastab teksti pikkuse")
        
        elif answer == "4":
            s = input("Sisesta tekst: ")
            print(s.upper())
            print("funktsioon muudab teksti kõik tähed suurteks")
        
        elif answer == "5":
            s = input("Sisesta tekst: ")
            print(s.lower())
            print("funktsioon muudab teksti kõik tähed väikesteks")
        
        elif answer == "6":
            s = input("Sisesta tekst: ")
            if s.isdigit():
                print("Tekst koosneb ainult numbritest.")
            else:
                print("Tekst ei koosne ainult numbritest.")
        
        elif answer == "7":
            s = input("Sisesta tekst: ")
            if s.isalpha():
                print("Tekst koosneb ainult tähtedest.")
            else:
                print("Tekst ei koosne ainult tähtedest.")
        
        elif answer == "8":
            s = input("Sisesta tekst: ")
            if s == s[::-1]:
                print("Tekst on palindroom.")
            else:
                print("Tekst ei ole palindroom.")
        
        elif answer == "9":
            s = input("Sisesta tekst: ")
            word_list = s.split()  
            print(f"Tekst on muudetud sõnade nimekirjaks: {word_list}")
        
        elif answer == "10":
            s = input("Sisesta tekst: ")
            print(s.strip())
            print("funktsioon eemaldab tühikud teksti algusest ja lõpust.")

        elif answer == "11":
            s = input("Введите строку для zfill: ")
            width = int(input("Введите ширину строки: "))
            print(s.zfill(width))

        elif answer == "12":
            s = input("Введите строку для подсчета: ")
            k = input("Введите подстроку для подсчета: ")
            print(s.count(k))

        
        elif answer == "0":
            print("Väljumine programmist.")
            break  
        
        else:
            print("Vale valik, proovige uuesti.")
