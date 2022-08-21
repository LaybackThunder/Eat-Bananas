
import sys, pygame, time

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
        pygame.display.set_caption('Bouncing Boxes!')

        # Color set-up
        self.BG_COLOR = self.settings.BG_COLOR
        self.BLACK = self.settings.BLACK
        self.WHITE = self.settings.WHITE
        self.RED = self.settings.RED
        self.GREEN = self.settings.GREEN
        self.BLUE = self.settings.BLUE

        # Set-up direccion variables
        self.DOWNLEFT = 'downleft'
        self.DOWNRIGHT = 'downright'
        self.UPLEFT = 'upleft'
        self.UPRIGHT = 'upright'

        # Set-up speed
        self.MOVESPEED = 4

        # Set up the box data structure.
        self.b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': self.RED, 'dir': self.UPRIGHT}
        self.b2 = {'rect': pygame.Rect(200, 200, 20, 20), 'color': self.GREEN, 'dir': self.UPLEFT}
        self.b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': self.BLUE, 'dir': self.DOWNLEFT}
        self.boxes = [self.b1, self.b2, self.b3]
        
    def moveBoxDataStructure(self):
        for b in self.boxes:
            # Move the box data structure.
            if b['dir'] == self.DOWNLEFT:
                b['rect'].left -= self.MOVESPEED
                b['rect'].top += self.MOVESPEED

            if b['dir'] == self.DOWNRIGHT:
                b['rect'].left += self.MOVESPEED
                b['rect'].top += self.MOVESPEED
                
            if b['dir'] == self.UPLEFT:
                b['rect'].left -= self.MOVESPEED
                b['rect'].top -= self.MOVESPEED

            if b['dir'] == self.UPRIGHT:
                b['rect'].left += self.MOVESPEED
                b['rect'].top -= self.MOVESPEED
            
            # Check whether the box has moved out of the window.
            if b['rect'].top < 0:
                # The box has moved past the top.
                if b['dir'] == self.UPLEFT:
                    b['dir'] = self.DOWNLEFT
                if b['dir'] == self.UPRIGHT:
                    b['dir'] = self.DOWNRIGHT
            
            if b['rect'].bottom > self.settings.screen_height:
                # The box has moved past the bottom.
                if b['dir'] == self.DOWNLEFT:
                    b['dir'] = self.UPLEFT
                if b['dir'] == self.DOWNRIGHT:
                    b['dir'] = self.UPRIGHT
            
            if b['rect'].left < 0:
                # The box has moved past the left side.
                if b['dir'] == self.DOWNLEFT:
                    b['dir'] = self.DOWNRIGHT
                if b['dir'] == self.UPLEFT:
                    b['dir'] = self.UPRIGHT

            if b['rect'].right > self.settings.screen_width:
                # The box has moved past the right side.
                if b['dir'] == self.DOWNRIGHT:
                    b['dir'] = self.DOWNLEFT
                if b['dir'] == self.UPRIGHT:
                    b['dir'] = self.UPLEFT
            
            # Draw the box onto the surface.
            pygame.draw.rect(self.screen, b['color'], b['rect'])

    def runScreen(self): # Show the BG on window
        while True: # game loop

            for event in pygame.event.get(): # checks for events
                if event.type == pygame.QUIT: # quit screen condition
                    print('QUIT!!!!!!!')
                    sys.exit()

            self.screen.fill(self.BG_COLOR) # background color
            self.moveBoxDataStructure() # Box movement
   
            pygame.display.flip() # draws elements per cycle
            time.sleep(0.02)


    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    w = Window()
    w.runScreen()