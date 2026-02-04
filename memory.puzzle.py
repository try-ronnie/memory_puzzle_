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
YMARGIN = int((WINDOWHEIGHT- (BOARDHEIGHT *(BOXSIZE *GAPSIZE)))/2)# this calculates the margin or spcae left which the board isnt cobvering 

