from pygame import *

width,height=500,500
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
myClock=time.Clock()
running=True

def drawCircles(x,y,radius,rows,fill):
    count=0
    for i in range(rows):
        for j in range(i+1):
            circle_x=x+i*radius*2
            circle_y=y+j*radius*2
            if count<fill:
                draw.circle(screen,BLUE,(circle_x,circle_y),radius)
            else:
                draw.circle(screen,WHITE,(circle_x,circle_y),radius,1)
            count+=1
            
drawCircles(30,30,25,5,12)
            
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    myClock.tick(60)
    display.flip()
            
quit()
