
import random
try:
    choice = input("камень, ножницы, бумага: ")
    print("Ваш выбор: ", choice)
    choices = ["камень", "ножницы", "бумага"]
    bot = random.choice(choices)
    print("Выбор бота: ", bot)
    if choice == bot:
        print("Ничья!")
    elif choice == "камень":
        if bot == "ножницы":
            print("Вы победили!")
        else:
            print("Вы проиграли!")
    elif choice == "ножницы":
        if bot == "бумага":
            print("Вы победили!")
        else:
            print("Вы проиграли!")
    elif choice == "бумага":
        if bot == "камень":
            print("Вы победили!")
        else:
            print("Вы проиграли!")
except:
    print("Ошибка! Пожалуйста, введите корректный выбор!")