# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

raw_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
final_list = []

for check_obj in raw_list:
    if check_obj.isdigit():
        final_list.extend(['"' f'{int(check_obj):02d}' '"'])
    elif (check_obj[0] in "-+") and check_obj[1:].isdigit():
        final_list.extend(['"' f'{check_obj[0]}{int(check_obj[1:]):02d}' '"'])
    else:
        final_list.append(check_obj)
print(final_list)
final_string = ' '.join(final_list)
print(final_string)
