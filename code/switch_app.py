import threading
import tkinter as tk
import pygame
import os
from alien_invasion import AlienInvasion

class SwitchApp:
    # Default: light mode
    def __init__(self, root, ai_game):
        self.root = root
        self.ai_game = ai_game
        self.root.title('Dark mode switch')
        self.root.geometry("20x200")
        self.dark_mode_on = False
        self.on_image = tk.PhotoImage(file="images/dm_on.png")
        self.off_image = tk.PhotoImage(file="images/dm_off.png")
        self.switch_button = tk.Button(root, image=self.off_image, bd=0, command=self.switch)
        self.switch_button.pack(pady=50)

    def switch(self):
        self.dark_mode_on = not self.dark_mode_on
        self.switch_button.config(image=self.on_image if self.dark_mode_on else self.off_image)
        self.ai_game.update_visuals(self.dark_mode_on)

if __name__ == "__main__":
    root = tk.Tk()
    ai_game = AlienInvasion()
    app = SwitchApp(root, ai_game)
    ai_game_thread = threading.Thread(target=ai_game.run_game)
    ai_game_thread.daemon = True
    ai_game_thread.start()
    root.mainloop()