# author: Boyo
# tutorial author: Clear Code
# date: 2024 Jan 7
# purpose: to learn pygame by following a Snake tutorial
# https://www.youtube.com/watch?v=QFvqStqPCRU


# intro
import pygame, sys

pygame.init()                               # starts pygame e.g. sound + graphics modules
screen = pygame.display.set_mode((400,500)) # display window / main game, width x height
clock = pygame.time.Clock()                 # clk obj that influences framerate

test_surface = pygame.Surface((100,200))    # test surface
test_surface.fill((0,0,200))
test_rect = test_surface.get_rect(center = (200,250))
while True:                                 # keeps window open, draw all our elements
    for event in pygame.event.get():        # check for every possible event at beginning of each loop
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()              # sys is another module, sys.exit makes sure code is closed
    screen.fill((175,215,70))
    screen.blit(test_surface,test_rect)     # block image t
    pygame.display.update()                 # display test surface
    clock.tick(60)                          # maximum speed for the game to run

# adding visuals: above is a display surface (only 1 and displayed by default), now we make surfaces (multiple display graphics)

