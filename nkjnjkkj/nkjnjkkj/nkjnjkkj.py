
import random
try:
    choice = input("������, �������, ������: ")
    print("��� �����: ", choice)
    choices = ["������", "�������", "������"]
    bot = random.choice(choices)
    print("����� ����: ", bot)
    if choice == bot:
        print("�����!")
    elif choice == "������":
        if bot == "�������":
            print("�� ��������!")
        else:
            print("�� ���������!")
    elif choice == "�������":
        if bot == "������":
            print("�� ��������!")
        else:
            print("�� ���������!")
    elif choice == "������":
        if bot == "������":
            print("�� ��������!")
        else:
            print("�� ���������!")
except:
    print("������! ����������, ������� ���������� �����!")