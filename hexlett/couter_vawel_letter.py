from symbols import is_vowel #  Из курса Hexlett. Там (в их интерпритаторе) она работала.


def count_vowels(text):
    vowel_letter_counter_in_text = is_vowel(text)
    counter_vowel_lette_in_text = 1

    for vowel_letter_counter_in_text in text:
        counter_vowel_lette_in_text += 1

        return counter_vowel_lette_in_text
