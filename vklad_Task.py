#можно юзать как схему для рассчёта крипты. sum_profit - сколько хочешь, sum_dup - скок имеешь. count - времени потребуется.
p = 0.1
count = 1
tupo = 0
och_tupo = 0

while True:

    sum_dep = int(input("Твой стартовый деп? -> "))
    sum_profit = int(input("Скок хочешь? -> "))

    while True:
        och_tupo = sum_dep * p #сколько от депозита в год
        print(och_tupo, "новый деп рассчёта")
        tupo += och_tupo #стакаем годовые проценты в каждой итерации

        print(tupo, "я деп", round(sum_profit), "я профит")

        if (sum_profit // tupo) == 0:
            print(tupo, "я новый деп")
            years = ((sum_profit - (och_tupo*10)) / och_tupo) #рассчёт бабок без учёта начальной суммы депозита
            print("потерпи стока лет -> ", float(years), "у тя будет стока бабла -> ", int(tupo))
            break

