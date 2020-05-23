# Import libraries
import pygame
import time
import random
import os

# Initializations
pygame.font.init()
pygame.mixer.init()

# Set constants
GROUND = 700 - 55
WIDTH, HEIGHT = 1333, 750

# Define window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farty Bird")

# Allocate specific mixer channel for player fart sfx
# Prevents overlap of player sounds
player_sfx_channel = pygame.mixer.Channel(0)
player_sfx_channel.set_volume(.8)

# Define custom pygame event to handle endgame
GAME_OVER = pygame.USEREVENT + 1

# Load Images
POWERUP_AVIALABLE = [
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa1.png")),
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa2.png")),
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa3.png")),
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa4.png")),
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa5.png")),
    pygame.image.load(os.path.join("assets/images/powerup/available","powerupa6.png"))
]
POWERUP_COLLIDE = [
    pygame.image.load(os.path.join("assets/images/powerup/collide","powerupb1.png")),
    pygame.image.load(os.path.join("assets/images/powerup/collide","powerupb2.png")),
    pygame.image.load(os.path.join("assets/images/powerup/collide","powerupb3.png")),
    pygame.image.load(os.path.join("assets/images/powerup/collide","powerupb4.png")),
    pygame.image.load(os.path.join("assets/images/powerup/collide","powerupb5.png"))
]
BUTT_FLY_ALIVE = [
    pygame.image.load(os.path.join("assets/images/butt_fly","static.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap1.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap2.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap3.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap4.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap5.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap6.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","flap7.png"))
]
BUTT_FLY_DEAD = [
    pygame.image.load(os.path.join("assets/images/butt_fly","death1.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death2.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death3.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death4.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death5.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death6.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death7.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death8.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death9.png")),
    pygame.image.load(os.path.join("assets/images/butt_fly","death10.png"))
]
BULLET = [
    pygame.image.load(os.path.join("assets/images/bullet","bullet1.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet2.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet3.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet4.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet5.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet6.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet7.png")),
    pygame.image.load(os.path.join("assets/images/bullet","bullet8.png"))
]
FLAPPING_BIRD = [
    pygame.image.load(os.path.join("assets/images","flap_1.gif")),
    pygame.image.load(os.path.join("assets/images","flap_2.gif")),
    pygame.image.load(os.path.join("assets/images","flap_3.gif")),
    pygame.image.load(os.path.join("assets/images","flap_4.gif")),
    pygame.image.load(os.path.join("assets/images","flap_5.gif")),
    pygame.image.load(os.path.join("assets/images","flap_6.gif")),
    pygame.image.load(os.path.join("assets/images","flap_7.gif"))
    ]
INTRO_FOG_ANIMATE = [
    pygame.image.load(os.path.join("assets/images/intro","fog_animate1.png")),
    pygame.image.load(os.path.join("assets/images/intro","fog_animate2.png")),
    pygame.image.load(os.path.join("assets/images/intro","fog_animate3.png"))
]
INTRO_FOG = pygame.image.load(os.path.join("assets/images/intro","fog.png"))
INTRO_BIRD = pygame.image.load(os.path.join("assets/images/intro","bird.png"))
INTRO_RAYS = pygame.image.load(os.path.join("assets/images/intro","rays.png"))
INTRO_TITLE = pygame.image.load(os.path.join("assets/images/intro","title.png"))
BG = pygame.image.load(os.path.join("assets/images","bg_3.png"))
BG_MID = pygame.image.load(os.path.join("assets/images","bg_2.png"))
BG_TOP = pygame.image.load(os.path.join("assets/images","bg_1.gif"))
STATIC_BIRD = pygame.image.load(os.path.join("assets/images","static.gif"))
DEAD_BIRD = pygame.image.load(os.path.join("assets/images", "death.png"))
FINGER_PIC = pygame.image.load(os.path.join("assets/images","finger.gif"))

# Load Audio Fx
HIGH_FART_FX = [
    pygame.mixer.Sound(os.path.join("assets/audio/sfx","fart_1.wav")),
    pygame.mixer.Sound(os.path.join("assets/audio/sfx","fart_3.wav"))
    ]
LOW_FART_FX = [
    pygame.mixer.Sound(os.path.join("assets/audio/sfx","fart_2.wav")),
    pygame.mixer.Sound(os.path.join("assets/audio/sfx","fart_4.wav")),
    pygame.mixer.Sound(os.path.join("assets/audio/sfx","fart_5.wav")),
    ]
