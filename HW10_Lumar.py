#Завдання 3
import math

def plus():
    var_1 = float(input("Уведіть перший доданок: "))
    var_2 = float(input("Уведіть другий доданок: "))
    return var_1 + var_2


def minus():
    var_1 = float(input("Уведіть зменшуване число: "))
    var_2 = float(input("Уведіть вд\'ємник: "))
    return var_1 - var_2


def mplic():
    var_1 = float(input("Уведіть перший множник: "))
    var_2 = float(input("Уведіть другий множник: "))
    return var_1 * var_2


def divis():
    var_1 = float(input("Уведіть ділене число: "))
    var_2 = float(input("Уведіть дільник: "))
    if var_2 == 0:
        return "На нуль ділити неможна"
    else:
        return var_1 / var_2


def power():
    var_1 = float(input("Уведіть число: "))
    var_2 = int(input("Уведіть степінь: "))
    return var_1 ** var_2


def m_root():
    var1 = float(input("Уведіть число: "))
    var2 = int(input("Уведіть степінь кореня: "))
    return var1 ** (1 / var2)


def sinus():
    var = float(input("Уведіть число: "))
    return math.sin(var)


def cosinus():
    var = float(input("Уведіть число: "))
    return math.cos(var)


def tangen():
    var = float(input("Уведіть число: "))
    return math.tan(var)


print("""Уведіть +, щоб додати
Уведіть -, щоб відняти
Уведіть *, щоб помножити
Уведіть /, щоб поділити
Уведіть **, щоб піднести до степеня
Уведіть r, щоб знайти корінь
Уведіть s, щоб знайти синус
Уведіть c, щоб знайти сосинус
Уведіть t, щоб знайти тангенс
Уведіть 0 для виходу""")

while True:
    enter = input("Оберіть необхідний пункт меню: ")
    if enter == "+":
        print("Відповідь: ", plus())
    elif enter == "-":
        print("Відповідь: ", minus())
    elif enter == "*":
        print("Відповідь: ", mplic())
    elif enter == "/":
        print("Відповідь: ", divis())
    elif enter == "**":
        print("Відповідь: ", power())
    elif enter == "r":
        print("Відповідь: ", m_root())
    elif enter == "s":
        print("Відповідь: ", sinus())
    elif enter == "c":
        print("Відповідь: ", cosinus())
    elif enter == "t":
        print("Відповідь: ", tangen())
    elif enter == "0":
        break
    else:
        print("Оберіть пункт меню")


#Завдання 4
pencil = [("black", 10, 5.5), ("orange", 10, 5.5), ("pink", 10, 5.5),
          ("indigo", 10, 5.5), ("red", 10, 5.5), ("blue", 10, 5.5)]
pen = [("black", 20, 10.7), ("violet", 15, 5.5), ("green", 10, 15.4),
       ("indigo", 20, 12.7), ("red", 15, 17.5), ("blue", 20, 10.5)]
notebook = [("12 cage", 100, 10.7), ("12 line", 100, 10.7), ("18 cage", 50, 20.4),
       ("18 line", 50, 20.7), ("48 cage", 200, 30.5), ("48 line", 200, 30.5)]


def my_choice(type_product, name_product):
    while True:
        print("""\nУведіть 1, щоб переглянути товар
Уведіть 2, щоб додати товар
Уведіть 3, щоб видалити товар
Уведіть 4, щоб змінити кількість товару
Уведіть 5, щоб змінити ціну товару
Уведіть 0 для відміни\n""")
        enter = input("Оберіть необхідний пункт меню: ")
        print()
        if enter == "1":
            print("\t" + name_product + ":")
            for i, joke in enumerate(type_product):
                print(i + 1, joke)
        elif enter == "2":
            new_unit = (input("Уведіть назву товару: "), int(input("Уведіть кількість товару: ")),
                             float(input("Уведіть ціну товару: ")))
            type_product.insert(0, new_unit)
            print("Ви додали: ", type_product[0])
        elif enter == "3":
            delet_unit = int(input("Який пункт бажаєте видалити: ")) - 1
            type_product.pop(delet_unit)
            print("Товар видалено")
        elif enter == "4":
            change_unit = int(input("Який пункт cписку бажаєте змінтити: ")) - 1
            new_amount = int(input("Який нова кількість цього товару: "))
            change_amount = list(type_product[change_unit])
            change_amount[1] = new_amount
            tuple_change = tuple(change_amount)
            type_product[change_unit] = tuple_change
            print("Кількість товару змінено: ", type_product[change_unit])
        elif enter == "5":
            change_unit = int(input("Який пункт cписку бажаєте змінтити: ")) - 1
            new_price = float(input("Яка нова ціна цього товару: "))
            change_amount = list(type_product[change_unit])
            change_amount[2] = new_price
            tuple_change = tuple(change_amount)
            type_product[change_unit] = tuple_change
            print("Кількість товару змінено: ", type_product[change_unit])
        elif enter == "0":
            break


while True:
    print("""\nУведіть 1, щоб дізнатися про олівці
Уведіть 2, щоб дізнатися про ручки
Уведіть 3, щоб дізнатися про зошити
Уведіть 0 для виходу\n""")
    enter = input("Оберіть необхідний пункт меню: ")
    print()
    if enter == "1":
        type_product = pencil
        name_product = "Олівці"
        my_choice(type_product, name_product)
    elif enter == "2":
        type_product = pen
        name_product = "Ручки"
        my_choice(type_product, name_product)
    elif enter == "3":
        type_product = notebook
        name_product = "Зошити"
        my_choice(type_product, name_product)
    elif enter == "0":
        break
    else:
        print("Оберіть пункт меню")
print(pencil)


