
import pygame as pg
import sys

pg.init()
screen=pg.display.set_mode((500,500))

text="Amy"
text1="is a great student"

font=pg.font.Font('freesansbold.ttf',20)
text_surface=font.render(text, True, (55, 2, 222))
#text_surface1=font.render(text1, True, (55, 199, 22))
text_rect=text_surface.get_rect(center =(100, 100))
#text_rect1=text_surface1.get_rect(center=(100, 130))


running =True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

    screen.fill((100,100,199))
    screen.blit(text_surface, text_rect)
    #screen.blit(text_surface1, text_rect1)
    pg.display.flip()



