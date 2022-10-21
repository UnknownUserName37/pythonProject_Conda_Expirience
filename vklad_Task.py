#можно юзать как схему для рассчёта крипты. sum_profit - сколько хочешь, sum_dup - скок имеешь. count - времени потребуется.
p = 1.1
count = 0
tupo = 0
while True:

    sum_dep = float(input("Твой стартовый деп? -> "))
    sum_profit = float(input("Скок хочешь? -> "))
    while sum_dep <= sum_profit:
        tupo += sum_dep * p
        och_tupo = sum_dep * p

        print(sum_dep, "я деп")
        print(sum_profit, 'я профит')
        count += 1
        if (sum_profit // tupo) == 0:
            years = sum_profit / och_tupo
            print("потерпи стока лет -> ", years, "у тя будет стока бабла -> ", tupo)

            break
