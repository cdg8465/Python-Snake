import pygame

from variables import GRID_SIZE, EMPTY_CELL


def initialize_grid():
    grid = list()

    for y in range(0, GRID_SIZE[0]):
        row = list()
        for x in range(0, GRID_SIZE[1]):
            row.append(EMPTY_CELL)
        grid.append(row)

    return grid


class Game:
    window: pygame.Surface
    grid: list

    def __init__(self, window: pygame.Surface):
        self.window = window
        self.grid = initialize_grid()

        self.display_main_menu()

    def display_main_menu(self):
        pass
