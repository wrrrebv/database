from table.cell import Cell
class Row:
    def __init__(self, cells: list[Cell]):
        self._gap = 10
        self._cells = cells

    def draw(self, x: int, y: int, surface):
        current_x = x
        for cell in self._cells:
            cell.draw(surface)
            current_x += self._gap + cell.size()

    def height(self):
        return self._cells[0].size()
