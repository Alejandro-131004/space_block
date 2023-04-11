import pygame
import game
import button


class Space_Block:
    __game_object = game.Game_Block()
    __running = True

    # Colors
    __white = (255, 255, 255)
    __light_grey = (200, 200, 200)
    __black = (0, 0, 0)
    __blue = (0, 122, 255)
    __red = (255, 0, 0)
    __grey = (128, 128, 128)
    __yellow = (255, 255, 0)
    #buttons
    __screen_buttons = []
    __level = -1
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Block:Roll the Block")
        self.__setup_window()
        self.__check_window("level")
        self.__listed_events()

    def __setup_window(self):
        # Window size
        width, height = 600, 400
        self.screen = pygame.display.set_mode((width, height))

    def __create_level_choice(self):
        self.__screen_buttons = [
            button.Button(self.__blue, 200, 75, 200, 50, "level", "Level 1"),
            button.Button(self.__blue, 200, 150, 200, 50, "level", "Level 2"),
            button.Button(self.__blue, 200, 225, 200, 50, "level", "Level 3"),
            button.Button(self.__red, 475, 300, 100, 50, "exit", "Exit")
        ]



    # play, solution, show level
    def __create_menu_options(self):
        self.__screen_buttons = [
            button.Button(self.__blue, 200, 125, 200, 50, "play", "Play"),
            button.Button(self.__blue, 200, 200, 200, 50, "solution", "Solution"),
            button.Button(self.__red, 475, 300, 100, 50, "back", "Back")
        ]



    def __create_search_options(self):
        self.__screen_buttons = [
            button.Button(self.__blue, 200, 75, 200, 50, "bfs", "BFS"),
            button.Button(self.__blue, 200, 150, 200, 50, "dfs", "DFS"),
            button.Button(self.__blue, 200, 225, 200, 50, "astar", "A* Star"),
            button.Button(self.__red, 475, 300, 100, 50, "back", "Back")
        ]


    def __check_button(self, identifier, level):
        match identifier:
            case "play":
                self.__check_window("game")
            case "level":
                self.__level = level+1
                self.__check_window("menu")
            case "solution":
                self.__check_window("search")
            case "back":
                self.__check_window("level")
            case "exit":
                self.__running = False



    def __check_window(self, window):
        self.__screen_buttons = []
        self.screen.fill(self.__white)
        match window:
            case "menu":
                self.__create_menu_options()
            case "level":
                self.__create_level_choice()
            case "search":
                self.__create_search_options()
            case "game":
                self.__game_object.set_level(self.__level, self.screen)


        for screen_button in self.__screen_buttons:
            screen_button.draw(self.screen, self.__black)

        pygame.display.update()

    def __update_player_position(self, event):
        self.__game_object.update_player_position(event, self.screen)
        pygame.display.update()
    def __listed_events(self):
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, screen_button in enumerate(self.__screen_buttons):
                        if screen_button.rect.collidepoint(event.pos):
                            self.__check_button(screen_button.identifier, index)
                elif event.type == pygame.KEYDOWN:
                    self.__update_player_position(event)

space_block = Space_Block()



