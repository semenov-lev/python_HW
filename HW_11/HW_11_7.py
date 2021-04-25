class ComplexNumber:
    def __init__(self, cpx):
        self.cpx = cpx

    @property
    def parse_complex(self):
        first_sign = "+"
        re_z = ""
        second_sign = ""
        im_z = ""
        if "+" in self.cpx:
            second_sign += "+"
            im_z += self.cpx.split("+")[1].split(self.cpx[-1])[0]
            if "-" in self.cpx.split("+")[0]:
                first_sign = "-"
                re_z += self.cpx.split("+")[0][1:]
            else:
                re_z += self.cpx.split("+")[0]
        else:
            second_sign += "-"
            if self.cpx.split("-")[0] == "":
                first_sign = "-"
                re_z += self.cpx.split("-")[1]
                im_z += self.cpx.split("-")[2].split(self.cpx[-1])[0]
            else:
                re_z += self.cpx.split("-")[0]
                im_z += self.cpx.split("-")[1].split(self.cpx[-1])[0]
        parsed_cpx = [int(first_sign + re_z), int(second_sign + im_z), "j"]
        return parsed_cpx

    def __add__(self, other):
        sign = ""
        result = [(self.parse_complex[0] + other.parse_complex[0]),
                  (self.parse_complex[1] + other.parse_complex[1]), "j"]
        if "-" not in str(result[1]):
            sign += "+"
        return f"{result[0]}{sign}{result[1]}j"

    def __mul__(self, other):
        sign = ""
        re_z = int((self.parse_complex[0] * other.parse_complex[0]) +
                   (self.parse_complex[1] * other.parse_complex[1] * (-1)))
        im_z = int((self.parse_complex[0] * other.parse_complex[1]) + (self.parse_complex[1] * other.parse_complex[0]))
        if "-" not in str(im_z):
            sign += "+"
        return f"{re_z}{sign}{im_z}j"


cpx_a = ComplexNumber("5+6j")
print(cpx_a.parse_complex)

cpx_b = ComplexNumber("2+3j")
print(cpx_b.parse_complex)

print(cpx_a + cpx_b)
print(cpx_a * cpx_b)
