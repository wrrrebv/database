import pygame
class Table:
    def __init__(self, rows: list):
        self._gap = 10
        self._rows = rows

    def draw(self, x: int, y: int, surface: pygame.Surface):
        current_y = y
        for row in self._rows:
            row.draw(current_y, x, surface)
            current_y += row.height() + self._gap
