######################################################
# Brendan Buck, Jonathan Reasoner, Nathan Worsham
# 4/8/2019
# Blast Racer
######################################################
import pygame
import sys, time, random, math
from pygame.locals import *
from Tkinter import *


######################################################
#
# VARIABLES FOR TKINTER
#
######################################################

LARGE_FONT = ("Verdana", 12)
windowWidth = 800
windowHeight = 400
GameStart = "Standard"


######################################################
#
# CLASSES/FUNCTIONS FOR TKINTER
#
######################################################

class Menu():

    def __init__(self):
        
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creates variables to store photos for use in GUI
        global titleBG
        titleBG = PhotoImage(file = "graphics/titleScreen.gif")

        global start
        start = PhotoImage(file = "graphics/start.gif")

        global racing
        racing = PhotoImage(file = "graphics/races.gif")

        global quitting
        quitting = PhotoImage(file = "graphics/quit.gif")

        global single
        single = PhotoImage(file = "graphics/singlePlayer.gif")

        global double
        double = PhotoImage(file = "graphics/twoPlayer.gif")

        global back
        back = PhotoImage(file = "graphics/back.gif")

        global standard
        standard = PhotoImage(file = "graphics/standardRace.gif")

        global drag
        drag = PhotoImage(file = "graphics/dragRace.gif")

        global Manual
        Manual = IntVar()

        choice = Checkbutton(self, text="Manual", variable=Manual)
        choice.pack()

        self.frames = {}

        frame1 = TitleScreen(container, self)
        self.frames[TitleScreen] = frame1
        frame1.grid(row=0, column=0, stick="nsew")

        frame2 = StartMenu(container, self)
        self.frames[StartMenu] = frame2
        frame2.grid(row=0, column=0, stick="nsew")

        frame3 = RacingModes(container, self)
        self.frames[RacingModes] = frame3
        frame3.grid(row=0, column=0, stick="nsew")

        self.show_frame(TitleScreen)

    @staticmethod
    def quitting():
        root = Menu()
        root.destroy()


    # changes the menu when called
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# creates the menu that show when you boot the game

class TitleScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #title_Label=Label(parent, image= titleBG)
        #title_Label.place(x=0, y=0, relwidth=1, relheight=1)
        #title_Label.image = titleBG
        
        startButton = Button(self, image = start, command=lambda: controller.show_frame(StartMenu))
        startButton.pack()
        
class StartMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = Button(self, image = racing, command=lambda: controller.show_frame(RacingModes))
        button.pack()    
        
        button2 = Button(self, image = quitting, command=lambda: getOut())
        button2.pack()


