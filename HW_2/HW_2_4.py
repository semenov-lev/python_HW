workers_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']

count = 0
len_list = len(workers_list)

for n in workers_list:
    _ = (n.split()[::-1])[0]
    name = _.lower().upper()[0] + _[1::].lower()  # В дальшейшем я узнал про .title()
    print("Привет, " + name + "!")
