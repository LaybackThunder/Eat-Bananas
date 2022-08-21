
import sys, pygame

from pygame.locals import *

from settings import Settings

class Window():

    def __init__(self):
        # You can't init methods without pyg
        pygame.init()

        # Accessing all object's settings 
        self.settings = Settings()

        # Screen set-up
        self.screen_size = (self.settings.screen_width, self.settings.screen_height)
        self.BG_COLOR = self.settings.BG_COLOR
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Hello world!')
        
    
    def runScreen(self): # Show the BG on window
        while True: # game loop

            for event in pygame.event.get(): # checks for events
                if event.type == pygame.QUIT: # quit screen condition
                    print('QUIT!!!!!!!')
                    sys.exit()


            self.screen.fill(self.BG_COLOR) # background color
            
            pygame.display.flip() # draws elements per cycle



    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    w = Window()
    w.runScreen()