#можно юзать как схему для рассчёта крипты. sum_profit - сколько хочешь, sum_dup - скок имеешь. count - времени потребуется.
p = 0.1
count = 1
tupo = 0
och_tupo = 0

while True:

    sum_dep = float(input("Твой стартовый деп? -> "))
    sum_profit = float(input("Скок хочешь? -> "))
    while True:
        tupo += sum_dep * p
        och_tupo += sum_dep * p
        if (sum_profit // tupo) == 0:
            years = sum_profit / tupo
            print("потерпи стока лет -> ", years, "у тя будет стока бабла -> ", tupo)
            break