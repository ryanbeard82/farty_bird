# Import libraries
import pygame
import time
import random
import os
import math
import csv
import pygame_textinput

# Initializations
pygame.font.init()
pygame.mixer.init()

# Set constants & Global Variables
GROUND = 700 - 55
WIDTH, HEIGHT = 1333, 750
GAME_SPEED = .75
FPS = 60
HIGH_SCORE_FILE = "high_scores.dat"

# Define window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farty Bird")

# Define custom pygame event to handle endgame
GAME_OVER = pygame.USEREVENT + 1

# Load Images
POWERUP_AVIALABLE = [
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa5.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/available","powerupa6.png")).convert_alpha()
]
POWERUP_COLLIDE = [
    pygame.image.load(os.path.join("./assets/images/powerup/collide","powerupb1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/collide","powerupb2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/collide","powerupb3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/collide","powerupb4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/powerup/collide","powerupb5.png")).convert_alpha()
]
BUTT_FLY_ALIVE = [
    pygame.image.load(os.path.join("./assets/images/butt_fly","static.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap5.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap6.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","flap7.png")).convert_alpha()
]
BUTT_FLY_DEAD = [
    pygame.image.load(os.path.join("./assets/images/butt_fly","death1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death5.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death6.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death7.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death8.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death9.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/butt_fly","death10.png")).convert_alpha()
]
BULLET = [
    pygame.image.load(os.path.join("./assets/images/bullet","bullet1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet5.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet6.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet7.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/bullet","bullet8.png")).convert_alpha()
]
FLAPPING_BIRD = [
    pygame.image.load(os.path.join("./assets/images","flap1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap3.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap4.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap5.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap6.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap7.png")).convert_alpha()
    ]
FLAPPING_FARTS = [
    pygame.image.load(os.path.join("./assets/images","flap1fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap2fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap3fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap4fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap5fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap6fart.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images","flap7.png")).convert_alpha()
    ]
INTRO_FOG_ANIMATE = [
    pygame.image.load(os.path.join("./assets/images/intro","fog_animate1.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/intro","fog_animate2.png")).convert_alpha(),
    pygame.image.load(os.path.join("./assets/images/intro","fog_animate3.png")).convert_alpha()
]
INTRO_FOG = pygame.image.load(os.path.join("./assets/images/intro","fog.png")).convert_alpha()
INTRO_BIRD = pygame.image.load(os.path.join("./assets/images/intro","bird.png")).convert_alpha()
INTRO_RAYS = pygame.image.load(os.path.join("./assets/images/intro","rays.png")).convert_alpha()
INTRO_TITLE = pygame.image.load(os.path.join("./assets/images/intro","title.png")).convert_alpha()
BG = pygame.image.load(os.path.join("./assets/images","bg_3.png")).convert()
BG_MID = pygame.image.load(os.path.join("./assets/images","bg_2.png")).convert_alpha()
BG_TOP = pygame.image.load(os.path.join("./assets/images","bg_1.png")).convert_alpha()
STATIC_BIRD = pygame.image.load(os.path.join("./assets/images","static.png")).convert_alpha()
DEAD_BIRD = pygame.image.load(os.path.join("./assets/images", "death.png")).convert_alpha()
FINGER_PIC = pygame.image.load(os.path.join("./assets/images","finger.png")).convert_alpha()
TURD_STREAKER_PIC = pygame.image.load(os.path.join("./assets/images","turd_streaker.png")).convert_alpha()

# Particle Color Options
FARTICLE_COLORS = [
    ((230,230,230)),
    ((179,179,179)),
    ((194,214,214)),
    ((128,128,128))
]
POOP_COLORS = [
    ((102,51,0)),
    ((204,153,0)),
    ((153,102,0)),
    ((153,102,51))
]

# Load Audio Fx
HIGH_FART_FX = [
    pygame.mixer.Sound(os.path.join("./assets/audio/sfx","fart_1.wav")),
    pygame.mixer.Sound(os.path.join("./assets/audio/sfx","fart_3.wav"))
    ]
LOW_FART_FX = [
    pygame.mixer.Sound(os.path.join("./assets/audio/sfx","fart_2.wav")),
    pygame.mixer.Sound(os.path.join("./assets/audio/sfx","fart_4.wav")),
    pygame.mixer.Sound(os.path.join("./assets/audio/sfx","fart_5.wav")),
    ]
SHOOT_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","shoot.wav"))
FINGER_HIT_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","finger_hit.wav"))
BUTTFLY_HIT_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","buttfly_hit.wav"))
RELOAD_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","reload.wav"))
BUTT_BUZZ_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","buzz.wav"))
POWERUP_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","powerup.wav"))
POWERUP_FX.set_volume(.3)
TURD_HIT_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","turd_pop.wav"))
TURD_WEE_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","turd_wee.wav"))
INTERFACE_FX = pygame.mixer.Sound(os.path.join("./assets/audio/sfx","interface.wav"))

