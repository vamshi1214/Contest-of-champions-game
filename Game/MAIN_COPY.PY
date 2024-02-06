from pickle import FALSE
from numpy import true_divide
import pygame
import button
from pygame import mixer
import random
pygame.init()
mixer.init()
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CONTEST OF CHAMPIONS')
clock = pygame.time.Clock()
FPS = 12

p1_maxhealth=500
p2_maxhealth=500
health_p1=500
health_p2=500
p1moving_left = False
p1moving_right = False
p1punch=False
p1punch_up=False
p1punch_down=False
p1punch_jump=False
p1punch_dash=False
p1punch_clap=False
p1punch_slap=False
p1Idle=True

p2Idle=True
p2moving_left = False
p2moving_right = False
p2straight_punch=False
p2right_punch=False
p2left_punch=False
p2up_punch=False
p2kick_up=False
p2kick_down=False
p2dash=False
p2death=False

x=100
y=100
x2=1000
y2=100
a=random.randint(0,3)
p1_hurt = pygame.mixer.Sound(r'Game\audio\2.mp3')
p1_hurt.set_volume(0.05)

BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
  
pygame.mixer.music.load(r'C:\PYTHON\VAMSHI\Game\audio\music.mp3')
pygame.mixer.music.set_volume(10)
pygame.mixer.music.play(-1, 0.0, 5000)

start_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/exit_btn.png').convert_alpha()
restart_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/restart_btn.png').convert_alpha()

start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)

hulk_won = pygame.image.load(r'C:\PYTHON\VAMSHI\Game\img\WON_img\hulk won ph.png').convert_alpha()
hulk_won = pygame.transform.scale(hulk_won , (1300,600))
blade_won=pygame.image.load(r'C:\PYTHON\VAMSHI\Game\img\WON_img\Blade won ph.png').convert_alpha()
blade_won = pygame.transform.scale(blade_won , (400,600))
#####score images
########P1
p1hulk = pygame.image.load(r'C:\PYTHON\VAMSHI\Game\img/score1.jpg').convert_alpha()
p1hulk = pygame.transform.scale(p1hulk , (80,80))
########p2
p2blade = pygame.image.load(r'C:\PYTHON\VAMSHI\Game\img/blade2.jpg').convert_alpha()
p2blade = pygame.transform.scale(p2blade , (80,80))

p1idle_0 = pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/IDLE/0.png').convert_alpha()
p1idle_0 = pygame.transform.scale(p1idle_0 , (x,y))
p1idle_0_rect=p1idle_0.get_rect()
p1idle_1= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/IDLE/1.png').convert_alpha()
p1idle_1 = pygame.transform.scale(p1idle_1 , (x,y))

p1Run_0= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/0.png').convert_alpha()
p1Run_0 = pygame.transform.scale(p1Run_0 , (x,y))
p1Run_1= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/1.png').convert_alpha()
p1Run_1 = pygame.transform.scale(p1Run_1 , (x,y))
p1Run_2= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/2.png').convert_alpha()
p1Run_2 = pygame.transform.scale(p1Run_2 , (x,y))
p1Run_3= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/3.png').convert_alpha()
p1Run_3 = pygame.transform.scale(p1Run_3 , (x,y))
p1Run_4= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/4.png').convert_alpha()
p1Run_4 = pygame.transform.scale(p1Run_4 , (x,y))
p1Run_5= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/5.png').convert_alpha()
p1Run_5 = pygame.transform.scale(p1Run_5 , (x,y))
p1Run_6= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/6.png').convert_alpha()
p1Run_6 = pygame.transform.scale(p1Run_6 , (x,y))
p1Run_7= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/7.png').convert_alpha()
p1Run_7 = pygame.transform.scale(p1Run_7 , (x,y))


