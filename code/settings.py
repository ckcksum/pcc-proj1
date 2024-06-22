# A settings class to store all settings for Alien Invasion.

from visual import Visual

class Settings:
    def __init__(self):         # Initialize the game's settings
        self.visual = Visual()

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600

        # Color settings
        self.bg_color = self.visual.bg_color
        self.bullet_color = self.visual.bullet_color
        self.sb_text_color = self.visual.sb_text_color
        self.play_btn_color = self.visual.play_btn_color
        self.play_btn_text_color = self.visual.play_btn_text_color

        # Ship settings
        self.ship_limit = 3
        
        # Bullet Settings
        self.bullet_width = 2
        self.bullet_height = 10
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
        self.alien_points = 50

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
    
    def switch_mode(self, dark_mode):
        self.visual.dark_mode = dark_mode
        self.visual.check_color_theme()
        self.bg_color = self.visual.bg_color
        self.bullet_color = self.visual.bullet_color
        self.sb_text_color = self.visual.sb_text_color
        self.play_btn_color = self.visual.play_btn_color
        self.play_btn_text_color = self.visual.play_btn_text_color