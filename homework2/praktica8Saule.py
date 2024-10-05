while True:
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        сумма = num1 + num2
        print(f"Сумма: {сумма}")
    except ValueError:
        print("Пожалуйста, введите целые числа.")