p1Run_r0= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/0.png').convert_alpha()
p1Run_r0 = pygame.transform.scale(p1Run_r0 , (x,y))
p1Run_r1= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/1.png').convert_alpha()
p1Run_r1 = pygame.transform.scale(p1Run_r1 , (x,y))
p1Run_r2= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/2.png').convert_alpha()
p1Run_r2 = pygame.transform.scale(p1Run_r2 , (x,y))
p1Run_r3= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/3.png').convert_alpha()
p1Run_r3 = pygame.transform.scale(p1Run_r3 , (x,y))
p1Run_r4= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/4.png').convert_alpha()
p1Run_r4= pygame.transform.scale(p1Run_r4 , (x,y))
p1Run_r5= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/5.png').convert_alpha()
p1Run_r5 = pygame.transform.scale(p1Run_r5 , (x,y))
p1Run_r6= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/6.png').convert_alpha()
p1Run_r6 = pygame.transform.scale(p1Run_r6 , (x,y))
p1Run_r7= pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/RUN/7.png').convert_alpha()
p1Run_r7 = pygame.transform.scale(p1Run_r7 , (x,y))

p1punch_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/HARDPUNCH/0.png').convert_alpha()
p1punch_0 = pygame.transform.scale(p1punch_0 , (x,y))
p1punch_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/HARDPUNCH/1.png').convert_alpha()
p1punch_1 = pygame.transform.scale(p1punch_1 , (x,y))
p1punch_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/HARDPUNCH/2.png').convert_alpha()
p1punch_2 = pygame.transform.scale(p1punch_2 , (x,y))
p1punch_3=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/HARDPUNCH/3.png').convert_alpha()
p1punch_3 = pygame.transform.scale(p1punch_3 , (x,y))
p1punch_4=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/HARDPUNCH/4.png').convert_alpha()
p1punch_4 = pygame.transform.scale(p1punch_4 , (x,y))

p1punch_up_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHUP/0.png').convert_alpha()
p1punch_up_0 = pygame.transform.scale(p1punch_up_0 , (x,y))
p1punch_up_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHUP/1.png').convert_alpha()
p1punch_up_1 = pygame.transform.scale(p1punch_up_1 , (x,y))
p1punch_up_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHUP/2.png').convert_alpha()
p1punch_up_2 = pygame.transform.scale(p1punch_up_2 , (x,y))
p1punch_up_3=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHUP/3.png').convert_alpha()
p1punch_up_3 = pygame.transform.scale(p1punch_up_3 , (x,y))
p1punch_up_4=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHUP/4.png').convert_alpha()
p1punch_up_4 = pygame.transform.scale(p1punch_up_4 , (x,y))

p1punch_down_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHDOWN/0.png').convert_alpha()
p1punch_down_0 = pygame.transform.scale(p1punch_down_0 , (x,y))
p1punch_down_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHDOWN/1.png').convert_alpha()
p1punch_down_1 = pygame.transform.scale(p1punch_down_1 , (x,y))
p1punch_down_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/PUNCHDOWN/2.png').convert_alpha()
p1punch_down_2 = pygame.transform.scale(p1punch_down_2 , (x,y))

p1punch_jump_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/JUMPPUNCH/0.png').convert_alpha()
p1punch_jump_0 = pygame.transform.scale(p1punch_jump_0 , (x,y))
p1punch_jump_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/JUMPPUNCH/1.png').convert_alpha()
p1punch_jump_1 = pygame.transform.scale(p1punch_jump_1 , (x,y))
p1punch_jump_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/JUMPPUNCH/2.png').convert_alpha()
p1punch_jump_2 = pygame.transform.scale(p1punch_jump_2 , (x,y))
p1punch_jump_3=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/JUMPPUNCH/3.png').convert_alpha()
p1punch_jump_3 = pygame.transform.scale(p1punch_jump_3 , (x,y))
p1punch_jump_4=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/JUMPPUNCH/4.png').convert_alpha()
p1punch_jump_4 = pygame.transform.scale(p1punch_jump_4 , (x,y))

p1punch_dash_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/0.png').convert_alpha()
p1punch_dash_0 = pygame.transform.scale(p1punch_dash_0 , (x,y))
p1punch_dash_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/1.png').convert_alpha()
p1punch_dash_1 = pygame.transform.scale(p1punch_dash_1 , (x,y))
p1punch_dash_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/2.png').convert_alpha()
p1punch_dash_2 = pygame.transform.scale(p1punch_dash_2 , (x,y))
p1punch_dash_3=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/3.png').convert_alpha()
p1punch_dash_3 = pygame.transform.scale(p1punch_dash_3 , (x,y))
p1punch_dash_4=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/4.png').convert_alpha()
p1punch_dash_4 = pygame.transform.scale(p1punch_dash_4 , (x,y))
p1punch_dash_5=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/5.png').convert_alpha()
p1punch_dash_5 = pygame.transform.scale(p1punch_dash_5 , (x,y))
p1punch_dash_6=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/6.png').convert_alpha()
p1punch_dash_6 = pygame.transform.scale(p1punch_dash_6 , (x,y))
p1punch_dash_7=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/DASH/7.png').convert_alpha()
p1punch_dash_7 = pygame.transform.scale(p1punch_dash_7 , (x,y))

