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

class Menu(Tk):

    def __init__(self):
        Tk.__init__(self)
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
    menu.destroy()
    

# gets the True/False value for manual
def MGet():
    print ("Manual is:", Manual.get())

#when standard is pressed, start pygame
def startStandard():
    global GameStart
    GameStart = "Standard"
    pygame.init()
    global screen
    screen = pygame.display.set_mode(display)
    getOut()




######################################################
#
# MAIN CODE FOR TKINTER
#
######################################################

##while (GameStart == "Menu"):
##    root = Tk()
##    
##   
##    
##    display = (windowWidth, windowHeight)
##
##    playGame = 1
##    while(playGame):

        

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
dx = math.cos(math.radians(degree))
dy = math.sin(math.radians(degree))
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
boostPress = False
windowWidth = 800
windowHeight = 400
rotRect = (360, 182)
timer2 = 0
laps = 0
prevFinish = 0
prevFinishMilli = 0


smallFont = pygame.font.SysFont(None, 20)
basicFont = pygame.font.SysFont(None, 24)
normalFont = pygame.font.SysFont(None, 30)
guessFont = pygame.font.SysFont(None, 36)
speed = 0.0
maxSpeed = 180
checkpoint1 = False
checkpoint2 = False
grassRect = []


BLACK = (0, 0, 0)
WHITE = (255,255,255)
BGREEN = (0, 200, 0)
GREEN = (0, 160, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LBLUE = (0, 200, 255)
GREY = (90,89,90)
BROWN = (139,69,19)
DGREY = (25,25,25)

blankFinish1 = normalFont.render("Lap 1 ~~ //://", True, WHITE)
blankFinish2 = normalFont.render("Lap 2 ~~ //://", True, WHITE)
blankFinish3 = normalFont.render("Lap 3 ~~ //://", True, WHITE)
blankFinish4 = normalFont.render("Lap 4 ~~ //://", True, WHITE)
blankFinish5 = normalFont.render("Lap 5 ~~ //://", True, WHITE)

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

playerImage = pygame.image.load('Racecar.png').convert_alpha()



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

#playerImage = [5,playerImage1,playerImage2,playerImage3,playerImage4,playerImage5,playerImage6,playerImage7,playerImage8,playerImage9]
playerSettings = [windowWidth/2-50,windowHeight/2,0,0]



#text8s = guessFont.render(str(timer), True, BLACK,)
#text8 = guessFont.render(str(timer), True, WHITE,)

#####################################################
#
# CLASSES/FUNCTIONS FOR PYGAME
#
#####################################################

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

def drawBack(x,y):
    for i in range(-4000,4000, 200):
        for j in range (-4000, 4000, 200):
            screen.blit(trackBG, (x+i, y+j))

            
    
def speedCheck(speed, boost):
    #detects the color the car is currently on
    centerColor = screen.get_at((400,200))[:3]
    #sets constant speed
    speed = 180


    #while car is on track colors, normals speed
    if centerColor == GREY or centerColor ==(88,88,88) or centerColor ==(91,91,91):
        if boostPress == True:
            speed= 250
        if boostPress == False:
            speed = 180
    else:
        if boostPress == True:
            speed = 100
        if boostPress == False:
            speed = 60
    return speed

# rotates both the car and the square determining the box for detecting checkpoints
def rotation(image,where,degree):
    # Calculate rotated graphics & centre position
    surf =  pygame.Surface((100,50))
    rotatedImage = pygame.transform.rotate(image,degree)
    oldCenter = (400,200)
    rotatedSurf =  pygame.transform.rotate(surf, degree)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return rotatedImage, rotRect, oldCenter, rotatedSurf


def checkpoints(x,y, timer2):

    #draws checkpoints and finish line
    global finishLine
    finishLine = pygame.draw.rect(screen, (RED), ( position[0] + 550, position[1]-100, 5, 300))
    global section1
    section1 = pygame.draw.rect(screen, WHITE,(x+500,y+1100, 1,300))
    global section2
    section2 = pygame.draw.rect(screen, WHITE,(x-200,y-1200, 1,300))

    #prints time onto screen
    global timer
    timer = pygame.time.get_ticks()
    global timerSecs
    timerSecs = timer/1000


        
    timerDisplay = normalFont.render("{}:{}".format(timerSecs, timer2), True, WHITE)
    screen.blit(timerDisplay, (700, 40))
    

#####################################################
#
# MAIN CODE FOR PYGAME
#
#####################################################

while( playGame):

    menu = Menu()
    while( GameStart == "Menu"):
        menu.mainloop()

    while (GameStart == "Standard"):

        #draws background and track
        screen.fill(GREEN)
        grassRect = drawBack(position[0],position[1])
        Track = drawTrack(position[0]+dx, position[1]-dy)
        maxSpeed = speedCheck(maxSpeed, boostPress)
        
        #uses while loop to alter milliseconds for timer bc it doesnt work in
        #checkpoint function for some reason lmao
        
        if (timer2 < 1000):
            timer2 += 1
        if (timer2 == 1000):
            timer2 = 0

        #draws checkpoints and blits timer
        checkpoints(position[0]+dx, position[1]-dy, timer2)



        

        #detects when a key has been pressed
        for event in pygame.event.get():

            if event.type == QUIT:
                GameStart = "Menu"
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord("a"):
                   moveLeft = True
                if event.key == K_RIGHT or event.key == ord("d"):
                   moveRight = True
                if event.key == K_UP or event.key == ord("w"):
                   moveUp = True
                if event.key == K_SPACE:
                    boostPress = True
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

        if(GameStart == "Standard"):
                    
            if moveLeft or moveRight:
                if boostPress == False:
                    if moveLeft:
                        if speed > 0:
                            degree += .7
                    if moveRight:
                        if speed > 0:
                            degree -= .7
                if boostPress == True:
                    if moveLeft:
                        if speed > 0:
                            degree += 1.5
                    if moveRight:
                        if speed > 0:
                            degree -= 1.5
                


            if moveUp:
                if (speed < maxSpeed):
                    if boostPress == False:
                        speed += .5
                    if boostPress == True:
                        speed += 1
                if (speed > maxSpeed):
                    speed -= 1

                    
                position = [position[0] + dx *(speed/75), position[1] - dy * (speed/75)]
            else:
                if (speed > 0):
                    speed -= .5
                position = [position[0] + dx *(speed/75), position[1] - dy * (speed/75)]
               

            if moveDown:
                if (speed > 0):
                    speed -= .10
                position = [position[0] - dx, position[1] + dy]
                
            dx = math.cos(math.radians(degree))
            dy = math.sin(math.radians(degree))
            
            where = playerSettings[0], playerSettings[1]
            playerRotatedImage, rotRect, oldCenter, rotatedSurf = rotation(playerImage, where,degree)

                
            screen.blit(playerRotatedImage,rotRect)


            #detects if checkpoints are touched to validate the lap
            if rotRect.colliderect(section1):
                checkpoint1 = True
            if rotRect.colliderect(section2):
                checkpoint2 = True
                
            # completes lap and recieves time if checkpoints have been touched
            if (rotRect.colliderect(finishLine) and checkpoint1 == True and checkpoint2 == True):
                laps += 1

                finishSec= timerSecs - prevFinish
                finishMilli= timer2 - prevFinish
                finishTime = normalFont.render("Lap {} ~~ {}:{}".format(laps, finishSec, finishMilli), True, WHITE)
                checkpoint1 = False
                checkpoint2 = False
                prevFinish = finishSec + prevFinish
                prevFinishMilli = finishMilli + prevFinishMilli

            
            #prints time statements for each lap
            if laps == 0:
                screen.blit(blankFinish1, (600, 250))
                screen.blit(blankFinish2, (600, 275))
                screen.blit(blankFinish3, (600, 300))
                screen.blit(blankFinish4, (600, 325))
                screen.blit(blankFinish5, (600, 350))
                
            if laps == 1:
                lap1 = finishTime
                screen.blit(lap1, (600, 250))
                screen.blit(blankFinish2, (600, 275))
                screen.blit(blankFinish3, (600, 300))
                screen.blit(blankFinish4, (600, 325))
                screen.blit(blankFinish5, (600, 350))
                
            if laps == 2:
                lap2 = finishTime
                screen.blit(lap1, (600, 250))
                screen.blit(lap2, (600, 275))
                screen.blit(blankFinish3, (600, 300))
                screen.blit(blankFinish4, (600, 325))
                screen.blit(blankFinish5, (600, 350))
                
            if laps == 3:
                lap3 = finishTime
                screen.blit(lap1, (600, 250))
                screen.blit(lap2, (600, 275))
                screen.blit(lap3, (600, 300))
                screen.blit(blankFinish4, (600, 325))
                screen.blit(blankFinish5, (600, 350))
            if laps == 4:
                lap4 = finishTime
                screen.blit(lap1, (600, 250))
                screen.blit(lap2, (600, 275))
                screen.blit(lap3, (600, 300))
                screen.blit(lap4, (600, 325))
                screen.blit(blankFinish5, (600, 350))
                
            if laps == 5:
                screen.blit(lap1, (600, 250))
                screen.blit(lap2, (600, 275))
                screen.blit(lap3, (600, 300))
                screen.blit(lap4, (600, 325))
                screen.blit(finishTime, (600, 350))

        ##    speedBar = 100
        ##    pygame.draw.rect(screen, BLACK, (100, 100, 100, 800))
        ##    pygame.draw.rect(screen, RED, (100,100,100,speedBar))
            
            pygame.display.update()
