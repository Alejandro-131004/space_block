import pygame
import game
import button


class Space_Block:
    __game_object = game.Game_Block()

    # Colors
    __white = (255, 255, 255)
    __light_grey = (200, 200, 200)
    __black = (0, 0, 0)
    __blue = (0, 122, 255)
    __red = (255, 0, 0)
    __grey = (128, 128, 128)
    __yellow = (255, 255, 0)
    #buttons
    __menu_first_screen_buttons = []

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Block:Roll the Block")
        self.__setup_window()

    def __setup_window(self):
        # Window size
        width, height = 600, 400
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(self.__light_grey)

    def __create_first_screen_buttons(self):
        self.__menu_first_screen_buttons = [
            button.Button(self.__blue, 200, 75, 200, 50, "play","Play"),
            button.Button(self.__blue, 200, 150, 200, 50, "solution","Solution"),
            button.Button(self.__blue, 200, 225, 200, 50, "show_level","Show level"),
            button.Button(self.__red, 500, 300, 100, 50, "exit","Exit")
        ]

        for screen_button in self.__menu_first_screen_buttons:
            screen_button.draw(self.screen, self.__black)

    #criar uma funcao para os botoes levels

    def __check_button(self,identifier):
        match identifier:
            case "play":
                self.check_window("level")

    def check_window(self, window):
        match window:
            case "menu":
                self.__create_first_screen_buttons()
            case "level":
                #fazer o mesmo
        pygame.display.update()
        self.__listed_events()



    def __listed_events(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for screen_button in self.__menu_first_screen_buttons:
                        if screen_button.rect.collidepoint(event.pos):
                            self.__check_button(screen_button.identifier)




space_block = Space_Block()
space_block.check_window("menu")



'''
# Algorithm Buttons
algorithm_sentence_button = Button(blue, 550, 200, 400, 50, "Choose the search algorithm")
algorithm_dfs_button = Button(blue, 650, 300, 200, 50, "DFS")
algorithm_bfs_button = Button(blue, 650, 400, 200, 50, "BFS")
algorithm_astar_button = Button(blue, 650, 500, 200, 50, "A* Algorithm")
algorithm_back_button = Button(red, 1200, 700, 100, 50,"Back")

# Level Buttons
level1_button = Button(blue, 650, 300, 200, 50, "Level 1")
level2_button = Button(blue, 650, 400, 200, 50, "Level 2")
level3_button = Button(blue, 650, 500, 200, 50, "Level 3")
level_back_button = Button(red, 1200, 700, 100, 50, "Back")




# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state == "menu":
                if menu_play_button.rect.collidepoint(event.pos):
                    state = "level_select"
                elif menu_solution_button.rect.collidepoint(event.pos):
                    state = "search_select"
                elif menu_showlevel_button.rect.collidepoint(event.pos):
                    state = "level_select"
                elif menu_exit_button.rect.collidepoint(event.pos):
                    running = False

            elif state == "level_select":
                if level1_button.rect.collidepoint(event.pos):
                    # b = game.Game_Block(1,1,'stand')
                    game_object.set_level(1)
                    init = game.create_block(level1)  #nao tamos a conseguir importar o create_block
                    print(init)
                    init.main(level1)
                elif level2_button.rect.collidepoint(event.pos):
                    print("Level 2") # meter o jogo do nivel 2
                elif level3_button.rect.collidepoint(event.pos):
                    print("Level 3") # meter o jogo do nivel 3
                elif level_back_button.rect.collidepoint(event.pos):
                    state = "menu"

            elif state == "search_select":
                if level1_button.rect.collidepoint(event.pos):
                    state = "solution_search"
                    print("Level 1")
                elif level2_button.rect.collidepoint(event.pos):
                    state = "solution_search"
                    print("Level 2")
                elif level3_button.rect.collidepoint(event.pos):
                    state = "solution_search"
                    print("Level 3")
                elif level_back_button.rect.collidepoint(event.pos):
                    state = "menu"

            elif state == "solution_search":
                if algorithm_dfs_button.rect.collidepoint(event.pos):
                    print("DFS")
                elif algorithm_bfs_button.rect.collidepoint(event.pos):
                    print("BFS")
                elif algorithm_astar_button.rect.collidepoint(event.pos):
                    print("A* Algorithm")
                elif algorithm_back_button.rect.collidepoint(event.pos):
                    state = "menu"

    screen.fill(light_grey)
    if state == "menu":
        menu_sentence_button.draw(screen, black)
        menu_play_button.draw(screen, black)
        menu_solution_button.draw(screen, black)
        menu_showlevel_button.draw(screen, black)
        menu_exit_button.draw(screen, black)

    elif state == "level_select":
        level1_button.draw(screen, black)
        level2_button.draw(screen, black)
        level3_button.draw(screen, black)
        level_back_button.draw(screen, black)

    elif state == "solution_search":
        algorithm_sentence_button.draw(screen, black)
        algorithm_dfs_button.draw(screen, black)
        algorithm_bfs_button.draw(screen, black)
        algorithm_astar_button.draw(screen, black)
        algorithm_back_button.draw(screen, black)

    elif state == "search_select":
        level1_button.draw(screen, black)
        level2_button.draw(screen, black)
        level3_button.draw(screen, black)
        level_back_button.draw(screen, black)

    elif state == "menu_open":
        resume_esc_button.draw(screen, black)
        quit_esc_button.draw(screen, black)

    pygame.display.update()

pygame.quit()'''

'''
THIS IS FOR A SIMPLE MENU WHEN IM PLAYING ONE OF THE LEVELS--> WHEN I CLICK ESC APPEARS A MENU WITH "RESUME" AND "QUIT" 
import pygame

pygame.init()

# Set up the game window
win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("My Game")

# Set up the menu buttons
menu_font = pygame.font.SysFont('Arial', 30)
resume_button = menu_font.render('Resume', True, (255, 255, 255))
quit_button = menu_font.render('Quit', True, (255, 255, 255))
button_width, button_height = 150, 50
button_padding = 20
resume_button_rect = pygame.Rect((win_width - button_width) // 2,
                                 (win_height - button_height) // 2 - button_height - button_padding, button_width,
                                 button_height)
quit_button_rect = pygame.Rect((win_width - button_width) // 2, (win_height - button_height) // 2 + button_padding,
                               button_width, button_height)

# Set up the game variables
running = True
paused = False

# Main game loop
while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Pause the game
                paused = True
        elif event.type == pygame.MOUSEBUTTONDOWN and paused:
            mouse_pos = pygame.mouse.get_pos()
            if resume_button_rect.collidepoint(mouse_pos):
                # Unpause the game
                paused = False
            elif quit_button_rect.collidepoint(mouse_pos):
                # Quit the game
                running = False

    # Game logic and rendering
    if not paused:
        # Update and render the game here
        pass

    # Draw the menu if paused
    if paused:
        # Draw a semi-transparent background
        menu_bg = pygame.Surface((win_width, win_height), pygame.SRCALPHA)
        menu_bg.fill((0, 0, 0, 100))
        win.blit(menu_bg, (0, 0))

        # Draw the buttons
        pygame.draw.rect(win, (255, 0, 0), resume_button_rect)
        pygame.draw.rect(win, (0, 255, 0), quit_button_rect)
        win.blit(resume_button, resume_button_rect)
        win.blit(quit_button, quit_button_rect)

    # Update the display
    pygame.display.update()

pygame.quit()'''

