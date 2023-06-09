import pygame

class Userinterface:

    SCREEN_COLOR ='#335555'
    WHITE = '#FFFFFF'
    RED = '#FF0000'

    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_width(), self.screen.get_height() 
        self.username = None
        self.big_font = pygame.font.SysFont("Verdana", 30)
        self.little_font = pygame.font.SysFont("Verdana", 18)
        self.host = pygame.transform.scale(pygame.image.load("../pictures/Monty_hall_host.jpg"), (50, 50))
        

    def start_screen(self):
        self.screen.fill(self.SCREEN_COLOR)
        welcome = self.big_font.render("WELCOMME TO MONTY HALL GAME", True, self.WHITE)
        start_game = self.little_font.render("START GAME", True, self.WHITE)
        scoreboard = self.little_font.render("SCOREBOARD", True, self.WHITE)
        self.screen.blit(welcome, (self.screen_width / 2 - welcome.get_width() / 2, 
                                   self.screen_height / 2 - 100))
        self.screen.blit(start_game, (self.screen_width / 2 - start_game.get_width() / 2, 
                                      self.screen_height / 2))
        self.screen.blit(scoreboard, (self.screen_width / 2 - scoreboard.get_width() / 2, 
                                      self.screen_height / 2 + 100))
        
    
    def game_screen(self):
        self.screen.fill(self.SCREEN_COLOR)
        self.screen.blit(self.host, (0, 0))


    def pause_screen(self):
        pass

    def end_screen(self):
        pass

    def scoreboard(self):
        pass

    def login(self, name:str):
        pass