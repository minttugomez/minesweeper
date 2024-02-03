import pygame
from os import path

class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = pygame.time.get.ticks()
            self.is_running = True

    def stop(self):
        self.is_running = False
    
    def reset(self):
        self.start_time = 0
        self.is_running = False

    def get_elapsed_time(self):
        if self.is_running:
            return pygame.time.get_ticks()
        else:
            return 0
        
class Button:
    def __init__(self, rect, grid_position):
        self.rect = pygame.Rect(rect)
        self.grid_position = grid_position
        
    def draw(self, screen, inner_color, outer_color, border_color, text=""):

        inner_size_x = self.rect.width - 10
        inner_size_y = self.rect.height - 10
        inner_rect = pygame.Rect(
            self.rect.centerx - inner_size_x // 2,
            self.rect.centery - inner_size_y // 2,
            inner_size_x,
            inner_size_y)

        pygame.draw.rect(screen, outer_color, self.rect)
        pygame.draw.rect(screen, border_color, self.rect, 1)
        pygame.draw.rect(screen, inner_color, inner_rect)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True

class Minesweeper:

    def __init__(self):

        # define colors
        self.white = (255, 255, 255)
        self.gray = (192, 192, 192)
        self.dark_gray = (128, 128, 128)
        self.darkest_gray = (50, 50, 50)

        self.screen = None
        self.game_status = 0 # not started
        self.mines_left = 0 # shows 0 until game started
        self.stopwatch = Stopwatch()

        # initialize font
        pygame.font.init()

        # initialize buttons
        self.buttons = []
        cell_size = 30
        for row in range(25):
            for col in range(25):
                rect = pygame.Rect(col * cell_size + 10, row * cell_size + 70, cell_size, cell_size)
                grid_position = (row, col)
                button = Button(rect, grid_position)
                self.buttons.append(button)

        # set up the window
        width, height = 770, 830
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Minesweeper")

        # set the surface icon
        icon_path = path.join(path.dirname(__file__), 'icons/mine.png')
        icon_surface = pygame.image.load(icon_path)
        pygame.display.set_icon(icon_surface)

        # initialize icons
        self.icon_size = (30, 30)

        icon1_path = path.join(path.dirname(__file__), 'icons/mine.png')
        self.mine = pygame.image.load(icon1_path)
        self.mine = pygame.transform.scale(self.mine, self.icon_size)

        icon2_path = path.join(path.dirname(__file__), 'icons/flag.png')
        self.flag = pygame.image.load(icon2_path)
        self.flag = pygame.transform.scale(self.flag, self.icon_size)

        icon4_path = path.join(path.dirname(__file__), 'icons/stats.png')
        self.stats = pygame.image.load(icon4_path)
        self.stats = pygame.transform.scale(self.stats, self.icon_size)

        icon3_path = path.join(path.dirname(__file__), 'icons/set.png')
        self.set = pygame.image.load(icon3_path)
        self.set = pygame.transform.scale(self.set, self.icon_size)

    def run(self):

        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
            
            # update game status
            self.update_game_status()

            self.screen.fill(self.darkest_gray)

            # draw buttons
            for button in self.buttons:
                button.draw(self.screen, self.gray, self.dark_gray, self.darkest_gray, "")

            # self.draw_grid()
            self.draw_info()

            # update the screen
            pygame.display.flip()

    def draw_info(self):

        info_boxes = [
            (10, 10, 90, 50),
            (110, 10, 60, 50),
            (325, 10, 120, 50),
            (630, 10, 60, 50),
            (700, 10, 60, 50)
        ]

        for i, box in enumerate(info_boxes):
            outer_box = pygame.Rect(*box)
            inner_box = pygame.Rect(box[0] + 5, box[1] + 5, box[2] - 10, box[3] - 10)

            button = Button(outer_box, i)
            self.buttons.append(button)

            button.draw(self.screen, self.gray, self.dark_gray, self.darkest_gray)

            # write the amount of mines left
            if i == 0:
                mine_rect = self.mine.get_rect(center=(inner_box.center[0] - 20, inner_box.center[1]))
                self.screen.blit(self.mine, mine_rect.topleft)
                text_position = (inner_box.center[0] + 15, inner_box.center[1])
                self.draw_text(str(self.mines_left), text_position)

            # draw the flag icon
            elif i == 1:
                flag_rect = self.flag.get_rect(center=inner_box.center)
                self.screen.blit(self.flag, flag_rect.topleft)              
            
            # draw the stopwatch
            elif i == 2:
                elapsed_time = int(self.stopwatch.get_elapsed_time())
                time_text = f"{elapsed_time // 60:02d}:{elapsed_time % 60:02d}"
                self.draw_text(time_text, inner_box.center)

            # draw the stats icon
            elif i == 3:
                stats_rect = self.stats.get_rect(center=inner_box.center)
                self.screen.blit(self.stats, stats_rect.topleft) 

            # draw the settings icon
            elif i == 4:
                set_rect = self.set.get_rect(center=inner_box.center)
                self.screen.blit(self.set, set_rect.topleft)  

    def draw_text(self, text, pos):
        font = pygame.font.Font(None, 40)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=pos)
        self.screen.blit(text_surface, text_rect)

    def update_game_status(self):
        pass