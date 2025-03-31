import pygame
pygame.init()

gamewindow= pygame.display.set_mode((1200,500))

pygame.display.set_caption("game loop")

# game specific variables
exit_game = False
game_over = False

# Creating a game loop  ( passing order using keyboard and mouse to do something like enter up key means run forward)

while not exit_game:
    pass

pygame.quit()     # exit from pygame
quit()            # exit from python