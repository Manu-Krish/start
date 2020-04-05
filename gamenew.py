import pygame
import random

pygame.init()

win=pygame.display.set_mode((750,650))
walkcount=0
run=True
clock=pygame.time.Clock()
tempidle=[pygame.image.load('i1.png'),pygame.image.load('i2.png'),pygame.image.load('i3.png')]
rockpic=[pygame.transform.scale(pygame.image.load('rocket.png'),(100,50)),pygame.transform.flip(pygame.transform.scale(pygame.image.load('rocket.png'),(100,50)),True,False)]
#oc=pygame.image.load('rocket.png')
walkleft=[]
idle=[]
walkright=[pygame.image.load('1.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),pygame.image.load('4.png'),pygame.image.load('5.png'),pygame.image.load('6.png')]
for i in walkright:
    p=i
    i=pygame.transform.scale(i,(50,70))
    #walkright[walkright.index(p)]=i
    walkleft.append(pygame.transform.flip(i,True,False))
    
walkright=[]
for i in walkleft:
     i=pygame.transform.scale(i,(50,70))
     walkright.append(pygame.transform.flip(i,True,False))
for i in tempidle:
     i=pygame.transform.scale(i,(50,70))
     idle.append(pygame.transform.flip(i,True,False))       
     
    

#walkright=[pygame.image.load('r1.jpg'),pygame.image.load('r2.jpg'),pygame.image.load('r3.jpg'),pygame.image.load('r4.jpg'),pygame.image.load('r5.jpg'),pygame.image.load('r6.jpg')]
bg=pygame.image.load('back2.jpeg')
tf=pygame.image.load('tofee.png')
tf=pygame.transform.scale(tf,(44,44))
lifein=pygame.image.load('life.png')
bombin=pygame.image.load('bomb.png')
lifein=pygame.transform.scale(lifein,(30,30))
score=0
bombin=pygame.transform.scale(bombin,(44,44))
life=3
icount=0

bgm=pygame.mixer.music.load('bgm.mp3')
psound=pygame.mixer.Sound('pointsound.wav')
bs=pygame.mixer.Sound('bs.wav')
alarm=pygame.mixer.Sound('alarm.wav')
space=pygame.mixer.Sound('space.wav')

class character:

    def __init__(self,x,y,height,width):

        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.left=False
        self.right=False
        self.vel=10
        self.hitbox=(self.x,self.y,40,40)
        self.isjumb=False
        self.jumbheight=10
        
    def disp(self,win):
        global walkcount
        global icount
        if walkcount+1>=18:
            walkcount=0
       
        
        if alien.left:   
            win.blit(walkleft[walkcount//3],(self.x,self.y))
            icount=0
        elif alien.right:   
            win.blit(walkright[walkcount//3],(self.x,self.y))
            icount=0
        else:
            if icount+1>=100:
                icount=0
            else:
                icount+=1
            if icount>50 and icount<56:   
                win.blit(idle[(icount-50)//2],(self.x,self.y))
            else:win.blit(idle[0],(self.x,self.y))
            
            




class point:
    def __init__(self,x,y,vel):
        self.x=x
        self.y=y
        self.vel=vel
        self.hitbox=(self.x,self.y,40,40)

    def disp(self,win):
        win.blit(tf,(self.x,self.y))
        
class bad():
    def __init__(self,x,y,vel):
        self.x=x
        self.y=y
        self.vel=vel

    def disp(self,win):
        win.blit(bombin,(self.x,self.y))
        
font=pygame.font.SysFont('comicsans',30,True)
font2=pygame.font.SysFont('comicsans',70,True)

def endgame(win):
    text2=font2.render('Game Over',1,(255,255,255))
    win.blit(text2,(200,200))
    text3=font.render('PRESS ENTER TO RESTART',1,(255,255,255))
    win.blit(text3,(200,300))
    pygame.display.update()
    #keys=pygame.K_UP
    i=True
    global bgap
    global tgap
    global isrocket
    isrocket=False
    
    global score
    score=0
    global life
    global j
    j=1
    
    life=3
    global tofees
    global bombs
    tofees=[]
    bombs=[]
    bgap=1
    tgap=10
    while(i):
        i=True
        
        for event in pygame.event.get():
         if event.type==pygame.QUIT:
             pygame.quit()
           
            
        global run
        key=pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
                 i=False
                 break
                 
                
                 
        if key[pygame.K_ESCAPE]:
            
                  run=False
                  break
        
    
class rocket:
    def __init__(self):
        num=random.randrange(0,2)
        
        if num==1:
            self.x=800
            self.y=550
            self.vel=10
            self.dirc=1
        else:
            self.x=-40
            self.y=550
            self.vel=10
            self.dirc=-1
            
              
    def disp(self,win):
             
             if self.dirc==-1:
                win.blit(rockpic[0],(self.x,self.y))
             else:
                  win.blit(rockpic[self.dirc],(self.x,self.y))

def displife():
     global life
     text3=font.render('Life  :',1,(255,255,255))
     win.blit(text3,(30,50))
     for i in range(life):
         win.blit(lifein,(100+40*i,40))
         
   
            
        
def maindisp():
    win.blit(bg,(0,0))
    if life==0:
        endgame(win)
    alien.disp(win)
    
    for tofee in tofees:
        tofee.disp(win)
        
    for bomb in bombs:
        bomb.disp(win)
        
    for rock in rockets:
        rock.disp(win)
       
        
    text=font.render('Score : '+ str(score*10),1,(255,255,255))
    win.blit(text,(550,50))
    displife()
   
    
    pygame.display.update()
    
    
alien=character(450,550,50,60)
win.blit(bg,(0,0))
j=0
tgap=10
tofees=[]
bombs=[]
bgap=1
pygame.mixer.music.play()
rockets=[]
isrocket=False
p=0





#main loop
while run:
     clock.tick(25)
     j=j+1
     alien.left=False
     alien.right=False
     

     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

     key=pygame.key.get_pressed()

     if key[pygame.K_LEFT] and alien.x>alien.vel:
         alien.x=alien.x-alien.vel
         alien.left=True
         alien.right=False
         walkcount+=1
     elif key[pygame.K_RIGHT] and alien.x<750-alien.vel:
         alien.x=alien.x+alien.vel
         alien.left=False
         alien.right=True
         walkcount+=1
     else:
        left=False
        right=False
     if key[pygame.K_SPACE]:
         alien.isjumb=True
     if alien.isjumb:
         if alien.jumbheight<-10:
             alien.isjumb=False
             alien.jumbheight=10
         else:    
             neg=1
             if alien.jumbheight<0:
                 neg=-1
             alien.y=alien.y-(alien.jumbheight**2)*0.5*neg
             alien.jumbheight-=1
     
     
     if score>13:
         tgap=4
     elif score>8:
         tgap=5
     if score>50:
         bgap=3
         
     elif score>30:
        bgap=5

     elif score>20:
          bgap=7

     if score>30 and isrocket==False:
         if j%25==0:
             on=random.randrange(0,10,1)
             if on==3:
                 isrocket=True
                 rockets.append(rocket())
                 alarm.play()
                 space.play()
             p=0
                 
                 
     for rock in rockets:
       

         if rock.dirc==-1:
            
             if rock.x+rock.vel>800:
                 rockets=[]
                 isrocket=False
                 space.stop()
                 alarm.stop()
             else:
                 rock.x-=(rock.vel*rock.dirc)
                 
         else:
             if rock.x<-40:
                 rockets=[]
                 isrocket=False
                 space.stop()
                 alarm.stop()
             else:
                 rock.x-=(rock.vel*rock.dirc)

         if rock.x<=alien.x and rock.x+160>=alien.x+80:
             
             if rock.y+40>=alien.y and rock.y<=alien.y+30:
                 
                 rockets=[]
                 life=0
                 isrocket=False
                 space.stop()
                 alarm.stop()
                 
     
         
     if j%(10*tgap)==0:
         num=random.randrange(0,bgap)
         if num==2:
             bombs.append(bad(random.randrange(50,700,10),0,5))

               
         else:   
             tofees.append(point(random.randrange(50,700,10),0,5))

         

     for tofee in tofees:
         
         if tofee.y>600:
             tofees.pop(tofees.index(tofee))
             life-=1
         else:
             tofee.y+=tofee.vel

         if tofee.x>alien.x-30 and tofee.x+40<alien.x+70:
             if tofee.y+40>=alien.y and  tofee.y<=alien.y+30:
                 score+=1
                 psound.play()
                 tofees.pop(tofees.index(tofee))
     for bomb in bombs:
        if bomb.y>600:
            bombs.pop(bombs.index(bomb))
        else:
            bomb.y+=bomb.vel

        if bomb.x>alien.x-30 and bomb.x+40<alien.x+70:
            if bomb.y<=alien.y+30 and bomb.y+44>alien.y:
                    life=0
                    bombs.pop(bombs.index(bomb))
                    bs.play()
            
                 
                 

             
     p+=1   
         
     maindisp()
    
     

pygame.quit()
