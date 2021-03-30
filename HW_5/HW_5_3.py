tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = ['9А', '7В', '9Б', '9В']


def gen_school(a, b):
    diff = len(a) - len(b)
    if diff > 0:
        for _add in range(diff):
            b.append("None")
    for name, klass in zip(a, b):
        output_message = (name, klass)
        yield print(output_message)


school = gen_school(tutors, klasses)
print(type(school))
next(school)
next(school)
next(school)
next(school)
next(school)
next(school)
next(school)
next(school)
