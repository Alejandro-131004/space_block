import pygame
from enum import Enum

class ButtonIdentifiers(Enum):
    LEVEL = "level"
    PLAY = "play"
    SOLUTION = "solution"
    BACK = "back"
    EXIT = "exit"
    BFS = "bfs"
    DFS = "dfs"

class Button:
    white = (255, 255, 255)

    def __init__(self, color, x, y, width, height, identifier,text=""):
        self.identifier = identifier
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface, outline=None):
        font = pygame.font.Font(None, 20)
        # Draw the button rectangle
        pygame.draw.rect(surface, self.color, self.rect, 0, border_radius=8)
        # Draw the button text
        text_surface = font.render(self.text, True, self.white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

