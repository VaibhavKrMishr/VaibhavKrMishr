import pygame
pygame.init()
import random
import tkinter
from tkinter.constants import *

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue  = (0,0,255)
height = 400
width = 600


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

clock = pygame.time.Clock()
font =  pygame.font.SysFont(None, 20)

with open("High_Score.txt", "r") as h:
    High_Score = h.read()

def text_screen(test, color, x ,y):
    screen_score = font.render(test, True, color)
    gamewindow.blit(screen_score, [x,y])

def gameloop():

    exit_game = False
    game_over = False
    eater_x = 25
    eater_y = 25
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0,width)
    food_y = random.randint(0,height)
    eater_size = 15
    food_size = eater_size
    score = 0
    fps = 30
    global High_Score 
    
    while not exit_game:
        if game_over:
            with open("High_Score.txt", "w") as h:
                h.write(str(High_Score))
             
            gamewindow.fill(white)
            text_screen("Game Over!!! Press Enter To Continue", red, width/4, height/4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                    tk = tkinter.Tk()
                    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
                    frame.pack(fill=BOTH,expand=1)
                    label = tkinter.Label(frame, text="Eater")
                    label.pack(fill=X, expand=1)
                    button = tkinter.Button(frame,text="Exit", width = 6, height = 2 ,command=tk.destroy)
                    button.pack(side=BOTTOM)

                    tk.mainloop()
                    

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +5
                        velocity_y = 0
                        
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                        
                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y =+ 5
                        velocity_x = 0

                        
            gamewindow.fill(white)
            text_screen("Score: " + str(score), blue ,5,5)
            text_screen("High Score: "+ str(High_Score), blue ,width-150,5)
            
            
            if abs(eater_x - food_x)<5 and (eater_y - food_y)<5:
                score = score + 1
            
                if score>int(High_Score):
                    High_Score = score 
    
                food_x = random.randint(0,width)
                food_y = random.randint(0,height)
         
                          
            if eater_x < 0 or eater_x > width or eater_y < 0 or eater_y > height:
                game_over = True
                       
            eater_x = eater_x +  velocity_x
            eater_y = eater_y +  velocity_y

            pygame.draw.rect(gamewindow ,black, [eater_x, eater_y, eater_size, eater_size])
            pygame.draw.rect(gamewindow, red, [food_x, food_y ,food_size/2 , food_size/2])
        pygame.init()
        pygame.display.update()
        clock.tick(fps)     
    pygame.quit()
gameloop()
           
