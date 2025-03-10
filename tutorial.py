import pygame
from pong import Game

width,height=700,500
window=pygame.display.set_mode((width,height))

game=Game(window,width,height)


run=True
clock=pygame.time.Clock()
while run:
    clock.tick(60)  # while loop can run only 60 times per second
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            break
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True,up=True)
    if keys[pygame.K_s]:
        game.move_paddle(left=True,up=False)
    
    game_info=game.loop()
    print(game_info.left_score,game_info.right_score)
    game.draw(False,True)
    pygame.display.update()
    
pygame.quit()