# creates the menu to display racing modes
class RacingModes(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Racing Modes!", font=LARGE_FONT).grid(row = 0, column = 0)

        label2 = Label(self, image = single).grid(row = 1, column = 0)

        label3 = Label(self, image = double).grid(row = 1, column = 1)

        button1 = Button(self, image = standard, command=lambda: startStandard()).grid(row = 2, column = 0)

        button2 = Button(self, image = drag, command=lambda: controller.show_frame(StartMenu)).grid(row = 3, column = 0)

        button3 = Button(self, image = drag, command=lambda: controller.show_frame(StartMenu)).grid(row = 3, column = 1)

        button = Button(self, image = back, command=lambda: controller.show_frame(StartMenu)).grid(row = 4, column = 0)

#quits Tkinter
def getOut():
    Menu.quitting()
    

# gets the True/False value for manual
def MGet():
    print ("Manual is:", Manual.get())

#when standard is pressed, start pygame
def startStandard():
    GameStart = "Standard"
    getOut()
    return GameStart




######################################################
#
# MAIN CODE FOR TKINTER
#
######################################################

while (GameStart == "Menu"):
    root = Tk()
    
    menu = Menu(root)
    
    display = (windowWidth, windowHeight)

    playGame = 1
    while(playGame):

        meun.mainloop()

#####################################################
#
# PYGAME
#
#####################################################
pygame.init()
clock = pygame.time.Clock()


#####################################################
#
# VARIABLES FOR PYGAME
#
#####################################################

degree = 180
position = [100, 100]
turnSpeed = 0
dx = math.cos(math.radians(degree))
dy = math.sin(math.radians(degree))
playGame = 1
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
boostPress = False
windowWidth = 800
windowHeight = 400
rotRect = (360, 182)
passed_time = 0
timer_started = False
done = False

smallFont = pygame.font.SysFont(None, 20)
basicFont = pygame.font.SysFont(None, 24)
normalFont = pygame.font.SysFont(None, 30)
guessFont = pygame.font.SysFont(None, 36)
speed = 0.0
maxSpeed = 180

BLACK = (0, 0, 0)
WHITE = (255,255,255)
BGREEN = (0, 200, 0)
GREEN = (0, 160, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LBLUE = (0, 200, 255)
LGREY = (75,75,75)
BROWN = (139,69,19)
DGREY = (25,25,25)

display = (800, 400)
screen = pygame.display.set_mode(display)

cover = pygame.surface.Surface((70,20)).convert()
cover.fill((GREEN))

bg = pygame.image.load("BG_Image.jpg").convert_alpha()
logo = pygame.image.load("logo.png").convert_alpha()
track = pygame.image.load("Track.png").convert_alpha()
PressStart = guessFont.render("Press ENTER to start", True, WHITE)
ShadPressStart = guessFont.render("Press ENTER to start", True, BLACK)
trackBG = pygame.image.load("graphics/overhead_tile.png").convert_alpha()
playerImage1 = pygame.image.load('Racecar.png').convert_alpha()
playerImage2 = pygame.image.load('Racecar.png').convert_alpha()
playerImage3 = pygame.image.load('Racecar.png').convert_alpha()
playerImage4 = pygame.image.load('Racecar.png').convert_alpha()
playerImage5 = pygame.image.load('Racecar.png').convert_alpha()
playerImage6 = pygame.image.load('Racecar.png').convert_alpha()
playerImage7 = pygame.image.load('Racecar.png').convert_alpha()
playerImage8 = pygame.image.load('Racecar.png').convert_alpha()
playerImage9 = pygame.image.load('Racecar.png').convert_alpha()
bikeImage = pygame.image.load('Racecar.png').convert_alpha()

trackImage11 = pygame.image.load('graphics/b-1-1.png').convert_alpha()
trackImage21 = pygame.image.load('graphics/b-2-1.png').convert_alpha()
trackImage31 = pygame.image.load('graphics/b-3-1.png').convert_alpha()
trackImage41 = pygame.image.load('graphics/b-4-1.png').convert_alpha()
trackImage5 = pygame.image.load('graphics/st-v-3.png').convert_alpha()
trackImage51 = pygame.image.load('graphics/st-v-3-k1.png').convert_alpha()
trackImage52 = pygame.image.load('graphics/st-v-3-k2.png').convert_alpha()
trackImage53 = pygame.image.load('graphics/st-v-3-k3.png').convert_alpha()
trackImage54 = pygame.image.load('graphics/st-v-3-k4.png').convert_alpha()
trackImage6 = pygame.image.load('graphics/st-h-3.png').convert_alpha()
trackImage61 = pygame.image.load('graphics/st-h-3-k1.png').convert_alpha()
trackImage62 = pygame.image.load('graphics/st-h-3-k2.png').convert_alpha()
trackImage63 = pygame.image.load('graphics/st-h-3-k3.png').convert_alpha()
trackImage64 = pygame.image.load('graphics/st-h-3-k4.png').convert_alpha()
trackImage12 = pygame.image.load('graphics/b-1-2.png').convert_alpha()
trackImage22 = pygame.image.load('graphics/b-2-2.png').convert_alpha()
trackImage32 = pygame.image.load('graphics/b-3-2.png').convert_alpha()
trackImage42 = pygame.image.load('graphics/b-4-2.png').convert_alpha()
trackImage13 = pygame.image.load('graphics/b-1-3.png').convert_alpha()
trackImage23 = pygame.image.load('graphics/b-2-3.png').convert_alpha()
trackImage33 = pygame.image.load('graphics/b-3-3.png').convert_alpha()
trackImage43 = pygame.image.load('graphics/b-4-3.png').convert_alpha()
trackImage14 = pygame.image.load('graphics/b-1-4.png').convert_alpha()
trackImage24 = pygame.image.load('graphics/b-2-4.png').convert_alpha()
trackImage34 = pygame.image.load('graphics/b-3-4.png').convert_alpha()
trackImage44 = pygame.image.load('graphics/b-4-4.png').convert_alpha()

playerImage = [5,playerImage1,playerImage2,playerImage3,playerImage4,playerImage5,playerImage6,playerImage7,playerImage8,playerImage9]
playerSettings = [windowWidth/2-50,windowHeight/2,0,0]



#text8s = guessFont.render(str(timer), True, BLACK,)
#text8 = guessFont.render(str(timer), True, WHITE,)

#####################################################
#
# CLASSES/FUNCTIONS FOR PYGAME
#
#####################################################

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



#draws track
def drawTrack(x,y):
    screen.blit(trackImage62,(x-500,y-115))
    screen.blit(trackImage6,(x-200,y-100))
    screen.blit(trackImage6,(x+100,y-100))
    screen.blit(trackImage6,(x+400,y-100))
    screen.blit(trackImage6,(x+500,y-100))
    screen.blit(trackImage64,(x+800,y-100))
    screen.blit(trackImage41,(x+1100,y-100))
    screen.blit(trackImage31,(x+1100,y+300))
    screen.blit(trackImage63,(x+800,y+385))
    screen.blit(trackImage6,(x+500,y+400))
    screen.blit(trackImage6,(x+200,y+400))
    screen.blit(trackImage61,(x-100,y+400))
    screen.blit(trackImage12,(x-600,y+400))
    screen.blit(trackImage22,(x-600,y+900))
    screen.blit(trackImage62,(x-100,y+1085))
    screen.blit(trackImage6,(x+200,y+1100))
    screen.blit(trackImage6,(x+500,y+1100))
    screen.blit(trackImage6,(x+800,y+1100))
    screen.blit(trackImage6,(x+1100,y+1100))
    screen.blit(trackImage63,(x+1400,y+1085))
    screen.blit(trackImage34,(x+1700,y+700))
    screen.blit(trackImage53,(x+2085,y+400))
    screen.blit(trackImage54,(x+2085,y+100))
    screen.blit(trackImage41,(x+2000,y-300))
    screen.blit(trackImage21,(x+1600,y-400))
    screen.blit(trackImage44,(x+1200,y-1100))
    screen.blit(trackImage11,(x+800,y-1100))
    screen.blit(trackImage31,(x+700,y-700))
    screen.blit(trackImage63,(x+400,y-615))
    screen.blit(trackImage62,(x+400,y-615))
    screen.blit(trackImage22,(x-100,y-800))
    screen.blit(trackImage41,(x-200,y-1200))
    screen.blit(trackImage64,(x-500,y-1200))
    screen.blit(trackImage61,(x-500,y-1200))
    screen.blit(trackImage14,(x-1200,y-1200))
    screen.blit(trackImage24,(x-1200,y-500))
        # Timing Lines

def drawBack():
    backPos = [0,0]
    if backPos[0] >= 200:
        backPos[0] -=200
    if backPos[0] <= -200:
        backPos[0] += 200
    if backPos[1] >= 200:
        backPos[1] -= 200
    if backPos[1] <= -200:
        backPos[1] += 200
    screen.blit(trackBG,(backPos[0]+1200,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+1000,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+800,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+600,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+400,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+200,backPos[1]-200))
    screen.blit(trackBG,(backPos[0],backPos[1]-200))
    screen.blit(trackBG,(backPos[0]-200,backPos[1]-200))
    screen.blit(trackBG,(backPos[0]+1200,backPos[1]))
    screen.blit(trackBG,(backPos[0]+1000,backPos[1]))
    screen.blit(trackBG,(backPos[0]+800,backPos[1]))
    screen.blit(trackBG,(backPos[0]+600,backPos[1]))
    screen.blit(trackBG,(backPos[0]+400,backPos[1]))
    screen.blit(trackBG,(backPos[0]+200,backPos[1]))
    screen.blit(trackBG,(backPos[0],backPos[1]))
    screen.blit(trackBG,(backPos[0]-200,backPos[1]))
    screen.blit(trackBG,(backPos[0]+1200,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+1000,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+800,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+600,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+400,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+200,backPos[1]+200))
    screen.blit(trackBG,(backPos[0],backPos[1]+200))
    screen.blit(trackBG,(backPos[0]-200,backPos[1]+200))
    screen.blit(trackBG,(backPos[0]+1200,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+1000,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+800,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+600,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+400,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+200,backPos[1]+400))
    screen.blit(trackBG,(backPos[0],backPos[1]+400))
    screen.blit(trackBG,(backPos[0]-200,backPos[1]+400))
    screen.blit(trackBG,(backPos[0]+1200,backPos[1]+600))
    screen.blit(trackBG,(backPos[0]+1000,backPos[1]+600))
    screen.blit(trackBG,(backPos[0]+800,backPos[1]+600))
    screen.blit(trackBG,(backPos[0]+600,backPos[1]+600))
    screen.blit(trackBG,(backPos[0]+400,backPos[1]+600))
    screen.blit(trackBG,(backPos[0]+200,backPos[1]+600))
    screen.blit(trackBG,(backPos[0],backPos[1]+600))
    screen.blit(trackBG,(backPos[0]-200,backPos[1]+600))


# rotates both the car and the square determining the box for detecting checkpoints
def rotation(image,imageNo,where,degree):
    # Calculate rotated graphics & centre position
    surf =  pygame.Surface((100,50))
    rotatedImage = pygame.transform.rotate(image[imageNo],degree)
    oldCenter = (400,200)
    rotatedSurf =  pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return rotatedImage, rotRect, oldCenter

#def timer(minutes, seconds, milliseconds):
#    milliseconds += 1
#    if milliseconds > 1000:
#        seconds += 1
#        milliseconds -= 1000
#        screen.blit(cover,(0,0))
#    if seconds > 60:
#        minutes += 1
#        seconds -= 60
#    milliseconds += clock.tick_busy_loop(60)
#    return minutes, seconds

def checkpoints(x,y):
    finishLine = pygame.draw.rect(screen, (RED), ( position[0] + 550, position[1]-100, 5, 300))
    section1 = pygame.draw.rect(screen, WHITE,(x+500,y+1100, 1,300))
    section2 = pygame.draw.rect(screen, WHITE,(x-200,y-1200, 1,300))

    

#def speed (x, y):
#    global car_rect
#    car_rect = pygame.draw.rect(screen,(200,200,200),rotRect)
#    speed = 1
    
    

#####################################################
#
# MAIN CODE FOR PYGAME
#
#####################################################

while (GameStart == "Standard"):
    #surf = pygame.Surface((100, 100))
    #surf.fill((255,255,255))
    #surf.set_colorkey((255,0,0))
  
    #drawBack()
    screen.fill((GREEN))
    Track = drawTrack(position[0]+dx, position[1]-dy)
    checkpoints(position[0]+dx, position[1]-dy)

    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord("a"):
               moveLeft = True
            if event.key == K_RIGHT or event.key == ord("d"):
               moveRight = True
            if event.key == K_UP or event.key == ord("w"):
               moveUp = True
            if event.key == K_SPACE:
                boostPress= True
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
            if event.key == K_SPACE:
                boostPress = False
                
    if moveLeft or moveRight:
        if moveLeft:
            turnSpeed = TurnLeft(turnSpeed)
            degree += .4
        if moveRight:
            turnSpeed = TurnRight(turnSpeed)
            degree -= .4


    if (not moveLeft and  not moveRight):
        turnSpeed = ResetTurnSpeed(turnSpeed)



    if moveUp:
        if (speed < maxSpeed):
            speed += .2
        if (speed == maxSpeed and boostPress == True):
            speed += .10
            
        position = [position[0] + dx *(speed/250), position[1] - dy * (speed/150)]
    else:
        if (speed > 0):
            speed -= .5
        position = [position[0] + dx *(speed/100), position[1] - dy * (speed/100)]
       

    if moveDown:
        if (speed > 0):
            speed -= 1
        position = [position[0] - dx, position[1] + dy]
    dx = math.cos(math.radians(degree))
    dy = math.sin(math.radians(degree))

    where = playerSettings[0], playerSettings[1]
    playerRotatedImage, rotRect, oldCenter = rotation(playerImage,playerImage[0], where,degree)


    screen.blit(playerRotatedImage,rotRect)

#    minutes, seconds = timer(minutes, seconds, milliseconds)
#    timelabel = basicFont.render("{}:{}".format(minutes,seconds), True, (0,0,0))
#    screen.blit(timelabel,(0,0))
    
    pygame.display.update()
