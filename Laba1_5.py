car_dict = dict()

def calculate_max_len_name():
    global car_dict
    Max = len("Название")
    for i in car_dict:
        if len(i) > Max:
            Max = len(i)
    return Max
def calculate_max_len_struct():
    global car_dict
    Max = len("Описание")
    for i in car_dict:
        if len(car_dict[i][0]) > Max:
            Max = len(car_dict[i][0])
    return Max
def calculate_max_len_price():
    global car_dict
    Max = len("цена")
    for i in car_dict:
        if len(str(car_dict[i][1])) > Max:
            Max = len(str(car_dict[i][1]))
    return Max

def calculate_max_len_count():
    global car_dict
    Max = len("Количество")
    for i in car_dict:
        if len(str(car_dict[i][2])) > Max:
            Max = len(str(car_dict[i][2]))
    return Max

def add_new_product(name, struct, price, count):
    global car_dict
    car_dict[name] = [struct, price, count]

def view_struct():
    global car_dict
    lengBorderLeft = calculate_max_len_name()
    lengBorderRight =  calculate_max_len_struct()
    lengBorder = lengBorderLeft + lengBorderRight + 4
    print("-"*lengBorder)

    sFormat = f"|%-{lengBorderLeft}s| %-{lengBorderRight}s|"

    print(sFormat % ("Название","Описание"))
    print("-" * lengBorder)
    for i in car_dict:
        print(sFormat % (i, car_dict[i][0]))
    print("-" * lengBorder)


def view_price():
    global car_dict

    lengBorderLeft = calculate_max_len_name()
    lengBorderRight = calculate_max_len_price()
    lengBorder = lengBorderLeft + lengBorderRight + 4
    print("-" * lengBorder)

    sFormat = f"|%-{lengBorderLeft}s| %-{lengBorderRight}s|"

    print(sFormat % ("Название", "цена"))
    print("-" * lengBorder)
    for i in car_dict:
        print(sFormat % (i, car_dict[i][1]))
    print("-" * lengBorder)

def view_count():
    global car_dict
    lengBorderLeft = calculate_max_len_name()
    lengBorderRight = calculate_max_len_count()
    lengBorder = lengBorderLeft + lengBorderRight + 4
    print("-" * lengBorder)

    sFormat = f"|%-{lengBorderLeft}s| %-{lengBorderRight}s|"

    print(sFormat % ("Название", "Количество"))
    print("-" * lengBorder)
    for i in car_dict:
        print(sFormat % (i, car_dict[i][2]))
    print("-" * lengBorder)


def view_all():
    global car_dict

    lenBorder1 = calculate_max_len_name()
    lenBorder2 = calculate_max_len_struct()
    lenBorder3 = calculate_max_len_price()
    lenBorder4 = calculate_max_len_count()

    lengBorder = lenBorder1 + lenBorder2 + lenBorder3 + lenBorder4 + 8

    print("-" * lengBorder)

    sFormat = f"|%-{lenBorder1}s| %-{lenBorder2}s| %-{lenBorder3}s| %-{lenBorder4}s|"

    print(sFormat % ("Название", "Описание","цена","количество"))
    for i in car_dict:
        print(sFormat % (i, car_dict[i][0],car_dict[i][1],car_dict[i][2]))

    print("-" * lengBorder)

def buy(name, count):
    if name in car_dict.keys():
        if count > car_dict[name][2]:
            print("У нас нет столько(")
        else:
            all_price = car_dict[name][1] * count
            print("Цена выбранных вами товаров составляет:", all_price)
            print("Будете покупать? - yes/no")
            answer = input()
            if answer == "yes":
                car_dict[name][2] -= count
                print("Спасибо за покупку)")
                if car_dict[name][2] == 0:
                    car_dict.pop(name)
                    print("Вы выкупили весь товар)")
                else:
                    print("Данного товара осталось: ", car_dict[name][2])
            elif answer == "no":
                print("Жаль, что вы не купили(")
            else:
                print("Вы ввели неправильный ответ")

    else:
        print("У нас нет такого товара(")


def menu():
    while True:
        print("1 - Просмотр описания")
        print("2 - Просмотр цены")
        print("3 - Просмотр количества")
        print("4 - Просмотр всей информации")
        print("5 - покупка")
        print("6 - выйти из программы")
        print("Ваш выбор: ")
        t = int(input())
        match t:
            case 1:
                view_struct()
            case 2:
                view_price()
            case 3:
                view_count()
            case 4:
                view_all()
            case 5:
                print("Введите название товара: ")
                name = input()
                if not(name in car_dict):
                    print("Такого товара у нас нет(")
                else:
                    print("Введите количество: ")
                    count = int(input())
                    buy(name, count)
            case 6:
                return

add_new_product("двигатель", "лень придумывать", 3.242, 3 )
add_new_product("колесо", "опять лень", 0.54, 30 )
add_new_product("руль", "всё ещё", 0.14, 300 )

menu()
