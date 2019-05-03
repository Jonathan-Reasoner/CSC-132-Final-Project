import Tkinter as tk
import pygame
import sys
import math
from pygame.locals import *

LARGE_FONT= ("Verdana", 12)

pygame.init()

degree = 0
turnSpeed = 0
dx = math.cos(math.radians(degree))
dy = math.sin(math.radians(degree))
playGame = 1
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
windowWidth = 800
windowHeight = 400
rotRect = (360, 182)

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
    if (turnSpeed < 0.6):
        turnSpeed += 0.05
    return turnSpeed

def TurnRight(turnSpeed):
    if (turnSpeed > -0.6):
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
def rotation(image, degree):
    surf = pygame.Surface((100, 80))
    rotatedImage = pygame.transform.rotate(image, degree)
    blittedRect = gameDisplay.blit(surf, (355, 170))
    oldCenter = blittedRect.center
    rotatedSurf = pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return rotatedImage, rotRect
    
menu = Menu()


display = (windowWidth, windowHeight)

# sets up the window for pygame
gameDisplay = pygame.display.set_mode(display)

# creates images for pygame
grass = pygame.image.load("grass.png")
car = pygame.image.load("car.gif").convert_alpha()

##rotRect = pygame.Rect(360, 182, 82, 36)


surf = pygame.Surface((100, 100))
surf.fill((255,255,255))
surf.set_colorkey((255,0,0))
position = [100, 100]

gameDisplay.blit(grass, (position[0] - dx -50, position[1] + dy - 50))
gameDisplay.blit(car, (200, 200))
while(playGame):
    
##    menu.mainloop()
##    MGet()
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord("a"):
               moveLeft = True
            if event.key == K_RIGHT or event.key == ord("d"):
               moveRight = True
            if event.key == K_UP or event.key == ord("w"):
               moveUp = True
            if event.key == K_DOWN or event.key == ord("s"):
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
                
    if moveLeft or moveRight:
        if moveLeft:
            turnSpeed = TurnLeft(turnSpeed)
            degree += turnSpeed
            car2 = pygame.transform.rotate(car, degree)
        if moveRight:
            turnSpeed = TurnRight(turnSpeed)
            degree += turnSpeed
            car2 = pygame.transform.rotate(car, degree)

    car2, rotRect = rotation(car, degree)

    if (not moveLeft and  not moveRight):
        turnSpeed = ResetTurnSpeed(turnSpeed)

    dx = math.cos(math.radians(degree))
    dy = math.sin(math.radians(degree))

    if moveUp:
        position = (position[0] + dx, position[1] - dy)

    
    
    gameDisplay.blit(grass, (position[0] - dx - 100, position[1] + dy - 100))
    section1 = Checkpoints()
    if rotRect.colliderect(section1):
        print "okay"
    pygame.draw.rect(gameDisplay, (200, 200, 200), rotRect)
    gameDisplay.blit(car2, (350, 170))
    pygame.display.update()