class GameObject: # GameCharacter superclass
    def __init__(self, x, y, health = 100, angle = 0, collision = False, direction = "up", image_counter = 0, playing_audio = False, draw_this_object = True):
        self.x = x
        self.y = y
        self.image = None
        self.velocity = None
        self.mask = None
        self.direction = direction
        self.collision = collision
        self.health = health
        self.image_counter = image_counter
        self.playing_audio = playing_audio
        self.SFX = None
        self.collisionSFX = None
        self.angle = angle
        self.draw_this_object = draw_this_object
        self.fart_image = None
        self.state = None
        
    def kill_audio(self):
        self.playing_audio = False
        if self.SFX != None: self.SFX.stop()
        if self.collisionSFX != None: self.collisionSFX.stop()
        
    def draw(self, window):
        if self.angle == 0:
            if self.image != None and self.draw_this_object: window.blit(self.image, (self.x, self.y))
        else:
            if self.image != None and self.draw_this_object: window.blit(pygame.transform.rotate(self.image,self.angle),(self.x, self.y))
        if self.state == "flying":
            if self.fart_image != None and self.draw_this_object: window.blit(self.fart_image, (self.x, self.y))
            
    def get_width(self):
        return self.image.get_width()
        
    def get_height(self):
        return self.image.get_height()

class Farticle():
    def __init__(self, x, y, x_velocity, y_velocity, timer, color):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.timer = timer
        self.color = color
        
    def update(self):
        self.x, self.y = (int(self.x + self.x_velocity), int(self.y + self.y_velocity))
        self.timer -= 0.05
        
    def draw(self,window):
        pygame.draw.rect(window, self.color, (self.x, self.y, int(self.timer), int(self.timer)))
        
