#Maria Ruiz Molina


import pygame, sys, os, random

#Objects:

class Player(pygame.sprite.Sprite):
    
    #Spawn a player
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.countanimation=0
        for i in range(0,4):
            img = pygame.image.load(os.path.join('images','aga' + str(i) + '.png')) #.convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            

    def control(self,x,y):

        #control player movement
        
        self.movex += x*0.4
        self.movey += y*0.4        

    def update(self):

        #Update sprite position

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        self.countanimation += 1
        if self.countanimation%5==0:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.images[self.frame]
            
        
        self.rect.clamp_ip(world.get_rect())



class Bullet(pygame.sprite.Sprite):

    #Spawn bullet
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        self.countanimation=0
        self.direction_x=0
        self.direction_y=0
        for i in range(0,4):
            img = pygame.image.load(os.path.join('images','bullet' + str(i) + '.png')) #.convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
            


    def control(self,x,y):

        #speed bullet movement
        
        self.movex += x * 0.0008
        self.movey += y * 0.0008

    #updates bullet position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

    #Animates the sprite
        self.countanimation += 1
        if self.countanimation%5==0:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.images[self.frame]
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
class Enemy(pygame.sprite.Sprite):

    #Spawn an enemy
    
    def __init__(self, centerpoint, *groups):
        super(Enemy, self).__init__(*groups)
        self.rect = pygame.Rect(0, 0, 64, 64)
        self.rect.center = centerpoint
        self.pos = self.rect.center
        self.frame = 0
        self.images = []
        self.tam=random.randint(0,2)
        #size can be S, M or L
        if self.tam==0:
            self.size='S'
        elif self.tam==1:
            self.size=''
        elif self.tam==2:
            self.size='L'
        self.survive_timer=0
        self.survivor_frequency = 500 #milliseconds
        self.surviving=0
        self.strength=0
        self.speed = random.randint(1,10)*0.1 #speed
        self.evasion= random.randint(0,9)*0.1 #speed movement change
        #
        
        
        
        if mostsurviving>self.surviving:
            self.speed=bestspeed
            self.evasion=bestevasion
            self.size=bestsize

            if superiorSpeed!=-1:
                self.speed= (self.speed + superiorSpeed)/2
            if superiorEvasion!=-1:
                self.evasion= (self.evasion + superiorEvasion)/2
            if superiorSize!='None':
                if (self.size=='L' and superiorSize == 'S') or (self.size=='S' and superiorSize == 'L'):
                    self.size = ''
            

        #new enemy mutates
        if random.randint(0,100) >= 70 and mostsurviving>self.surviving:
            self.speed=self.speed+random.randint(-10,10)*0.1
            if self.speed < 0.1:
                self.speed = 0.1
            if self.speed > 1:
                self.speed = 1

        if random.randint(0,100) >= 70 and mostsurviving>self.surviving:
            self.evasion=self.evasion+random.randint(-10,10)*0.1
            if self.evasion < 0:
                self.evasion = 0
            if self.evasion > 0.9:
                self.evasion = 0.9

        if random.randint(0,100) >= 80 and mostsurviving>self.surviving:
            self.tam=random.randint(0,2)
            if self.tam==0:
                self.size='S'
            elif self.tam==1:
                 self.size=''
            elif self.tam==2:
                self.size='L'
            
        #sprite with animation. Load all images        
        for i in range(0,4):
            img = pygame.image.load(os.path.join('images','donehre' + self.size + str(i) + '.png'))
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

        self.countanimation =0

        #moves to center
        self.pos = self.pos[0] + ((random.randint(-5, 5))*self.speed * dt), self.pos[1] +(random.randint(-5, 5))*self.speed*dt
        self.rect.center = self.pos
        self.rect.clamp_ip(world.get_rect())

    #moves the enemy to a new position    
    def move(self, dt):
        self.pos = self.pos[0] + ((random.randint(-5, 5))*self.speed * dt), self.pos[1] +(random.randint(-5, 5)*self.speed*dt)
        self.rect.center = self.pos
        self.rect.clamp_ip(world.get_rect()) #inside the screen

    #moves enemy and updates the parameters if it's low evasion parameter    
    def update(self, dt):
        if(random.randint(0,10)*0.1>self.evasion):
            self.move(dt)

        #animate the sprite
        self.countanimation += 1
        if self.countanimation%5==0:
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            self.image = self.images[self.frame]

        #+1 time surviving
        self.survive_timer += dt
        
        if self.survive_timer >= self.survivor_frequency:
            self.survivor(dt) 
            self.survive_timer -= self.survivor_frequency
            

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def survivor(self, dt):
        self.surviving += 1


#Setup
        
worldx = 960
worldy = 720


pygame.init()
main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
ALPHA = (0,255,0)

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','backgroundAljaraque.png')).convert()
backdropbox = world.get_rect()
player = Player()   # spawn player
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10      # how fast to move in pixels

firstEnemies=0
lives=8
fps=60 #frame rate
clock = pygame.time.Clock()
spawn_timer = 0
spawn_frequency = 1700 #milliseconds

inmunity_timer= 0
inmunity_limit = 3000 #milliseconds

shooter_timer= 0
shooter_limit= 1000 #milliseconds

superiorSpeed= -1
superiorSize= 'None'
superiorEvasion= -1

mostsurviving=0
bestspeed= -1
bestevasion= -1
bestsize= 'None'

print "Vidas restantes: ", lives
inmunity= False
enemies = pygame.sprite.Group()
dt= clock.tick(fps)
win=False
gameover=False
bullet_list=pygame.sprite.Group()

