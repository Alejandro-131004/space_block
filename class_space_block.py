import game
import pygame
import button
from enum import Enum

class Space_Block_Windows(Enum):
    LEVEL = "level"
    MENU = "menu"
    SEARCH = "search"
    GAME = "game"


class Space_Block:
    __game_object = game.Game_Block()
    __running = True
    __active_window = Space_Block_Windows.LEVEL

    __white = (255, 255, 255)
    __black = (0, 0, 0)
    __blue = (0, 122, 255)
    __red = (255, 0, 0)
    __font = ""
    __text = ""
    __textRect = ""

    __screen_buttons = []
    __level = -1

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Space Block: Roll the Block")
        self.__font = pygame.font.Font(None, 32)
        self.__check_window(Space_Block_Windows.LEVEL)
        self.__listed_events()

    def __setup_window(self, width, height):

        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(self.__white)

    def __create_level_choice(self):

        self.__text = self.__font.render('Choose a level to start', True, self.__black)

        self.__screen_buttons = [
            button.Button(self.__blue, 50, 75, 200, 50, button.ButtonIdentifiers.LEVEL, "Level 1"),
            button.Button(self.__blue, 50, 150, 200, 50, button.ButtonIdentifiers.LEVEL, "Level 2"),
            button.Button(self.__blue, 50, 225, 200, 50, button.ButtonIdentifiers.LEVEL, "Level 3")
        ]

    def __create_menu_options(self):

        self.__text = self.__font.render('Select an option', True, self.__black)

        self.__screen_buttons = [
            button.Button(self.__blue, 50, 75, 200, 50, button.ButtonIdentifiers.PLAY, "Play"),
            button.Button(self.__blue, 50, 150, 200, 50, button.ButtonIdentifiers.SOLUTION, "Solution"),
            button.Button(self.__red, -20, 250, 340, 25, button.ButtonIdentifiers.BACK, "Back")
        ]

    def __create_search_options(self):

        self.__screen_buttons = [
            button.Button(self.__blue, 50, 75, 200, 50, button.ButtonIdentifiers.BFS, "BFS"),
            button.Button(self.__blue, 50, 150, 200, 50, button.ButtonIdentifiers.DFS, "DFS"),
            button.Button(self.__red, -20, 325, 340, 25, button.ButtonIdentifiers.BACK, "Back")
        ]

    def __check_button(self, identifier: button.ButtonIdentifiers, level):

        match identifier:
            case button.ButtonIdentifiers.PLAY:
                self.__check_window(Space_Block_Windows.GAME)
            case button.ButtonIdentifiers.LEVEL:
                self.__level = level + 1
                self.__check_window(Space_Block_Windows.MENU)
            case button.ButtonIdentifiers.SOLUTION:
                self.__check_window(Space_Block_Windows.SEARCH)
            case button.ButtonIdentifiers.BFS:
                self.__check_window(Space_Block_Windows.GAME)
            case button.ButtonIdentifiers.DFS:
                self.__check_window(Space_Block_Windows.GAME)
            case button.ButtonIdentifiers.BACK:
                self.__check_window(Space_Block_Windows.LEVEL)
            case button.ButtonIdentifiers.EXIT:
                self.__running = False

    def __start_game(self):

        if self.__level == 1:
            self.__setup_window(400, 240)
        elif self.__level == 2:
            self.__setup_window(600, 240)
        elif self.__level == 3:
            self.__setup_window(600, 400)

        self.__game_object.set_level(self.__level, self.screen)

        self.__text = self.__font.render('', True, self.__black)

    def __check_window(self, window: Space_Block_Windows):

        self.__screen_buttons = []
        match window:
            case Space_Block_Windows.LEVEL:
                self.__setup_window(300, 350)
                self.__create_level_choice()
            case Space_Block_Windows.MENU:
                self.__setup_window(300, 275)
                self.__create_menu_options()
            case Space_Block_Windows.SEARCH:
                self.__setup_window(300, 350)
                self.__create_search_options()
            case Space_Block_Windows.GAME:
                self.__start_game()

        for screen_button in self.__screen_buttons:
            screen_button.draw(self.screen, self.__black)

        self.__textRect = self.__text.get_rect()
        self.__textRect.center = (self.screen.get_width() / 2, 30)

        self.screen.blit(self.__text, self.__textRect)

        pygame.display.update()
        self.__active_window = window

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
                elif event.type == pygame.KEYDOWN and self.__active_window == Space_Block_Windows.GAME:
                    self.__update_player_position(event)