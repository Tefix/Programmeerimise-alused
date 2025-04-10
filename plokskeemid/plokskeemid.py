# #1
# while True:
#     try:
#         num1 = float(input("Sisesta esimene number: "))
#         break  
#     except:
#         print("Palun sisestage korrektne number!")

# while True:
#     try:
#         num2 = float(input("Sisesta teine number: "))
#         break  
#     except:
#         print("Palun sisestage korrektne number!")

# if num1 > num2:
#     print(f"Suurim number: {num1}")
# elif num2 > num1:
#     print(f"Suurim number: {num2}")
# else:
#     print("Mõlemad numbrid on võrdsed.")
    

# #2
# while True:
#     try:
#         P = int(input("Sisesta numbrite arv: "))
#         sum_neg = 0

#         for i in range(P):
#             while True:
#                 try:
#                     num = float(input("Sisesta number: "))
#                     if num < 0:  
#                         sum_neg += num
#                     break
#                 except ValueError:
#                     print("Viga: Sisestage korrektne number.")
        
#         print(f"Negatiivsete numbrite summa: {sum_neg}")
#         break
#     except ValueError:
#         print("Viga: Sisestage korrektne numbrite arv.")

#3
while True:
    try:
        inim = int(input("Sisesta inimeste arv: "))
        if inim > 0:
            break
        else:
            print("Inimeste arv peab olema positiivne number.")
    except ValueError:
        print("Inimeste arv peab olema positiivne number.")

OK = 0

for i in range(inim):
    while True:
        try:
            vanus = int(input("Sisesta vanus: "))
            if vanus > 15:
                print("Sa saad minna restorani.")
                OK += 1
            break
        except:
                print("Sa ei saa minna restorani.")
       

print(f"Inimeste arv, kes saavad minna restorani: {OK}")

    

#4
while True:
    try:
        töötajad = int(input("Sisesta töötajate arv: "))
        count = 0

        for i in range(töötajad):
            while True:
                try:
                    palk = float(input("Sisesta töötaja palk (€): "))
                    vanus = int(input("Sisesta töötaja vanus: "))
                    if palk > 1200 and vanus >= 65:
                        count += 1
                    break
                except ValueError:
                    print("Viga: Sisestage korrektne palk või vanus.")
        
        print(f"Töötajate arv, kelle palk on üle 1200€ ja kes on pensionil: {count}")
        break
    except ValueError:
        print("Viga: Sisestage korrektne töötajate arv.")
