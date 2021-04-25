class NotANumber(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def check_for_nan(number_input):
        try:
            if float(number_input):
                return True
        except ValueError:
            return False


def create_list():
    user_list = []
    number_input = input("Введите число, или 'exit', чтобы закончить список: ")
    while number_input != "exit":
        try:
            if not NotANumber.check_for_nan(number_input):
                raise NotANumber("Некорректный ввод! В список вносятся только числа.")
            else:
                user_list.append(number_input)
        except NotANumber as err:
            print(err)
        number_input = input("Введите число, или 'exit', чтобы закончить список: ")
    return f"Список введенных чисел: {user_list}"


print(create_list())
