import tkinter as tk
from PIL import Image,ImageTk
import pygame
from pygame import mixer
import random
mixer.init()
def music():
    pygame.mixer.music.load(r'Game\audio\music.mp3')
    pygame.mixer.music.set_volume(10)
    pygame.mixer.music.play(-1, 0.0, 5000)
i=random.randint(0,10)
def st():
    root.destroy()
    import main
def start():
    global bg,can,root
    root = tk.Tk()               
    root.geometry("1300x600")
    can = tk.Canvas(root,width=1300,height=600)
    bg = Image.open(r'Game\img\Menu/'+str(i) +'.jpg')
    bg = bg.resize((1300,600))
    bg = ImageTk.PhotoImage(bg)
    img_play = Image.open(r'Game\img\start_btn.png')
    img_play = ImageTk.PhotoImage(img_play)
    img_exit = Image.open(r'Game\img\exit_btn.png')
    img_exit = ImageTk.PhotoImage(img_exit)

    btn_play = tk.Button(can,image=img_play,borderwidth=0,command=st)
    btn_play.place(x=540,y=80)
    btn_exit = tk.Button(can,image=img_exit,borderwidth=0,command=root.destroy)
    btn_exit.place(x=540,y=350)
    can.create_image(0,0,image=bg,anchor='nw')
    can.pack()
    music()
    root.mainloop()

start()     
