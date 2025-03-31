import pygame
pygame.init()

screen_width =500
screen_height =300
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game loop")
pygame.display.update()

black= (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white= (255,255,255)

exit_game = False
game_over = False




while not exit_game:
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:           
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("Your pressed right arrow key")
            else:
                print("you pressed",event.key)


    gamewindow.fill(red)
    pygame.display.update()
pygame.quit()     
quit()