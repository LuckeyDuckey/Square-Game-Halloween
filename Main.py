import pygame, sys, time, os, math, random, pickle
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Square Game Halloween")
pygame.mouse.set_visible(False)

screen_size = (1500,900)#(3000,1800)

while screen_size[0] > pygame.display.Info().current_w or screen_size[1] > pygame.display.Info().current_h or abs(screen_size[1]-pygame.display.Info().current_h) < 50:
    screen_size = (screen_size[0] - 150, screen_size[1] - 90)
    
screen = pygame.display.set_mode(screen_size, DOUBLEBUF, 32)
scale = [screen_size[0]/500, screen_size[1]/300]
display = pygame.Surface((500,300))

screen.set_alpha(None)
#display.set_alpha(None)

pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP])

#-----
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(64)

pygame.mixer.music.load(os.path.join(os.getcwd(), "DATA\\SOUNDS\\Music.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.0)

lightning_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\lightning_sound.wav"))###
enemy_hit_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\enemy_hit_sound.wav"))###
fireball_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\fireball_sound.wav"))###
fireball_sound_explosion = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\fireball_sound_explosion.wav"))###
teleport_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\teleport_sound.wav"))###
jump_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\jump_sound.wav"))###
second_attack_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\second_attack_sound.wav"))###
second_attack_explosion_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\second_attack_explosion_sound.wav"))###
candy_corn_collection_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\candy_corn_collection_sound.wav"))###
wepon_switching_sound_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\wepon_switching_sound_sound.wav"))###
bounce_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\bounce.wav"))###
orb_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\orb_shoot.wav"))###
orb_explosion_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\orb_explode.wav"))###
death_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), "DATA\\SOUNDS\\death.wav"))###

sounds = [lightning_sound, enemy_hit_sound, fireball_sound, fireball_sound_explosion, teleport_sound, jump_sound, second_attack_sound, second_attack_explosion_sound, candy_corn_collection_sound, wepon_switching_sound_sound, bounce_sound, orb_explosion_sound, orb_sound, death_sound]
#-----

clock, last_time = pygame.time.Clock(), time.time()
fps, delta_fps = 175, 60

PLAYER_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Square.png")),(24,24)).convert_alpha()
ENEMY_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Enemy.png")),(24,40)).convert_alpha()
WAND_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Wand.png")),(16,16)).convert_alpha()
HEAL_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Heal.png")),(26,32)).convert_alpha()
HEAL_IMG1 = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Heal.png")),(20,24)).convert_alpha()
BOLT_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Lightning.png")),(30,300)).convert_alpha()
BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Bg.png")),(500,300)).convert_alpha()
WITCH_HAT_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\witch_hat.png")),(42,32)).convert_alpha()
TOP_HAT_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\top_hat.png")),(30,44)).convert_alpha()

#ENEMY_IMG.set_alpha(150)

DECORATIONS = []

PUMPKIN_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\pumpkin.png")),(41,41)).convert_alpha()
CANDY_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Candy.png")),(41,41)).convert_alpha()
GRAVE_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Grave.png")),(41,41)).convert_alpha()
CANDLES_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Candles.png")),(23,23)).convert_alpha()
WEB_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Web.png")),(50,50)).convert_alpha()
SKULL_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Skull.png")),(41,41)).convert_alpha()
CASE_IMG = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "DATA\\IMAGES\\Case.png")),(32,32)).convert_alpha()

DECORATIONS.append([CASE_IMG, [675,-32]])
DECORATIONS.append([PUMPKIN_IMG, [375,-161]])
DECORATIONS.append([PUMPKIN_IMG, [890,-211]])
DECORATIONS.append([CANDY_IMG, [128,-251]])
DECORATIONS.append([CANDY_IMG, [580,-251]])
DECORATIONS.append([CANDY_IMG, [520,-41]])
DECORATIONS.append([GRAVE_IMG, [210,-41]])
DECORATIONS.append([GRAVE_IMG, [700,-121]])
DECORATIONS.append([CANDLES_IMG, [75,-103]])
DECORATIONS.append([CANDLES_IMG, [420,-143]])
DECORATIONS.append([CANDLES_IMG, [886,-23]])
DECORATIONS.append([CANDLES_IMG, [620,-231]])
DECORATIONS.append([WEB_IMG, [0,-68]])
DECORATIONS.append([pygame.transform.flip(WEB_IMG, True, False), [950,-280]])
DECORATIONS.append([SKULL_IMG, [95,-251]])
DECORATIONS.append([SKULL_IMG, [846,-41]])
DECORATIONS.append([SKULL_IMG, [485,-41]])

title = pygame.font.SysFont(None, 50)
body = pygame.font.SysFont(None, 20)

from SCRIPTS.Player_Script import Player
from SCRIPTS.Enemy_Script import Enemy
from SCRIPTS.Circle_Particles_Script import Particle
from SCRIPTS.Text_Script import Font
from SCRIPTS.Fireball_Script import Fireball
from SCRIPTS.Bouncy_Script import Ball
from SCRIPTS.Orb_Script import Orb

title = Font(os.path.join(os.getcwd(), "DATA\\FONTS\\large_font.png"), [255,255,255], 2.5)
body = Font(os.path.join(os.getcwd(), "DATA\\FONTS\\small_font.png"), [255,255,255], 2)

difficulty, show_fps = "Easy", "True"
music_volume, sound_volume = 50, 50
high_score = 0

#save = {"highscorehard":0, "highscoreeasy":0, "musicvolume":50, "soundvolume":50}
#file = open("DATA//data.pkl", "wb")
#pickle.dump(save, file)
#file.close()

file = open("DATA//data.pkl", "rb")
settings = pickle.load(file)
#print(settings)
file.close()

