import pygame

class Userinterface:

    COLOR = '#FFFFFF'

    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.username = None
        self.big_font = pygame.font.SysFont("Verdana", 50)
        self.little_font = pygame.font.SysFont("Verdana", 32)

    def start_screen(self):
        self.screen.fill('#335555')
        start_text = self.big_font.render("WELCOMME TO MONTY HALL GAME", False, self.COLOR)
        start_game = self.little_font.render("START GAME", False, self.COLOR)
        


    
    def game_screen(self):
        pass

    def pause_screen(self):
        pass

    def end_screen(self):
        pass

    def scoreboard(self):
        pass
