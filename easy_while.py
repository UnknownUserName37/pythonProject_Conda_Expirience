#Хард_шо_пизда
#я в ахуе
#)

lucky = int(input("Введите номер билетика: "))
num = 0
count = 1

while True:
    lucky //= 10
    num += lucky
    print(count, "считаю и отображаю само число -> ", lucky, num)
    count += 1

    if count <= 3:
        left_side = num
        #print(left_side)
        continue

    if count >= 4 and count <= 6:
        right_side = num
       # print(right_side)
        break

