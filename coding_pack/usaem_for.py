#lOL_task

for i in 0, 1, 2, 3, 4, 5:
    print(i / 2)

#Lol_task#2
count = 0

for joint in 33, 11, 49, 92, 534, 840, 1260:
   if (joint % 420) == 0:
    print('lucky 420 x5 free BUDS, his # ->', joint)
    count += 1
    print("our luckers", count)

# Hardly_Task #3
#P.S. Easy_Task
for num in 3, 4, 5, 6, 7:
    print(num **3, num ** 4, num ** 5)

#Real_Hardly_Task #4
tickets_luck_hund = 0
count_1 = 1

for tickets_luck in 33, 442, 777, 666, 420:
    if tickets_luck >= 100 and tickets_luck <= 999 and tickets_luck % 5 == 0:
        print("You are lucky", tickets_luck)

#Easy_Task_again #5
text = "Python!"

for fifth in range (5):
    print("Hi, dudes")

#Do_Tasks

time = int(input("Сколько будем по времени ужиматься в деньгах? -> ☼ -> "))
money = int(input("Скок откидываешь?? ->> "))
summ = 0

for month in range(time):
    print("Это месяц", month+1)
    summ = money * time
    print("ПОздравляю, у тебя", summ, "бабок ♀ и ты потратил на это всего", month + 1, "месяца :-D")

#Degree**2_Task

degree = 2

for decimal in range(10):
    summa = (decimal+1) ** degree
    if summa != 1:
        print("Квадраты числе = ", summa)

#ky_ky_Task_=)

printit = "ку-ку"
times_ky_ky = int(input("Сколько раз ку-ку? -> "))
for numir in range(times_ky_ky):
    print(printit)

#janother_Task_na(on)_FOR_ degree from 0 to 20

degree = 0
new_mir = 2
for initiger in range(20):
    print(new_mir ** degree)
    print(degree)
    degree += 1
