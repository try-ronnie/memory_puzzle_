import random , pygame , sys
from pygame.locals import *
# first we write the memory required to run this game 


fps = 30 # general speed of the program
WINDOWWIDTH = 640 # height of the windows width in pixels 
WINDOWHEIGHT = 480 # THE HEIGHT IN PIXELS OF THE WINDOW OFC
REVEALSPEED = 8 # speed of the boxes sliding to reveal the hidden content 
BOXSIZE = 40 # size of the box height and width in pixels
GAPSIZE = 10 # size og the gap between the boxes in pixels
BOARDWIDTH = 10 # number of the columns of icons 
BOARDHEIGHT = 7 # number of rows of ico
assert(BOARDWIDTH * BOARDHEIGHT) % 2 == 0 , 'board needs to have an even number of boxes for pairs of matches'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE*GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT- (BOARDHEIGHT *(BOXSIZE *GAPSIZE)))/2)# these 2  calculates the margin or spcae left which the board isnt cobvering 

# setting up the colours to use for the game
GRAY = (100,100,100)
NAVYBLUE = (60 , 60 , 100)
WHITE = (255, 255 ,255)
RED = (255 ,0,0)
GREEN = (0 , 255 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255 , 0)
ORANGE = (255 , 128, 0)
PURPLE = (255 , 0 ,255)
CYAN = (0 , 255 ,255)


# setting up COLOUR FOR THE SURFACE 
BGCOLOUR = NAVYBLUE # this will work for our display fill
LIGHTBGCOLOUR = GRAY # 
BOXCOLOUR = WHITE
HIGHLIGHTCOLOUR = BLUE

# setting up shapes  =MEMORY FOR THE IF STATEMENTS IG
DONUT = 'donut' 
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLOURS = (RED, GREEN, BLUE,YELLOW,ORANGE, PURPLE, CYAN , GRAY, NAVYBLUE, WHITE)
ALLSHAPES = (DONUT , SQUARE, DIAMOND , LINES , OVAL )

assert len(ALLCOLOURS) * len(ALLSHAPES) * 2 >= BOARDHEIGHT * BOARDWIDTH , ' THE BOARD IS TOO SMALL FOR THE NUMBER OF SHAPES AND CLOURS DEFINED'

def main ():
    global FPSCLOCK , DISPLAYSURF # This is used to set this variables to be global and not consider any scoping
    pygame.init() # to start the lib 
    FPSCLOCK = pygame.time.Clock()  #this creates a time object that handles the timing of occurences so that the computer canuse the objects methods to keep track of time and manage it
    DISPLAYSURF = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)
    mouse_x = 0 # used to store the x_axis calibration of the mouse
    mouse_y = 0 # calculates the y_acis calibration
    pygame.display.set_captiom('memory puzzle 2.0')
    