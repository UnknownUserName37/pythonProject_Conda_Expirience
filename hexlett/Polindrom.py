def reverse_string(text):
    # Начальное значение
    reverse_text = ''
    is_text_null = str(text == '')
    is_polindrome = ''

    for char in text:
        reverse_text = char + reverse_text
        is_polindrome = str(reverse_text == text)

        # print(f"->{reverse_text}<-")

    return is_polindrome or is_text_null



print('Здесь ->', reverse_string('motor'), '<- Это я, пустая строка, motor')  # => '!og'# => '!og'
print('Здесь ->', reverse_string('ergerg'), '<- Это я, пустая строка, motor')  # => '!og'# => '!og'
print('Здесь ->', reverse_string('erg'), '<- Это я, пустая строка, motor')  # => '!og'# => '!og'
print('Здесь ->', reverse_string('!@$@#$'), '<- Это я, пустая строка, motor')  # => '!og'# => '!og'
print('Здесь ->', reverse_string('SKJDFGSD'), '<- Это я, пустая строка, motor')  # => '!og'# => '!og'
print('Здесь ->', reverse_string(''), '<- Это я, пустая строка')  # => '!og'
print('Здесь ->', reverse_string('rotor'), '<- Это я, пустая строка, rotor')