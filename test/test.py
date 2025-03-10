
from operator import index
from random import randint





sõne ="Programmerimine"
print(sõne)
sõne_list=list(sõne)
print(sõne_list)
sõne_list.reverse()
print(sõne_list)
print(sõne_list.index("P"))

print (len(sõne_list))
print(len(sõne))

kogus_m= sõne_list.count("m")
for m in range(kogus_m):
    sõne_list.remove("m")
tähed= randint(1,6)
for i in range(tähed):
    while 1:
        try:
            t= input("Sisesta täht: ")
            if t.isalpha(): break
        except:
          print("Vale sisend")
    sõne_list.append(t)

print(sõne_list)

# tähed= randint(1,6)
# for i in range(tähed):
#     while 1:
#         try:
#             t= input("Sisesta täht: ")
#             if t.isalpha(): break
#         except:
#           print("Vale sisend")
#     while 1:
#         try:
#             ind= input("Sisesta index: ")
#             if ind.isnumeric() & ind<len(sõne_list): break
#         except:
#           print("Vale index")
#     sõne.list.insert(int(ind,t))

print(sõne_list)
def funktsion(e):
        return len(e)
sõne_list.sort(reverse=True, key=funktsion)
print(sõne_list)

