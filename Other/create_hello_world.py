
#from re import U
import sys
import pygame

#from pygame.locals import *

from settings import Settings


class HelloWorld():

    def __init__(self):
        # You can't init methods without pyg
        pygame.init()

        # Accessing all object's settings
        self.settings = Settings()

        # Screen set-up
        self.screen_size = (
            self.settings.screen_width, self.settings.screen_height
            )
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Hello world!')

        # Color set-up
        self.BG_COLOR = self.settings.BG_COLOR
        self.BLACK = self.settings.BLACK
        self.WHITE = self.settings.WHITE
        self.RED = self.settings.RED
        self.GREEN = self.settings.GREEN
        self.BLUE = self.settings.BLUE

        # Set-up font & its Rec
        self.basic_font = pygame.font.SysFont(None, 100)
        # Set-up text
        self.text = self.basic_font.render(
            'Hello world!', True, self.WHITE, self.BLUE
        )

        # Get font & screen Rec & set screen cordinates for font
        self.text_rect = self.text.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.text_rect.centerx = self.screen_rect.centerx  # potential error
        self.text_rect.centery = self.screen_rect.centery  # potential error


    def _check_events(self):

        for event in pygame.event.get():  # checks for events
            if event.type == pygame.QUIT:  # quit screen condition
                print('QUIT!!!!!!!')
                pygame.quit()
                sys.exit()

    def _drawElements(self):
        
        self.screen.fill(self.BG_COLOR)  # background color
        self.screen.blit(self.text, self.text_rect) # Draw a surface on to another surface

    def runScreen(self):  # Show the BG on window
        while True:  # game loop

            self._check_events()
            self._drawElements()
            pygame.display.flip()  # Update the full display Surface to the screen


if __name__ == '__main__':
    # Make a game instance, and run the game.
    hw = HelloWorld()
    hw.runScreen()
