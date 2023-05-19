import pygame

class Userinterface:

    COLOR = '#FFFFFF'

    def __init__(self, screen):
        self.screen = screen
        self.username = None
        self.big_font = pygame.font.SysFont("Verdana", 25)
        self.little_font = pygame.font.SysFont("Verdana", 15)

    def start_screen(self):
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height() 
        self.screen.fill('#335555')
        welcome = self.big_font.render("WELCOMME TO MONTY HALL GAME", True, self.COLOR)
        start_game = self.little_font.render("START GAME", True, self.COLOR)
        scoreboard = self.little_font.render("SCOREBOARD", True, self.COLOR)
        self.screen.blit(welcome, (self.screen_width / 2 - welcome.get_width() / 2, 
                                   self.screen_height / 2 - 100))
        self.screen.blit(start_game, (self.screen_width / 2 - start_game.get_width() / 2, 
                                   self.screen_height / 2))
        self.screen.blit(scoreboard, (self.screen_width / 2 - scoreboard.get_width() / 2, 
                                   self.screen_height / 2 + 100))
        
    
    def game_screen(self):
        pass

    def pause_screen(self):
        pass

    def end_screen(self):
        pass

    def scoreboard(self):
        pass
