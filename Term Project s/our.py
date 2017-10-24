#import all necessary modules
import pygame
from pygame.locals import *

#initializations
pygame.init()
screen=pygame.display.set_mode((800,800)) ##this is the size the window the game appears in 
pygame.display.set_caption('Term Project') ##this appears in the left hand corner 
background=pygame.Surface(screen.get_size())
background=background.convert()
color=(40,200,40) ## this is the paintbrush color 
startPos=(0,0)
clock=pygame.time.Clock()
background.fill((0,40,40))  ##this is the color of the main background while playing 
font=pygame.font.SysFont('Verdana',40) ##this controls the font and of "press c for painting options"
colorName="Grey" ## this names the color in use
welcomeFont=pygame.font.SysFont('verdana',30) ## this controls the main headings in the welcome 
colorConfigFont=pygame.font.SysFont('verdana',10) ## this controls the font of the rest of the stuff and the size
welcomeScreen=True ##True turns on the welcome screen False makes it disspears


#mainloop
while 1:
    #welcomescreen
    while welcomeScreen:
       for i in pygame.event.get():
           mainScreenPressed=pygame.key.get_pressed()
           if i.type==QUIT or mainScreenPressed[K_q]:
               exit()
           screen.fill((60,60,0)) ##this is the background color of the welcome screen 
           screen.blit(welcomeFont.render("Paint Program Example For Learning",True,(0,255,0)),(100,100))
           screen.blit(colorConfigFont.render("Painting Options",True,(0,255,0)),(100,150))
           screen.blit(colorConfigFont.render("d-Default Color(Black)",True,(0,255,0)),(100,175))
           screen.blit(colorConfigFont.render("b-Blue Color",True,(0,255,0)),(100,200))
           screen.blit(colorConfigFont.render("r-Red Color",True,(0,55,0)),(140,225)) ##first parenthesis are the color of the words ### second number is how the words are aligned 
           screen.blit(colorConfigFont.render("y-Yellow Color",True,(0,255,0)),(100,250))
           screen.blit(colorConfigFont.render("g-Green Color",True,(0,255,0)),(100,275))
           screen.blit(colorConfigFont.render("e-Eraser",True,(0,255,0)),(100,300))
           screen.blit(colorConfigFont.render("s-Save Image",True,(0,255,0)),(100,325))
           screen.blit(colorConfigFont.render("l-Load Image",True,(0,255,0)),(100,350))
           screen.blit(welcomeFont.render("Press p for painting",True,(0,255,0)),(100,400))
           pygame.display.flip()
           if mainScreenPressed[K_p]:
               welcomeScreen=False ##true means that the main screen stays open false lets the program continue 

    #paint screen        
    pressed=pygame.key.get_pressed()
    if pressed[K_8]: ##pressing which keys here r causes red to work
        color=(255,0,0)
        colorName="Red"
    elif pressed[K_g]: ##still assigning keys 
        color=(0,255,0)
        colorName="Green"
    elif pressed[K_b]:
        color=(0,0,255)
        colorName="Blue"
    elif pressed[K_y]:
        color=(255,255,0)
        colorName="Yellow"
    elif pressed[K_e]:
        color=(255,255,255)
        colorNAme="White"
    elif pressed[K_d]:
        color=(0,0,0)
        colorName="Black"
    elif pressed[K_c]:
        color=(0,0,0)
        colorName="Black"
        welcomeScreen=True
    elif pressed[K_s]:
        pygame.image.save(background,'image.png')
    elif pressed[K_l]:
        background=pygame.image.load('image.png')
        colorName="Black"
        color=(0,0,0)


    for i in pygame.event.get():
        if i.type==QUIT or pressed[K_q]: ## this is how we quit the game (closes the window)
            exit()
        elif i.type==pygame.MOUSEMOTION:
            endPos=pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()==(1,0,0):
                pygame.draw.line(background,color,startPos,endPos,3)
            startPos=endPos

    screen.blit(background,(0,0))
    if color==(800,800,800):
     screen.blit(font.render("Eraser In Use",True,(0,0,0)),(400,400))
     screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))
    else:
     screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))   
     screen.blit(font.render("Color In Use : %s"%colorName,True,color),(400,400))
    pygame.display.flip()