import pygame


def main():
    pygame.init()

    pygame.display.set_mode((1280, 720))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == '__main__':
    main()
