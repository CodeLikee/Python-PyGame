import pygame
pygame.init()

gamewindow= pygame.display.set_mode((500,300))
pygame.display.set_caption("game loop")
pygame.display.update()


exit_game = False
game_over = False

while not exit_game:
    # making an event handler
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:            # to quit the game
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("Your pressed right arrow key")
            else:
                print("you pressed",event.key)
pygame.quit()     
quit()
