import pygame

class Ship:
        def __init__(self, ai_game):
            self.screen = ai_game.screen
            # pygame allows us to treat elements as rectangle
            self.screen_rect = ai_game.screen.get_rect()

            self.image = pygame.image.load("images/ship.bmp")
            self.rect = self.image.get_rect()
            self.rect.midbottom = self.screen_rect.midbottom
        
        # Method that draws the image to the screen at the pos specs by self.rect
        def blitme(self):
            self.screen.blit(self.image, self.rect)