class Cell:
    def __init__(self, row, col, block, x, y):
        self.value = "."
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


class Container:  # Every cell is part of 3 containers: 1 row, 1 column and 1 block
    def __init__(self):
        self.cells = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def can_add_cell(self, cell):
        return cell not in self.cells and len(self.cells) + 1 <= 9


class Grid:

    def __init__(self):
        rows = [Container() for _ in range(9)]
        cols = [Container() for _ in range(9)]
        blocks = [Container() for _ in range(9)]

        self.grid = []

        for r in range(9):
            self.grid.append([])
            for c in range(9):
                # https://stackoverflow.com/a/20268305
                self.grid[r].append(Cell(rows[r], cols[c], blocks[r // 3 * 3 + c // 3], r, c))

    def add_values(self):
        print("Fill the Sudoku grid")
        print("Use format number@row,col (e.g 5@1,7 will place a 5 on row 1 and column 7")
        pass
        # hier dan input vragen

    def __str__(self):
        out = "1 2 3 4 5 6 7 8 9".center(20, " ") + "\n"
        col_count = 1

        for r_index, r in enumerate(self.grid):
            if r_index % 3 == 0:
                out += ("- " * 10).rstrip(" ") + "\n"

            for c_index, c in enumerate(r):
                if c_index % 3 == 0:
                    out = out.rstrip(" ") + "|"
                out += c.value + " "

            out = out.rstrip(" ") + "| " + str(col_count) + "\n"
            col_count += 1

        return (out + "- " * 10).rstrip(" ")


g = Grid()
print(g)
