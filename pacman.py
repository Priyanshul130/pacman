#DEVELOPED BY <PRIYANSHUL SHARMA>
#Webpage Priyanshul.is-a.dev
import pygame
import random
import time
from pygame.locals import *

pygame.init()
pygame.display.set_caption("pac man")

screen_width=900
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])

fruits1=["fruit1.png","fruit2.png","fruit3.png"]

ghost1=["ghost1.png","ghost2.png","ghost3.png"]

def change_bg(img):
    background=pygame.image.load(img)
    #set its size
    bg=pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))



class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pacman.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()


class Fruits(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()
        #SPEED IS RANDOMLY GENERATED
        self.speed=random.randint(1,7)



class Ghost(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
      
        self.moveLeft=False
    



fruit_list=pygame.sprite.Group()
allSprite=pygame.sprite.Group()
ghost_list=pygame.sprite.Group()




for i in range(50):
    fruit=Fruits(random.choice(fruits1))
  
    fruit.rect.x=random.randrange(screen_width)
    fruit.rect.y=random.randrange(screen_height)
  
    fruit_list.add(fruit)
    allSprite.add(fruit)



for i in range(30):
    ghost=Ghost(random.choice(ghost1))
  
    ghost.rect.x=random.randrange(screen_width)
    ghost.rect.y=random.randrange(screen_height)
    
    ghost_list.add(ghost)
    allSprite.add(ghost)


pacman=Pacman()
allSprite.add(pacman)


white=(255,255,255)
red=(255,0,0)


playing=True
score=0


clock=pygame.time.Clock()

start_time=time.time()


my_font=pygame.font.SysFont("Times New Roman",40)

time_font=pygame.font.SysFont("Times New Roman",70)

text=my_font.render("score " +str(0),True,white )




while playing:
    clock.tick(30)

    
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False


   
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

        keys=pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if pacman.rect.y> 0:
                pacman.rect.y -= 5
                
        if keys[pygame.K_DOWN]:
            if pacman.rect.y< 630:
                pacman.rect.y += 5

        if keys[pygame.K_LEFT]:
            if pacman.rect.x> 0:
                pacman.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            if pacman.rect.x< 850:
                pacman.rect.x += 5


        
        fruit_hit_list = pygame.sprite.spritecollide(pacman, fruit_list, True)
        ghost_hit_list=pygame.sprite.spritecollide(pacman, ghost_list, True)


        
        for fruit in fruit_hit_list:
            score+=1
            text=my_font.render("Score ="+str(score),True,white)

        for ghost in ghost_hit_list:
            score-=5
            text=my_font.render("Score ="+str(score),True,white)

        screen.blit(text,(730,80))
        allSprite.draw(screen)
    pygame.display.update()
pygame.quit()