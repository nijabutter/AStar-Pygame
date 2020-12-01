import pygame
class Cell:
    
    def __init__(self, _window, _x, _y, _w, _h, _idX, _idY):
        self.g = 0
        self.h = 0
        self.f = 0
        self.x = _x
        self.y = _y
        self.width = _w
        self.height = _h
        self.window = _window
        self.idX = _idX
        self.idY = _idY
        self.visited = False
        self.neighbours = []
        self.obstacle = False
        self.previous = None

    def draw(self, color):
        filled_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.window, color, filled_rect)
    