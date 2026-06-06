#1
num_1 = input("введи 5 чисел через пробіл:").split()
print("/n".join(num_1))
#2
list_2 = ["a", "d", "r", "x", "g", "b"]
index_2 = int(input("Введіть індекс:"))
print(list_2[index_2])
#3
names = input("введи 3 імен через пробіл:").split()
index_3 = int(input("Введіть індекс:"))
name_new = input("Введи нове ім'я:")
names.insert(index_3, name_new)
print(names)
#4
element = input("Введи елементи через пробіл").split()
element = tuple(element)
print(len(element))
#6
strochka = input("Введи рядок:")
print(f"Рядок: {strochka}")
print(f"Довжина рядка: {len(strochka)}")
print(f"перший елемент:{strochka[0]}")
print(f"останній елемент:{strochka[-1]}")
#7
1 = input("Введи 1 рядок:")
2 = input("Введи 2 рядок")
print(1 + 2)
# 8
a = int(input("Ціле число: "))
b = float(input("Число з крапкою: "))
print("Сума:", a + b)
print("Різниця:", a - b)
print("Добуток:", a * b)
print("Частка:", a / b)
# 9
student = {"ім'я": "Оля", "вік": 18}
ключ = input("Що додати? (оцінка, курс тощо): ")
значення = input("Значення: ")
student[ключ] = значення
print(student)

# 10
числа = input("Числа через пробіл: ")
множина = set(числа.split())
print("Унікальних елементів:", len(множина))

# 11
рядок1 = input("Перший набір чисел: ")
рядок2 = input("Другий набір чисел: ")
set1 = set(рядок1.split())
set2 = set(рядок2.split())
print("Об'єднання:", set1 | set2)
print("Перетин:", set1 & set2)
print("Різниця (1-2):", set1 - set2)

# 12
список = [int(input("Число1: ")), int(input("Число2: ")), int(input("Число3: "))]
текст = input("Рядок: ")
словник = {текст: список, "сума": sum(список)}
print(словник)

# 13
дані = input("Введіть значення: ")
print("Тип:", type(дані).__name__)
if дані.isdigit():
    print("Як int:", int(дані))
else:
    print("Не число, не конвертується в int")