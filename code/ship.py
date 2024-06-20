import pygame
from pygame.sprite import Sprite

class Ship(Sprite) :
        def __init__(self, ai_game):
            super().__init__()
            self.screen = ai_game.screen
            self.settings = ai_game.settings

            # pygame allows us to treat elements as rectangle
            self.screen_rect = ai_game.screen.get_rect()

            self.image = pygame.image.load("images/ship.bmp")
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
            
            # Store a decimal value for the ship's horizontal position.
            self.x = float(self.rect.x)

            self.moving_right = False
            self.moving_left = False

        def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed
            self.rect.x = self.x # self.rect.x only store integer

        def center_ship(self):
            self.rect.midbottom = self.screen_rect.midbottom
            self.x = float(self.rect.x)

        # Method that draws the image to the screen at the pos specs by self.rect
        def blitme(self):
            self.screen.blit(self.image, self.rect)