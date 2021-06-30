import re


class Cell:
    def __init__(self, row, col, block, x, y, value):
        self.value = value
        self.row = row
        self.column = col
        self.block = block
        self.x = x
        self.y = y
        assert self.row.can_add_cell(self) and self.column.can_add_cell(self) and self.block.can_add_cell(self), \
            "Cell could not be added"

        self.row.add_cell(self)
        self.column.add_cell(self)
        self.block.add_cell(self)

    def __str__(self):
        return str(self.value)

    def value_is_changeable(self, value):
        if not isinstance(value, int):  # you may always fill in e.g "*" of "." as a placeholder
            return True
        return not self.row.has_value(value) and not self.column.has_value(value) and not self.block.has_value(value)


class Container:  # Every cell is part of 3 containers: 1 row, 1 column and 1 block
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def can_add_cell(self, cell):
        return cell not in self.cells and len(self.cells) + 1 <= 9

    def has_value(self, value):
        return value in {cell.value for cell in self.cells}


class Grid:
    def __init__(self):
        self.rows = [Container() for _ in range(9)]
        self.cols = [Container() for _ in range(9)]
        self.blocks = [Container() for _ in range(9)]

        self.grid = []

        for row in range(9):
            self.grid.append([])
            for col in range(9):
                # https://stackoverflow.com/a/20268305
                self.grid[row].append(
                    Cell(self.rows[row], self.cols[col], self.blocks[row // 3 * 3 + col // 3], row, col, "*"))
        print(self)
        self.add_values()

    def is_value(self, value):
        return bool(re.fullmatch("[1-9]", str(value)))

    def handle_input(self, target):
        err_msg = f"Your input for a {target} must be an integer value in [1,9]"
        good_input = False
        value = None
        while not good_input:
            try:
                value = int(input(f"Enter the {target}: "))
                if not self.is_value(value):
                    print(err_msg)
                else:
                    good_input = True
            except ValueError:
                print(err_msg)
        return value

    def add_values(self):
        print("Fill the Sudoku grid")
        go = "y"
        while go.lower() == "y":
            row = self.handle_input("row")
            col = self.handle_input("column")
            value = self.handle_input("value")

            cell = self.grid[row - 1][col - 1]
            if cell.value_is_changeable(value):
                cell.value = value
            else:
                print(
                    f"You cannot change the value in ({row}, {col}) to {value}"
                    f", the value must be unique in the row, column and block")

            print("\n", self)
            go = input("Do you wish to continue? (y/n)")
            while go.lower() not in ["y", "n"]:
                go = input("Do you wish to continue? (y/n)")

        self.complete_grid()

    def complete_grid(self):
        pass

    def recursion_manager(self, row, col, value):
        pass

    def next_index(self, current_row, current_col):
        next_col = current_col + 1 % 8
        next_row = current_row + 1 if next_col == 0 else current_row
        return [next_row, next_col] if 0 <= next_row <= 8 else None

    def __str__(self):
        out = " ".join([str(i) for i in range(1, 10)]).center(20, " ") + "\n"
        col_count = 1

        for r_index, r in enumerate(self.grid):
            if r_index % 3 == 0:
                out += "+-----" * 3 + "+" + "\n"

            for c_index, c in enumerate(r):
                if c_index % 3 == 0:
                    out = out.rstrip(" ") + "|"
                out += str(c.value) + " "

            out = out.rstrip(" ") + "| " + str(col_count) + "\n"
            col_count += 1

        return out + "+-----" * 3 + "+"


if __name__ == '__main__':
    Grid()