#Main loop

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
            
#bullet generator for shooting
        if event.type == pygame.MOUSEBUTTONDOWN:

            if shooter_timer >= shooter_limit:
                pygame.mixer.music.load(os.path.join('sound','aga' + '.wav'))
                pygame.mixer.music.play(0)
            
                bullet = Bullet()
                bullet.rect.x=player.rect.x
                bullet.rect.y=player.rect.y
                
                bullet_list.add(bullet)
            
                go_to_x= pygame.mouse.get_pos()[0]
                go_to_y= pygame.mouse.get_pos()[1]
            
                bullet.direction_x= go_to_x-bullet.rect.x
                bullet.direction_y= go_to_y-bullet.rect.y

                #adding difficulty:
                shooter_timer-=shooter_limit #so player can't be shooting 100% of the time

            else: #charging sound
                pygame.mixer.music.load(os.path.join('sound','charging' + '.wav'))
                pygame.mixer.music.play(0)
            
#player control keys   
#either with W, A, S and D
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,steps)
#or arrow keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0,-steps)
                
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False   

    world.fill(BLACK)
    world.blit(backdrop, backdropbox)

#6 enemies at the start of the game
    if firstEnemies==0:
        #print "SPAWN"
        pygame.mixer.music.load(os.path.join('sound','donehre7' + '.wav'))
        pygame.mixer.music.play(0)
        spawn_timer -= spawn_frequency
        for i in [1,2,3,4,5,6,7]:
            Enemy(world.get_rect().center,enemies)
            
        #values for these enemies, 2 will be completely random    
        enemiesList=enemies.sprites()
        enemiesList[0].speed=0.5
        enemiesList[0].evasion=0.5
        
        enemiesList[1].speed=0.9
        enemiesList[1].evasion=0.4
        
        enemiesList[2].speed=0.9
        enemiesList[2].evasion=0.6
        
        enemiesList[3].speed=0.7
        enemiesList[3].evasion=0.3
        
        enemiesList[4].speed=0.8
        enemiesList[4].evasion=0.1
            
        firstEnemies=1


#what enemy is surviving for the most time
    

#1 enemy-gen/spawn_frequency seconds
    spawn_timer += dt
    if spawn_timer >= spawn_frequency:
        pygame.mixer.music.load(os.path.join('sound','donehre' + '.wav'))
        pygame.mixer.music.play(0)
        spawn_timer -= spawn_frequency
        Enemy(world.get_rect().center, enemies)

    for enemy in enemies:
        for bullet in bullet_list:
            if enemy.rect.colliderect(bullet.rect):
                pygame.mixer.music.load(os.path.join('sound','eliminate' + '.wav'))
                pygame.mixer.music.play(0)
                enemies.remove(enemy)
                bullet_list.remove(bullet)
    enemies.update(dt)

    #if there's no enemies left, player wins
    if len(enemies)==0:
        main=False
        win= True
    #if an enemy touches the player -> game over
    for enemy in enemies:
        #enemy with largest amount of time on screen
        if enemy.surviving>mostsurviving:
            bestspeed=enemy.speed
            bestevasion=enemy.evasion
            bestsize=enemy.size
            mostsurviving=enemy.surviving

        #enemies that touched the player
        if enemy.rect.colliderect(player.rect) and inmunity == False:
            pygame.mixer.music.load(os.path.join('sound','hurt' + '.wav'))
            pygame.mixer.music.play(0)
            lives= lives-1
            enemy.strength += 1
            stronger=enemy
            for enemy in enemies:
                if enemy.strength>stronger.strength:
                    stronger=enemy
                    superiorSpeed= stronger.speed
                    superiorEvasion= stronger.evasion
                    superiorSize= stronger.size
            print "Vidas restantes: ", lives
            inmunity= True
            #game over
            if lives== 0:
                main=False
                gameover= True
            
    
    player.update()
    player_list.draw(world) #refresh player position

    for bullet in bullet_list:
        bullet.control(bullet.direction_x,bullet.direction_y)
        bullet.update()
        
    bullet_list.update()
    bullet_list.draw(world) #refresh bullets position
    
    
    enemies.draw(world) #refresh enemies position
    shooter_timer += dt

    #inmunity time so player can run away from the enemy after losing 1 live
    if inmunity==True:
        inmunity_timer +=dt
        
    if inmunity_timer >= inmunity_limit:
        inmunity=False
        inmunity_timer -= inmunity_limit
        
    pygame.display.flip()
    clock.tick(fps)






#winner window
screen = pygame.display.set_mode((1280, 720))
backdrop = pygame.image.load(os.path.join('images','agawins.png')).convert()
backdropbox = world.get_rect()

if win == True:
    pygame.mixer.music.load(os.path.join('sound','chisPun' + '.wav'))
    pygame.mixer.music.play(0)

while win== True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
    
    screen.fill(BLACK)
    screen.blit(backdrop, backdropbox)
    pygame.display.flip()


#game over window
screen = pygame.display.set_mode((1280, 720))
backdrop = pygame.image.load(os.path.join('images','donehrewins.png')).convert()
backdropbox = world.get_rect()

if gameover == True:
    pygame.mixer.music.load(os.path.join('sound','gameOver' + '.wav'))
    pygame.mixer.music.play(0)

while gameover== True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
            
    screen.fill(BLACK)
    screen.blit(backdrop, backdropbox)
    pygame.display.flip()



#
