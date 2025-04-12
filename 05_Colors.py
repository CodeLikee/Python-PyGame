import pygame
import time
pygame.init()

screen_width =500
screen_height =300
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Colors")
pygame.display.update()

game_over=False
exit_game=False

# creating colors using rgb ( use this : https://www.rapidtables.com/web/color/blue-color.html )
black= (0,0,0)
red = (255,0,0)
Lime = (0,255,0)
blue = (0,0,255)
white= (255,255,255)

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        
    # changing the color
    gamewindow.fill(blue)
    pygame.display.update()
    # time.sleep(1)
    # gamewindow.fill(red)
    # pygame.display.update()
    # time.sleep(1)
    # gamewindow.fill(Lime)
    # pygame.display.update()
    # time.sleep(1)
    # gamewindow.fill(blue)
    # pygame.display.update()




pygame.quit()
quit()
