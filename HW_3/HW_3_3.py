def thesaurus(*args, sort=False):  # Добавил возможность сортировки по ключам через аргумент
    names_lib = {}
    if sort:
        args_s = list(sorted(args))
    else:
        args_s = list(args)
    for n in list(args_s):
        n.startswith(n[0])
        names_lib[n[0]] = list(*[filter(lambda el: el.startswith(n[0]), args_s)])
    return names_lib


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Станислав", "Яков", "Саид", "Ахмед", "Нурсултан", "Добрыня",
                sort=False))
