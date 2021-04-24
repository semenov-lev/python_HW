class Date:
    def __init__(self, dmy_str):
        self.dmy_str = dmy_str

    @classmethod
    def convert_date(cls, dmy_str):
        try:
            converted_date = [int(num) for num in dmy_str.split("-")] if len(dmy_str.split("-")) == 3 else "Error"
            if converted_date == "Error":
                raise ValueError
            return converted_date
        except ValueError:
            return "Неправильный формат даты! Введите дату в формате «день-месяц-год»"

    @staticmethod
    def valid_date(dmy_str):
        try:
            day, month, year = Date.convert_date(dmy_str)
            if year > 0 and 0 < month <= 12 and 0 < day <= 31:
                return True
            else:
                return False
        except ValueError:
            return "Неправильный формат даты! Введите дату в формате «день-месяц-год»"


print(Date.convert_date("08-05-2021"))
print(Date.valid_date("08-05-2021"))

date = Date("08-05-2021")
print(date.convert_date("5008-05-2021"))
print(date.valid_date("5008-05-2021"))

date = Date("11-12-1662")
print(date.convert_date("5008-05-2021-50"))
print(date.valid_date("5008-05-2021-80"))
