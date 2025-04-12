import pygame

pygame.init()

screen_width =500
screen_height =300
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Draw a rectangle")
pygame.display.update()
red = (255,0,0)
white= (255,255,255)

# game var
game_over=False
exit_game=False

rect_x_cord =20
rect_y_cord =20
rect_width = 20
rect_height =30

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        
    
    gamewindow.fill(red)    
    pygame.draw.rect(gamewindow,white,[rect_x_cord,rect_y_cord,rect_width,rect_height])
    pygame.display.update()
    


pygame.quit()
quit()
