def get_jokes(n, repeat=True):
    """
    List joke generator
    :param n: number of jokes:
    :param repeat: True or False:
    :return:
    """
    from random import choice
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    output_jokes = []
    for _ in range(0, n):
        if repeat:
            zip(nouns, adverbs, adjectives)
            output_jokes.append(*[f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'])
        else:
            try:
                a = choice(nouns)
                b = choice(adverbs)
                c = choice(adjectives)
                nouns.remove(a)
                adverbs.remove(b)
                adjectives.remove(c)
                output_jokes.append(*[f'{a} {b} {c}'])
            except IndexError:
                output_jokes.append("шуток больше нет")
    return output_jokes


print(get_jokes(6, repeat=False))
