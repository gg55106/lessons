#1
day = int(input("Введи день тижня"))
match day:
    case 1:
        print("Понеділок")
    case 2:
        print("Вівторок")
    case 3:
        print("Середа")
    case 4:
        print("Четверг")
    case 5:
        print("П'ятниця")
    case 6:
        print("Субота")
    case 7:
        print("Неділя")
    case _:
        print("Невірний день тижня спробуй спочатку")
#2
operation = input("Введи операцію:")
number_1 = int(input("Ввели перше число:"))
number_2 = int(input("Ввели друге число:"))
match operation:
    case "add":
        print(number_1 + number_2)
    case "min":
        print(number_1 - number_2)
    case "mul":
        print(number_1 * number_2)
    case "div":
        print(number_1 / number_2)
    case _:
        print("Такої операції немає")
#3
figure = input("Введи назву фігури:")
match figure:
    case "circle":
        print("0 сторін")
    case "square":
        print("4 сторін")
    case "triangle":
        print("3 сторін")
    case "rectangle":
        print("4 сторін")
    case _:
        print("Такої операції немає")
#4

    