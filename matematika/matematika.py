import random

tase1 = ['+', '-']
tase2 = ['*', '/']
tase3 = ['**']

try:
    level = int(input("Выбери уровень сложности: 1, 2 или 3 => "))
except ValueError:
    print("Пожалуйста выберите уровень 1,2 или 3!")
    exit()

primeri = 5
correct_primeri = 0

for i in range(primeri):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 50)
    
    if level == 1:
        operation = random.choice(tase1)
    elif level == 2:
        operation = random.choice(tase2)
    elif level == 3:
        operation = random.choice(tase3)
    else:
        print("Неверный уровень сложности.")

    if operation == '+':
        correct_answer = number1 + number2
        print(f"{number1} + {number2} = ")
    elif operation == '-':
        correct_answer = number1 - number2
        print(f"{number1} - {number2} = ")
    elif operation == '*':
        correct_answer = number1 * number2
        print(f"{number1} * {number2} = ")
    elif operation == '/':
        while number2 == 0:
            number2 = random.randint(1, 10)
        correct_answer = number1 / number2
        print(f"{number1} / {number2} = ")
    elif operation == '**':
        correct_answer = number1 ** number2
        print(f"{number1} ** {number2} = ")

    try:
        user_answer = float(input("Ваш ответ: "))
        if user_answer == correct_answer:
            print("Правильно!")
            correct_primeri += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_answer}")
    except ValueError:
        print("Пожалуйста введите правильное число.")

score = (correct_primeri / primeri) * 100

if score < 60:
    hinne = 2
elif 60 <= score < 75:
    hinne = 3
elif 75 <= score < 90:
    hinne = 4
else:
    hinne = 5

print(f"Вы ответили правильно на {correct_primeri} из {primeri} примеров.")
print(f"Ваша оценка: Hinne {hinne}")