p1punch_slap_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/SLAP/0.png').convert_alpha()
p1punch_slap_0 = pygame.transform.scale(p1punch_slap_0 , (x,y))
p1punch_slap_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/SLAP/1.png').convert_alpha()
p1punch_slap_1 = pygame.transform.scale(p1punch_slap_1 , (x,y))
p1punch_slap_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/SLAP/2.png').convert_alpha()
p1punch_slap_2 = pygame.transform.scale(p1punch_slap_2 , (x,y))

p1punch_clap_0=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/CLAP/0.png').convert_alpha()
p1punch_clap_0 = pygame.transform.scale(p1punch_clap_0 , (x,y))
p1punch_clap_1=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/CLAP/1.png').convert_alpha()
p1punch_clap_1 = pygame.transform.scale(p1punch_clap_1 , (x,y)) 
p1punch_clap_2=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/CLAP/2.png').convert_alpha()
p1punch_clap_2 = pygame.transform.scale(p1punch_clap_2 , (x,y)) 
p1punch_clap_3=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/CLAP/3.png').convert_alpha()
p1punch_clap_3 = pygame.transform.scale(p1punch_clap_3 , (x,y)) 
p1punch_clap_4=pygame.image.load('C:/Users/CS5/Desktop/HULK/SEP_IMAGES/CLAP/4.png').convert_alpha()
p1punch_clap_4 = pygame.transform.scale(p1punch_clap_4 , (x,y))                

p2idle_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/IDLE/0.png').convert_alpha()
p2idle_0 = pygame.transform.scale(p2idle_0 , (x,y))
p2idle_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/IDLE/1.png').convert_alpha()
p2idle_1 = pygame.transform.scale(p2idle_1 , (x,y))

p2run_0   = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/0.png').convert_alpha()
p2run_0 = pygame.transform.scale(p2run_0 , (x,y))
p2run_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/1.png').convert_alpha()
p2run_1 = pygame.transform.scale(p2run_1 , (x,y))
p2run_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/2.png').convert_alpha()
p2run_2 = pygame.transform.scale(p2run_2 , (x,y))
p2run_3= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/3.png').convert_alpha()
p2run_3 = pygame.transform.scale(p2run_3 , (x,y))
p2run_4= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/4.png').convert_alpha()
p2run_4 = pygame.transform.scale(p2run_4 , (x,y))
p2run_5= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RUN/5.png').convert_alpha()
p2run_5 = pygame.transform.scale(p2run_5 , (x,y))

p2straight_punch_0   = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/STRAIGHT_PUNCH/0.png').convert_alpha()
p2straight_punch_0 = pygame.transform.scale(p2straight_punch_0 , (x,y))
p2straight_punch_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/STRAIGHT_PUNCH/1.png').convert_alpha()
p2straight_punch_1  = pygame.transform.scale(p2straight_punch_1  , (x,y))

p2right_punch_0  = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RIGHT_PUNCH/0.png').convert_alpha()
p2right_punch_0  = pygame.transform.scale(p2right_punch_0 , (x,y))
p2right_punch_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RIGHT_PUNCH/1.png').convert_alpha()
p2right_punch_1  = pygame.transform.scale(p2right_punch_1 , (x,y))
p2right_punch_2 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/RIGHT_PUNCH/2.png').convert_alpha()
p2right_punch_2  = pygame.transform.scale(p2right_punch_2 , (x,y))

