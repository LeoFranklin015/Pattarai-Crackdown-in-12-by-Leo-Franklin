import pygame

import time
n=int(input("Enter the number of times the ball want to bounce vertically: "))
print("Customize your screen and ball yourself :)")

#to select the colour of screen
print("Enter 1 for red colour screen ")
print("Enter 2 for yellow colour screen")
print("Enter 3 for black colour screen")
print("Enter 4 for white colour screen")
print("Enter 5 for blue colour screen")
screen_colour=int(input("Enter the number of the colour of the screen from above data:"))
if screen_colour==1:
    filler=(255,0,0)
elif screen_colour==2:
    filler=(255,255,0)
elif screen_colour==3:
    filler=(0,0,0)
elif screen_colour==4:
    filler=(255,255,255)
elif screen_colour==5:
    filler=(173,216,230)

#to select the colour of the ball
print("Enter 1 for red colour ball ")
print("Enter 2 for yellow colour ball")
print("Enter 3 for green colour ball")
print("Enter 4 for white colour ball")
print("Enter 5 for black colour ball")
print("Enter 6 for grey colour ball")
ball_colour=int(input("Enter the number of the colour of the ball from above data:"))
if ball_colour==1:
    ball_filler=(255,0,0)
elif ball_colour==2:
    ball_filler=(255,255,0)
elif ball_colour==3:
    ball_filler=(0,255,0)
elif ball_colour==4:
    ball_filler=(255,255,255)
elif ball_colour==5:
    ball_filler=(0,0,0)
elif ball_colour==6:
    ball_filler=(128,128,128)
print("Enjoy watching your ball bounce in the pygame screen :)")
pygame.init() 

screen=pygame.display.set_mode((500,300)) 
x=1
y=1 
direction=1 

counter=0 

while True:

    screen.fill(filler)

    pygame.draw.circle(screen,ball_filler,(250,y),13,0)
    pygame.display.update()
    time.sleep(0.0005)

    if y==300:

        direction=-1 

    elif y==0: 

        direction=1 

        counter=counter+1 

    y=y+direction 
    

    if counter==n: 

        pygame.quit() 

        break 
