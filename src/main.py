#!/usr/bin/env python

__author__ = 'Daniel Elisabethsønn Antonsen'
__version__ = '0.0.1'

import numpy, sys, os, pygame
from gui import Userinterface
from game import Monty_Hall

class game_loop:

    WIDTH, HEIGHT = 800, 600
    FPS = 70

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.run_game = True
        self.start_screen = False
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Monty Hall Game")
        self.UI = Userinterface(self.SCREEN)
    
    def draw(self):
        pygame.display.update()


    def events(self):
        """
        Event handler
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start_screen = False
                self.run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.start_screen = False
                    self.run_game = False

    def run(self):
        """
        Main game loop
        """
        while self.run_game:
            # Setting FPS
            self.clock.tick(self.FPS)

            # Setting start screen
            while self.start_screen:
                self.clock.tick(self.FPS)
                self.UI.start_screen()
                self.events()
                self.draw()
            
            # Running game
            self.UI.game_screen()    
            self.events()
            self.draw()
        
        pygame.quit() 
        sys.exit()





if __name__ == "__main__":
    loop = game_loop()
    loop.run()
