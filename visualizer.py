import pygame
import random
import math
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

    FONT = pygame.font.SysFont('arial', 10)
    LARGE_FONT = pygame.font.SysFont('arial', 30)

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
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOUR)

    title = draw_info.FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1 , draw_info.BLACK)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render(" Reset - R | Start Sorting - SPACE | Ascending - A | Decending - D", 1 , draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 35))

    Sorting = draw_info.FONT.render(" Insertion Sort - I | Bubble Sort - B ", 1 , draw_info.BLACK)
    draw_info.window.blit(Sorting, (draw_info.width/2 - Sorting.get_width()/2, 65))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clera_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, 
                            draw_info.height - draw_info.TOP_PAD)
        
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOUR, clera_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height

        colour = draw_info.GRAYS[i % 3] 

        if i in color_positions:
            colour = color_positions[i]

        pygame.draw.rect(draw_info.window, colour, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

def generate_starting_list(n, min_value, max_value):
    lst = []

    for _ in range(n):
        val = random.randint(min_value, max_value)
        lst.append(val)
    
    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True
    return

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_value = 0
    max_value = 100

    lst = generate_starting_list(n, min_value, max_value)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(200)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #lets us quit the game by clicking the x
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                sorting = False
                lst = generate_starting_list(n, min_value, max_value)
                draw_info.set_list(lst)
                
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False


    pygame.quit()


if __name__ == "__main__":
    main()
