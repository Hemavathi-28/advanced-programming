import pgzrun
from random import randint
WIDTH=1221
HEIGHT=588
vx=5
vy=5
female=Actor("female.")
female.bottom=478
female.x=50
coin=Actor("coin")
coin.bottom=300
coin.x=400
score=0
jump=False
jump_time = 0.0
distance = 0
skysun=Actor("skysun1")
skysun.bottom=588
skysun.x=610
background1=Actor("b3")
missed=False
win=False

door=Actor("door")
door.bottom=478
door.x=110

bullets=[]
enemies=[]
zombie_is=[]


def draw():
    global score
    if female.x < WIDTH:
         screen.clear()
         skysun.draw()
         if score == 100:
             door.draw()
         if score > 100 and score < 200:
             for zombie_i in zombie_is:
                 zombie_i.draw()
         female.draw()
         if score!=100:
             coin.draw()
         screen.draw.text("ADVENTUROUS GAME",(400,0),color='green')
         screen.draw.text("SCORE:"+str(score),(10,10),fontsize=30,color='black')
         for bullet in bullets:
             bullet.draw()
         if score ==0 or score <100:
           for enemy in enemies:
             enemy.draw()
         if missed==True:
             position=((WIDTH//2)-200,(HEIGHT//2)-80)
             screen.draw.text("Oops you're dead",position,fontsize=80,color='red')
         if win==True:
             position=((WIDTH//2)-300,(HEIGHT//2)-100)
             screen.draw.text("HURRAY, WE DESTROYED ALL ZOMBIES",position,fontsize=60,color='orange')
    
def update(dt):
  global missed,score,win
  if missed==False and win == False:
    global jump,jump_time
    move_player()
    check_boundary()
    if jump:
        jump_time -=dt
        if jump_time < 0:
            female.bottom = 478
            jump = False
    check_coin()
    move_bullet()
    if score == 0 or score < 100:
        move_enemy()
        bullet_collision()
        female_collision()
    if score==100:
        levels()
    if score > 100 and score < 200:
        level2()
        move_zombie()
        bullet_collision1()
        zombie_collision()
    if score == 200:
        for zombie_i in zombie_is:
            zombie_is.remove(zombie_i)
        win=True
        missed2()
    
def on_key_down(key):
    if not missed:
        if key == keys.SPACE:
             create_bullet()
             sounds.sfireball.play()

def jump1():
    global jump,jump_time
    female.bottom = 378
    jump = True
    jump_time = 0.1
   
def move_player():
    global vx,vy
    if keyboard.left:
        female.x -= vx
    if keyboard.right:
        female.x += vx
    if keyboard.up:
       jump1()  
clock.schedule_interval(move_player,0.2)


images=["fwalk0","fwalk1","fwalk2","fwalk3","fwalk4","fwalk5","fwalk6","fwalk7"]
image_counter=0


def animate_female():
    if missed==False:
       global image_counter
       if keyboard.right:
         female.image=images[image_counter % len(images)]
         image_counter+=1
       if keyboard.left:
         female.image=images[image_counter % len(images)]
         image_counter+=1
clock.schedule_interval(animate_female,0.2)
    

def move_bullet():
    for bullet in bullets:
        if bullet.x > WIDTH:
            bullets.remove(bullet)
        else:
            bullet.x+=10
            

def move_enemy():
    for enemy in enemies:
       if enemy.x < female.x:
          enemy.x += 2
       if enemy.x > female.x:
          enemy.x -= 2
            

images1=["walk7","walk6","walk5","walk4","walk3","walk2","walk1","walk0"]
def animate_enemy():
    if  missed==False:
       global image_counter
       for enemy in enemies:
            enemy.image=images1[image_counter % len(images1)]
            image_counter += 1
clock.schedule_interval(animate_enemy,0.2)

def create_bullet():
    bullet = Actor("bullet")
    bullet.x =female.x
    bullet.y = female.y+20
    bullets.append(bullet)

def create_enemy():
        enemy = Actor("zombie")
        enemy.x=1200
        enemy.bottom=478
        enemies.append(enemy)
clock.schedule_interval(create_enemy,4.0)

def bullet_collision():
    for enemy in enemies:
         for bullet in bullets:
            if enemy.colliderect(bullet):
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    sounds.fall.play()
                    enemies.remove(enemy)
                if len(enemies) == 0:
                    create_enemy()

def female_collision():
    global missed
    for enemy in enemies:
       if female.colliderect(enemy):  
           female.image="falldownfemale"
           missed=True
           sounds.die.play()

    
def missed_1():
    if missed==True:
        position=((WIDTH//2)-100,(HEIGHT//2)-100)
        screen.draw.text("Oops you're dead",position,fontsize=80,color='red')

    
def check_boundary():
    global WIDTH
    if female.x <20:
        female.x=20
    if female.bottom > 478:
        female.bottom = 478
    if female.x > WIDTH:
        female.x = 0
    

def check_coin():
    global score
    if female.colliderect(coin):
        sounds.picking.play()
        if coin.x < WIDTH:
          coin.x += 300
          score+=10
          if coin.x > WIDTH:
             coin.x=30

def levels():
    global door,score
    if female.colliderect(door):
            skysun.image="b3"
            score+=10
           
def level2():
    if score>100:
        for enemy in enemies:
            enemies.remove(enemy)

def create_zombie():
    zombie_i=Actor("zombie_i")
    zombie_i.x=1200
    zombie_i.bottom=478
    zombie_is.append(zombie_i)
clock.schedule_interval(create_zombie,10.0)

images2=["zombie_i","zombie_w1","zombie_w2"]
def animate_zombie():
    if  missed==False:
       global image_counter
       for zombie_i in zombie_is:
            zombie_i.image=images2[image_counter % len(images2)]
            image_counter += 1
clock.schedule_interval(animate_zombie,0.2)

def move_zombie():
    for zombie_i in zombie_is:
       if zombie_i.x < female.x:
          zombie_i.x += 5
       if zombie_i.x > female.x:
          zombie_i.x -= 5

def bullet_collision1():
    for zombie_i in zombie_is:
         for bullet in bullets:
                if zombie_i.colliderect(bullet): 
                   if bullet in bullets:
                     bullets.remove(bullet)
                   if zombie_i in zombie_is:
                     sounds.fall.play()
                     zombie_is.remove(zombie_i)
                   if len(zombie_is) == 0:
                     create_zombie()

def zombie_collision():
    global missed
    for zombie_i in zombie_is:
       if female.colliderect(zombie_i):  
           female.image="falldownfemale"
           missed=True
           sounds.die.play()

def missed2():
        sounds.worldclear.play()

create_enemy()
create_zombie()
pgzrun.go()