music_volume, sound_volume = settings["musicvolume"], settings["soundvolume"]
high_score_hard = settings["highscorehard"]
high_score_easy = settings["highscoreeasy"]

show_hat = "none"

pygame.mixer.music.set_volume(music_volume/100)
for sound in sounds: sound.set_volume(sound_volume/100)

def Main_Menu():
    global last_time, fps, delta_fps, difficulty, show_fps, high_score_hard, high_score_easy
    
    PLAY_BUTTON = pygame.Rect(170, 130, 150, 26)
    MULTIPLAYER_BUTTON = pygame.Rect(170, 160, 150, 26)
    OPTIONS_BUTTON = pygame.Rect(170, 190, 150, 26)
    QUIT_BUTTON = pygame.Rect(170, 220, 150, 26)

    BLACK_BOX = pygame.Rect(125, 0, 250, 300)
    WHITE_LINE = pygame.Rect(125, -5, 250, 310)

    LINE = pygame.Rect(160, 107, 177, 1)
    TIME_STEP = 0

    GLOW_PARTICLES, delta_counter = [], 0
    
    while 1:

        clock.tick(fps)

        delta_time = time.time() - last_time
        delta_time *= delta_fps
        last_time = time.time()

        screen.fill((0,0,0))
        display.fill((0,0,100))

        #-----
        display.blit(BG_IMG, (0,0))

        delta_counter += delta_time

        if delta_counter > 1:
            delta_counter = 0

            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, 183, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, 187, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, 143, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, 147, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            
        for i,particle in sorted(enumerate(GLOW_PARTICLES),reverse=True):
            temp = particle.main(display, delta_time, [0,0], True)
            if temp == 0:
                GLOW_PARTICLES.remove(particle)
                del particle     
        #-----

        pygame.draw.rect(display, (0, 0, 0), BLACK_BOX)
        pygame.draw.rect(display, (255, 255, 255), WHITE_LINE, 1)

        if TIME_STEP ** 2 / 4 < 255: TIME_STEP += delta_time
        display.set_alpha(TIME_STEP ** 2 / 4)

        mx, my = int(pygame.mouse.get_pos()[0] / scale[0]), int(pygame.mouse.get_pos()[1] / scale[1])

        if PLAY_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), PLAY_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), PLAY_BUTTON, width=1, border_radius=5)

        if MULTIPLAYER_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), MULTIPLAYER_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), MULTIPLAYER_BUTTON, width=1, border_radius=5)

        if OPTIONS_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), OPTIONS_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), OPTIONS_BUTTON, width=1, border_radius=5)

        if QUIT_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), QUIT_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), QUIT_BUTTON, width=1, border_radius=5)

        pygame.draw.rect(display, (255, 255, 255), LINE)
        
        title.render("Square Game", display, (157, 60))
        body.render("Play", display, (235, 137))
        body.render("Multiplayer", display, (211, 167))
        body.render("Options", display, (224, 197))
        body.render("Quit", display, (236, 227))

        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(mx-2, my-2, 4, 4))

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    if PLAY_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        TIME_STEP = 0
                        Single_Player()

                    if MULTIPLAYER_BUTTON.collidepoint((mx,my)):
                        pass

                    if OPTIONS_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        TIME_STEP = 0
                        Options_Menu(True)

                    if QUIT_BUTTON.collidepoint((mx,my)):
                        pygame.quit()
                        sys.exit()

        surf = pygame.transform.scale(display, screen_size)
        try:
            screen.blit(surf,(0,0))
            pygame.display.update()
        except: pass

