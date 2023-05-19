#!/usr/bin/env python

__author__ = 'Daniel Elisabethsønn Antonsen'
__version__ = '0.0.1'

import numpy, sys, os, pygame
from gui import Userinterface
from game import Monty_Hall

class game_loop:

    WIDTH, HEIGHT = 800, 600

    def __init__(self):
        pygame.init()
        self.run_game = True
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Monty Hall Game")
        self.UI = Userinterface(self.SCREEN, self.WIDTH, self.HEIGHT)
    
    def draw(self):
        self.UI.start_screen()
        pygame.display.update()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run_game = False

    def run(self):
        while self.run_game:
            self.events()
            self.draw()
        
        pygame.quit() 
        sys.exit()





if __name__ == "__main__":
    loop = game_loop()
    loop.run()
