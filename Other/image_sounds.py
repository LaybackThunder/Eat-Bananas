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
        pygame.display.set_caption('Sprites and Sounds!')

        # Set up colors
        self.BG_COLOR = self.settings.BG_COLOR
        self.BLACK = self.settings.BLACK
        self.WHITE = self.settings.WHITE
        self.RED = self.settings.RED
        self.GREEN = self.settings.GREEN
        self.BLUE = self.settings.BLUE

        # Set up the player and food data structures.
        self.player_rect = pygame.Rect(300, 100, 80, 80)
        self.player_img_address = "/home/layback_thunder/Desktop/pract_code/Projects/pygame_pract/images/Rustle.bmp"
        self.player_image = pygame.image.load(self.player_img_address)
        self.player_stretched_image = pygame.transform.scale(self.player_image, (80,80))

        # Set up food image
        self.food_image_address = "/home/layback_thunder/Desktop/pract_code/Projects/pygame_pract/images/small_banana.bmp"
        self.food_image = pygame.image.load(self.food_image_address)
        # food rect is created in a loop in the "drawElements" method

        # Set up food values
        self.NEWFOOD = self.settings.NEWFOOD
        self.FOODSIZE = self.settings.FOODSIZE
        self.food_counter = self.settings.food_counter
        self.foods = self.settings.foods # List
        # Set up food positions on screen
        self.foods_randomX = self.settings.foods_randomX
        self.foods_randomY = self.settings.foods_randomY
        
        # Set up movemnet variables
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # Set up motion
        self.MOVESPEED = self.settings.MOVESPEED
    

    def runGame(self):
        # Game logic

        self.createInitFood()

        while True:
            
            self._checkEvents() # Keyboard & mouse input/events
            self.addNewFood() # Click screen a new food appears
            self.movePlayer() # Keyboard input moves player 
            self.playerfoodCollision() # Did we eat food? Yes? Remove food from screen
            self.drawElements() # Draw them graphics on screen
            
    def _checkEvents(self):
        # Keyboard & corner x events
        for event in pygame.event.get():  # checks for events
            if event.type == QUIT:  # quit screen condition
                print('QUIT!!!!!!!')
                pygame.quit()
                sys.exit()

            self.keyUpEvents(event)
            self.keyDownEvents(event)
            
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

            if event.key == K_x: # Teleportasion
                self.playerTeleport()

        if event.type == MOUSEBUTTONUP: # needs explanation
            self.food_rect = pygame.Rect(event.pos[0], event.pos[1], self.FOODSIZE, self.FOODSIZE)
            self.foods.append(self.food_rect)

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
            self.food_rect = pygame.Rect(self.foods_randomX, self.foods_randomY, self.FOODSIZE, self.FOODSIZE)
            self.foods.append(self.food_rect)  
    
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
            self.food_rect = pygame.Rect(self.foods_randomX, self.foods_randomY, self.FOODSIZE, self.FOODSIZE)
            self.foods.append(self.food_rect)

    def drawElements(self):
        # Draw background
        self.screen.fill(self.BG_COLOR)
        # Draw player
        self.screen.blit(self.player_stretched_image, self.player_rect)
        # Draw the food
        for i in range(len(self.foods)):
            self.screen.blit(self.food_image, self.foods[i])
        
        pygame.display.flip()
        self.maine_clock.tick(40)
        
    def movePlayer(self):
        if self.move_down and self.player_rect.bottom < self.settings.screen_height:
            self.player_rect.top += self.MOVESPEED

        if self.move_up and self.player_rect.top > 0:
            #print(self.player.top)
            self.player_rect.top -= self.MOVESPEED
        
        if self.move_left and self.player_rect.left > 0:
            self.player_rect.left -= self.MOVESPEED

        if self.move_right and self.player_rect.right < self.settings.screen_width:
            self.player_rect.right += self.MOVESPEED

    def playerfoodCollision(self):  
        for food in self.foods[:]: # This list is a copy to facilitate iteration
            if self.player_rect.colliderect(food):
                print(str(self.player_rect.width))
                self.player_rect.width += 5
                self.player_rect.height += 5
                self.player_stretched_image = pygame.transform.scale(self.player_image, (self.player_rect.width, self.player_rect.height))
                self.foods.remove(food)
                
    def playerTeleport(self):
        self.player_rect.top = random.randint(
            0, self.settings.screen_height - self.player_rect.height
            )
        self.player_rect.left = random.randint(
            0, self.settings.screen_width - self.player_rect.width
            )



if __name__ == '__main__':
    # Make a game instance, and run the game.
    cdg = collitionDetection()
    cdg.runGame()
