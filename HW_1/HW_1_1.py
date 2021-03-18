minute = 60
hour = minute * 60
day = hour * 24
month = day * 30
year = month * 12
output_message = ""

duration = int(input("Введите время, в секундах: "))

years = duration // year
remain_year = duration % year
if years != 0:
    output_message += str(years) + " лет "

months = remain_year // month
remain_month = remain_year % month
if months != 0:
    output_message += str(months) + " мес "

days = remain_month // day
remain_day = remain_month % day
if days != 0:
    output_message += str(days) + " дн "

hours = remain_day // hour
remain_hour = remain_day % hour
if hours != 0:
    output_message += str(hours) + " час "

minutes = remain_hour // minute
if minutes != 0:
    output_message += str(minutes) + " мин "

seconds = remain_hour % minute
if seconds != 0:
    output_message += str(seconds) + " сек "

print(output_message)
