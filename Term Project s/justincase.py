import pygame
import time
import random
#set up
pygame.init()

#define colors rgb
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
brown = (163,115,51)

##images
man_img = pygame.image.load("man.png")
man_w = 85
old_img = pygame.image.load("oldm.png")
tour_img = pygame.image.load("tour.png")
home_img = pygame.image.load("home.png")
home_hover = pygame.image.load("homehover.png")

##window size
screen_w = 1250
screen_h = 900
gamedisplay = pygame.display.set_mode((screen_w,screen_h))
##name of window
pygame.display.set_caption("City Run")
##time fps
clock = pygame.time.Clock()

##displays man
def man(x,y):
    gamedisplay.blit(man_img,(x,y))

#home screen
def homescreen(x,y):
    gamedisplay.blit(home_img,(0,0))

def homehover(x,y):
    gamedisplay.blit(home_hover,(0,0))

##obstacles 
def obs_old(oldx,oldy,oldw,oldh):
    gamedisplay.blit(old_img,(oldx,oldy))

def obs_tour(tourx,toury,tourw,tourh):
    gamedisplay.blit(tour_img,(tourx,toury))

#keeps score
def points(count): 
    font = pygame.font.SysFont(None,50)
    text = font.render("Points: "+ str(count), True, brown)
    gamedisplay.blit(text,(550,100))

#textobjects
def text_objects(text,font):
    textsurface = font.render(text, True, brown)
    return textsurface, textsurface.get_rect()

##mesage
def messagedisplay(text):
    message = pygame.font.Font("freesansbold.ttf", 80)
    Textsurf, textrect = text_objects(text,message)
    textrect.center = ((screen_w/2), (screen_h/2))
    gamedisplay.blit(Textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    gameloop()

def play(x,y,w,h,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() 

    if x + w > mouse[0] > x and y + h > mouse [1] > y: 
        homehover(0,0)
        if click[0] == 1 and action !=None:
            if action == "play":
                gameloop()
    else:
        homescreen(0,0)

##what happens when crash
def crash():
    messagedisplay("You crashed")

##start menu before game starts
def startmenu(): 
    intro = True
    while intro: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

        play(447,650,403,90,"play")
        pygame.display.update()
        clock.tick(20)

#gameloop
def gameloop():
    x = (screen_w*.5)
    y = (screen_h*.7)
    x_change = 0
    y_change = 0
    oldx = random.randrange(0,screen_w)
    tourx = random.randrange(0,screen_w)
    oldy = -300
    toury = -200
    old_speed = 1
    tourspeed = 4
    oldw = 125
    oldh = 245
    tourw = 125
    tourh = 264

    dodged = 0

    ##stops the game 
    gameexit = False 

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            ##when the button is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5

            ##when the button is let go 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
                elif event.key == pygame.K_DOWN or pygame.K_UP:
                    y_change = 0
                

        x = x + x_change
        y = y + y_change
        gamedisplay.fill(white)

        obs_old(oldx,oldy,oldh,oldw)
        obs_tour(tourx,toury,tourh,tourw)
        oldy = oldy + old_speed
        toury = toury + tourspeed
        man(x,y)
        points(dodged)

        ##defining boundaries
        if x > screen_w - man_w or x < 0:
            crash()

        #new old man obstacles
        if oldy > screen_h: 
            oldy = 0 - oldh
            oldx = random.randrange(0,screen_w)
            dodged = dodged + 1
            old_speed = old_speed + 1
        
        #calculating if player crashed with old man 
        if y < oldy + oldh: 
            if (x > oldx and x < oldx + oldw) or (x + man_w > oldx and x + man_w < oldx + oldw):
                crash()
        
        #new tourist obstacles
        if toury > screen_h:
            toury = 0 - tourh
            tourx = random.randrange(0+tourw,screen_w-tourw)
            dodged = dodged + 2
            tourspeed = tourspeed + 1

        #calculate if player crashed with tourist
        if y < toury + tourh: 
            if (x > tourx and x < tourx + tourw) or (x + man_w > tourx and x + man_w < tourx + tourw):
                crash()

        pygame.display.update()
        clock.tick(60)

startmenu()
gameloop()
pygame.quit()
quit()