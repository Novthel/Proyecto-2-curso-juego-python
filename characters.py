import pygame
from constants import WIDTH_CHARACTERS, HEIGHT_CHARACTERS, COLOR

class Personaje():
    
    def __init__(self, x, y):
        
        self.forma = pygame.Rect(0, 0, WIDTH_CHARACTERS, HEIGHT_CHARACTERS)
        self.forma.center = (x,y)
    
    
    def movimiento(self, delta_x, delta_y):
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
    
    def draw(self, surface):
        pygame.draw.rect(surface, COLOR, self.forma)
    
        