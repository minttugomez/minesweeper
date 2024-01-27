import pygame
from os import path

class Minesweeper:

    def __init__(self):

        # define colors
        self.white = (255, 255, 255)
        self.gray = (192, 192, 192)
        self.dark_gray = (128, 128, 128)
        self.darkest_gray = (50, 50, 50)

        self.screen = None

        # set up the window
        width, height = 770, 980
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper")

        # set the icon
        self.mine = path.join(path.dirname(__file__), 'icons/mine.png')
        icon_surface = pygame.image.load(self.mine)
        pygame.display.set_icon(icon_surface)

    def run(self):

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()

            self.screen.fill(self.darkest_gray)
            self.draw_grid()
            self.draw_info()

            # update the screen
            pygame.display.flip()

    def draw_grid(self):

        # draw the grid
        cell_size = 30
        for row in range(30):
            for col in range(25):
                rect = pygame.Rect(col * cell_size + 10, row * cell_size + 70, cell_size, cell_size)

                # draw the outer square
                outer_size = 30
                outer_rect = pygame.Rect(rect.centerx - outer_size // 2, rect.centery - outer_size // 2, outer_size, outer_size)
                pygame.draw.rect(self.screen, self.dark_gray, outer_rect)
                
                # draw the inner square
                inner_size = 20
                inner_rect = pygame.Rect(rect.centerx - inner_size // 2, rect.centery - inner_size // 2, inner_size, inner_size)
                pygame.draw.rect(self.screen, self.gray, inner_rect)

                # draw the grid
                pygame.draw.rect(self.screen, self.darkest_gray, rect, 1)

    def draw_info(self):

        info_boxes = [
            (10, 10, 90, 50),
            (110, 10, 60, 50),
            (325, 10, 120, 50),
            (630, 10, 60, 50),
            (700, 10, 60, 50)
        ]

        for box in info_boxes:
            outer_box = pygame.Rect(*box)
            inner_box = pygame.Rect(box[0] + 5, box[1] + 5, box[2] - 10, box[3] - 10)

            pygame.draw.rect(self.screen, self.dark_gray, outer_box)
            pygame.draw.rect(self.screen, self.gray, inner_box)
            pygame.draw.rect(self.screen, self.darkest_gray, outer_box, 1)