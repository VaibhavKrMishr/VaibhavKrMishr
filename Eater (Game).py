import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
height = 400
width = 600


# this tkinter one have i taken from python manuals doc thikter example.
import tkinter
from tkinter.constants import *


tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label = tkinter.Label(frame, text="Eater")
label.pack(fill=X, expand=1)

button = tkinter.Button(frame,text="Start", width = 6, height = 2 ,command=tk.destroy)

button.pack(side=BOTTOM)

tk.mainloop()


gamewindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Eater")
pygame.display.update()

exit_game = False
game_over = False
eater_x = 0
eater_y = 0
velocity_x = 0
velocity_y = 0
eater_size =10
fps = 30

clock = pygame.time.Clock()

while not exit_game:

    
    gamewindow.fill(white)
    pygame.draw.rect(gamewindow ,black, [eater_x, eater_y, eater_size, eater_size])
    
    pygame.display.update()
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                velocity_x= +5
                
            if event.key == pygame.K_LEFT:
                velocity_x= -5
                
            if event.key == pygame.K_UP:
                velocity_y = -5
                
            if event.key == pygame.K_DOWN:
                velocity_y =+5
                

                
    eater_x = eater_x +  velocity_x
    eater_y = eater_y +  velocity_y

    
    



    
       

pygame.quit()
quit()

