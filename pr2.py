while True:
    input("Это приложение конвертер валют ")
    start = input(" Если вы хотите выйти нажмите: end")
    if start == "end":
        print("Приложение завершило работу.")
        break

    else:
        val =input("Введите валюту, в которую хотите перевести:"
                   "евро \n доллары\n тенге\n юани\n")
        a = float(input("Введите сумму в рублях: "))
        usd = 0.011061
        evro = 0.010096
        tenge = 5.07
        cny = 0.079003
        if val not in ('доллары', 'евро', 'тенге', 'юани'):
            raise Exception("Вы ввели неккореткную операцию, введите операцию из списка")
        if val == 'доллары':
            print(f"Сумма в долларах {a*usd}")
        elif val == 'евро':
            print(f"Сумма в евро {a*evro}")
        elif val == 'тенге':
            print(f"Сумма в тенге {a*tenge}")
        elif val == 'юани':
            print(f"Сумма в юанях {a*cny}")