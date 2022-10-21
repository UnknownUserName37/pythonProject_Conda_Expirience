
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

a = input("Zdarov, ebash ")
b = input("A mne pohuy ")
print("nu i gavno")
print (a, b)
a, b = b, a
print (a, b)

time = int(input("Минуты введите: "))
hours = time // 60
print ("Во введённом числе", hours, "часов")
minutes = time % 60
print ("Во введённом числе", minutes, "минут")

a = int(input("Zdarov, ☺ ebash po 3 "))
b = int(input("A mne pohuy, no tebe toje 3 "))
a %= 100
b %= 100
c = a + b
print("nu i gavno, no ", c)