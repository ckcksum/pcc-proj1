# Create a class to represent the game

# Import modules.
import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()

        # Create a display windows: (Wide,High) in pixels 
        self.screen = pygame.display.set_mode((1200,600)) 
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 200)

    def run_game(self):
        # Main loop for the game:
        while True:
            # Watch for keyboard and mouse events
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()