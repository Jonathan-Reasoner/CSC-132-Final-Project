############################################################
# Jonathan Reasoner, Brendan Buck, Nathan Worshom
# 3/25/2019
# Final Project GUI + Blast Racer
############################################################

import Tkinter as tk
import pygame
import sys
import math
from pygame.locals import *

LARGE_FONT= ("Verdana", 12)

pygame.init()
mainClock = pygame.time.Clock()

degree = 0 # holds the rotation of the car
dx = math.cos(math.radians(degree)) # used for moving the car on the track left and right
dy = math.sin(math.radians(degree)) # used for moving the car on the track up and down
playGame = 1
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
windowWidth = 800 # how wide the window for the game will be
windowHeight = 400 # how high the window for the game will be
display = (windowWidth, windowHeight) # used to create a 800 x 400 display
playerSettings = [windowWidth / 2 - 50, windowHeight / 2] # 0-Player x-position, 1-Player y-position
position = [100, 100] # Determines the locations for a majority of the moving pieces not being rotated
speed = 0.0 # what the car starts off accelerating at
fps = [ 0, 30, 10, 60, 0]
brake = 0
carSettings = [1, 0.5, 0, 200, 3.0] # 0-maximum turning, 1-turning increase over time, 2-how much the car is turning at the moment, 3-Maximum Speed, 4-Maximum braking power
carPosition = 0
class Menu(tk.Tk):

    def __init__(self):
        
        tk.Tk.__init__(self)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creates variables to store photos for use in GUI

        global racing
        racing = tk.PhotoImage(file = "races.gif")

        global quitting
        quitting = tk.PhotoImage(file = "quit.gif")

        global single
        single = tk.PhotoImage(file = "singlePlayer.gif")

        global double
        double = tk.PhotoImage(file = "twoPlayer.gif")

        global back
        back = tk.PhotoImage(file = "back.gif")

        global standard
        standard = tk.PhotoImage(file = "standardRace.gif")

        global drag
        drag = tk.PhotoImage(file = "dragRace.gif")

        global Manual
        Manual = tk.IntVar()

        choice = tk.Checkbutton(self, text="Manual", variable=Manual)
        choice.pack()

        self.frames = {}

        for F in (StartMenu, RacingModes):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartMenu)

    # changes the menu when called
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# creates the menu that show when you boot the game
class StartMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, image = racing, command=lambda: controller.show_frame(RacingModes))
        button.pack()

        button2 = tk.Button(self, image = quitting, command = quit)
        button2.pack()


# creates the menu to display racing modes
class RacingModes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Racing Modes!", font=LARGE_FONT).grid(row = 0, column = 0)

        label2 = tk.Label(self, image = single).grid(row = 1, column = 0)

        label3 = tk.Label(self, image = double).grid(row = 1, column = 1)

        button1 = tk.Button(self, image = standard, command=lambda: controller.show_frame(StartMenu)).grid(row = 2, column = 0)

        button2 = tk.Button(self, image = drag, command=lambda: controller.show_frame(StartMenu)).grid(row = 3, column = 0)

        button3 = tk.Button(self, image = drag, command=lambda: controller.show_frame(StartMenu)).grid(row = 3, column = 1)

        button = tk.Button(self, image = back, command=lambda: controller.show_frame(StartMenu)).grid(row = 4, column = 0)

# quits the tkinter menu but doesn't completely close it
def quit():
    menu.quit()

# gets the True/False value for manual
def MGet():
    print ("Manual is:", Manual.get())

def TurnLeft(turnSpeed):
    if (turnSpeed < 1.0):
        turnSpeed += 0.05
    return turnSpeed

def TurnRight(turnSpeed):
    if (turnSpeed > -1.0):
        turnSpeed -= 0.05
    return turnSpeed

def ResetTurnSpeed(turnSpeed):
    if (turnSpeed > 0):
        turnSpeed -= 0.05
    if (turnSpeed < 0):
        turnSpeed += 0.05
    return turnSpeed

def Checkpoints():
    section1 = pygame.draw.rect(gameDisplay, (255, 255, 255), ( position[0] + 100, position[1] + 100, 1, 60))
    return section1

