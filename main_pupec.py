# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("nu i gavno, no ")

a = int(input("Zdarov, ☺ ebash po 4 "))

a_t = a // 1000
a_h = (a % 1000) // 100
a_tens = (((a % 1000) % 100) // 10)
a_num = (((a % 1000) % 100) % 10) / 1
print("nu i gavno, no toje", a_t, a_h, a_tens, int(a_num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
