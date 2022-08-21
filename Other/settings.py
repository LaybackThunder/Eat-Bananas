import pygame

class Settings():

    def __init__(self):
        pygame.init()
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # Color settings
        self.BG_COLOR = (53, 101, 77)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        # Set food
        self.NEWFOOD = 40
        self.FOODSIZE = 40
        self.food_counter = 0
        self.foods = []
        self.foods_randomX = 0
        self.foods_randomY = 0
        # Set up motion
        self.MOVESPEED = 6