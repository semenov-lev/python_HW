class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def make_order(self, line):
        lines_of_cell = ""
        for _ in range(self.cell_count // line):
            lines_of_cell += ("*" * line + "\n")
        lines_of_cell += "*" * (self.cell_count % line)
        return lines_of_cell

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def __str__(self):
        return str(self.cell_count)


cell_1 = Cell(25)
cell_2 = Cell(50)

print(cell_2.make_order(11))

print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
