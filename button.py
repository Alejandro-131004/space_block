import pygame
from enum import Enum

class ButtonIdentifiers(Enum): # we used enumerators to make sure the variables stay string for the rest of the code, they can never change
    LEVEL = "level"
    PLAY = "play"
    SOLUTION = "solution"
    BACK = "back"
    EXIT = "exit"
    BFS = "bfs"
    DFS = "dfs"
    ASTAR = "astar"

class Button:
    white = (255, 255, 255)

    # we define a class with the color, x and y coordinates, width, height, the identifier and the text for the button
    def __init__(self, color, x, y, width, height, identifier,text=""):
        self.identifier = identifier
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    # this function draw´s and center the buttons with a border instead of a simple rectangle
    def draw(self, surface, outline=None):
        font = pygame.font.Font(None, 20)
        # Draw the button rectangle
        pygame.draw.rect(surface, self.color, self.rect, 0, border_radius=8)
        # Draw the button text
        text_surface = font.render(self.text, True, self.white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