def Options_Menu(change_diff):
    global last_time, fps, delta_fps, difficulty, show_fps, music_volume, sound_volume, high_score_hard, high_score_easy, sounds, show_hat
    
    DIFFICULTY_BUTTON_UP = pygame.Rect(297, 186, 15, 15)
    DIFFICULTY_BUTTON_DOWN = pygame.Rect(249, 186, 15, 15)
    SHOW_FPS_BUTTON_UP = pygame.Rect(297, 211, 15, 15)
    SHOW_FPS_BUTTON_DOWN = pygame.Rect(249, 211, 15, 15)
    HAT_BUTTON_UP = pygame.Rect(297, 236, 15, 15)
    HAT_BUTTON_DOWN = pygame.Rect(249, 236, 15, 15)

    MUSIC_SLIDER = pygame.Rect(225, 142, 88, 4)
    MUSIC_BUTTON = pygame.Rect(((music_volume / (100 / 84)) + 225), 139, 4, 10) #267
    SOUND_SLIDER = pygame.Rect(225, 167, 88, 4)
    SOUND_BUTTON = pygame.Rect(((sound_volume / (100 / 84)) + 225), 164, 4, 10)
    
    BACK_BUTTON = pygame.Rect(170, 255, 150, 26)

    BLACK_BOX = pygame.Rect(125, 0, 250, 300)
    WHITE_LINE = pygame.Rect(125, -5, 250, 310)

    LINE = pygame.Rect(160, 107, 177, 1)
    TIME_STEP = 0

    RUN = True

    clicking_music, clicking_sound = False, False

    GLOW_PARTICLES, delta_counter = [], 0
    
    while RUN:

        clock.tick(fps)

        delta_time = time.time() - last_time
        delta_time *= delta_fps
        last_time = time.time()

        screen.fill((0,0,0))
        display.fill((0,0,100))

        #-----
        display.blit(BG_IMG, (0,0))

        delta_counter += delta_time

        if delta_counter > 1:
            delta_counter = 0

            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, 183, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, 187, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, 143, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, 147, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            
        for i,particle in sorted(enumerate(GLOW_PARTICLES),reverse=True):
            temp = particle.main(display, delta_time, [0,0], True)
            if temp == 0:
                GLOW_PARTICLES.remove(particle)
                del particle     
        #-----

        pygame.draw.rect(display, (0, 0, 0), BLACK_BOX)
        pygame.draw.rect(display, (255, 255, 255), WHITE_LINE, 1)

        if TIME_STEP ** 2 / 4 < 255: TIME_STEP += delta_time
        display.set_alpha(TIME_STEP ** 2 / 4)

        mx, my = int(pygame.mouse.get_pos()[0] / scale[0]), int(pygame.mouse.get_pos()[1] / scale[1])

        if clicking_music == True:
            if not mx < 225 or not mx > 313: MUSIC_BUTTON.x = mx
            if mx < 225: MUSIC_BUTTON.x = 225
            if mx > 309: MUSIC_BUTTON.x = 309
            music_volume = int((MUSIC_BUTTON.x - 225) * (100 / 84))
            pygame.mixer.music.set_volume(music_volume/100)

        if clicking_sound == True:
            if not mx < 225 or not mx > 313: SOUND_BUTTON.x = mx
            if mx < 225: SOUND_BUTTON.x = 225
            if mx > 309: SOUND_BUTTON.x = 309
            sound_volume = int((SOUND_BUTTON.x - 225) * (100 / 84))
            for sound in sounds: sound.set_volume(sound_volume/100)

        #if BACK_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), BACK_BUTTON
        #else: pygame.draw.rect(display, (40, 40, 40), BACK_BUTTON, 1)

        if BACK_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), BACK_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), BACK_BUTTON, width=1, border_radius=5)

        pygame.draw.rect(display, (255, 255, 255), MUSIC_SLIDER, 1)
        pygame.draw.rect(display, (255, 255, 255), MUSIC_BUTTON)
        pygame.draw.rect(display, (255, 255, 255), SOUND_SLIDER, 1)
        pygame.draw.rect(display, (255, 255, 255), SOUND_BUTTON)

        pygame.draw.rect(display, (255, 255, 255), LINE)
        
        title.render("Options", display, (193, 60))
        body.render("Music", display, (182, 137))
        body.render("Sound", display, (182, 162))
        
        body.render("Difficulty", display, (182, 187))
        if change_diff: body.render("<      >", display, (253, 187))
        body.render("  "+difficulty, display, (253, 187))
        
        body.render("Show Fps", display, (182, 212))
        body.render("<      >", display, (253, 212))
        if show_fps == "True": body.render("  True", display, (253, 212))
        else: body.render("False", display, (264, 212))

        body.render("Show Hat", display, (182, 237))
        body.render("<      >", display, (253, 237))
        if show_hat == "none": body.render("  None", display, (253, 237))
        if show_hat == "witch": body.render("Witch", display, (264, 237))
        if show_hat == "top": body.render(" Top", display, (263, 237))
        
        body.render("Back", display, (236, 262))

        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(mx-2, my-2, 4, 4))

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    if MUSIC_BUTTON.collidepoint((mx,my)):
                        clicking_music = True

                    if SOUND_BUTTON.collidepoint((mx,my)):
                        clicking_sound = True
                    
                    if DIFFICULTY_BUTTON_UP.collidepoint((mx,my)) and change_diff:
                        if difficulty == "Easy": difficulty = "Hard"
                        else: difficulty = "Easy"

                    if DIFFICULTY_BUTTON_DOWN.collidepoint((mx,my)) and change_diff:
                        if difficulty == "Hard": difficulty = "Easy"
                        else: difficulty = "Hard"

                    if SHOW_FPS_BUTTON_UP.collidepoint((mx,my)):
                        if show_fps == "True": show_fps = "False"
                        else: show_fps = "True"

                    if SHOW_FPS_BUTTON_DOWN.collidepoint((mx,my)):
                        if show_fps == "False": show_fps = "True"
                        else: show_fps = "False"

                    if HAT_BUTTON_UP.collidepoint((mx,my)):
                        if show_hat == "none": show_hat = "witch"
                        elif show_hat == "witch": show_hat = "top"
                        elif show_hat == "top": show_hat = "none"

                    if HAT_BUTTON_DOWN.collidepoint((mx,my)):
                        if show_hat == "none": show_hat = "top"
                        elif show_hat == "witch": show_hat = "none"
                        elif show_hat == "top": show_hat = "witch"

                    if BACK_BUTTON.collidepoint((mx,my)):
                        save = {"highscorehard":high_score_hard, "highscoreeasy":high_score_easy, "musicvolume":music_volume, "soundvolume":sound_volume}
                        file = open("DATA//data.pkl", "wb")
                        pickle.dump(save, file)
                        file.close()
                        RUN = False

                if event.button == 3:
                    TIME_STEP = 0

            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    clicking_music = False
                    clicking_sound = False
                    save = {"highscorehard":high_score_hard, "highscoreeasy":high_score_easy, "musicvolume":music_volume, "soundvolume":sound_volume}
                    file = open("DATA//data.pkl", "wb")
                    pickle.dump(save, file)
                    file.close()

        surf = pygame.transform.scale(display, screen_size)
        try:
            screen.blit(surf,(0,0))
            pygame.display.update()
        except: pass

def DARKEN(size,color):
    surf = pygame.Surface((size))
    surf.fill((0,0,0))
    surf.set_alpha(150)
    return surf

def ONSREEN(x, y, width, height):
    if (x > 0 and x < 500) or (x <= 0 and (x+width) > 0):
        if (y > 0 and y < 300) or (y <= 0 and (y+height) > 0): return True
        else: return False
    else: return False