p2left_punch_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/0.png').convert_alpha()
p2left_punch_0  = pygame.transform.scale(p2left_punch_0 , (x,y))
p2left_punch_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/1.png').convert_alpha()
p2left_punch_1  = pygame.transform.scale(p2left_punch_1 , (x,y))
p2left_punch_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/2.png').convert_alpha()
p2left_punch_2  = pygame.transform.scale(p2left_punch_2 , (x,y))
p2left_punch_3= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/3.png').convert_alpha()
p2left_punch_3  = pygame.transform.scale(p2left_punch_3 , (x,y))
p2left_punch_4= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/4.png').convert_alpha()
p2left_punch_4  = pygame.transform.scale(p2left_punch_4 , (x,y))
p2left_punch_5= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/5.png').convert_alpha()
p2left_punch_5  = pygame.transform.scale(p2left_punch_5 , (x,y))
p2left_punch_6= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/LEFT_PUNCH/6.png').convert_alpha()
p2left_punch_6  = pygame.transform.scale(p2left_punch_6 , (x,y))

p2up_punch_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/UP_PUNCH/0.png').convert_alpha()
p2up_punch_0  = pygame.transform.scale(p2up_punch_0 , (x,y))
p2up_punch_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/UP_PUNCH/1.png').convert_alpha()
p2up_punch_1  = pygame.transform.scale(p2up_punch_1 , (x,y))
p2up_punch_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/UP_PUNCH/2.png').convert_alpha()
p2up_punch_2  = pygame.transform.scale(p2up_punch_2 , (x,y))

p2kick_up_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/0.png').convert_alpha()
p2kick_up_0  = pygame.transform.scale(p2kick_up_0 , (x,y))
p2kick_up_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/1.png').convert_alpha()
p2kick_up_1  = pygame.transform.scale(p2kick_up_1 , (x,y))
p2kick_up_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/2.png').convert_alpha()
p2kick_up_2  = pygame.transform.scale(p2kick_up_2 , (x,y))
p2kick_up_3= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/3.png').convert_alpha()
p2kick_up_3  = pygame.transform.scale(p2kick_up_3 , (x,y))
p2kick_up_4= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/4.png').convert_alpha()
p2kick_up_4  = pygame.transform.scale(p2kick_up_4 , (x,y))
p2kick_up_5= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_UP/5.png').convert_alpha()
p2kick_up_5  = pygame.transform.scale(p2kick_up_5 , (x,y))

p2kick_down_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/0.png').convert_alpha()
p2kick_down_0  = pygame.transform.scale(p2kick_down_0 , (x,y))
p2kick_down_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/1.png').convert_alpha()
p2kick_down_1  = pygame.transform.scale(p2kick_down_1 , (x,y))
p2kick_down_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/2.png').convert_alpha()
p2kick_down_2  = pygame.transform.scale(p2kick_down_2 , (x,y))
p2kick_down_3= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/3.png').convert_alpha()
p2kick_down_3  = pygame.transform.scale(p2kick_down_3 , (x,y))
p2kick_down_4= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/4.png').convert_alpha()
p2kick_down_4  = pygame.transform.scale(p2kick_down_4 , (x,y))
p2kick_down_5= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/5.png').convert_alpha()
p2kick_down_5  = pygame.transform.scale(p2kick_down_5 , (x,y))
p2kick_down_6= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/6.png').convert_alpha()
p2kick_down_6  = pygame.transform.scale(p2kick_down_6 , (x,y))
p2kick_down_7= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/KICK_DOWN/7.png').convert_alpha()
p2kick_down_7  = pygame.transform.scale(p2kick_down_7 , (x,y))

p2dash_0 = pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/0.png').convert_alpha()
p2dash_0  = pygame.transform.scale(p2dash_0 , (x,y))
p2dash_1= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/1.png').convert_alpha()
p2dash_1  = pygame.transform.scale(p2dash_1 , (x,y))
p2dash_2= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/2.png').convert_alpha()
p2dash_2  = pygame.transform.scale(p2dash_2 , (x,y))
p2dash_3= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/3.png').convert_alpha()
p2dash_3  = pygame.transform.scale(p2dash_3 , (x,y))
p2dash_4= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/4.png').convert_alpha()
p2dash_4  = pygame.transform.scale(p2dash_4 , (x,y))
p2dash_5= pygame.image.load('C:/PYTHON/VAMSHI/BLADE/DASH/5.png').convert_alpha()
p2dash_5  = pygame.transform.scale(p2dash_5 , (x,y))

pine1_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/Background/'+str(a)+'.jpg').convert_alpha()
sky_img = pygame.image.load('C:/PYTHON/VAMSHI/Game/img/Background/sky_cloud.png').convert_alpha()