# rotates both the car and the square determining the box for detecting checkpoints
def rotation(image, playerLocation, degree):
    surf = pygame.Surface((100, 60))
    rotatedImage = pygame.transform.rotate(image, degree)
    blittedRect = gameDisplay.blit(surf, playerLocation)
    oldCenter = blittedRect.center
    rotatedSurf = pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return rotatedImage, rotRect

def framerate():
    mainClock.tick(fps[1])
    fps[2]=int(mainClock.get_fps())
    if fps[0]==1:
        text = smallFont.render('Set FPS - ' + str(fps[1]), True, WHITE,)
        windowSurface.blit(text, (10,WINDOWHEIGHT-60))
        text1 = smallFont.render('Current FPS - ' + str(fps[2]), True, WHITE,)
        windowSurface.blit(text1, (10,WINDOWHEIGHT-40))
        text2 = smallFont.render('Lowest FPS - ' + str(fps[3]), True, WHITE,)
        windowSurface.blit(text2, (10,WINDOWHEIGHT-20))
        if fps[2]<fps[3]:
            fps[3]=fps[2]
        if fps[2]>fps[4]:
            fps[4]=fps[2]

    
menu = Menu()

# sets up the window for pygame
gameDisplay = pygame.display.set_mode(display)

# creates images for pygame
grass = pygame.image.load("grass.png")
car = pygame.image.load("car.gif").convert_alpha()
##
##rotRect = pygame.Rect(360, 182, 82, 36)
##
### creates a variable for rotating the car image
##car2 = pygame.transform.rotate(car, degree)

playerLocation = playerSettings[0], playerSettings[1]
car2, rotRect = rotation(car, playerLocation, degree)

while(playGame):
    
##    menu.mainloop()
##    MGet()
    
    for event in pygame.event.get():
        
        # checks for the player quitting pygame
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        # checks for the player pressing any keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord("a"):
               moveLeft = True
            if event.key == K_RIGHT or event.key == ord("d"):
               moveRight = True
            if event.key == K_UP or event.key == ord("w"):
               moveUp = True
            if event.key == K_DOWN or event.key == ord("s"):
                moveDown = True
                
        # checks for the player letting go of any keys
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
                
    

    # increases speed if the player is hitting the acceleration button
    if moveUp:
        
        if (speed < carSettings[3]):
            speed += 1
            
    # decreases speed if the player is not hitting the acceleration button button
    else:
        if (speed > 0):
            speed -= 1

    if moveDown:
        if(brake < carSettings[4]):
            brake += 0.5
            
        if (speed > 0):
            speed -= brake

        if (speed < 0):
            speed = 0

    # affects where the car moves based on angle and speed
    dx = math.cos(math.radians(degree)) * speed / 10
    dy = math.sin(math.radians(degree)) * speed / 10

    # changes the cars position and rotation if it is moving
    if (speed > 0):
        if moveLeft or moveRight:
            if moveLeft and not moveRight:
                carSettings[2] = TurnLeft(carSettings[2])
                degree += carSettings[2]
                car2 = pygame.transform.rotate(car, degree)
            if moveRight and not moveLeft:
                carSettings[2] = TurnRight(carSettings[2])
                degree += carSettings[2]
                car2 = pygame.transform.rotate(car, degree)

            elif moveRight and moveLeft:
                degree += carSettings[2]
                car2 = pygame.transform.rotate(car, degree)

        car2, rotRect = rotation(car, playerLocation, degree)

        if (not moveLeft and  not moveRight):
            carSettings[2] = ResetTurnSpeed(carSettings[2])
            degree += carSettings[2]
            car2 = pygame.transform.rotate(car, degree)
        position = (position[0] + dx, position[1] - dy)
    
    
    gameDisplay.blit(grass, (position[0] - dx - 100, position[1] + dy - 100))
    section1 = Checkpoints()
##    if rotRect.colliderect(section1):
##        print "okay"
    pygame.draw.rect(gameDisplay, (200, 200, 200), rotRect)
    gameDisplay.blit(car2, rotRect)
    framerate()
    pygame.display.update()