def Single_Player():
    global last_time, fps, delta_fps, DECORATIONS, high_score_hard, high_score_easy, difficulty, show_fps, sounds, show_hat

    display.set_alpha(255)

    loop = 1

    CANDY = []
    
    true_scroll, scroll = [0,0], [0,0]
    GLOW_PARTICLES, NORMAL_PARTICLES, CANDLE_PARTICLES = [], [], []

    CANDLE_PARTICLES.append(Particle(80, -96, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50)) # 75,-103 # 420,-143 # 886,-23 # 620,-231 #
    CANDLE_PARTICLES.append(Particle(92, -92, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))

    CANDLE_PARTICLES.append(Particle(425, -136, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))
    CANDLE_PARTICLES.append(Particle(437, -132, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))

    CANDLE_PARTICLES.append(Particle(891, -16, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))
    CANDLE_PARTICLES.append(Particle(903, -12, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))

    CANDLE_PARTICLES.append(Particle(625, -223, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))
    CANDLE_PARTICLES.append(Particle(637, -219, [0,0], 0, 1, 1, 4, [255,255,255], [50,35,2], 0, 3, -50))

    TILES = [pygame.Rect(1000, -350, 20, 350),
             pygame.Rect(-20, -350, 20, 350),
             pygame.Rect(-20, -300, 1040, 20),
             pygame.Rect(-20, 0, 1040, 20),
             pygame.Rect(80, -210, 170, 12),
             pygame.Rect(290, -120, 170, 12),
             pygame.Rect(490, -210, 170, 12),
             pygame.Rect(790, -170, 170, 12),
             pygame.Rect(620, -80, 170, 12),
             pygame.Rect(0, -80, 130, 12)]

    PLAYER = Player(340, -144, PLAYER_IMG, 24, 24)
    ENEMYS = []
    if difficulty == "Easy": ENEMYS.append(Enemy(100, -100, ENEMY_IMG, 24, 40, False))
    if difficulty == "Hard": ENEMYS.append(Enemy(100, -100, ENEMY_IMG, 24, 40, True))

    candy_timer, ult_timer, enemy_timer = time.time(), time.time(), time.time()#20, 15, 10
    enemy_spawn_len = 10 if difficulty == "Easy" else 1

    LIVES = 3

    BOLTS, BOLTS_TIMER = [[BOLT_IMG, [350, -150]]], 0

    attack = 1
    FIRE_BALLS = []
    BALLS = []
    ORBS = []
                          
    screen_shake = 0
    spell = False
    clear = False

    delta_counter = 0

    score = 0

    fps_avg = [0] * 75

    while loop:

        clock.tick(fps)

        if difficulty == "Easy": high_score_easy = score if high_score_easy < score else high_score_easy
        if difficulty == "Hard": high_score_hard = score if high_score_hard < score else high_score_hard

        #fps independance -----
        delta_time = time.time() - last_time
        delta_time *= delta_fps 
        last_time = time.time()

        delta_counter += delta_time
        #if delta_counter > 1: delta_counter = 0

        #pos += 1 * delta_time #anything else must nowbe multiplied by delta time
        #----------------------

        mx, my = int(pygame.mouse.get_pos()[0] / scale[0]), int(pygame.mouse.get_pos()[1] / scale[1])
        
        #NORMAL_PARTICLES.append(Particle(mx, my, [random.uniform(-2,2),random.uniform(-2,2)], 0.1, 5, 5, 5, [255,255,255], [0,0,0], 0.1, 0, 0.5))
        #GLOW_PARTICLES.append(Particle(mx, my, [random.uniform(-2,2),random.uniform(-2,2)], 0, 5, 5, 5, [255,255,255], [50,0,0], 0.1, 3, 0.5))
        
        display.fill((0,0,100))

        #0.5*display.y - player.img.y*0.5 = 267 for offset to center the player #0.5*display.x - player.img.x*0.5 = 491 for offset to center the player
        true_scroll = [true_scroll[0] + ((int(PLAYER.pos[0])-true_scroll[0]-244)/15) * delta_time, true_scroll[1] + ((int(PLAYER.pos[1])-true_scroll[1]-144)/15) * delta_time]
        if true_scroll[0] < 0: true_scroll[0] = 0
        if true_scroll[0] > 500: true_scroll[0] = 500
        if true_scroll[1] > -280: true_scroll[1] = -280
        if true_scroll[1] < -330: true_scroll[1] = -330
        true_scroll[1] = -280
        scroll = [int(true_scroll[0]) + random.randint(-int(screen_shake*100),int(screen_shake*100))/100, int(true_scroll[1]) + random.randint(-int(screen_shake*100),int(screen_shake*100))/100]

        #if true_scroll[0] < 0: true_scroll[0] = 0

        if screen_shake > 0: screen_shake -= 0.025
        if screen_shake < 0: screen_shake = 0

        angle = -(180 / math.pi) * -math.atan2((mx-(PLAYER.pos[0]+24-scroll[0])), (my-(PLAYER.pos[1]+12-scroll[1])))

        for decoration in DECORATIONS:
            if ONSREEN(decoration[1][0]-scroll[0],decoration[1][1]-scroll[1], decoration[0].get_width(), decoration[0].get_height()):
                display.blit(decoration[0],(decoration[1][0]-scroll[0],decoration[1][1]-scroll[1]))

        PLAYER.main(display, TILES, delta_time, scroll, int(angle))
        if show_hat == "witch": display.blit(WITCH_HAT_IMG,(PLAYER.body.x-9-scroll[0],PLAYER.body.y-25-scroll[1]))
        elif show_hat == "top": display.blit(TOP_HAT_IMG,(PLAYER.body.x-3-scroll[0],PLAYER.body.y-20-scroll[1]))
        
        img_copy = pygame.transform.rotate(WAND_IMG, angle+220)
        display.blit(img_copy, ((PLAYER.body.x+24) - int(img_copy.get_width() / 2) - scroll[0], (PLAYER.body.y+12) - int(img_copy.get_height() / 2) - scroll[1]))

        for i,candy in sorted(enumerate(CANDY),reverse=True):
            if candy.colliderect(PLAYER.body):
                pygame.mixer.Sound.play(sounds[8])
                candy_timer = time.time()
                if difficulty == "Hard":
                    if LIVES < 3: LIVES += 1
                else:
                    if LIVES < 6: LIVES += 1
                CANDY.remove(candy)
                for i in range(25):
                    NORMAL_PARTICLES.append(Particle(int(PLAYER.pos[0])+12, int(PLAYER.pos[1])+12, [random.randint(-100,100)/100,random.randint(-100,100)/100], 0.1, 3, 3, 0, random.choice([[255,255,0],[255,255,255],[255,125,0]]), [0,0,0], random.randint(20,40)/1000, 0, 1))
                #for i in range(25):
                    #GLOW_PARTICLES.append(Particle(int(PLAYER.pos[0])+12+random.randint(-5,5), int(PLAYER.pos[1])+20+random.randint(-5,5), [random.randint(-50,50)/100,random.randint(-50,50)/100], 0, random.randint(2,4), 3, 3, [255,255,255], [10,2,2], random.randint(20,40)/1000, 3, 1))
            else: 
                display.blit(HEAL_IMG, (candy.x-scroll[0], candy.y-scroll[1]))
                    
        for TILE in TILES[3:]:
            if ONSREEN(TILE.x-scroll[0], TILE.y-scroll[1], TILE.w, TILE.h):
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(TILE.x-scroll[0], TILE.y-scroll[1], TILE.w, TILE.h))

        for i,particle in sorted(enumerate(NORMAL_PARTICLES),reverse=True):
            render = ONSREEN((particle.x-particle.glow_size*6+particle.length/2)-scroll[0],(particle.y-particle.glow_size*6+particle.length/2)-scroll[1], particle.length*2, particle.length*2)
            temp = particle.main(display, delta_time, scroll, render)
            if temp == 0:
                NORMAL_PARTICLES.remove(particle)
                del particle

        for i,enemy in sorted(enumerate(ENEMYS),reverse=True):
            if enemy.playercollider.colliderect(PLAYER.body):
                pygame.mixer.Sound.play(sounds[13])
                clear = True
            if ONSREEN(enemy.body.x-scroll[0], enemy.body.y-scroll[1], enemy.body.w, enemy.body.h):
                temp = enemy.main(display, delta_time, scroll, PLAYER.body.x, PLAYER.body.y, True)
            else:
                temp = enemy.main(display, delta_time, scroll, PLAYER.body.x, PLAYER.body.y, False)

            if temp:
                for i in range(25):
                    GLOW_PARTICLES.append(Particle(int(enemy.pos[0])+12+random.randint(-5,5), int(enemy.pos[1])+20+random.randint(-5,5), [random.randint(-50,50)/100,random.randint(-50,50)/100], 0, random.randint(2,4), 3, 3, [255,255,255], [2,2,10], random.randint(20,40)/1000, 3, 1))
                ENEMYS.remove(enemy)
                del enemy
                score += 1

                #ENEMYS = [Enemy(100, -340, ENEMY_IMG, 24, 40)]

        if clear == True:
            clear = False
            PLAYER.pos = [340, -144]
            for i in range(25):
                NORMAL_PARTICLES.append(Particle(int(PLAYER.pos[0])+12, int(PLAYER.pos[1])+12, [random.randint(-100,100)/100,random.randint(-100,100)/100], 0.1, 3, 3, 0, random.choice([[255,255,0],[255,255,255],[255,125,0]]), [0,0,0], random.randint(20,40)/1000, 0, 1))
            LIVES -= 1
            for i,enemy in sorted(enumerate(ENEMYS),reverse=True):
                ENEMYS.remove(enemy)
                del enemy

        display.blit(DARKEN([500,300], [10,10,10]),(0,0))

        for i,orb in sorted(enumerate(ORBS),reverse=True):
                temp = orb.main(display, ENEMYS, delta_time, scroll)
                if delta_counter > 1:
                    for i in range(5):
                        GLOW_PARTICLES.append(Particle(orb.body.x+3+random.randint(-2,2), orb.body.y+3+random.randint(-2,2), [0,0], 0, 5, 5, 5, [255,255,255], [random.randint(5,35)]*3, random.randint(30,40)/50, 1, 1))
                if temp:
                    for i in range(10):
                        GLOW_PARTICLES.append(Particle(orb.body.x+3, orb.body.y+3, [random.randint(-50,50)/50,random.randint(-50,50)/50], 0, 5, 5, 6, [255,255,255], [random.randint(5,35)]*3, random.randint(30,40)/250, 1, 1))
                    ORBS.remove(orb)
                    del orb
                    pygame.mixer.Sound.play(sounds[11])
                else:
                    for enemy in ENEMYS:
                        if orb.body.colliderect(enemy.body):
                            orb.dead = True
                            enemy.hit(34)
                    if orb.dead == True:
                        for i in range(15):
                            GLOW_PARTICLES.append(Particle(orb.body.x+3, orb.body.y+3, [random.randint(-50,50)/50,random.randint(-50,50)/50], 0, 5, 5, 6, [255,255,255], [random.randint(5,35)]*3, random.randint(30,40)/250, 1, 1))
                        ORBS.remove(orb)
                        del orb
                        screen_shake = 1
                        pygame.mixer.Sound.play(sounds[11])

        for i,ball in sorted(enumerate(BALLS),reverse=True):
                temp = ball.main(display, TILES, delta_time, scroll, sounds[10])
                if delta_counter > 1:
                    for i in range(5):
                        GLOW_PARTICLES.append(Particle(ball.body.x+3+random.randint(-2,2), ball.body.y+3+random.randint(-2,2), [0,0], 0, 5, 5, 5, [255,255,255], [random.randint(5,35),5,35], random.randint(30,40)/50, 1, 1))
                if temp:
                    pygame.mixer.Sound.play(sounds[3])
                    for i in range(25):
                        GLOW_PARTICLES.append(Particle(ball.body.x+3, ball.body.y+3, [random.randint(-50,50)/50,random.randint(-50,50)/50], 0, 5, 5, 5, [255,255,255], [random.randint(5,35),5,35], random.randint(30,40)/250, 1, 1))
                    BALLS.remove(ball)
                    del ball
                    screen_shake = 1
                else:
                    for enemy in ENEMYS:
                        if ball.body.colliderect(enemy.body):
                            ball.dead = True
                            enemy.hit(50)
                            pygame.mixer.Sound.play(sounds[1])

        for i,ball in sorted(enumerate(FIRE_BALLS),reverse=True):
                temp = ball.main(display, TILES, delta_time, scroll)
                if delta_counter > 1:
                    for i in range(5):
                        GLOW_PARTICLES.append(Particle(ball.body.x+5+random.randint(-5,5), ball.body.y+5+random.randint(-5,5), [0, random.randint(-50,0)/100], 0, 9, 9, 7, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/50, 1, 1))
                if temp:
                    pygame.mixer.Sound.play(sounds[7])
                    for i in range(25):
                        GLOW_PARTICLES.append(Particle(ball.body.x+6, ball.body.y+6, [random.randint(-150,150)/75, random.randint(-200,25)/75], 0.1, 6, 6, 6, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/250, 1, 1))
                    FIRE_BALLS.remove(ball)
                    del ball
                    screen_shake = 1
                else:
                    for enemy in ENEMYS:
                        if ball.body.colliderect(enemy.body):
                            ball.dead = True
                            enemy.hit(100)
                            pygame.mixer.Sound.play(sounds[1])

        if BOLTS_TIMER > 0:
            BOLTS_TIMER -= 1
            for bolt in BOLTS:
                if ONSREEN(bolt[1][0]-scroll[0],bolt[1][1]-scroll[1], 30, 300):
                    display.blit(bolt[0],(bolt[1][0]-scroll[0],bolt[1][1]-scroll[1]))

        for i,particle in sorted(enumerate(CANDLE_PARTICLES),reverse=True):
            render = ONSREEN((particle.x-particle.glow_size*6+(particle.length*0.5))-scroll[0],(particle.y-particle.glow_size*6+(particle.length*0.5))-scroll[1], (particle.glow_size*6+particle.length/2)*2, (particle.glow_size*6+particle.length/2)*2)
            temp = particle.main(display, delta_time, scroll, render)
            if temp == 0:
                CANDLE_PARTICLES.remove(particle)
                del particle

        for i,particle in sorted(enumerate(GLOW_PARTICLES),reverse=True):
            render = ONSREEN((particle.x-particle.glow_size*6+(particle.length*0.5))-scroll[0],(particle.y-particle.glow_size*6+(particle.length*0.5))-scroll[1], (particle.glow_size*6+particle.length/2)*2, (particle.glow_size*6+particle.length/2)*2)
            temp = particle.main(display, delta_time, scroll, render)
            if temp == 0:
                GLOW_PARTICLES.remove(particle)
                del particle
                
        if spell:
            for i in range(20):
                if delta_counter >= 1:
                    GLOW_PARTICLES.append(Particle(int(PLAYER.pos[0])+18-15 * math.cos(math.radians(angle+90)), int(PLAYER.pos[1])+18+15 * math.sin(math.radians(angle+90)), [-2.5 * math.cos(math.radians(angle+90))+random.randint(-6,6)/10, 2.5 * math.sin(math.radians(angle+90))+random.randint(-6,6)/10], 0, 5, 5, 4, [255,255,255], [35,random.randint(0,35),5], random.randint(20,40)/1000, 3, 1))

        display.blit(HEAL_IMG1, (450,5))
        body.render("x "+str(LIVES), display, (475, 10))

        if (time.time() - candy_timer) > 20:
            if len(CANDY) == 0:
                temp = pygame.Rect(0, 0, 26, 32)
                Run = True
                while Run:
                    Run = False
                    for tile in TILES:
                        if temp.colliderect(tile):
                            temp.x = random.randint(0,950)
                            temp.y = random.randint(-250,0)
                            Run = True

                CANDY.append(temp)

                for i in range(25):
                    NORMAL_PARTICLES.append(Particle(temp.x+13, temp.y+16, [random.randint(-100,100)/100,random.randint(-100,100)/100], 0.1, 3, 3, 0, random.choice([[255,255,0],[255,255,255],[255,125,0]]), [0,0,0], random.randint(20,40)/1000, 0, 1))

        if (time.time() - ult_timer) > 15:
            if CANDLE_PARTICLES[0].glow_color == [50,35,2]:
                for i in CANDLE_PARTICLES:
                    i.glow_color = [2,35,50]
            
            if delta_counter > 1:
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, -97, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, -93, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, -137, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, -133, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(891+random.randint(-20,20)/10, -17, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(903+random.randint(-20,20)/10, -13, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(625+random.randint(-20,20)/10, -224, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(637+random.randint(-20,20)/10, -220, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [5,random.randint(5,35),35], random.randint(30,40)/500, 3, 1))

        else:
            if CANDLE_PARTICLES[0].glow_color == [2,35,50]:
                for i in CANDLE_PARTICLES:
                    i.glow_color = [50,35,2]
                    
            if delta_counter > 1:
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, -97, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, -93, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, -137, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, -133, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(891+random.randint(-20,20)/10, -17, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(903+random.randint(-20,20)/10, -13, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: CANDLE_PARTICLES.append(Particle(625+random.randint(-20,20)/10, -224, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
                if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(637+random.randint(-20,20)/10, -220, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))


        if (time.time() - enemy_timer) > enemy_spawn_len:
            enemy_timer = time.time()
            if enemy_spawn_len > 1: enemy_spawn_len -= 1
            num = 1024 if random.randint(1,2) == 1 else -24
            if difficulty == "Easy": ENEMYS.append(Enemy(num, random.randint(-340, 40), ENEMY_IMG, 24, 40, False))
            if difficulty == "Hard": ENEMYS.append(Enemy(num, random.randint(-340, 40), ENEMY_IMG, 24, 40, True))
                    
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if attack == 1 and len(FIRE_BALLS) < 3:
                        pygame.mixer.Sound.play(sounds[2])
                        FIRE_BALLS.append(Fireball(PLAYER.body.x+15, PLAYER.body.y+3, 18, 18, angle))
                        screen_shake = 1
                        
                    if attack == 2 and len(BALLS) < 5:
                        pygame.mixer.Sound.play(sounds[6])
                        BALLS.append(Ball(PLAYER.body.x+21, PLAYER.body.y+9, 6, 6, angle))
                        screen_shake = 1

                    if attack == 3 and len(ORBS) < 6:
                        for i in range(3):
                            ORBS.append(Orb(PLAYER.body.x+21, PLAYER.body.y+9, 6, 6, angle-10+(10*i)))
                        screen_shake = 1
                        pygame.mixer.Sound.play(sounds[12])
                            
                if event.button == 2:
                    for i in ENEMYS:
                        i.hit(110)

                if event.button == 5:
                    pygame.mixer.Sound.play(sounds[9])
                    if attack > 1: attack -= 1
                    else: attack = 3
                    
                if event.button == 4:
                    pygame.mixer.Sound.play(sounds[9])
                    if attack < 3: attack += 1
                    else: attack = 1
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    spell = False
                if event.button == 3:
                    pygame.mixer.Sound.play(sounds[4])
                    
                    PLAYER.pos[0] = mx + scroll[0] - 12
                    PLAYER.pos[1] = my + scroll[1] - 12

                    if PLAYER.pos[0] < 0: PLAYER.pos[0] = 0
                    if PLAYER.pos[0] > 976: PLAYER.pos[0] = 976
                    if PLAYER.pos[1] < -1000: PLAYER.pos[1] = -1000
                    if PLAYER.pos[1] > -24: PLAYER.pos[1] = -24
                    
                    PLAYER.movement[1] = 0
                    for i in range(50):
                        GLOW_PARTICLES.append(Particle(int(PLAYER.pos[0]+12), int(PLAYER.pos[1]+12), [random.randint(-80,80)/50,random.randint(-120,80)/50], 0.1, random.randint(2,3), 3, 3, [255,255,255], [25,2,2], random.randint(20,40)/1000, 3, 1))

                
            if event.type == KEYDOWN:
                
                if event.key == K_ESCAPE:
                    if Paused(): loop = 0

                if event.key == K_e:
                    if len(ENEMYS) > 0 and (time.time() - ult_timer) > 15:
                        pygame.mixer.Sound.play(sounds[0])
                        ult_timer = time.time()
                        BOLTS = []
                        BOLTS_TIMER = 10
                        screen_shake = 3
                        for i in ENEMYS:
                            BOLTS.append([BOLT_IMG, [i.body.x+12, i.body.y-288]])
                            i.hit(210)
                    
                if event.key == K_d:
                    PLAYER.movement[0] = 1.75
                    
                if event.key == K_a:
                    PLAYER.movement[0] = -1.75
                    
                if event.key == K_SPACE:
                    if PLAYER.jumps > 0:
                        pygame.mixer.Sound.play(sounds[5])
                        PLAYER.movement[1] = -2
                        PLAYER.jumps -= 1

                if event.key == K_1:
                    pygame.mixer.Sound.play(sounds[9])
                    attack = 1

                if event.key == K_2:
                    pygame.mixer.Sound.play(sounds[9])
                    attack = 2

                if event.key == K_3:
                    pygame.mixer.Sound.play(sounds[9])
                    attack = 3
                    
            if event.type == KEYUP:
                
                if event.key == K_d:
                    if PLAYER.movement[0] == 1.75: PLAYER.movement[0] = 0
                        
                if event.key == K_a:
                    if PLAYER.movement[0] == -1.75: PLAYER.movement[0] = 0

        if show_fps == "True": body.render("FPS: "+str(int(clock.get_fps())), display, (100, 10))
        body.render("Score: "+str(score), display, (10, 10))
        #body.render(str(int(angle)), display, (125, 25))
        #body.render(str(len(ENEMYS)), display, (125, 25))
        #body.render("Num_Particles: "+str(len(GLOW_PARTICLES)), display, (200, 10))
        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(mx-2, my-2, 4, 4))

        fps_avg.append(int(clock.get_fps()))
        fps_avg.remove(fps_avg[0])
        #body.render(str(int(sum(fps_avg)/75)), display, (175, 25))

        if delta_counter > 1: delta_counter = 0

        surf = pygame.transform.scale(display, screen_size)
        try:
            screen.blit(surf,(0,0))
            if loop: pygame.display.update()
        except: pass
        
        if LIVES < 1:
            loop = 0
            Dead(score)

def Multiplayer():
    pass

def Dead(score):
    global last_time, fps, delta_fps, difficulty, show_fps, high_score_hard, high_score_easy, music_volume, sound_volume

    save = {"highscorehard":high_score_hard, "highscoreeasy":high_score_easy, "musicvolume":music_volume, "soundvolume":sound_volume}
    file = open("DATA//data.pkl", "wb")
    pickle.dump(save, file)
    file.close()
    
    MAIN_MENU_BUTTON = pygame.Rect(170, 220, 150, 26)

    BLACK_BOX = pygame.Rect(125, 0, 250, 300)
    WHITE_LINE = pygame.Rect(125, -5, 250, 310)

    LINE = pygame.Rect(160, 107, 177, 1)
    TIME_STEP = 0

    GLOW_PARTICLES, delta_counter = [], 0
    
    while 1:

        clock.tick(fps)

        delta_time = time.time() - last_time
        delta_time *= delta_fps
        last_time = time.time()

        screen.fill((0,0,0))
        display.fill((0,0,100))

        #-----
        display.blit(BG_IMG, (0,0))

        delta_counter += delta_time

        if delta_counter > 1:
            delta_counter = 0

            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, 183, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, 187, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, 143, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, 147, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            
        for i,particle in sorted(enumerate(GLOW_PARTICLES),reverse=True):
            temp = particle.main(display, delta_time, [0,0], True)
            if temp == 0:
                GLOW_PARTICLES.remove(particle)
                del particle     
        #-----

        pygame.draw.rect(display, (0, 0, 0), BLACK_BOX)
        pygame.draw.rect(display, (255, 255, 255), WHITE_LINE, 1)

        if TIME_STEP ** 2 / 4 < 255: TIME_STEP += delta_time
        display.set_alpha(TIME_STEP ** 2 / 4)

        mx, my = int(pygame.mouse.get_pos()[0] / scale[0]), int(pygame.mouse.get_pos()[1] / scale[1])

        if MAIN_MENU_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), MAIN_MENU_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), MAIN_MENU_BUTTON, width=1, border_radius=5)

        pygame.draw.rect(display, (255, 255, 255), LINE)
        
        title.render("You Died", display, (190, 60))
        body.render("Score: "+str(score), display, (225, 137))
        if difficulty == "Easy": body.render("Highscore: "+str(high_score_easy), display, (215, 167))
        if difficulty == "Hard": body.render("Highscore: "+str(high_score_hard), display, (215, 167))
        body.render("Difficulty: "+difficulty, display, (203, 197))
        body.render("Main Menu", display, (213, 227))

        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(mx-2, my-2, 4, 4))

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:

                    if MAIN_MENU_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        return True

        surf = pygame.transform.scale(display, screen_size)
        try:
            screen.blit(surf,(0,0))
            pygame.display.update()
        except: pass