p1run_list=[]
p1run_list.append(p1Run_0)
p1run_list.append(p1Run_1)
p1run_list.append(p1Run_2)
p1run_list.append(p1Run_3)
p1run_list.append(p1Run_4)
p1run_list.append(p1Run_5)
p1run_list.append(p1Run_6)
p1run_list.append(p1Run_7)
p1run_index=0

p1run_list_reverse=[]
p1run_list_reverse.append(p1Run_r0)
p1run_list_reverse.append(p1Run_r1)
p1run_list_reverse.append(p1Run_r2)
p1run_list_reverse.append(p1Run_r3)
p1run_list_reverse.append(p1Run_r4)
p1run_list_reverse.append(p1Run_r5)
p1run_list_reverse.append(p1Run_r6)
p1run_list_reverse.append(p1Run_r7)
p1run_reverse_index=0

p1punch_list=[]
p1punch_list.append(p1punch_0)
p1punch_list.append(p1punch_1)
p1punch_list.append(p1punch_2)
p1punch_list.append(p1punch_3)
p1punch_list.append(p1punch_4)
p1punch_index=0

p1punch_up_list=[]
p1punch_up_list.append(p1punch_up_0)
p1punch_up_list.append(p1punch_up_1)
p1punch_up_list.append(p1punch_up_2)
p1punch_up_list.append(p1punch_up_3)
p1punch_up_list.append(p1punch_up_4)
p1punch_up_index=0

p1punch_down_list=[]
p1punch_down_list.append(p1punch_down_0)
p1punch_down_list.append(p1punch_down_1)
p1punch_down_list.append(p1punch_down_2)
p1punch_down_index=0

p1punch_jump_list=[]
p1punch_jump_list.append(p1punch_jump_0)
p1punch_jump_list.append(p1punch_jump_1)
p1punch_jump_list.append(p1punch_jump_2)
p1punch_jump_list.append(p1punch_jump_3)
p1punch_jump_list.append(p1punch_jump_4)
p1punch_jump_index=0

p1punch_dash_list=[]
p1punch_dash_list.append(p1punch_dash_0)
p1punch_dash_list.append(p1punch_dash_1)
p1punch_dash_list.append(p1punch_dash_2)
p1punch_dash_list.append(p1punch_dash_3)
p1punch_dash_list.append(p1punch_dash_4)
p1punch_dash_list.append(p1punch_dash_5)
p1punch_dash_list.append(p1punch_dash_6)
p1punch_dash_list.append(p1punch_dash_7)
p1punch_dash_index=0

p1punch_clap_list=[]
p1punch_clap_list.append(p1punch_clap_0)
p1punch_clap_list.append(p1punch_clap_1)
p1punch_clap_list.append(p1punch_clap_2)
p1punch_clap_list.append(p1punch_clap_3)
p1punch_clap_list.append(p1punch_clap_4)
p1punch_clap_index=0

p1punch_slap_list=[]
p1punch_slap_list.append(p1punch_slap_0)
p1punch_slap_list.append(p1punch_slap_1)
p1punch_slap_list.append(p1punch_slap_2)
p1punch_slap_index=0

p2idle_list=[]
p2idle_list.append(p2idle_0)
p2idle_index=0

p2run_list=[]
p2run_list.append(p2run_0 )
p2run_list.append(p2run_1)
p2run_list.append(p2run_2)
p2run_list.append(p2run_3)
p2run_list.append(p2run_4)
p2run_list.append(p2run_5)
p2run_index=0

p2straight_punch_list=[]
p2straight_punch_list.append(p2straight_punch_0 )
p2straight_punch_list.append(p2straight_punch_1)
p2straight_punch_index=0

p2right_punch_list=[]
p2right_punch_list.append(p2right_punch_0 )
p2right_punch_list.append(p2right_punch_1)
p2right_punch_list.append(p2right_punch_2)
p2right_punch_index=0

p2left_punch_list=[]
p2left_punch_list.append(p2left_punch_0 )
p2left_punch_list.append(p2left_punch_1)
p2left_punch_list.append(p2left_punch_2)
p2left_punch_list.append(p2left_punch_3)
p2left_punch_list.append(p2left_punch_4)
p2left_punch_list.append(p2left_punch_5)
p2left_punch_list.append(p2left_punch_6)
p2left_punch_index=0

