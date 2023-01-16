def my_substr(string, index):
    string_change_magic = ''
    i = 0

    while i < index:
        string_change_magic += string[i]
        i += 1
        print(i)

    return string_change_magic


print(my_substr('lalala', 5))
