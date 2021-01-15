
import pygame as pg
import sys

pg.init()
screen=pg.display.set_mode((500,500))

text="Jeremiah"

font=pg.font.Font('freesansbold.ttf',20)#we need a font
text_surface=font.render(text, True, (55, 2, 222))#we need a text surface
text_rect=text_surface.get_rect(center =(100, 100))#we need a text rect



running =True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

    screen.fill((100,100,199))
    screen.blit(text_surface, text_rect)#we need to blit the text_surface onto the screen at a location
    
    pg.display.flip()



