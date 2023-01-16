def is_contains_char(string, char_symbol):
    i = 0
    transformation_to_string = ''
    index = len(string) - 1

    while i <= index:
        contains_symbol = string[i] + transformation_to_string
        print(contains_symbol)
        i += 1

        return contains_symbol

print(is_contains_char('Hexlett', 'Hexlett'))
print(is_contains_char('Hexlett', 't'))
print(is_contains_char('Hexlett', 'h'))
# print(is_contains_char('Hexlett', 'H'), 'h')
# print(is_contains_char('Hexlett', 'e'), 'e')
print(is_contains_char('Hexlett', 'edf'), 'esdvsdv')
# print(is_contains_char('Hexlett', 'sdvsdvsv'), 'esdvsdv')
# print(is_contains_char('Hexlett', 'qqqqqq'), 'esdvsdv')
# print(is_contains_char('Hexlett', 'vvvvvvvvv'), 'esdvsdv')
# print(is_contains_char('Hexlett', 'F'), 'esdvsdv')
# print(is_contains_char('Hexlett', 'FSDFSDF'), 'esdvsdv')
