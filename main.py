import pygame
from table.cell import Cell
from table.row import Row
from table.table import Table

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Tables')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cell = Cell(0, 0, 200, 'информация', 25)
    cell.draw(screen)
    row = Row([cell])
    table = Table([row])
    table.draw(0, 0, screen)
    pygame.display.flip()


