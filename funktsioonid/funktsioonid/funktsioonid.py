

def season(month):
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3, 4, 5]:
        return "kevad"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [9, 10, 11]:
        return "sügis"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца (от 1 до 12): "))
print(season(month))




def season(month):
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3, 4, 5]:
        return "kevad"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [9, 10, 11]:
        return "sügis"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца (от 1 до 12): "))
print(season(month))

def seasonInput()->str:
    month = int(input("Введите номер месяца (от 1 до 12): "))
    return season(month)
k = int(input("Введите количество месяцев: "))
while True:
    if k in range(1,13):
        break
    else:
        k = int(input("Введите номер месяца (от 1 до 12): "))
        # return season(k)




#6
def is_prime(number:float)->bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


number = int(input("Введите число от 0 до 1000: "))
print(is_prime(number))