p2up_punch_list=[]
p2up_punch_list.append(p2up_punch_0 )
p2up_punch_list.append(p2up_punch_1)
p2up_punch_list.append(p2up_punch_2)
p2up_punch_index=0

p2kick_up_list=[]
p2kick_up_list.append(p2kick_up_0 )
p2kick_up_list.append(p2kick_up_1)
p2kick_up_list.append(p2kick_up_2)
p2kick_up_list.append(p2kick_up_3)
p2kick_up_list.append(p2kick_up_4)
p2kick_up_list.append(p2kick_up_5)
p2kick_up_index=0

p2kick_down_list=[]
p2kick_down_list.append(p2kick_down_0 )
p2kick_down_list.append(p2kick_down_1)
p2kick_down_list.append(p2kick_down_2)
p2kick_down_list.append(p2kick_down_3)
p2kick_down_list.append(p2kick_down_4)
p2kick_down_list.append(p2kick_down_5)
p2kick_down_list.append(p2kick_down_6)
p2kick_down_list.append(p2kick_down_7)
p2kick_down_index=0

p2dash_list=[]
p2dash_list.append(p2dash_0 )
p2dash_list.append(p2dash_1)
p2dash_list.append(p2dash_2)
p2dash_list.append(p2dash_3)
p2dash_list.append(p2dash_4)
p2dash_list.append(p2dash_5)
p2dash_index=0

p1x = 0
p1y = 500
p2x=1100
p2y=500
p1idle_0_rect.bottomleft=(p1x,p1y)



