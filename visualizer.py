import pygame
import random
pygame.init() 

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOUR = WHITE

    GRAYS = [
        (128, 128, 128),
        (165, 165, 165),
        (197, 197, 197)
    ]

    TOP_PAD = 150
    SIDE_PAD = 100 

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visual")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height

        colour = draw_info.GRAYS[i % 3] 

        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.block_width, draw_info.height))


def generate_starting_list(n, min_value, max_value):
    lst = []

    for _ in range(n):
        val = random.randint(min_value, max_value)
        lst.append(val)
    
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_value = 0
    max_value = 100

    lst = generate_starting_list(n, min_value, max_value)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)

        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #lets us quit the game by clicking the x
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