SHOOT_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","shoot.wav"))
FINGER_HIT_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","finger_hit.wav"))
BUTTFLY_HIT_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","buttfly_hit.wav"))
RELOAD_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","reload.wav"))
BUTT_BUZZ_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","buzz.wav"))
POWERUP_FX = pygame.mixer.Sound(os.path.join("assets/audio/sfx","powerup.wav"))
POWERUP_FX.set_volume(.3)

class Bullet: #Handles animation of bullets
    def __init__(self, x, y, vel = 10, bullet_images = BULLET, img_counter = 0):
        self.x = x
        self.y = y
        self.vel = vel
        self.bullet_images = bullet_images
        self.img_counter = img_counter
        self.img = None
        self.mask = None
        
    def update(self):
        self.x += self.vel
        
    def draw(self, window):
        self.img = self.bullet_images[self.img_counter//3]
        window.blit(self.img,(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.img)
        self.img_counter += 1
        if self.img_counter == 22:
            self.img_counter = 0

class ScoreNotifcation:
    def __init__(self, x, y, ydelta, vel = 3, alpha = 255):
        self.x = x
        self.ydelta = ydelta
        self.y = y
        self.vel = vel
        self.alpha = alpha
        self.font = pygame.font.SysFont("connectionserif", 25)
        self.text = None
        self.surface = None
        
    def update(self, player_y):
        self.ydelta -= self.vel
        self.y = player_y + self.ydelta
        self.alpha -= 10
        if self.alpha < 0:
            self.alpha = 0
        
    def draw(self, window):
        self.surface = self.font.render("+1", 1, (255,255,255))
        self.surface.set_alpha(self.alpha)
        window.blit(self.surface, (self.x, self.y))

class PowerUp:
    def __init__(self, x, y, starty, up_down, playing_audio = False, available_images = POWERUP_AVIALABLE, collide_images = POWERUP_COLLIDE, speed = 3, collide = False, img_timer=0):
        self.x = x
        self.y = y
        self.starty = starty
        self.up_down = up_down
        self.available_images = available_images
        self.collide_images = collide_images
        self.collide = collide
        self.img_timer = img_timer
        self.img =  None
        self.speed = speed
        self.mask = None
        self.playing_audio = playing_audio
        
    def kill_audio(self):
        self.playing_audio = False
        POWERUP_FX.stop()
        
    def update(self, score):
            
        if self.up_down == "up" and self.collide == False:
            if self.y > self.starty - 10:
                self.y -= 1
            else:
                self.y += 1
                self.up_down = "down"
        elif self.up_down == "down" and self.collide == False:
            if self.y < self.starty + 10:
                self.y += 1
            else:
                self.y -= 1
                self.up_down = "up"
                
        self.x = self.x - (self.speed * ((.25*(score//20))+1))
        
        if self.x < WIDTH and self.x > 0 - self.img.get_width() and self.playing_audio == False and self.collide == False:
                self.playing_audio = True
                POWERUP_FX.play(-1)
        
    def draw(self, window):
        if self.collide:
            self.img = self.collide_images[self.img_timer//8]
            self.mask = pygame.mask.from_surface(self.img)
            if self.img_timer < 32:
                window.blit(self.img,(self.x, self.y))
                self.img_timer += 1

        else:
            self.img = self.available_images[self.img_timer]
            window.blit(self.img,(self.x, self.y))
            self.mask = pygame.mask.from_surface(self.img)
            self.img_timer += 1
            if self.img_timer == 6:
                self.img_timer = 0

class ButtFly:
    def __init__(self, x, y, up_down = "up", health = 100, vel = 5, img_counter = 0, shot = False, playing_audio = False):
        self.x = x
        self.y = y
        self.up_down = up_down
        self.health = health
        self.vel = vel
        self.mask = None
        self.img = None
        self.img_counter = img_counter
        self.shot = shot
        self.playing_audio = playing_audio
        
    def kill_audio(self):
        self.playing_audio = False
        BUTT_BUZZ_FX.stop()
        
    def update(self):
        
        if self.shot == True:
            self.health = 0
        else:
            if self.up_down == "up":
                if self.y > 200:
                    self.y -= 2
                else:
                    self.up_down = "down"
                    self.y += 2
            else:
                if self.y < 400:
                    self.y += 2
                else:
                    self.up_down = "up"
                    self.y -= 2
        self.x -= self.vel
        
        if self.x < WIDTH and self.x > 0 - self.img.get_width() and self.playing_audio == False and self.shot == False:
            self.playing_audio = True
            BUTT_BUZZ_FX.play(-1)
    
    def draw(self, window):
        if self.health != 0:
            self.img = BUTT_FLY_ALIVE[self.img_counter//8]
            window.blit(self.img,(self.x, self.y))
            self.mask = pygame.mask.from_surface(self.img)
            self.img_counter += 1
            if self.img_counter > 56:
                self.img_counter = 0
        else:
            if self.img_counter < 46:
                self.img = BUTT_FLY_DEAD[self.img_counter//5]
                window.blit(self.img,(self.x, self.y))
                self.mask = pygame.mask.from_surface(self.img)
                self.img_counter += 1

class Player:
    MAXSPEED = 20
    MAXFALL = -35
    VELOCITY_MULT = 1.03
    FALL_MULT = .05

    def __init__(self, x, y, velocity = 0, health=100, state="static", angle = 0, powerup = False, bullets = 0, cooldown = 0):
        self.x = x
        self.y = y
        self.health = health
        self.state = state
        self.flycount = None
        self.velocity = velocity
        self.mask = None
        self.image =  None
        self.angle = angle
        self.powerup = powerup
        self.bullets = bullets
        self.cooldown = cooldown

    def update_v(self):
        
        if self.cooldown > 0:
            self.cooldown -= 1
            
        if self.state == "flying":
            
            if self.velocity == 0:
                self.velocity = 1
            
            if self.velocity != self.MAXSPEED:
                if self.velocity >= 1:
                    self.velocity = self.velocity * self.VELOCITY_MULT
                elif self.velocity <1 and self.velocity >-1:
                    self.velocity = 1
                else:
                    self.velocity = self.velocity - (self.velocity * self.VELOCITY_MULT)
                    
            if self.velocity > self.MAXSPEED:
                self.velocity = self.MAXSPEED
            
            if self.y - self.velocity > 10:
                self.y = self.y - self.velocity
            else:
                self.y = 10

        if self.state == "static":
            
            if self.y == GROUND:
                self.velocity = 0
            else:
                if self.velocity != self.MAXFALL:
                    if self.velocity >= 1:
                        self.velocity = self.velocity - (self.velocity * self.FALL_MULT)
                    elif self.velocity <1 and self.velocity >-1:
                        self.velocity = -1
                    else:
                        self.velocity = self.velocity * (1 + self.FALL_MULT)
                    
                if self.velocity < self.MAXFALL:
                    self.velocity = self.MAXFALL
                    
            if self.y - self.velocity < 10:
                self.y = 10
            elif self.y - self.velocity < GROUND:
                self.y = self.y - self.velocity
            else:
                self.y = GROUND
                
    def get_height(self):
        if self.state == "flying":
            return self.image.get_height()
        else:
            return self.image.get_height()
    
    def get_width(self):
        if self.state == "flying":
            return self.image.get_width()
        else:
            return self.image.get_width()
            
    def shoot(self, bullets):
        SHOOT_FX.play()
        self.bullets -= 1
        self.cooldown = 60
        new_bullet = Bullet(self.x + self.get_width()/2,self.y + self.get_height()/4)
        bullets.append(new_bullet)
            
    def draw(self, window):

        if self.state == "flying":
            
            self.image = FLAPPING_BIRD[self.flycount//5]
            window.blit(self.image, (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
            
            self.flycount += 1
            
            if self.flycount > 30:
                self.flycount = 0

        elif self.state == "static":

            self.flycount=0
            
            self.image = STATIC_BIRD
            window.blit(self.image,(self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
            
        elif self.state == "death":
            
            self.image = DEAD_BIRD
            
            if self.angle != 180:
                self.angle += 1
            
            self.y += 4
            
            window.blit(pygame.transform.rotate(self.image,self.angle),(self.x, self.y))

class Finger:
    def __init__(self, FINGER_IMG = FINGER_PIC, speed = 3, direction = "up", scored = False, shot = False):
        self.FINGER_IMG = FINGER_IMG
        self.x = None
        self.y = None
        self.speed = speed
        self.direction = direction
        self.mask = None
        self.scored = scored
        self.shot = shot
        self.image = None
        
    def get_width(self):
        return self.FINGER_IMG.get_width()
        
    def draw(self, window):
        if self.direction == "up":
            if self.shot:
                if self.y < 750:
                    self.y += 3
            self.image = self.FINGER_IMG
            window.blit(self.image, (self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            if self.shot:
                if self.y > -550:
                    self.y -= 3
            self.image = pygame.transform.flip(self.FINGER_IMG,True,True)
            window.blit(self.image,(self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)
            
    def update(self, score):
        self.x = self.x - (self.speed * ((.25*(score//20))+1))

class Intro_Animation:
    def __init__(self, BIRD_IMG, BG_IMG, FOG_IMG, RAYS_IMG, birdy = 750, fogy = 350, raysy = 0, title_alpha = 0, draw_title = False, draw_rays = False, temp_int = 0, fog_animation_timer = 0):
        self.BIRD_IMG = BIRD_IMG
        self.birdy = birdy
        self.BG_IMG = BG_IMG
        self.fog_animations_list = INTRO_FOG_ANIMATE
        self.fogy = fogy
        self.FOG_IMG = FOG_IMG
        self.RAYS_IMG = RAYS_IMG
        self.raysy = raysy
        self.rays_up_down = None
        self.draw_title = draw_title
        self.draw_rays = draw_rays
        self.TITLE_IMG = INTRO_TITLE.convert()
        self.title_rect = self.TITLE_IMG.get_rect()
        self.title_alpha = title_alpha
        self.title_in_out = None
        self.timer = None
        self.fog_animation_timer = fog_animation_timer
        self.temp_int = temp_int
        
    def update(self):
        # raise Bird and Fog at t=0
        if self.timer >= 0:
            if self.birdy > 0:
                if self.birdy - 5 > 0:
                    self.birdy -= 5
                else:
                    self.birdy = 0
                self.rays_up_down = "down" # Prime the rays to animate
            else:
                self.birdy = 0
            if self.fogy > 0:
                if self.fogy - 3 > 0:
                    self.fogy -= 3
                else:
                    self.fogy = 0
            else:
                self.fogy = 0
        # fade in title
        if self.timer >= 120:
            self.draw_title = True
            if self.title_alpha == 0:
                self.title_in_out = "in"
                self.title_alpha += 5
            elif self.title_in_out == "in":
                if self.title_alpha < 255:
                    self.title_alpha += 5
                else:
                    self.title_in_out = "out"
                    self.title_alpha -=5
            else: # self.title_alpha = "out"
                if self.title_alpha > 150:
                    self.title_alpha -= 5
                else:
                    self.title_in_out = "in"
                    self.title_alpha +=1
        if self.birdy == 0:
            self.draw_rays = True
            if self.rays_up_down == "down":
                if self.raysy < 20:
                    self.raysy += 1
                else:
                    self.rays_up_down = "up"
                    self.raysy -=1
            else: # self.rays_up_down = "up"
                if self.raysy > 0:
                    self.raysy -= 1
                else:
                    self.rays_up_down = "down"
                    self.raysy += 1
        
    def draw(self, window):
        window.blit(self.BG_IMG,(0,0))
        
        window.blit(self.BIRD_IMG,(0,self.birdy))
        
        self.temp_int += 1
        if self.temp_int == 10:
            self.fog_animation_timer += 1
            if self.fog_animation_timer == 3:
                self.fog_animation_timer = 0
            self.temp_int = 0
            
        window.blit(self.FOG_IMG,(0,self.fogy))
        window.blit(self.fog_animations_list[self.fog_animation_timer],(0,self.fogy))
        
        if self.draw_rays:
            window.blit(self.RAYS_IMG,(0,self.raysy))
        
        if self.draw_title:
            self.TITLE_IMG.set_alpha(self.title_alpha)
            window.blit(self.TITLE_IMG,self.title_rect)

class Background:
    def __init__(self, BG_IMG, MID_IMG, TOP_IMG, bg_x1 = 0, bg_x2 = 1500, mid_x1 = 0, mid_x2 = 1500, top_x1 = 0, top_x2 = 1500):
        self.BG_IMG = BG_IMG
        self.MID_IMG = MID_IMG
        self.TOP_IMG = TOP_IMG
        self.bg_x1 = bg_x1
        self.bg_x2 = bg_x2
        self.mid_x1 = mid_x1
        self.mid_x2 = mid_x2
        self.top_x1 = top_x1
        self.top_x2 = top_x2
    
    def draw(self,window):
        window.blit(self.BG_IMG,(self.bg_x1,0))
        window.blit(self.BG_IMG,(self.bg_x2,0))
        window.blit(self.MID_IMG,(self.mid_x1,0))
        window.blit(self.MID_IMG,(self.mid_x1,0))
        window.blit(self.TOP_IMG,(self.top_x1,0))
        window.blit(self.TOP_IMG,(self.top_x2,0))
        
    def update(self):
        if self.bg_x1 >= -1500 and self.bg_x2 > self.bg_x1:
            self.bg_x1 -= 1
            self.bg_x2 = self.bg_x1 + 1500
        elif self.bg_x2 >= -1500:
            self.bg_x2 -= 1
            self.bg_x1 = self.bg_x2 + 1500
        else:
            self.bg_x1 = 0
            self.bg_x2 = 1500
        
        if self.mid_x1 >= -1500 and self.mid_x2 > self.mid_x1:
            self.mid_x1 -= 2
            self.mid_x2 = self.mid_x1 + 1500
        elif self.mid_x2 >= -1500:
            self.mid_x2 -= 2
            self.mid_x1 = self.mid_x2 + 1500
        else:
            self.mid_x1 = 0
            self.mid_x2 = 1500
            
        if self.top_x1 >= -1500 and self.top_x2 > self.top_x1:
            self.top_x1 -= 3
            self.top_x2 = self.top_x1 + 1500
        elif self.top_x2 >= -1500:
            self.top_x2 -= 3
            self.top_x1 = self.top_x2 + 1500
        else:
            self.top_x1 = 0
            self.top_x2 = 1500

def collide(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
    
def spawn_enemies(enemylist):
    
    if len(enemylist)==0:
            new_enemy = Finger()
            new_enemy.y = random.randint(250,650)
            new_enemy.x = WIDTH + 50
            new_enemy.direction = "up"
            enemylist.append(new_enemy)
            
    while len(enemylist) != 20:
        new_enemy = Finger()
        
        if enemylist[len(enemylist)-1].direction == "up":
            new_enemy.direction = "down"
            new_enemy.y = enemylist[len(enemylist)-1].y - 700
            new_enemy.x = enemylist[len(enemylist)-1].x
        else:
            new_enemy.direction = "up"
            new_enemy.y = random.randint(250, 650)
            new_enemy.x = enemylist[len(enemylist)-1].x + random.randint(300, 450)
            
        enemylist.append(new_enemy) 
        
    return enemylist

def spawn_butt_flys(butt_fly_list, level):
    
    if len(butt_fly_list)==0:
        new_butt_fly = ButtFly(random.randint(1500,5000),300)
        butt_fly_list.append(new_butt_fly)
        
    return butt_fly_list

def spawn_powerup(powerup_list, enemy_list, powerup_timer):
    if len(powerup_list) > 0:
        for item in powerup_list:
            if item.x < 0 - item.img.get_width() or (item.collide == True and item.img_timer > 32):
                if item.playing_audio == True:
                    item.kill_audio()
                powerup_list.remove(item)
    elif len(powerup_list)==0:
        if random.randint(0, 300) == 100 and powerup_timer == 0:
            powerup_timer = 240
            new_powerup = PowerUp(3000,0,random.randint(200,550),random.choice(["up","down"]))
            new_powerup.y = new_powerup.starty
            
            if len(powerup_list)>1:
                if new_powerup.x < (powerup_list[len(powerup_list)-1].x + 4000):
                    new_powerup.x += 4000
            
            # evaluate x and place between enemies
            i = 0
            for enemy in enemy_list:
                i += 1
                if enemy.x > new_powerup.x: # found the right barrier
                    new_powerup.x = enemy_list[i-2].x + (enemy.x - enemy_list[i-2].x)/2
                    break
            powerup_list.append(new_powerup)
    return powerup_timer
    
def kill_all_sfx(buttflys, powerups):
    for butt in buttflys:
        if butt.playing_audio == True:
            butt.kill_audio()
    for powerup in powerups:
        if powerup.playing_audio == True:
            powerup.kill_audio() 

def spawn_score(score_notifications, player):
    new_score = ScoreNotifcation(WIDTH/2, player.y, -5)
    score_notifications.append(new_score)
    return score_notifications

def main():

    level = 0
    new_level = False
    level_timer = 0
    run = True
    FPS = 60
    enemies = []
    powerups = []
    lost = False
    score = 0
    fart_timer = 0
    powerup_timer = 0
    bullets = []
    butt_flys = []
    play_endgame = False
    score_notifications = []
    
    lost_font = pygame.font.SysFont("connectionserif", 40)
    level_font = pygame.font.SysFont("connectionserif", 70)
    score_font = pygame.font.SysFont("connectionserif", 25)

    player = Player(WIDTH/2 - STATIC_BIRD.get_width()/2,GROUND)
    background =  Background(BG,BG_MID,BG_TOP)
    clock = pygame.time.Clock()

    def redraw_window():
        nonlocal new_level
        nonlocal level_timer
        nonlocal new_level
        nonlocal score
        nonlocal level
        
        background.update()
        background.draw(WIN)
        
        for enemy in enemies:
            enemy.update(score)
            enemy.draw(WIN)
         
        for butt_fly in butt_flys:
            butt_fly.update()
            butt_fly.draw(WIN)
        
        for powerup in powerups:
            powerup.update(score)
            powerup.draw(WIN)
            
        for bullet in bullets:
            bullet.update()
            bullet.draw(WIN)
        
        player.update_v()
        player.draw(WIN)
        
        for notification in score_notifications:
            notification.update(player.y)
            notification.draw(WIN)
        
        if level_timer > 0:
            new_level = False
            level_timer -= 1
            level_label = level_font.render("Level ", 1, (255,255,255))
            level_value = level_font.render(str(level), 1, (255,255,255))
            WIN.blit(level_label, (WIDTH/2 - level_label.get_width()/2 - level_value.get_width()/2 - 5, HEIGHT/2 - level_label.get_height()/2))
            WIN.blit(level_value, (WIDTH/2 + level_label.get_width()/2 + level_value.get_width()/2 + 5, HEIGHT/2 - level_label.get_height()/2))
        
        # Draw Score
        score_label = score_font.render("Score: ", 1, (255,255,255))
        score_value = score_font.render(str(score), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 15))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 15))
        
        # Draw Bullet Count
        score_label = score_font.render("Bullets: ", 1, (255,255,255))
        score_value = score_font.render(str(player.bullets), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 45))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 45))
        
        pygame.display.update()
        
    def draw_endgame():
        
        background.draw(WIN)
        
        for enemy in enemies:
            enemy.draw(WIN)
            
        for butt_fly in butt_flys:
            butt_fly.draw(WIN)
            
        for powerup in powerups:
            powerup.draw(WIN)
            
        for bullet in bullets:
            bullet.draw(WIN)
            
        for notification in score_notifications:
            notification.update(player.y)
            notification.draw(WIN)
        
        score_label = score_font.render("Score: ", 1 , (255,255,255))
        score_value = score_font.render(str(score), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 15))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 15))
        
        score_label = score_font.render("Bullets: ", 1, (255,255,255))
        score_value = score_font.render(str(player.bullets), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 45))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 45))
        
        lost_label = lost_font.render("You pulled my finger", 1 , (255,255,255))
        WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()))
        
        lost_label = lost_font.render("...and lost", 1 , (255,255,255))
        WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 + 5))
        
        player.draw(WIN)
        
        pygame.display.update()
        
    while run:
        
        clock.tick(FPS)
        
        if lost:
            player.state = "death"
            
            while play_endgame:
            
                draw_endgame()
            
                for event in pygame.event.get():
                    if event.type == GAME_OVER:
                        play_endgame =  False
            
            main_menu()
        
        for enemy in enemies[:]:
            if enemy.x <= 0 - enemy.FINGER_IMG.get_width():
                enemies.remove(enemy)
                
            if enemy.scored == False and enemy.direction == "up":    
                if enemy.x + enemy.get_width() < player.x:
                    enemy.scored = True
                    score += 1
                    score_notifications = spawn_score(score_notifications[:],player)
                
            if collide(enemy, player):
                if lost == False:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(os.path.join("assets/audio/music","game_over.wav"))
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_endevent(GAME_OVER)
                    kill_all_sfx(butt_flys, powerups)
                    play_endgame = True
                    lost = True
                
            for bullet in bullets[:]:
                if collide(bullet, enemy) and enemy.shot == False:
                    FINGER_HIT_FX.play()
                    bullets.remove(bullet)
                    enemy.shot = True
        
        for butt_fly in butt_flys[:]:
            if butt_fly.x <= 0 - butt_fly.img.get_width():
                butt_fly.kill_audio()
                butt_flys.remove(butt_fly)
            
            if collide(butt_fly,player) and butt_fly.shot == False:
                if lost == False:
                    butt_fly.kill_audio()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(os.path.join("assets/audio/music","game_over.wav"))
                    pygame.mixer.music.set_endevent(GAME_OVER)
                    pygame.mixer.music.play()
                    kill_all_sfx(butt_flys, powerups)
                    play_endgame = True
                    lost = True
                
            for bullet in bullets[:]:
                if collide(bullet,butt_fly) and butt_fly.shot == False:
                    BUTTFLY_HIT_FX.play()
                    butt_fly.kill_audio()
                    butt_fly.shot = True
                    butt_fly.img_counter = 0
                    bullets.remove(bullet)
                
        for powerup in powerups:
            if collide(powerup, player):
                if powerup.collide == False:
                    powerup.kill_audio()
                    RELOAD_FX.play()
                    powerup.collide = True
                    player.bullets += 2
                    
        for notification in score_notifications[:]:
            if notification.alpha == 0:
                score_notifications.remove(notification)
        
        if powerup_timer > 0:
            powerup_timer -= 1
        
        if score//20 + 1 > level:
            level += 1
            level_timer = 120
            new_level = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        powerup_timer = spawn_powerup(powerups,enemies,powerup_timer)
            
        enemies = spawn_enemies(enemies[:])
        
        if level > 1:
            butt_flys = spawn_butt_flys(butt_flys[:],level)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and lost == False:
            player.state="flying"
            if player_sfx_channel.get_busy() == False and fart_timer==0:
                if player.y > 350:
                    player_sfx_channel.play(LOW_FART_FX[random.randint(0,2)])
                    fart_timer=random.randint(60,120)
                else:
                    player_sfx_channel.play(HIGH_FART_FX[random.randint(0,1)])
                    fart_timer=random.randint(60,120)
            if fart_timer > 0:
                fart_timer -= 1
        elif keys[pygame.K_q]:
            kill_all_sfx(butt_flys, powerups)
            main_menu()
        elif keys[pygame.K_SPACE]:
            if player.bullets > 0 and player.cooldown == 0:
                player.shoot(bullets)
        else:
            player.state="static"
            fart_timer=0
            
        if lost == False:    
            redraw_window()

def main_menu():
    
    menu_font = pygame.font.SysFont("connectionserif",25)
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    intro_timer = 0
    intro_vid = Intro_Animation(INTRO_BIRD,BG,INTRO_FOG,INTRO_RAYS)
    
    # stop any game music if returning to menu
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    
    # load and play menu music
    pygame.mixer_music.load(os.path.join("assets/audio/music","main_menu.wav"))
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1)
    
    def draw_menu():
        menu_label = menu_font.render("<Press the SPACEBAR to begin>", 1, (255,255,255))
        WIN.blit(menu_label,(WIDTH/2 - menu_label.get_width()/2, HEIGHT - menu_label.get_height() - 40))
        menu_label = menu_font.render("<Press Q to Quit>", 1, (255,255,255))
        WIN.blit(menu_label,(WIDTH/2 - menu_label.get_width()/2, HEIGHT - menu_label.get_height() - 10))
    
    while run:
        
        clock.tick(FPS)
                
        intro_timer += 1
        
        intro_vid.timer = intro_timer
        intro_vid.update()
        intro_vid.draw(WIN)
        
        if intro_timer > 120:
            draw_menu()
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and intro_timer > 120:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    
                    pygame.mixer.music.load(os.path.join("assets/audio/music","main_game.wav"))
                    pygame.mixer.music.play(-1)
                    
                    play_endgame = False
                    main()
                if event.key == pygame.K_q:
                    quit()
                    
    quit()
    
main_menu()
