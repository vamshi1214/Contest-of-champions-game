from tkinter import *     #importing tkinter
import tkvideo           #importing tkvideo
import pygame           #importing pygame
pygame.mixer.init()      #importing mixer
def ply ():     
        global root1  #root1 is main window
        #MUSIC       
        pygame.mixer.music.load(r'Game\audio\New Marvel Studios Intro Logo HD - 2013.mp3')
        pygame.mixer.music.set_volume(50)
        pygame.mixer.music.play()     
        #CREATING A WINDOW
        root1 = Tk()          #created a window 
        my_label = Label(root1)         ##labelig for placing
        my_label.pack()             #
        root1.title("MARVEL")
        player = tkvideo.tkvideo(r"Game\New Marvel Studios Intro Logo HD - 2013.mp4", my_label, loop = 0, size = (1280,720))
        player.play()
        root1.after(29000,lambda:root1.destroy())
        root1.mainloop()
ply()