def Paused():
    global last_time, fps, delta_fps, difficulty, show_fps, high_score_hard, high_score_easy, music_volume, sound_volume

    save = {"highscorehard":high_score_hard, "highscoreeasy":high_score_easy, "musicvolume":music_volume, "soundvolume":sound_volume}
    file = open("DATA//data.pkl", "wb")
    pickle.dump(save, file)
    file.close()
    
    RESUME_BUTTON = pygame.Rect(170, 130, 150, 26)
    OPTIONS_BUTTON = pygame.Rect(170, 160, 150, 26)
    MAIN_MENU_BUTTON = pygame.Rect(170, 190, 150, 26)

    BLACK_BOX = pygame.Rect(125, 0, 250, 300)
    WHITE_LINE = pygame.Rect(125, -5, 250, 310)

    LINE = pygame.Rect(160, 107, 177, 1)
    TIME_STEP = 0

    GLOW_PARTICLES, delta_counter = [], 0
    
    while 1:

        clock.tick(fps)

        delta_time = time.time() - last_time
        delta_time *= delta_fps
        last_time = time.time()

        screen.fill((0,0,0))
        display.fill((0,0,100))

        #-----
        display.blit(BG_IMG, (0,0))

        delta_counter += delta_time

        if delta_counter > 1:
            delta_counter = 0

            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(80+random.randint(-20,20)/10, 183, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(92+random.randint(-20,20)/10, 187, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(425+random.randint(-20,20)/10, 143, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            if random.randint(1,2) == 2: GLOW_PARTICLES.append(Particle(437+random.randint(-20,20)/10, 147, [0, random.randint(-50,0)/100], 0, 3, 3, 2, [255,255,255], [35,random.randint(5,35),5], random.randint(30,40)/500, 3, 1))
            
        for i,particle in sorted(enumerate(GLOW_PARTICLES),reverse=True):
            temp = particle.main(display, delta_time, [0,0], True)
            if temp == 0:
                GLOW_PARTICLES.remove(particle)
                del particle     
        #-----

        pygame.draw.rect(display, (0, 0, 0), BLACK_BOX)
        pygame.draw.rect(display, (255, 255, 255), WHITE_LINE, 1)

        if TIME_STEP ** 2 / 4 < 255: TIME_STEP += delta_time
        display.set_alpha(TIME_STEP ** 2 / 4)

        mx, my = int(pygame.mouse.get_pos()[0] / scale[0]), int(pygame.mouse.get_pos()[1] / scale[1])

        if RESUME_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), RESUME_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), RESUME_BUTTON, width=1, border_radius=5)

        if OPTIONS_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), OPTIONS_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), OPTIONS_BUTTON, width=1, border_radius=5)

        if MAIN_MENU_BUTTON.collidepoint((mx,my)): pygame.draw.rect(display, (55, 55, 55), MAIN_MENU_BUTTON, border_radius=5)
        pygame.draw.rect(display, (255, 255, 255), MAIN_MENU_BUTTON, width=1, border_radius=5)

        pygame.draw.rect(display, (255, 255, 255), LINE)
        
        title.render("Paused", display, (200, 60))
        body.render("Resume", display, (225, 137))
        body.render("Options", display, (225, 167))
        body.render("Main Menu", display, (213, 197))

        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(mx-2, my-2, 4, 4))

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    if RESUME_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        return False

                    if OPTIONS_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        TIME_STEP = 0
                        Options_Menu(False)

                    if MAIN_MENU_BUTTON.collidepoint((mx,my)):
                        display.set_alpha(255)
                        return True

        surf = pygame.transform.scale(display, screen_size)
        try:
            screen.blit(surf,(0,0))
            pygame.display.update()
        except: pass

Main_Menu()
