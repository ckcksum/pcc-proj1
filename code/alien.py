import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    def switch_mode(self, dark_mode):
        if dark_mode:
            self.image = pygame.image.load('images/alien_dark.png').convert_alpha()
        else:
            self.image = pygame.image.load('images/alien.bmp').convert_alpha()
        # Preserve the alien's position
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