run=True 
while run:
    clock.tick(FPS)
    screen.blit(mountain_img,(0,0))   
    ratio1 = health_p1 / p1_maxhealth
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 154, 24))
    pygame.draw.rect(screen, RED, (x, y, 150, 20))
    pygame.draw.rect(screen, GREEN, (x,y, 150 * ratio1, 20))
    ratio2 = health_p2 / p2_maxhealth
    pygame.draw.rect(screen, BLACK, (x2 - 2, y2 - 2, 154, 24))
    pygame.draw.rect(screen, RED, (x2, y2, 150, 20))
    pygame.draw.rect(screen, GREEN, (x2,y2, 150 * ratio2, 20))
    screen.blit(p1hulk,(x,y-80))
    screen.blit(p2blade,(x2,y-80))

    if health_p1 % 5==0 and health_p1<500 and p2Idle == FALSE:
        p1_hurt.play()
    if p1x<0:
        p1x=0
        p1moving_left=False
        p1Idle=True
    if p2x+100>1300:
        p2x=1200
        p2moving_right=False
        p2Idle=True     
    if p1Idle==True:
        screen.blit(p1idle_0,(p1x,p1y))
    if p2Idle==True:
        screen.blit(p2idle_list[p2idle_index],(p2x,p2y))
        p2idle_index+=1
        if p2idle_index>0:
            p2idle_index=0

    if p1moving_right==True:
        p1Idle=False
        p1x+=5
        screen.blit(p1run_list[p1run_index],(p1x,p1y))
        p1run_index+=1
        if p1run_index>7:
            p1run_index=0
        
    if p2moving_right==True:
        p2Idle=False
        p2x+=5
        screen.blit(p2run_list[p2run_index],(p2x,p2y))
        p2run_index+=1
        if p2run_index>5:
            p2run_index=0

    if p1moving_left==True:
        p1Idle=False
        p1x-=5
        screen.blit(p1run_list_reverse[p1run_reverse_index],(p1x,p1y))
        p1run_reverse_index+=1
        if p1run_reverse_index>7:
            p1run_reverse_index=0

    if p2moving_left==True:
        p2Idle=False
        p2x-=5
        screen.blit(p2run_list[p2run_index],(p2x,p2y))
        p2run_index+=1
        if p2run_index>5:
            p2run_index=0
            



    if p1punch_up==True:
        p1Idle=False
        screen.blit(p1punch_up_list[p1punch_up_index],(p1x,p1y))
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if p1punch_up_list[p1punch_up_index] == p1punch_up_list[2] or p1punch_up_list[3] or p1punch_list[p1punch_index] == p1punch_list[4]:
                health_p2-=10
        p1punch_up_index+=1
        if p1punch_up_index>4:
            p1punch_up_index=0
                

    if p2up_punch==True:
        p2Idle=False
        screen.blit(p2up_punch_list[p2up_punch_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2up_punch_list[p2up_punch_index] == p2up_punch_list[1] or p2up_punch_list[p2up_punch_index] == p2up_punch_list[2]: 
                health_p1-=10
        p2up_punch_index+=1
        if p2up_punch_index>2:
            p2up_punch_index=0

    if p1punch==True:
        p1Idle=False
        screen.blit(p1punch_list[p1punch_index],(p1x,p1y))
        hit = 0
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if p1punch_list[p1punch_index] == p1punch_list[2] or p1punch_list[p1punch_index] == p1punch_list[4]:
                health_p2-=5  
        p1punch_index+=1
        if p1punch_index>4:
            p1punch_index=0

    if p2straight_punch==True:
        p2Idle=False
        screen.blit(p2straight_punch_list[p2straight_punch_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2straight_punch_list[p2straight_punch_index]==p2straight_punch_list[1]: 
                health_p1-=5
        p2straight_punch_index+=1
        if p2straight_punch_index>1:
            p2straight_punch_index=0

    if p1punch_down==True:
        p1Idle=False
        screen.blit(p1punch_down_list[p1punch_down_index],(p1x,p1y))
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if p1punch_down_list[p1punch_down_index] == p1punch_down_list[2] :
                health_p2-=4
        p1punch_down_index+=1
        if p1punch_down_index>2:
            p1punch_down_index=0

    if p2right_punch==True:
        p2Idle=False
        screen.blit(p2right_punch_list[p2right_punch_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2right_punch_list[p2right_punch_index]==p2right_punch_list[1] or p2right_punch_list[p2right_punch_index]==p2right_punch_list[2]: 
                health_p1-=7
        p2right_punch_index+=1
        if p2right_punch_index>2:
            p2right_punch_index=0

    if p1punch_jump==True:
        p1Idle=False
        screen.blit(p1punch_jump_list[p1punch_jump_index],(p1x,p1y))
        p1x+=1
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if p1punch_jump_list[p1punch_jump_index] == p1punch_jump_list[3]:
                health_p2-=10
        p1punch_jump_index+=1
        if p1punch_jump_index>4:
            p1punch_jump_index=0
            
    if p2left_punch==True:
        p2Idle=False
        screen.blit(p2left_punch_list[p2left_punch_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2left_punch_list[p2left_punch_index] == p2left_punch_list[5] or p2left_punch_list[p2left_punch_index] == p2left_punch_list[6] :
                health_p1-=7
        p2left_punch_index+=1
        if p2left_punch_index>6:
            p2left_punch_index=0
    
    if p1punch_dash==True:
        p1Idle=False
        screen.blit(p1punch_dash_list[p1punch_dash_index],(p1x,p1y))          
        p1x+=1
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[1]) or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[2]) or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[3]) or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[4])  or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[5]) or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[6]) or (p1punch_dash_list[p1punch_dash_index] == p1punch_dash_list[7]):
                health_p2-=3
        p1punch_dash_index+=1
        if p1punch_dash_index>7:
            p1punch_dash_index=2

    if p2dash==True:
        p2Idle=False
        screen.blit(p2dash_list[p2dash_index],(p2x,p2y-10))          
        p2x-=5
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if (p2dash_list[p2dash_index] == p2dash_list[3]) or (p2dash_list[p2dash_index] == p2dash_list[2]) or (p2dash_list[p2dash_index] == p2dash_list[4] or (p2dash_list[p2dash_index] == p2dash_list[5])) :
                health_p1-=3                
        p2dash_index+=1
        if p2dash_index>5:
            p2dash_index=5



    if p2kick_up==True:
        p2Idle=False
        screen.blit(p2kick_up_list[p2kick_up_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2kick_up_list[p2kick_up_index] == p2kick_up_list[2] :
                health_p1-=15
        p2kick_up_index+=1
        if p2kick_up_index>5:
            p2kick_up_index=0




    if p1punch_clap==True:
        p1Idle=False
        screen.blit(p1punch_clap_list[p1punch_clap_index],(p1x,p1y))
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            if p1punch_clap_list[p1punch_clap_index] == p1punch_clap_list[2] or p1punch_clap_list[p1punch_clap_index] == p1punch_clap_list[3]  or p1punch_clap_list[p1punch_clap_index] == p1punch_clap_list[4]:
                health_p2-=6
        p1punch_clap_index+=1
        if p1punch_clap_index>4:
            p1punch_clap_index=0


    if p2kick_down==True:
        p2Idle=False
        screen.blit(p2kick_down_list[p2kick_down_index],(p2x,p1y))
        if p2x< p1x +100 and p2x > p1x:
            if p2kick_down_list[p2kick_down_index] == p2kick_down_list[2]  or p2kick_down_list[p2kick_down_index] == p2kick_down_list[3]:
                health_p1-=4
        p2kick_down_index+=1
        if p2kick_down_index>7:
            p2kick_down_index=0

    if p1punch_slap==True:
        p1Idle=False
        screen.blit(p1punch_slap_list[p1punch_slap_index],(p1x,p1y))
        if p1x+100 >= p2x and p1x+100 <= p2x + 100:
            health_p1-=5
        p1punch_slap_index+=1
        if p1punch_slap_index>2:
            p1punch_slap_index=0

    if health_p1<=0:
        screen.fill(RED)
        screen.blit(blade_won,(500,0))
    if health_p2<=0:
        screen.fill(WHITE)
        screen.blit(hulk_won,(0,0))
    if p2moving_left==False and p2moving_right==False and p2up_punch==False and p2straight_punch==False and \
        p2right_punch==False and p2left_punch==False and p2kick_up ==False and p2kick_down ==False and p2dash==False :
            p2Idle=True
    if p1moving_right==False and p1moving_left==False and p1punch==False and p1punch_up==False and  \
        p1punch_down==False and p1punch_jump==False and p1punch_dash==False and p1punch_clap==False and \
        p1punch_slap==False:
            p1Idle=True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                p1moving_left = True
            if event.key == pygame.K_d:
                p1moving_right = True
            if event.key == pygame.K_SPACE:
                p1punch = True
            if event.key == pygame.K_w:
                p1punch_up = True
            if event.key == pygame.K_s:
                p1punch_down = True
            if event.key == pygame.K_j:
                p1punch_jump = True
            if event.key == pygame.K_f:
                p1punch_dash = True
            if event.key == pygame.K_c:
                p1punch_clap = True
            if event.key == pygame.K_x:
                p1punch_slap = True
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_LEFT:
                p2moving_left = True
            if event.key == pygame.K_RIGHT:
                p2moving_right = True
            if event.key == pygame.K_8 :
                p2up_punch = True
            if event.key == pygame.K_7:
                p2dash = True
            if event.key == pygame.K_5:
                p2straight_punch = True
            if event.key == pygame.K_6:
                p2right_punch = True 
            if event.key == pygame.K_4:
                p2left_punch = True
            if event.key == pygame.K_UP:
                p2kick_up = True
            if event.key == pygame.K_DOWN:
                p2kick_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                p1moving_left = False
            if event.key == pygame.K_d:
                p1moving_right = False
            if event.key == pygame.K_SPACE:
                p1punch = False
            if event.key == pygame.K_w:
                p1punch_up = False
            if event.key == pygame.K_s:
                p1punch_down = False
            if event.key == pygame.K_j:
                p1punch_jump = False
            if event.key == pygame.K_f:
                p1punch_dash = False
            if event.key == pygame.K_c:
                p1punch_clap = False
            if event.key == pygame.K_x:
                p1punch_slap = False

            if event.key == pygame.K_LEFT:
                p2moving_left = False
            if event.key == pygame.K_RIGHT:
                p2moving_right = False
            if event.key == pygame.K_8 :
                p2up_punch = False
            if event.key == pygame.K_7:
                p2dash = False
            if event.key == pygame.K_5:
                p2straight_punch = False
            if event.key == pygame.K_6:
                p2right_punch = False
            if event.key == pygame.K_4:
                p2left_punch = False
            if event.key == pygame.K_UP:
                p2kick_up = False
            if event.key == pygame.K_DOWN:
                p2kick_down = False
    pygame.display.update()
pygame.quit()
        
