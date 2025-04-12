import pygame
pygame.init()

screen_width =500
screen_height =300
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake eating food")
pygame.display.update()


black= (0,0,0)
red = (255,0,0)
Lime = (0,255,0)
blue = (0,0,255)
white= (255,255,255)

# game specific variables
game_over=False
exit_game=False

rect_x =20
rect_y=10
rect_size=20
velocity_x=5
velocity_y=5

# clock to update frame
fps = 30
clock = pygame.time.Clock()


# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                rect_x+=5    
            elif event.key==pygame.K_LEFT:
                rect_x-=5    
            elif event.key==pygame.K_UP:
                rect_y-=5    
            elif event.key==pygame.K_DOWN:
                rect_y+=5   
    rect_x+=velocity_x
    rect_y+=velocity_y

    gamewindow.fill(red)
    pygame.draw.rect(gamewindow,blue,[rect_x,rect_y,rect_size,rect_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
