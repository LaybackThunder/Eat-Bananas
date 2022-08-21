from pydoc import plain
import pygame, sys, random
from pygame.locals import *

from settings import Settings

class collitionDetection():

    def __init__(self):
        # Init pygame functionality
        pygame.init()
        # set clock variable
        self.maine_clock = pygame.time.Clock()

        # Set-up of settings object from other file
        self.settings = Settings()

        # Set up Window
        self.screen_size = (
            self.settings.screen_width, self.settings.screen_height
            )
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Collision Game!')

        # Set up colors
        self.BG_COLOR = self.settings.BG_COLOR
        self.BLACK = self.settings.BLACK
        self.WHITE = self.settings.WHITE
        self.RED = self.settings.RED
        self.GREEN = self.settings.GREEN
        self.BLUE = self.settings.BLUE

        # Set up the player and food data structures.
        self.player = pygame.Rect(300, 100, 50, 50)
        self.NEWFOOD = 40
        self.FOODSIZE = 20
        self.food_counter = 0
        self.foods = []
        self.foods_randomX = 0
        self.foods_randomY = 0
        
        # Set up movemnet variables
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # Set up motion
        self.MOVESPEED = 6
    

    def runGame(self):

        self.createInitFood()

        while True:
            
            self._checkEvents()
            self.addNewFood()
            self.movePlayer()
            self.playerfoodCollision()
            self.drawElements()
            


    def _checkEvents(self):
        # Keyboard & corner x events
        for event in pygame.event.get():  # checks for events
            if event.type == QUIT:  # quit screen condition
                print('QUIT!!!!!!!')
                pygame.quit()
                sys.exit()
            
            self.keyDownEvents(event)
            self.keyUpEvents(event)

    def keyUpEvents(self, event):
        # KEYUP events
        if event.type == KEYUP:
        # Change the keyboard variables.
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_LEFT or event.key == K_a:
                self.move_left = False

            if event.key == K_RIGHT or event.key == K_d:
                self.move_right = False

            if event.key == K_UP or event.key == K_w:
                self.move_up = False

            if event.key == K_DOWN or event.key == K_s:
                self.move_down = False

            if event.key == K_x:
                self.player.top = random.randint(
                    0, self.settings.screen_height - self.player.height
                    ) # FOOD and Player use same code!!!! Make it a setting
                self.player.left = random.randint(
                    0, self.settings.screen_width - self.player.width
                    )
        
        if event.type == MOUSEBUTTONUP: # needs explanation
            self.foods.append(
                pygame.Rect(event.pos[0], event.pos[1], self.FOODSIZE, self.FOODSIZE)
                )

    def keyDownEvents(self, event):
        # KEYDOWN events
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                self.move_right = False
                self.move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                self.move_left = False
                self.move_right = True

            if event.key == K_UP or event.key == K_w:
                self.move_down = False
                self.move_up = True

            if event.key == K_DOWN or event.key == K_s:
                self.move_up = False
                self.move_down = True

        return event

    def createInitFood(self): # Setter
        # Create food when game starts
        for i in range(20):
            self.foods_randomX = random.randint(
                0, self.settings.screen_width - self.FOODSIZE
                )
            self.foods_randomY = random.randint(
                0, self.settings.screen_height - self.FOODSIZE
                )
            self.foods.append(pygame.Rect(
                self.foods_randomX, self.foods_randomY, self.FOODSIZE, self.FOODSIZE)
                )
    
    def addNewFood(self): # Setter
        # Add new food 
        self.foods_randomX = random.randint(
            0, self.settings.screen_width - self.FOODSIZE
            )
        self.foods_randomY = random.randint(
            0, self.settings.screen_height - self.FOODSIZE
            )

        self.food_counter += 1
        if self.food_counter >= self.NEWFOOD:
            self.food_counter = 0
            self.foods.append(
                pygame.Rect(self.foods_randomX, self.foods_randomY, self.FOODSIZE, self.FOODSIZE) 
            )

    def drawElements(self):
        # Draw background
        self.screen.fill(self.BG_COLOR)
        # Draw player
        pygame.draw.rect(self.screen, self.BLACK, self.player)
        # Draw the food
        for i in range(len(self.foods)):
            pygame.draw.rect(self.screen, self.GREEN, self.foods[i])
            # print('FOOD!')
        
        pygame.display.update()
        self.maine_clock.tick(40)
        
    def movePlayer(self):
        if self.move_down and self.player.bottom < self.settings.screen_height:
            self.player.top += self.MOVESPEED

        if self.move_up and self.player.top > 0:
            self.player.top -= self.MOVESPEED
        
        if self.move_left and self.player.left > 0:
            self.player.left -= self.MOVESPEED

        if self.move_right and self.player.right < self.settings.screen_width:
            self.player.right += self.MOVESPEED

    def playerfoodCollision(self):
        for food in self.foods[:]: # This list is a copy to facilitate iteration
            if self.player.colliderect(food):
                self.foods.remove(food)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    cdg = collitionDetection()
    cdg.runGame()
