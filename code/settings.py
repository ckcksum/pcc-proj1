# A setting class to store all settings for Alien Invasion.
class Settings:
    def __init__(self):         # Initialize the game's setting
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_limit = 3
        
        # Bullet Settings
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 5

        # Speed up settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.alien_speed = 1
        self.bullet_speed = 1
        self.ship_speed = 0.3

        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)