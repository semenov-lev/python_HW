eng_ru = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate_adv(eng):
    if str(eng).istitle():
        ru = eng_ru.setdefault(str(eng.lower()), "none").title()
    else:
        ru = eng_ru.setdefault(str(eng.lower()), "none")
    return ru


print(num_translate_adv("Two"))
