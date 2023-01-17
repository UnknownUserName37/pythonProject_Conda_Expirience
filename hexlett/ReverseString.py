#   Очень найс урок. Very nice lectuan.
def reverse_string(text, one_searching_symbol_from_text):
    index = 0
    length_text = len(text) - 1
    searching_sybol_match = ''
    print(f'{index} LOL?')

    while index <= length_text:
        current_char_from_text = text[index]
        searching_sybol_match = searching_sybol_match + one_searching_symbol_from_text
        index = index + 1

        print(f"{current_char_from_text} I' am JUST value of current variabale {index}")

        if current_char_from_text == one_searching_symbol_from_text:
            is_contain_symbol = (current_char_from_text == one_searching_symbol_from_text)

            print(f"{is_contain_symbol} I'am Dick. Shit. But contain, HEALL, YA")
            return is_contain_symbol

        elif current_char_from_text.upper() == one_searching_symbol_from_text:
            print("WOW, I'am WORK!")

            return True

    return False


print(f"{reverse_string('Game Of Thrones', 'S')} Who I'am?")  # 'senorhT fO emaG'
