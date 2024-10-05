while True:
    try:
        a = float(input("Введите первое число (a): "))
        b = float(input("Введите второе число (b): "))
        
        # Определяем границы
        lower = int(min(a, b))
        upper = int(max(a, b))

        # Проверяем, есть ли целые числа между a и b
        if upper - lower <= 0.1:
            print("Между числами нет целых чисел.")
        else:
            print("Целые числа между a и b:")
            for number in range(lower + 1, upper + 1):
                print(number)

    except ValueError:
        print("Пожалуйста, вводите только вещественные числа.")
