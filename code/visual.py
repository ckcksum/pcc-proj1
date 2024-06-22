# Set the color
class Visual:
    def __init__(self):
        self.dark_mode = False
        self.check_color_theme()

    def check_color_theme(self):
        # Light mode
        if not self.dark_mode:
            self.bg_color = (230, 230, 230)
            self.bullet_color = (255, 0, 0)
            self.sb_text_color = (30, 30, 30)
            self.play_btn_color = (0, 255, 0)
            self.play_btn_text_color = (255, 255, 255)
        else:
            self.bg_color = (30, 30, 30)
            self.bullet_color = (255, 153, 153)
            self.sb_text_color = (230, 230, 230)
            self.play_btn_color = (0, 100, 0)  
            self.play_btn_text_color = (0, 0, 0)

