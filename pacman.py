import pygame
import random
import time
from pygame.locals import *


#change background
def change_bg(img):
    background=pygame.image.load(img)
    #set its size
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))


#initliasing pygame
pygame.init()
pygame.display.set_caption("pac man")
#SET HEIGHT WIDTH OF SCREEN
screen_width=900
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])



#creating sprite-pacman
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pacman.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()


#creating fruits sprite
class Fruits(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        #SPEED IS RANDOMLY GENERATED
        self.speed=random.randint(1,7)



#creating ghost sprites sprite
class Ghost(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        #this determine target has to move left or right
        self.moveLeft=False


#list ofimage for fruits  class
fruits1=["fruit1.png","fruit2.png","fruit3.png"]


#list ofimage for ghost class
ghost1=["ghost1.png","ghost2.png","ghost3.png"]



#create sprite group
fruit_list=pygame.sprite.Group()
allSprite=pygame.sprite.Group()
ghost_list=pygame.sprite.Group()




#create fruits sprites on ramdom location
for i in range(50):
    fruit=Fruits(random.choice(fruits1))
    #set a rondom location
    fruit.rect.x=random.randrange(screen_width)
    fruit.rect.y=random.randrange(screen_height)
    #add to stone list
    fruit_list.add(fruit)
    allSprite.add(fruit)



#create ghost sprites on ramdom location
for i in range(30):
    ghost=Ghost(random.choice(ghost1))
    #set a rondom location
    ghost.rect.x=random.randrange(screen_width)
    ghost.rect.y=random.randrange(screen_height)
    #add to soldier list
    ghost_list.add(ghost)
    allSprite.add(ghost)

#create pirate
pacman=Pacman()
allSprite.add(pacman)


#init essential variables
#def colour
white=(255,255,255)
red=(255,0,0)


playing=True
score=0


#clock
clock=pygame.time.Clock()
#start time
start_time=time.time()

#font to print score on screen
my_font=pygame.font.SysFont("Times New Roman",40)

time_font=pygame.font.SysFont("Times New Roman",70)

text=my_font.render("score " +str(0),True,white )



#main program loop
while playing:
    #refresh 30 times in a sec(fps 30) it can be used to control speed
    clock.tick(30)

    
    #quit the game
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False


    #check if time starts with 60 sec and end at 0 sec
    timeElapsed=time.time()-start_time
    if timeElapsed>=60:
        if score>20:
            text=my_font.render("YOU WIN",True,red)
            change_bg("winscreen.jfif")
        else:
            text=my_font.render("BETTER LUCK NEXT TIME",True,red)
            change_bg("losescreen.jpg")
        screen.blit(text,(250,40))

    
    else:
        change_bg("gamescreen.jpg")
        countDown=time_font.render(str(60-int(timeElapsed)),True,red)
        screen.blit(countDown,(800,10))

        
        #move the pacman as per key presed
        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:#up
            if pacman.rect.y> 0:
                pacman.rect.y -= 5
                
        if keys[pygame.K_DOWN]:#DOWN
            if pacman.rect.y< 630:
                pacman.rect.y += 5

        if keys[pygame.K_LEFT]:#LEFT
            if pacman.rect.x> 0:
                pacman.rect.x -= 5

        if keys[pygame.K_RIGHT]:#RIGHT
            if pacman.rect.x< 850:
                pacman.rect.x += 5


        #see if stone and pirate has collide
        fruit_hit_list = pygame.sprite.spritecollide(pacman, fruit_list, True)
        ghost_hit_list=pygame.sprite.spritecollide(pacman, ghost_list, True)


        #check the list of collision
        for fruit in fruit_hit_list:
            score+=1
            text=my_font.render("Score ="+str(score),True,white)

        for ghost in ghost_hit_list:
            score-=5
            text=my_font.render("Score ="+str(score),True,white)

        screen.blit(text,(730,80))


        #draw all the sprites
        allSprite.draw(screen)
    pygame.display.update()
pygame.quit()





















        
