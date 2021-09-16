import pygame

from variables import WINDOW_SIZE


def main():
    pygame.init()

    pygame.display.set_caption("Snake")
    pygame.display.set_mode(WINDOW_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == '__main__':
    main()