class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image_list = BULLET
        self.velocity = 10
        
    def update(self):
        self.x += self.velocity
        self.image = self.image_list[(self.image_counter//3)-1]
        self.mask = pygame.mask.from_surface(self.image)
        self.image_counter = (self.image_counter % 21) + 1

class ScoreNotifcation(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.y_delta = -5
        self.alpha = 255
        self.velocity = 3
        self.font = pygame.font.SysFont("connectionserif", 25)
        
    def update(self, player_y):
        self.y_delta -= self.velocity
        self.y = player_y + self.y_delta
        self.alpha -= 10 if self.alpha >10 else 0
        self.image = self.font.render("+1", 1, (255,255,255))
        self.image.set_alpha(self.alpha)

class PowerUp(GameObject):
    def __init__(self, x, y, start_y):
        super().__init__(x, y)
        self.start_y = start_y
        self.available_images = POWERUP_AVIALABLE
        self.collide_images = POWERUP_COLLIDE
        self.velocity = 3
        self.SFX = POWERUP_FX
        self.collisionSFX = RELOAD_FX
        
    def update(self):
        if self.direction == "up" and self.collision == False:
            self.y, self.direction = (self.y - 1,"up") if self.y > (self.start_y - 10) else (self.y + 1, "down")
        elif self.direction == "down" and self.collision == False:
            self.y, self.direction = (self.y + 1,"down") if self.y < (self.start_y + 10) else (self.y - 1, "up")
            
        self.x -= (self.velocity * GAME_SPEED)
             
        if self.collision:
            if self.image_counter < 33:
                self.image = self.collide_images[(self.image_counter//8)]
                self.mask = pygame.mask.from_surface(self.image)
                self.image_counter += 1
            else:
                self.draw_this_object = False 
        else:
            self.image = self.available_images[(self.image_counter//5) - 1]
            self.mask = pygame.mask.from_surface(self.image)
            self.image_counter = (self.image_counter % 20) + 1
            
        if (0 - self.get_width()) < self.x < WIDTH and self.playing_audio == False and self.collision == False:
             self.playing_audio = True
             self.SFX.play(-1).set_volume(.5)

class TurdStreaker(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = 2
        self.SFX = TURD_WEE_FX
        self.collisionSFX = TURD_HIT_FX
        self.center_y = None
        self.center_x = None
        self.angle = 0
        self.radius = 200
        self.image = TURD_STREAKER_PIC
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, farticles):
        if self.collision == False:
            if self.playing_audio == False and self.x < WIDTH:
                self.playing_audio = True
                self.SFX.play(-1)
                
            self.x = self.radius * math.sin(self.angle) + self.center_x
            self.y = self.radius * math.cos(self.angle) + self.center_y
            
            self.angle -= .02
            self.center_x -= self.velocity
            
            new_farticle = Farticle(self.x + self.get_width()/2, self.y + self.get_height()/2, random.randint(0, 40)/10 - 2, random.randint(0,40)/10 - 2, int(random.randint(1,3)),random.choice(POOP_COLORS))
            farticles.append(new_farticle)
            
        else:
            
            self.SFX.stop()
            self.playing_audio = False
            self.image_counter += 1
            
            if self.image_counter<=30:
                self.image = pygame.transform.scale(TURD_STREAKER_PIC,(self.get_width()+ 3, self.get_height()+ 1))
                self.x -= self.velocity
            elif self.image_counter < 60:
                self.draw_this_object = False
                new_farticle = Farticle(self.x + self.get_width()/2, self.y + self.get_height()/2, random.randint(0, 40)/10 - 2, random.randint(0,40)/10 - 2, int(random.randint(5,15)),random.choice(POOP_COLORS))
                farticles.append(new_farticle)
            
class ButtFly(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = 4
        self.SFX = BUTT_BUZZ_FX
        self.collisionSFX = BUTTFLY_HIT_FX
        
    def update(self, farticles):
        
        if self.collision:
            self.health = 0
            
            if self.image_counter < 46:
                new_farticle = Farticle(self.x + 5, self.y + self.get_height()/2, random.randint(0, 40)/10 - 2, random.randint(0,40)/10 - 2, int(random.randint(2,5)),random.choice(POOP_COLORS))
                farticles.append(new_farticle)
        
        if self.direction == "up" and self.collision == False:
            self.y, self.direction = (self.y - 2,"up") if self.y > 150 else (self.y + 2, "down")
        elif self.direction == "down" and self.collision == False:
            self.y, self.direction = (self.y + 2,"down") if self.y < 550 else (self.y - 2, "up")
        
        self.x -= (self.velocity * GAME_SPEED)
          
        if self.health != 0:
            self.image = BUTT_FLY_ALIVE[(self.image_counter//6)-1]
            self.mask = pygame.mask.from_surface(self.image)
            self.image_counter = (self.image_counter % 42) + 1
        else:
            if self.image_counter < 46:
                self.image = BUTT_FLY_DEAD[(self.image_counter//5)]
                self.mask = pygame.mask.from_surface(self.image)
                self.image_counter += 1
            else:
                self.draw_this_object = False
                
        if (0 - self.get_width()) < self.x < WIDTH and self.playing_audio == False and self.collision == False:
            self.playing_audio = True
            self.SFX.play(-1)

class Player(GameObject):
    
    MAXSPEED = 20
    MAXFALL = -35
    VELOCITY_MULT = 1.03
    FALL_MULT = .05
    
    def __init__(self, x, y, state="static", powerup = False, bullets = 0, cooldown = 0): #TESTING BULLETS
        super().__init__(x, y)
        self.powerup = powerup
        self.bullets = bullets
        self.cooldown = cooldown
        self.state = state
        self.velocity = 0
        self.SFX = SHOOT_FX
        self.fart_image = None
        
    def shoot(self, bullets):
        if self.bullets == 0: return
        self.SFX.play()
        self.bullets -= 1
        self.cooldown = 30
        new_bullet = Bullet(self.x + self.get_width()/2,self.y + self.get_height()/4)
        new_bullet.update()
        bullets.append(new_bullet)
        
    def update(self, farticles):
        if self.cooldown > 0: self.cooldown -= 1
        
        if self.state == "flying":
            # set image
            self.image = FLAPPING_BIRD[(self.image_counter//5)-1]
            self.fart_image = FLAPPING_FARTS[(self.image_counter//5)-1]
            self.mask = pygame.mask.from_surface(self.image)
            self.image_counter = (self.image_counter % 30) + 1
            
            # calc velocity
            if self.velocity == 0: self.velocity = 1
            if self.velocity < self.MAXSPEED:
                if self.velocity >= 1:
                    self.velocity = self.velocity * self.VELOCITY_MULT
                elif self.velocity <1 and self.velocity >-1:
                    self.velocity = 1
                else:
                    self.velocity = self.velocity - (self.velocity * self.VELOCITY_MULT)
            if self.velocity > self.MAXSPEED: self.velocity = self.MAXSPEED
            
            # calc y value
            if (self.y - self.velocity) > 10: self.y -= self.velocity
            else: self.y = 10 # lower limit (top of screen)
            
            # create farticles
            new_farticle1 = Farticle(self.x + 10, self.y + self.get_height() - 25, random.randint(-20, 40) / 10 - 4, random.randint(-5, 30) / 10, int(random.randint(2,7)), random.choice(FARTICLE_COLORS))
            new_farticle2 = Farticle(self.x + 10, self.y + self.get_height() - 25, random.randint(-20, 40) / 10 - 4, random.randint(-5, 30) / 10, int(random.randint(2,7)), random.choice(FARTICLE_COLORS))
            farticles.append(new_farticle1)
            farticles.append(new_farticle2)
            
        elif self.state == "static":
            # set image
            if self.image_counter != 0 and self.image_counter != 31:
                self.image = FLAPPING_BIRD[(self.image_counter//5)-1]
                self.mask = pygame.mask.from_surface(self.image)
                self.image_counter = (self.image_counter % 31)+1
            else:
                self.image_counter = 0
                self.image = STATIC_BIRD
                self.mask = pygame.mask.from_surface(self.image)
            
            # calc velocity
            if self.y == GROUND: self.velocity = 0
            else:
                if self.velocity > self.MAXFALL:
                    if self.velocity >= 1:
                        self.velocity = self.velocity - (self.velocity * self.FALL_MULT)
                    elif self.velocity < 1 and self.velocity > -1:
                        self.velocity = -1
                    else:
                        self.velocity = self.velocity * (1 + self.FALL_MULT)
                if self.velocity < self.MAXFALL: self.velocity = self.MAXFALL
            
            # set y value
            if (self.y - self.velocity) < 10:
                self.y = 10
            elif (self.y - self.velocity) < GROUND:
                self.y -= self.velocity
            else: self.y = GROUND
            
        elif self.state == "death":
            # set image
            self.image = DEAD_BIRD
            self.mask = pygame.mask.from_surface(self.image)
            
            # set angle & y values
            if self.angle != 180: self.angle += 1
            self.y += 4
            
class Finger(GameObject):
    def __init__ (self, x, y, scored = False):
        super().__init__(x, y)
        self.scored = scored
        self.velocity = 3
        self.SFX = FINGER_HIT_FX
        
    def update(self):
        self.x -= (self.velocity * GAME_SPEED)
        if self.x > WIDTH or (self.x + self.get_width()) < 0: self.draw_this_object = False
        else: self.draw_this_object = True
        
        if self.direction == "up":
            if self.collision and self.y < 750: self.y += 3
            self.image = FINGER_PIC
            self.mask = pygame.mask.from_surface(self.image)
        else:
            if self.collision and self.y > -550: self.y -= 3
            self.image = pygame.transform.flip(FINGER_PIC,True,True)
            self.mask = pygame.mask.from_surface(self.image)

class Intro_Animation: # Handles startup / menu animation sequence
    def __init__(self, BIRD_IMG, BG_IMG, FOG_IMG, RAYS_IMG, bird_y = 750, fog_y = 350, rays_y = 0, title_alpha = 0, draw_title = False, draw_rays = False, temp_int = 0, fog_animation_timer = 0):
        self.BIRD_IMG = BIRD_IMG
        self.bird_y = bird_y
        self.BG_IMG = BG_IMG
        self.fog_animations_list = INTRO_FOG_ANIMATE
        self.fog_y = fog_y
        self.FOG_IMG = FOG_IMG
        self.RAYS_IMG = RAYS_IMG
        self.rays_y = rays_y
        self.rays_up_down = "down"
        self.draw_title = draw_title
        self.draw_rays = draw_rays
        self.TITLE_IMG = INTRO_TITLE
        self.title_rect = self.TITLE_IMG.get_rect()
        self.title_alpha = title_alpha
        self.title_in_out = None
        self.timer = None
        self.fog_animation_timer = fog_animation_timer
        self.fog_animation_delay = 0
        
    def update(self):
        # raise Bird and Fog at t=0
        if self.timer >= 0:
            self.bird_y -= 5 if self.bird_y - 5 >= 0 else 0
            self.fog_y -= 3 if self.fog_y - 3 >= 0 else 0
        # fade in title
        if self.timer >= 120:
            self.draw_title = True
            
            # set title alpha
            if self.title_alpha == 0: self.title_in_out, self.title_alpha = ("in", 5)
            elif self.title_in_out == "in":
                self.title_alpha, self.title_in_out = (self.title_alpha + 5, "in") if self.title_alpha < 255 else (self.title_alpha - 5, "out")
            else: # self.title_alpha = "out"
                self.title_alpha, self.title_in_out = (self.title_alpha - 5, "out") if self.title_alpha > 150 else (self.title_alpha + 5, "in")
        
        if self.bird_y == 0:
            self.draw_rays = True
            if self.rays_up_down == "down":
                self.rays_y, self.rays_up_down = (self.rays_y + 1, "down") if self.rays_y < 20 else (self.rays_y - 1, "up")
            else: # self.rays_up_down = "up"
                self.rays_y, self.rays_up_down = (self.rays_y - 1, "up") if self.rays_y > 0 else (self.rays_y + 1, "down")
        
    def draw(self, window):
        window.blit(self.BG_IMG,(0,0))
        
        window.blit(self.BIRD_IMG,(0,self.bird_y))
        
        self.fog_animation_delay += 1
        if self.fog_animation_delay == 10:
            self.fog_animation_timer = (self.fog_animation_timer % 3) + 1
            self.fog_animation_delay = 0
            
        window.blit(self.FOG_IMG,(0,self.fog_y))
        window.blit(self.fog_animations_list[self.fog_animation_timer - 1],(0,self.fog_y))
        
        if self.draw_rays:
            window.blit(self.RAYS_IMG,(0,self.rays_y))
        
        if self.draw_title:
            self.TITLE_IMG.set_alpha(self.title_alpha)
            window.blit(self.TITLE_IMG,self.title_rect)

class Background: # handles background parallax effect
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

class high_score:
    def __init__(self):
        self.name = None
        self.score = None

def sort_by_score(hscore):
    return(int(hscore.score))

def collide(obj1, obj2): # detects object collision
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
    
def spawn_fingers(fingerlist): # maintains a series of 20 finger enemenies
    if len(fingerlist)==0:
            new_finger = Finger(WIDTH + 50, random.randint(250,650))
            fingerlist.append(new_finger)
    while len(fingerlist) != 20:
        new_finger = Finger(0,0)
        if fingerlist[len(fingerlist)-1].direction == "up":
            new_finger.direction = "down"
            new_finger.y, new_finger.x = fingerlist[len(fingerlist)-1].y - 700,  fingerlist[len(fingerlist)-1].x
        else:
            new_finger.y, new_finger.x = random.randint(250, 650), fingerlist[len(fingerlist)-1].x + random.randint(300, 450)
        fingerlist.append(new_finger) 
        
    return fingerlist

def spawn_butt_flys(butt_fly_list): # spawns a single butt-fly at a time
    if len(butt_fly_list)==0:
        new_butt_fly = ButtFly(random.randint(1500,5000),300)
        butt_fly_list.append(new_butt_fly)

def spawn_powerup(powerup_list, finger_list, powerup_timer): # random chance to spawn a single powerup after the power-up timer expires
    if len(powerup_list)==0 and random.randint(0, 300) == 100:
        powerup_timer = 240
        new_powerup = PowerUp(3000,0,random.randint(200,550))
        new_powerup.y = new_powerup.start_y
        
        if len(powerup_list)>1 and new_powerup.x < (powerup_list[len(powerup_list)-1].x + 4000):
            new_powerup.x += 4000
        
        # evaluate x and place between fingers
        i = 0
        for finger in finger_list:
            i += 1
            if finger.x > new_powerup.x: # found the right barrier
                new_powerup.x = finger_list[i-2].x + (finger.x - finger_list[i-2].x)/2
                break
        new_powerup.update()
        powerup_list.append(new_powerup)
            
    return powerup_timer
    
def kill_all_sfx(buttflys, powerups, turd_streakers): # kills all repeating SFX (butt-fly and powerup)
    for butt in buttflys:
        if butt.playing_audio == True: butt.kill_audio()
    for powerup in powerups:
        if powerup.playing_audio == True: powerup.kill_audio()
    for turd in turd_streakers:
        if turd.playing_audio == True: turd.kill_audio()

def spawn_score(score_notifications, player): # shows floating score indicator
    new_score = ScoreNotifcation(WIDTH/2, player.y)
    score_notifications.append(new_score)
    return score_notifications
    
def play_endgame_music(): #initiates endgame music
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(os.path.join("./assets/audio/music","game_over.wav"))
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(GAME_OVER)

def spawn_turdstreaker(turd_streakers):
    if len(turd_streakers)==0:
        new_turd = TurdStreaker(random.randint(1500,5000), 350)
        new_turd.y = (HEIGHT/2 - new_turd.get_height()/2 - 50)
        new_turd.center_y = new_turd.y
        new_turd.center_x = new_turd.x
        turd_streakers.append(new_turd)

def get_high_score(high_scores):
    if len(high_scores) > 0:    
        # Sort High Scores for comparison
        high_scores.sort(key=sort_by_score)
        return int(high_scores[len(high_scores)-1].score)
    else:
        return 0
        
def get_all_high_scores(high_scores):
    # First read all existing high-scores
    with open(HIGH_SCORE_FILE,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            tempScore = high_score()
            tempScore.name,tempScore.score = row[0],row[1]
            high_scores.append(tempScore)
    file.close()
    high_scores.sort(key=sort_by_score, reverse=True)
    return high_scores
    
def check_high_score(cur_score, high_scores):
    
    if len(high_scores)<10: return True
    elif cur_score > int(high_scores[0].score): 
        del high_scores[0]
        return True
    else: return False

def update_high_score_file(high_scores):
    high_scores.sort(key=sort_by_score)
    with open(HIGH_SCORE_FILE,"w+") as file:
        writer = csv.writer(file)
        for score in high_scores:
            tempRow = [score.name,score.score]
            writer.writerow(tempRow)
    file.close()

def main():
    
    global GAME_SPEED
    global FPS
    level = 0
    level_timer = 0
    run = True
    fingers = []
    powerups = []
    lost = False
    score = 0
    fart_timer = 0
    powerup_timer = 0
    bullets = []
    butt_flys = []
    play_endgame = False
    score_notifications = []
    player_sfx_channel = None
    farticles = []
    turd_streakers = []
    cur_high_score = 0
    high_scores = []
    new_high_score = False
    
    lost_font = pygame.font.SysFont("connectionserif", 40)
    level_font = pygame.font.SysFont("connectionserif", 70)
    score_font = pygame.font.SysFont("connectionserif", 25)

    player = Player(WIDTH/2 - STATIC_BIRD.get_width()/2,GROUND)
    background =  Background(BG,BG_MID,BG_TOP)
    clock = pygame.time.Clock()
    
    high_scores = get_all_high_scores(high_scores)
    cur_high_score = get_high_score(high_scores)

    def redraw_window():
        nonlocal level_timer
        nonlocal score
        nonlocal level
        
        background.update()
        background.draw(WIN)
        
        for finger in fingers:
            finger.update()
            finger.draw(WIN)
         
        for butt_fly in butt_flys:
            butt_fly.update(farticles)
            butt_fly.draw(WIN)
            
        for turd in turd_streakers:
            turd.update(farticles)
            turd.draw(WIN)
        
        for powerup in powerups:
            powerup.update()
            powerup.draw(WIN)
            
        for bullet in bullets:
            bullet.update()
            bullet.draw(WIN)
        
        for farticle in farticles[:]:
            if farticle.timer <= 0: farticles.remove(farticle)
            farticle.update()
            farticle.draw(WIN)
        
        player.update(farticles)
        player.draw(WIN)
        
        for notification in score_notifications:
            notification.update(player.y)
            notification.draw(WIN)
        
        if level_timer > 0:
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
        
        # Draw Current High Score
        score_label = score_font.render("High Score: ", 1, (255,255,255))
        score_value = score_font.render(str(cur_high_score), 1, (255,255,255))
        WIN.blit(score_label,(20, 15))
        WIN.blit(score_value, (score_label.get_width() + 30, 15))
        
        pygame.display.update()
        
    def draw_endgame():
        
        background.draw(WIN)
        
        for finger in fingers:
            finger.draw(WIN)
            
        for butt_fly in butt_flys:
            butt_fly.draw(WIN)
            
        for turd in turd_streakers:
            turd.draw(WIN)
            
        for powerup in powerups:
            powerup.draw(WIN)
            
        for bullet in bullets:
            bullet.draw(WIN)
            
        for notification in score_notifications:
            notification.update(player.y)
            notification.draw(WIN)
        
        # Draw Score
        score_label = score_font.render("Score: ", 1 , (255,255,255))
        score_value = score_font.render(str(score), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 15))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 15))
        
        # Draw Bullet Count
        score_label = score_font.render("Bullets: ", 1, (255,255,255))
        score_value = score_font.render(str(player.bullets), 1, (255,255,255))
        WIN.blit(score_label,(WIDTH - score_label.get_width() - score_value.get_width() - 20, 45))
        WIN.blit(score_value, (WIDTH - score_value.get_width() - 10, 45))
        
        # Draw Current High Score
        score_label = score_font.render("High Score: ", 1, (255,255,255))
        score_value = score_font.render(str(cur_high_score), 1, (255,255,255))
        WIN.blit(score_label,(20, 15))
        WIN.blit(score_value, (score_label.get_width() + 30, 15))
        
        lost_label = lost_font.render("You pulled my finger", 1 , (255,255,255))
        WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 - lost_label.get_height()))
        
        lost_label = lost_font.render("...and lost", 1 , (255,255,255))
        WIN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, HEIGHT/2 + 5))
        
        for farticle in farticles[:]:
            if farticle.timer <= 0: farticles.remove(farticle)
            farticle.update()
            farticle.draw(WIN)
        
        player.update(farticles)
        player.draw(WIN)
        
        pygame.display.update()
        
    while run:
        clock.tick(FPS)
        if lost:
            player.state = "death"
            
            new_high_score = check_high_score(score,high_scores)
            
            while play_endgame:
                draw_endgame()
                for event in pygame.event.get():
                    if event.type == GAME_OVER:
                        play_endgame =  False
            
            if new_high_score: enter_high_score(score,high_scores)
            
            main_menu()
        
        # COLLISION CHECKS
        for finger in fingers[:]:
            if finger.x <= 0 - finger.get_width(): fingers.remove(finger)
                
            if finger.scored == False and finger.direction == "up" and  (finger.x + finger.get_width()) < player.x:
                finger.scored = True
                score += 1
                score_notifications = spawn_score(score_notifications[:],player)
                
            if collide(finger, player) and lost == False:
                kill_all_sfx(butt_flys, powerups, turd_streakers)
                play_endgame_music()
                play_endgame = True
                lost = True
                
            for bullet in bullets[:]:
                if collide(bullet, finger) and finger.collision == False:
                    finger.SFX.play()
                    bullets.remove(bullet)
                    finger.collision = True
        
        for turd in turd_streakers[:]:
            if turd.x <= 0 - turd.get_width() - 100 or (turd.collision == True and turd.image_counter > 60):
                turd.kill_audio()
                turd_streakers.remove(turd)
                
            if collide(turd, player) and lost == False:
                kill_all_sfx(butt_flys, powerups, turd_streakers)
                play_endgame_music()
                play_endgame = True
                lost = True
                
            for bullet in bullets[:]:
                if collide(bullet,turd) and turd.collision == False:
                    turd.kill_audio()
                    turd.collisionSFX.play()
                    turd.collision = True
                    bullets.remove(bullet)
                
        for butt_fly in butt_flys[:]:
            if butt_fly.x <= 0 - butt_fly.get_width():
                butt_fly.kill_audio()
                butt_flys.remove(butt_fly)
            
            if collide(butt_fly,player) and butt_fly.collision == False  and lost == False:
                kill_all_sfx(butt_flys, powerups, turd_streakers)
                play_endgame_music()
                play_endgame = True
                lost = True
                
            for bullet in bullets[:]:
                if collide(bullet,butt_fly) and butt_fly.collision == False:
                    butt_fly.kill_audio()
                    butt_fly.collisionSFX.play()
                    butt_fly.collision = True
                    butt_fly.img_counter = 0
                    bullets.remove(bullet)
                
        for powerup in powerups[:]:
            if collide(powerup, player) and powerup.collision == False:
                powerup.kill_audio()
                powerup.collisionSFX.play()
                powerup.collision = True
                player.bullets += 2
            if powerup.collision == True and powerup.image_counter > 32:
                if powerup.playing_audio == True: powerup.kill_audio()
                powerups.remove(powerup)
            if powerup.x < 0 - powerup.get_width():
                if powerup.playing_audio == True: powerup.kill_audio()
                powerups.remove(powerup)
                
        for notification in score_notifications[:]:
            if notification.alpha == 0: score_notifications.remove(notification)
        
        if powerup_timer > 0: powerup_timer -= 1
        else: powerup_timer = spawn_powerup(powerups,fingers,powerup_timer)
        
        if score//20 + 1 > level:
            level += 1
            level_timer = 120
            GAME_SPEED += .25
        
        if score > cur_high_score:
            cur_high_score = score
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
            
        fingers = spawn_fingers(fingers[:])
        
        if level > 1: spawn_butt_flys(butt_flys)
        if level > 2: spawn_turdstreaker(turd_streakers)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and lost == False:
            player.state = "flying"
            if fart_timer==0:
                if player.y > 350:
                    pygame.mixer.Sound.play(LOW_FART_FX[random.randint(0,2)]).set_volume(.8)
                    fart_timer=random.randint(60,120)
                else:
                    pygame.mixer.Sound.play(HIGH_FART_FX[random.randint(0,1)]).set_volume(.5)
                    fart_timer=random.randint(60,120)
            if fart_timer > 0 and fart_timer != 0: fart_timer -= 1
        elif keys[pygame.K_q]:
            kill_all_sfx(butt_flys, powerups)
            INTERFACE_FX.play()
            main_menu()
        elif keys[pygame.K_SPACE]:
            if player.bullets > 0 and player.cooldown == 0: player.shoot(bullets)
        else:
            player.state="static"
            fart_timer=0
            
        if lost == False: redraw_window()

def enter_high_score(score, high_scores):
    global FPS
    run = True
    score_font = pygame.font.SysFont("connectionserif",25)
    clock = pygame.time.Clock()
    user_input = pygame_textinput.TextInput()
    
    while run:
        
        clock.tick(FPS)
        
        WIN.blit(BG,(0,0))
        
        instruction_label = score_font.render("Enter your name:", 1, (255,255,255))
        WIN.blit(instruction_label,(WIDTH/2 - instruction_label.get_width()/2, 100))
    
        events = pygame.event.get()
         
        for event in events:
            if event.type ==  pygame.QUIT:
                run = False
        
        if user_input.update(events):
            INTERFACE_FX.play()
            new_high_score = high_score()
            new_high_score.name = user_input.get_text()
            new_high_score.score = score
            high_scores.append(new_high_score)
            update_high_score_file(high_scores)
            run = False
        
        WIN.blit(user_input.get_surface(),(WIDTH/2 - user_input.get_surface().get_width()/2, HEIGHT/2))
        
        pygame.display.update() 

def high_score_screen():
    global FPS
    run = True
    current_y = None
    y_delta = 30
    clock = pygame.time.Clock()
    left_x_bound = None
    right_x_bound = ModuleNotFoundError
    score_font = pygame.font.SysFont("connectionserif",25)
    header_font = pygame.font.SysFont("connectionserif", 70)
    high_scores = []
    clear_prompt = False
    delete_high_scores = False
    
    high_scores = get_all_high_scores(high_scores)
    
    while run:
        
        clock.tick(FPS)
        
        WIN.blit(BG,(0,0))
        
        if clear_prompt:
            
            instruction_label = score_font.render("<Press Y to confirm, N to cancel>", 1, (255,255,255))
            WIN.blit(instruction_label,(WIDTH/2 - instruction_label.get_width()/2, HEIGHT - 40))
            
            delete_prompt_label = header_font.render("Permanently delete", 1, (255,255,255))
            WIN.blit(delete_prompt_label,(WIDTH/2 - delete_prompt_label.get_width()/2,HEIGHT/2 - delete_prompt_label.get_height()))
            delete_prompt_label2 = header_font.render("all High-Scores?", 1, (255,255,255))
            WIN.blit(delete_prompt_label2,(WIDTH/2 - delete_prompt_label2.get_width()/2,HEIGHT/2 + 10))
            
            if delete_high_scores:
                high_scores.clear()
                update_high_score_file(high_scores)
                clear_prompt = False
                delete_high_scores = False
        
        else:
            
            instruction_label = score_font.render("<Press Q to Exit>", 1, (255,255,255))
            WIN.blit(instruction_label,(WIDTH/2 - instruction_label.get_width()/2, HEIGHT - 70))
            
            if len(high_scores) > 0:
                instruction_label = score_font.render("<Press C to clear High-Scores>", 1, (255,255,255))
                WIN.blit(instruction_label,(WIDTH/2 - instruction_label.get_width()/2, HEIGHT - 40))
            
            name_header = header_font.render("Name", 1, (255,255,255))
            score_header = header_font.render("Score", 1, (255,255,255))
            left_x_bound = WIDTH/2 - (name_header.get_width()/2 + 100 + score_header.get_width()/2)
            right_x_bound = WIDTH/2 + (name_header.get_width()/2 + 100 + score_header.get_width()/2)
            WIN.blit(name_header,(left_x_bound,100))
            WIN.blit(score_header,(right_x_bound - score_header.get_width(),100))
            pygame.draw.line(WIN,(255,255,255),(left_x_bound,100+score_header.get_height()+2),(right_x_bound,100+score_header.get_height()+2),5)
            
            current_y = 100+score_header.get_height() + 17 # Includes line weight + buffer
            
            for high_score in high_scores:
                name = score_font.render(high_score.name, 1, (255,255,255))
                score = score_font.render(high_score.score, 1, (255,255,255))
                WIN.blit(name,(left_x_bound,current_y))
                WIN.blit(score,(right_x_bound - score.get_width(),current_y))
                current_y += y_delta
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    INTERFACE_FX.play()
                    main_menu()
                if event.key == pygame.K_c:
                    if len(high_scores) > 0:
                        INTERFACE_FX.play()
                        if clear_prompt == False: clear_prompt = True
                if event.key == pygame.K_y:
                    INTERFACE_FX.play()
                    if clear_prompt == True: delete_high_scores = True
                if event.key == pygame.K_n:
                    INTERFACE_FX.play()
                    if clear_prompt == True: clear_prompt = False
                        
        pygame.display.update()  
             
def main_menu():
    
    global GAME_SPEED
    global FPS
    menu_font = pygame.font.SysFont("connectionserif",25)
    run = True
    clock = pygame.time.Clock()
    intro_timer = 0
    intro_vid = Intro_Animation(INTRO_BIRD,BG,INTRO_FOG,INTRO_RAYS)
    
    # stop any game music if returning to menu
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    
    # load and play menu music
    pygame.mixer_music.load(os.path.join("./assets/audio/music","main_menu.wav"))
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1)
    
    def draw_instructions():
        menu_label = menu_font.render("<Press the SPACEBAR to begin>", 1, (255,255,255))
        WIN.blit(menu_label,(WIDTH/2 - menu_label.get_width()/2, HEIGHT - menu_label.get_height() - 70))
        menu_label = menu_font.render("<Press S to view High Scores>", 1, (255,255,255))
        WIN.blit(menu_label,(WIDTH/2 - menu_label.get_width()/2, HEIGHT - menu_label.get_height() - 40))
        menu_label = menu_font.render("<Press Q to Quit>", 1, (255,255,255))
        WIN.blit(menu_label,(WIDTH/2 - menu_label.get_width()/2, HEIGHT - menu_label.get_height() - 10))
    
    while run:
        
        clock.tick(FPS)
                
        intro_timer += 1
        
        intro_vid.timer = intro_timer
        intro_vid.update()
        intro_vid.draw(WIN)
        
        if intro_timer > 120: draw_instructions()
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and intro_timer > 120:
                    INTERFACE_FX.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    
                    pygame.mixer.music.load(os.path.join("./assets/audio/music","main_game.wav"))
                    pygame.mixer.music.play(-1)
                    
                    play_endgame = False
                    GAME_SPEED = 0.75
                    main()
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_s:
                    INTERFACE_FX.play()
                    high_score_screen()
                    
    quit()
    
main_menu()