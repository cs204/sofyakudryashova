def calculate_fuel():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split("/"))
            if x >= y or y == 0:
                print("Некорректный ввод. Попробуйте еще раз.")
                continue
            percent = round(x / y * 100)
            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
        except ZeroDivisionError:
            print("Деление на ноль. Попробуйте еще раз.")
calculate_fuel()