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
playGame = 1
GameStart = "Menu"



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
        self.displayTrack = 0

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

        global logo
        logo = PhotoImage(file = "graphics/NeonLogo.gif")

        global raceLogo
        raceLogo = PhotoImage(file = "graphics/racersLogo.gif")

        global track1
        track1 = PhotoImage(file = "graphics/track1.gif")

        global track2
        track2 = PhotoImage(file = "graphics/track2.gif")

        global track3
        track3 = PhotoImage(file = "graphics/track3.gif")

        global track4
        track4 = PhotoImage(file = "graphics/track4.gif")

        global track5
        track5 = PhotoImage(file = "graphics/track5.gif")

        global track6
        track6 = PhotoImage(file = "graphics/track6.gif")

        global track7
        track7 = PhotoImage(file = "graphics/track7.gif")

        global track8
        track8 = PhotoImage(file = "graphics/track8.gif")
        
        global track9
        track9 = PhotoImage(file = "graphics/track9.gif")

        global presetImage
        presetImage = [track1, track2, track3, track4, track5, track6, track7, track8, track9]

        global racecar
        racecar = PhotoImage(file = "graphics/Racecar.gif")

        

        #global Manual
        #Manual = IntVar()

        #choice = Checkbutton(self, text="Manual", variable=Manual)
        #choice.pack()

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

    def change_frame(self, container):
        frame2 = StartMenu(container,self)
        self.frames[StartMenu] = frame2
        frame2.grid(row=0, column = 0, stick = "nsew")
        self.show_frame(StartMenu)

# creates the menu that show when you boot the game

class TitleScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #title_Label=Label(parent, image= titleBG)
        #title_Label.place(x=0, y=0, relwidth=1, relheight=1)
        #title_Label.image = titleBG
        self.pack(fill=BOTH, expand=1)

        TitleLogo = Label(self, width = windowWidth/1.2, image = logo)
        TitleLogo.pack()
        
        startButton = Button(self, image = start, command=lambda: controller.show_frame(RacingModes))
        startButton.pack()

        button2 = Button(self, image = quitting, command=lambda: quitGame())
        button2.pack()

# creates the menu to display racing modes
class RacingModes(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, height = windowHeight/3, image = raceLogo)\
            .grid(row = 0, column = 0, columnspan = 4)

        button1 = Button(self, text = "STANDARD", font= LARGE_FONT, bg = "black", fg = "pink"\
            , command=lambda: controller.show_frame(StartMenu))\
                .grid(row = 1, column = 0, columnspan = 2, stick = "nsew")

        button2 = Button(self, height = 7, text = "DRAG", font = LARGE_FONT, bg = "black", fg = "pink"\
            , command=lambda: startDrag())\
                .grid(row = 1, column = 2,columnspan = 2, stick = "nsew" )

        button3 = Button(self, text = "INSTRUCTIONS", font = LARGE_FONT,bg = "black", fg = "pink"\
            , command=lambda: controller.show_frame(StartMenu))\
                .grid(row = 2, column = 2, columnspan = 2, stick = "nsew")

        button = Button(self, height = 7, text = "BACK", bg = "black", font = LARGE_FONT, fg = "pink"\
            , command=lambda: controller.show_frame(TitleScreen))\
                .grid(row = 2, column = 0, columnspan = 2, stick = "nsew")
        
class StartMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)       
        
        
        label = Label(self, text = "STANDARD", width= 35, bg = "black", font= LARGE_FONT, fg = "pink")\
                .grid(row = 0, column = 0, columnspan = 4, stick = "nsew")
        
        button1 = Button(self, text = "<", font= LARGE_FONT, bg = "black", fg = "pink"\
            , command=lambda: decreaseTrack(parent, controller))\
                .grid(row = 1, column = 0, stick = "nsew")

        button2 = Label(self, text = "TRACK", font = LARGE_FONT, bg = "black", fg = "pink")\
                .grid(row = 1, column = 1,columnspan = 2, stick = "nsew" )

        button3 = Button(self, text = ">", font = LARGE_FONT,bg = "black", fg = "pink"\
            , command=lambda: increaseTrack(parent, controller))\
                .grid(row = 1, column = 3, stick = "nsew")

        button4 = Button(self, text = "<", bg = "black", font = LARGE_FONT, fg = "pink"\
            , command=lambda: controller.show_frame(StartMenu))\
                .grid(row = 2, column = 0, stick = "nsew")
        
        button5 = Label(self, text = "CAR", font= LARGE_FONT, bg = "black", fg = "pink")\
                .grid(row = 2, column = 1, columnspan = 2, stick = "nsew")

        button6 = Button(self, text = ">", font = LARGE_FONT,height = 5, bg = "black", fg = "pink"\
            , command=lambda: controller.show_frame(StartMenu))\
                .grid(row = 2, column = 3, stick = "nsew" )

        button7 = Button(self, text = "BACK", height = 5, font = LARGE_FONT,bg = "black", fg = "pink"\
            , command=lambda: controller.show_frame(RacingModes))\
                .grid(row = 3, column = 0, columnspan = 2, stick = "nsew")

        button8 = Button(self, text = "START", bg = "black", font = LARGE_FONT, fg = "pink"\
            , command=lambda: startStandard())\
                .grid(row = 3, column = 2, columnspan = 2, stick = "nsew")
        
        button9 = Label(self, image = presetImage[controller.displayTrack])\
            .grid(row = 0, column = 4, rowspan = 2, stick = "nsew")
            
        button10 = Label(self, image = racecar)\
                .grid(row = 2, column = 4,rowspan = 2, stick = "nsew" )
        
        
        




#quits Tkinter
def quitGame():
    global playGame
    playGame = 2
    global GameStart
    GameStart = "stop"
    menu.destroy()
    
def getOut():
    menu.destroy()

def increaseTrack(parent, controller):
    global trackSelect
    if trackSelect == 8:
        trackSelect = 0
        controller.displayTrack = trackSelect
        controller.change_frame(parent)
    else:
        trackSelect += 1
        controller.displayTrack = trackSelect
        controller.change_frame(parent)

def decreaseTrack(parent, controller):
    global trackSelect
    if trackSelect == 0:
        trackSelect = 8
        controller.displayTrack = trackSelect
        controller.change_frame(parent)
    else:
        trackSelect -= 1
        controller.displayTrack = trackSelect
        controller.change_frame(parent)

#def trackImageSelect():

    

# gets the True/False value for manual
#def MGet():
#    print ("Manual is:", Manual.get())

#when standard is pressed, start pygame
def startStandard():
    global GameStart
    GameStart = "Standard"
    pygame.init()
    getOut()

def startDrag():
    global GameStart
    global trackSelect
    trackSelect = "dragTrack"
    GameStart = "Drag"
    pygame.init()
    getOut()

        

#####################################################
#
# PYGAME
#
#####################################################


#####################################################
#
# VARIABLES FOR PYGAME
#
#####################################################


#playerImage = [5,playerImage1,playerImage2,playerImage3,playerImage4,playerImage5,playerImage6,playerImage7,playerImage8,playerImage9]


#####################################################
#
# CLASSES/FUNCTIONS FOR PYGAME
#
#####################################################

#draws track
def drawTrack(x,y):
    global finishLine
    global section1
    global section2

    if trackSelect == 0:
        screen.blit(trackImage62,(x-1000,y-115))
        screen.blit(trackImage6,(x-700,y-100))
        screen.blit(trackImage6,(x-400,y-100))
        screen.blit(trackImage6,(x-100,y-100))
        screen.blit(trackImage6,(x,y-100))
        screen.blit(trackImage64,(x+300,y-100))
        screen.blit(trackImage41,(x+600,y-100))
        screen.blit(trackImage31,(x+600,y+300))
        screen.blit(trackImage63,(x+300,y+385))
        screen.blit(trackImage6,(x,y+400))
        screen.blit(trackImage6,(x-300,y+400))
        screen.blit(trackImage61,(x-600,y+400))
        screen.blit(trackImage12,(x-1100,y+400))
        screen.blit(trackImage22,(x-1100,y+900))
        screen.blit(trackImage62,(x-600,y+1085))
        screen.blit(trackImage6,(x-300,y+1100))
        screen.blit(trackImage6,(x,y+1100))
        screen.blit(trackImage6,(x+300,y+1100))
        screen.blit(trackImage6,(x+600,y+1100))
        screen.blit(trackImage63,(x+900,y+1085))
        screen.blit(trackImage34,(x+1200,y+700))
        screen.blit(trackImage53,(x+1585,y+400))
        screen.blit(trackImage54,(x+1585,y+100))
        screen.blit(trackImage41,(x+1500,y-300))
        screen.blit(trackImage21,(x+1100,y-400))
        screen.blit(trackImage44,(x+700,y-1100))
        screen.blit(trackImage11,(x+300,y-1100))
        screen.blit(trackImage31,(x+200,y-700))
        screen.blit(trackImage63,(x-100,y-615))
        screen.blit(trackImage62,(x-100,y-615))
        screen.blit(trackImage22,(x-600,y-800))
        screen.blit(trackImage41,(x-700,y-1200))
        screen.blit(trackImage64,(x-1000,y-1200))
        screen.blit(trackImage61,(x-1000,y-1200))
        screen.blit(trackImage14,(x-1700,y-1200))
        screen.blit(trackImage24,(x-1700,y-500))
        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x,y+1100, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x-700,y-1200, 1,300))

    if trackSelect == 1:
        screen.blit(trackImage64,(x-100,y-100))
        screen.blit(trackImage41,(x+200,y-100))
        screen.blit(trackImage32,(x+100,y+300))
        screen.blit(trackImage11,(x-300,y+500))
        screen.blit(trackImage22,(x-300,y+900))
        screen.blit(trackImage62,(x+200,y+1085))
        screen.blit(trackImage63,(x+500,y+1085))
        screen.blit(trackImage31,(x+800,y+1000))
        screen.blit(trackImage53,(x+885,y+700))
        screen.blit(trackImage5,(x+900,y+400))
        screen.blit(trackImage5,(x+900,y+100))
        screen.blit(trackImage54,(x+885,y-200))
        screen.blit(trackImage42,(x+700,y-700))
        screen.blit(trackImage21,(x+300,y-800))
        screen.blit(trackImage42,(x+100,y-1300))
        screen.blit(trackImage11,(x-300,y-1300))
        screen.blit(trackImage32,(x-500,y-900))
        screen.blit(trackImage63,(x-800,y-715))
        screen.blit(trackImage6,(x-1100,y-700))
        screen.blit(trackImage61,(x-1400,y-700))
        screen.blit(trackImage11,(x-1800,y-700))
        screen.blit(trackImage51,(x-1800,y-300))
        screen.blit(trackImage52,(x-1800,y))
        screen.blit(trackImage22,(x-1800,y+300))
        screen.blit(trackImage62,(x-1300,y+485))
        screen.blit(trackImage31,(x-1000,y+400))
        screen.blit(trackImage12,(x-900,y-100))
        screen.blit(trackImage61,(x-400,y-100))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+400,y+1100, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x+100,y-1300, 1,300))

    if trackSelect == 2:
        # Track Circs
        screen.blit(trackImage61,(x-900,y-100))
        screen.blit(trackImage6,(x-600,y-100))
        screen.blit(trackImage6,(x-300,y-100))
        screen.blit(trackImage6,(x,y-100))
        screen.blit(trackImage64,(x+200,y-100))
        screen.blit(trackImage41,(x+500,y-100))
        screen.blit(trackImage31,(x+500,y+300))
        screen.blit(trackImage11,(x+100,y+400))
        screen.blit(trackImage21,(x+100,y+800))
        screen.blit(trackImage62,(x+500,y+885))
        screen.blit(trackImage31,(x+800,y+800))
        screen.blit(trackImage11,(x+900,y+400))
        screen.blit(trackImage41,(x+1300,y+400))
        screen.blit(trackImage54,(x+1385,y+800))
        screen.blit(trackImage53,(x+1385,y+900))
        screen.blit(trackImage34,(x+1000,y+1200))
        screen.blit(trackImage63,(x+700,y+1585))
        screen.blit(trackImage62,(x+400,y+1585))
        screen.blit(trackImage21,(x,y+1500))
        screen.blit(trackImage41,(x-100,y+1100))
        screen.blit(trackImage11,(x-500,y+1100))
        screen.blit(trackImage31,(x-600,y+1500))
        screen.blit(trackImage22,(x-1100,y+1400))
        screen.blit(trackImage12,(x-1100,y+900))
        screen.blit(trackImage31,(x-600,y+800))
        screen.blit(trackImage41,(x-600,y+400))
        screen.blit(trackImage64,(x-900,y+400))
        screen.blit(trackImage62,(x-900,y+385))
        screen.blit(trackImage21,(x-1300,y+300))
        screen.blit(trackImage11,(x-1300,y-100))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+900,y+1600, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x-600,y+900, 1,300))

    if trackSelect == 3:
        screen.blit(trackImage61,(x-100,y-100))
        screen.blit(trackImage6,(x+100,y-100))
        screen.blit(trackImage6,(x+400,y-100))
        screen.blit(trackImage6,(x+700,y-100))
        screen.blit(trackImage6,(x+1000,y-100))
        screen.blit(trackImage64,(x+1200,y-100))
        screen.blit(trackImage41,(x+1500,y-100))
        screen.blit(trackImage22,(x+1600,y+300))
        screen.blit(trackImage32,(x+2100,y+300))
        screen.blit(trackImage11,(x+2300,y-100))
        screen.blit(trackImage43,(x+2700,y-100))
        screen.blit(trackImage54,(x+2985,y+500))
        screen.blit(trackImage33,(x+2700,y+800))
        screen.blit(trackImage63,(x+2400,y+1085))
        screen.blit(trackImage6,(x+2100,y+1100))
        screen.blit(trackImage62,(x+1800,y+1085))
        screen.blit(trackImage22,(x+1300,y+900))
        screen.blit(trackImage42,(x+1100,y+400))
        screen.blit(trackImage11,(x+700,y+400))
        screen.blit(trackImage51,(x+700,y+800))
        screen.blit(trackImage22,(x+700,y+1100))
        screen.blit(trackImage41,(x+1200,y+1300))
        screen.blit(trackImage33,(x+1000,y+1700))
        screen.blit(trackImage21,(x+600,y+1900))
        screen.blit(trackImage41,(x+500,y+1500))
        screen.blit(trackImage21,(x+100,y+1400))
        screen.blit(trackImage52,(x+100,y+1100))
        screen.blit(trackImage41,(x,y+700))
        screen.blit(trackImage23,(x-600,y+400))
        screen.blit(trackImage12,(x-600,y-100))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+3000,y+600, 300,1))
        section2 = pygame.draw.rect(screen, WHITE,(x+700,y+900, 300,1))

    if trackSelect == 4:
        screen.blit(trackImage11,(x-1300,y-100))
        screen.blit(trackImage61,(x-900,y-100))
        screen.blit(trackImage6,(x-600,y-100))
        screen.blit(trackImage6,(x-300,y-100))
        screen.blit(trackImage6,(x,y-100))
        screen.blit(trackImage6,(x+300,y-100))
        screen.blit(trackImage6,(x+600,y-100))
        screen.blit(trackImage64,(x+900,y-100))
        screen.blit(trackImage44,(x+1200,y-100))
        screen.blit(trackImage54,(x+1585,y+600))
        screen.blit(trackImage31,(x+1500,y+900))
        screen.blit(trackImage21,(x+1100,y+900))
        screen.blit(trackImage41,(x+1000,y+500))
        screen.blit(trackImage64,(x+700,y+500))
        screen.blit(trackImage61,(x+400,y+500))
        screen.blit(trackImage11,(x,y+500))
        screen.blit(trackImage21,(x,y+900))
        screen.blit(trackImage41,(x+400,y+1000))
        screen.blit(trackImage54,(x+485,y+1400))
        screen.blit(trackImage33,(x+200,y+1700))
        screen.blit(trackImage63,(x-100,y+1985))
        screen.blit(trackImage6,(x-300,y+2000))
        screen.blit(trackImage62,(x-600,y+1985))
        screen.blit(trackImage21,(x-1000,y+1900))
        screen.blit(trackImage11,(x-1000,y+1500))
        screen.blit(trackImage31,(x-600,y+1400))
        screen.blit(trackImage53,(x-515,y+1100))
        screen.blit(trackImage54,(x-515,y+800))
        screen.blit(trackImage41,(x-600,y+400))
        screen.blit(trackImage64,(x-900,y+400))
        screen.blit(trackImage62,(x-900,y+385))
        screen.blit(trackImage21,(x-1300,y+300))
        screen.blit(trackImage11,(x-1300,y-100))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+1500,y+1000, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x-500,y+2000, 1,300))

    if trackSelect == 5:
        screen.blit(trackImage12,(x-1800,y-100))
        screen.blit(trackImage61,(x-1300,y-100))
        screen.blit(trackImage6,(x-1200,y-100))
        screen.blit(trackImage6,(x-900,y-100))
        screen.blit(trackImage6,(x-600,y-100))
        screen.blit(trackImage6,(x-300,y-100))
        screen.blit(trackImage6,(x,y-100))
        screen.blit(trackImage6,(x+300,y-100))
        screen.blit(trackImage64,(x+600,y-100))
        screen.blit(trackImage42,(x+900,y-100))
        screen.blit(trackImage54,(x+1085,y+400))
        screen.blit(trackImage5,(x+1100,y+700))
        screen.blit(trackImage5,(x+1100,y+1000))
        screen.blit(trackImage5,(x+1100,y+1300))
        screen.blit(trackImage5,(x+1100,y+1600))
        screen.blit(trackImage53,(x+1085,y+1900))
        screen.blit(trackImage34,(x+700,y+2200))
        screen.blit(trackImage22,(x+200,y+2400))
        screen.blit(trackImage52,(x+200,y+2100))
        screen.blit(trackImage5,(x+200,y+1800))
        screen.blit(trackImage54,(x+185,y+1500))
        screen.blit(trackImage44,(x-200,y+800))
        screen.blit(trackImage64,(x-500,y+800))
        screen.blit(trackImage6,(x-800,y+800))
        screen.blit(trackImage62,(x-1100,y+785))
        screen.blit(trackImage24,(x-1800,y+400))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+700,y+2600, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x-1000,y+800, 1,300))

    if trackSelect == 6:
        screen.blit(trackImage11,(x-700,y-100))
        screen.blit(trackImage61,(x-300,y-100))
        screen.blit(trackImage64,(x,y-100))
        screen.blit(trackImage41,(x+300,y-100))
        screen.blit(trackImage32,(x+200,y+300))
        screen.blit(trackImage11,(x-200,y+500))
        screen.blit(trackImage23,(x-200,y+900))
        screen.blit(trackImage34,(x+400,y+800))
        screen.blit(trackImage53,(x+785,y+500))
        screen.blit(trackImage51,(x+800,y+400))
        screen.blit(trackImage14,(x+800,y-300))
        screen.blit(trackImage34,(x+1500,y-700))
        screen.blit(trackImage44,(x+1500,y-1400))
        screen.blit(trackImage13,(x+900,y-1400))
        screen.blit(trackImage32,(x+700,y-800))
        screen.blit(trackImage21,(x+300,y-700))
        screen.blit(trackImage43,(x,y-1300))
        screen.blit(trackImage14,(x-700,y-1300))
        screen.blit(trackImage34,(x-1100,y-600))
        screen.blit(trackImage11,(x-1500,y-200))
        screen.blit(trackImage23,(x-1500,y+200))
        screen.blit(trackImage32,(x-900,y+300))
        screen.blit(trackImage11,(x-700,y-100))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+400,y+1200, 1,300))
        section2 = pygame.draw.rect(screen, WHITE,(x+700,y-600, 1,300))

    if trackSelect == 7:
        screen.blit(trackImage14,(x-1200,y-100))
        screen.blit(trackImage61,(x-500,y-100))
        screen.blit(trackImage6,(x-200,y-100))
        screen.blit(trackImage63,(x+100,y-115))
        screen.blit(trackImage31,(x+400,y-200))
        screen.blit(trackImage14,(x+500,y-900))
        screen.blit(trackImage44,(x+1200,y-900))
        screen.blit(trackImage34,(x+1200,y-200))
        screen.blit(trackImage11,(x+800,y+200))
        screen.blit(trackImage51,(x+800,y+600))
        screen.blit(trackImage52,(x+800,y+600))
        screen.blit(trackImage21,(x+800,y+900))
        screen.blit(trackImage32,(x+1200,y+800))
        screen.blit(trackImage11,(x+1400,y+400))
        screen.blit(trackImage61,(x+1800,y+400))
        screen.blit(trackImage6,(x+2100,y+400))
        screen.blit(trackImage63,(x+2400,y+385))
        screen.blit(trackImage33,(x+2700,y+100))
        screen.blit(trackImage11,(x+3000,y-300))
        screen.blit(trackImage44,(x+3400,y-300))
        screen.blit(trackImage34,(x+3400,y+400))
        screen.blit(trackImage14,(x+2700,y+800))
        screen.blit(trackImage33,(x+2400,y+1500))
        screen.blit(trackImage63,(x+2100,y+1785))
        screen.blit(trackImage6,(x+1800,y+1800))
        screen.blit(trackImage6,(x+1500,y+1800))
        screen.blit(trackImage6,(x+1200,y+1800))
        screen.blit(trackImage62,(x+900,y+1785))
        screen.blit(trackImage21,(x+500,y+1700))
        screen.blit(trackImage41,(x+400,y+1300))
        screen.blit(trackImage64,(x+100,y+1300))
        screen.blit(trackImage6,(x-200,y+1300))
        screen.blit(trackImage62,(x-500,y+1285))
        screen.blit(trackImage24,(x-1200,y+900))
        screen.blit(trackImage52,(x-1200,y+600))
        screen.blit(trackImage51,(x-1200,y+600))

        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+800,y+700, 300,1))
        section2 = pygame.draw.rect(screen, WHITE,(x+1700,y+1800, 1,300))

    if trackSelect == 8:
        screen.blit(trackImage11,(x-800,y-100))
        screen.blit(trackImage61,(x-400,y-100))
        screen.blit(trackImage6,(x-100,y-100))
        screen.blit(trackImage63,(x+200,y-115))
        screen.blit(trackImage31,(x+500,y-200))
        screen.blit(trackImage11,(x+600,y-600))
        screen.blit(trackImage44,(x+1000,y-600))
        screen.blit(trackImage54,(x+1385,y+100))
        screen.blit(trackImage53,(x+1385,y+100))
        screen.blit(trackImage34,(x+1000,y+400))
        screen.blit(trackImage21,(x+600,y+700))
        screen.blit(trackImage41,(x+500,y+300))
        screen.blit(trackImage13,(x-100,y+300))
        screen.blit(trackImage23,(x-100,y+900))
        screen.blit(trackImage42,(x+500,y+1200))
        screen.blit(trackImage54,(x+685,y+1700))
        screen.blit(trackImage52,(x+700,y+1700))
        screen.blit(trackImage22,(x+700,y+2000))
        screen.blit(trackImage41,(x+1200,y+2200))
        screen.blit(trackImage32,(x+1100,y+2600))
        screen.blit(trackImage63,(x+800,y+2785))
        screen.blit(trackImage6,(x+500,y+2800))
        screen.blit(trackImage62,(x+200,y+2785))
        screen.blit(trackImage24,(x-500,y+2400))
        screen.blit(trackImage52,(x-500,y+2100))
        screen.blit(trackImage5,(x-500,y+1800))
        screen.blit(trackImage54,(x-515,y+1600))
        screen.blit(trackImage42,(x-700,y+1100))
        screen.blit(trackImage23,(x-1300,y+800))
        screen.blit(trackImage11,(x-1300,y+400))
        screen.blit(trackImage31,(x-900,y+300))
        # Timing Lines
        finishLine = pygame.draw.rect(screen, LBLUE,(x+50,y-100, 1,300))
        section1 = pygame.draw.rect(screen, WHITE,(x+1400,y+200, 300,1))
        section2 = pygame.draw.rect(screen, WHITE,(x+1300,y+2600, 300,1))

    if trackSelect == "dragTrack":
        for i in range(-50000,200, 300):
            screen.blit(trackImage5, (250, y+i))
        #screen.blit(trackImage5, (100, 100))
        
def drawBack(x,y):
    global GameStart
    if GameStart == "Standard":
    
        for i in range(-4000,4000, 200):
            for j in range (-4000, 4000, 200):
                screen.blit(trackBG, (x+i, y+j))
    
    if GameStart == "Drag":

        for i in range(-51000, 1000, 200):
            for j in range (-1000,1000,200):
                screen.blit(trackBG, (x+j, y+i))
    
def speedCheck(speed, boost):
    #detects the color the car is currently on
    centerColor = screen.get_at((400,200))[:3]
    #sets constant speed
    speed = 180
    global maxBoost

    #while car is on track colors, normals speed
    if centerColor == (43,43,43):# or centerColor ==(43,43,43) or centerColor ==(91,91,91):
        if boostPress == True:
            if maxBoost > 0:
                maxBoost -= .3
                speed= 250
        if boostPress == False:
            speed = 180
    else:
        if boostPress == True:
            if maxBoost >0:
                maxBoost -= .3
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


def timerBlit(x,y, timer2):



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

while(playGame == 1):

    while( GameStart == "Menu"):
        trackSelect = 0
        menu = Menu()
        menu.mainloop()
        pygame.time.wait(2000)
        clock = pygame.time.Clock()
        setVariables = 0
        

    while (GameStart == "Standard"):
        ###########################
        # SETS VARIABLES ONCE
        ###########################
        if setVariables == 0:
            
            degree = 0

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
            maxBoost = 100
            raceFinishSec = 0
            raceFinishMilli = 0
            speed = 0.0
            maxSpeed = 180
            checkpoint1 = False
            checkpoint2 = False
            grassRect = []
            playerSettings = [windowWidth/2-50,windowHeight/2,0,0]
            display = (800, 400)
            screen = pygame.display.set_mode(display)


            smallFont = pygame.font.SysFont(None, 20)
            basicFont = pygame.font.SysFont(None, 24)
            normalFont = pygame.font.SysFont(None, 30)
            guessFont = pygame.font.SysFont(None, 36)



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


            PressStart = guessFont.render("Press ENTER to start", True, WHITE)
            ShadPressStart = guessFont.render("Press ENTER to start", True, BLACK)

            trackBG = pygame.image.load("graphics/NeonBackground2.png").convert_alpha()

            playerImage = pygame.image.load('graphics/TronCar2.0.png').convert_alpha()



            trackImage11 = pygame.image.load('graphics/Neon1-1.png').convert_alpha()
            trackImage21 = pygame.image.load('graphics/Neon2-1.png').convert_alpha()
            trackImage31 = pygame.image.load('graphics/Neon3-1.png').convert_alpha()
            trackImage41 = pygame.image.load('graphics/Neon4-1.png').convert_alpha()
            trackImage5 = pygame.image.load('graphics/StNeon7.png').convert_alpha()
            trackImage51 = pygame.image.load('graphics/StNeon8.png').convert_alpha()
            trackImage52 = pygame.image.load('graphics/StNeon9.png').convert_alpha()
            trackImage53 = pygame.image.load('graphics/StNeon10.png').convert_alpha()
            trackImage54 = pygame.image.load('graphics/StNeon11.png').convert_alpha()
            trackImage6 = pygame.image.load('graphics/StNeon-1.png').convert_alpha()
            trackImage61 = pygame.image.load('graphics/StNeon3.png').convert_alpha()
            trackImage62 = pygame.image.load('graphics/StNeon4.png').convert_alpha()
            trackImage63 = pygame.image.load('graphics/StNeon5.png').convert_alpha()
            trackImage64 = pygame.image.load('graphics/StNeon6.png').convert_alpha()
            trackImage12 = pygame.image.load('graphics/Neon1-2.png').convert_alpha()
            trackImage22 = pygame.image.load('graphics/Neon2-2.png').convert_alpha()
            trackImage32 = pygame.image.load('graphics/Neon3-2.png').convert_alpha()
            trackImage42 = pygame.image.load('graphics/Neon4-2.png').convert_alpha()
            trackImage13 = pygame.image.load('graphics/Neon1-3.png').convert_alpha()
            trackImage23 = pygame.image.load('graphics/Neon2-3.png').convert_alpha()
            trackImage33 = pygame.image.load('graphics/Neon3-3.png').convert_alpha()
            trackImage43 = pygame.image.load('graphics/Neon4-3.png').convert_alpha()
            trackImage14 = pygame.image.load('graphics/Neon1-4.png').convert_alpha()
            trackImage24 = pygame.image.load('graphics/Neon2-4.png').convert_alpha()
            trackImage34 = pygame.image.load('graphics/Neon3-4.png').convert_alpha()
            trackImage44 = pygame.image.load('graphics/Neon4-4.png').convert_alpha()
            setVariables += 1
            
        #draws background and track
        screen.fill(LBLUE)
  
        grassRect = drawBack(position[0],position[1])
        Track = drawTrack(position[0]+dx, position[1]-dy)

        if not laps == 5:
            maxSpeed = speedCheck(maxSpeed, boostPress)
            timerBlit(position[0]+dx, position[1]-dy, timer2)
        if laps == 5:
            maxSpeed = 0
        
        #uses while loop to alter milliseconds for timer bc it doesnt work in
        #checkpoint function for some reason lmao
        
        if (timer2 < 1000):
            timer2 += 1
        if (timer2 == 1000):
            timer2 = 0




        

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

                        #draws boost and speed bars
            speedBar = -(speed/250) * 100
            boostBar = -(maxBoost/100) * 100
            boostText = smallFont.render("BST", True, WHITE)
            speedText = smallFont.render("SPD", True, WHITE)
            SboostText = smallFont.render("BST", True, BLACK)
            SspeedText = smallFont.render("SPD", True, BLACK)
            
            if boostBar < 0:
                boostBar = boostBar
            if boostBar > 0:
                boostBar = 0
            #draws speed bar
            pygame.draw.rect(screen, WHITE, (23, 248, 29, 104))
            pygame.draw.rect(screen, BLACK, (25, 250, 25, 100))
            pygame.draw.rect(screen, RED, (25,350,25,speedBar))
            pygame.draw.rect(screen, WHITE, (25, 275, 25, 1))

            #draws boost bar
            pygame.draw.rect(screen, WHITE, (58, 248, 29, 104))
            pygame.draw.rect(screen, BLACK, (60, 250, 25, 100))
            pygame.draw.rect(screen, BLUE, (60, 350, 25, boostBar))

            #adds label text for bars
            screen.blit(SboostText, (62, 367))
            screen.blit(boostText, (60,365))
            screen.blit(SspeedText, (27, 367))
            screen.blit(speedText, (25, 365))


            #detects if checkpoints are touched to validate the lap
            if rotRect.colliderect(section1):
                checkpoint1 = True
            if rotRect.colliderect(section2):
                checkpoint2 = True
                
            # completes lap and recieves time if checkpoints have been touched
            if (rotRect.colliderect(finishLine) and checkpoint1 == True):# and checkpoint2 == True):
                laps += 1
                maxBoost = 100

                finishSec= timerSecs - prevFinish
                finishMilli= timer2 - prevFinish
                finishTime = normalFont.render("Lap {} ~~ {}:{}".format(laps, finishSec, finishMilli), True, WHITE)
                checkpoint1 = False
                checkpoint2 = False
                prevFinish = finishSec + prevFinish
                prevFinishMilli = finishMilli + prevFinishMilli

                raceFinishSec += finishSec
                raceFinishMilli += finishMilli

            
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
  
                congrats = normalFont.render("Congratulations, you finished in:", True, WHITE)
                timerDisplay = normalFont.render("{}:{}".format(raceFinishSec, raceFinishMilli), True, RED)
                screen.blit(congrats, (200, 200))
                screen.blit(timerDisplay, (400,300))
                screen.blit(lap1, (600, 250))
                screen.blit(lap2, (600, 275))
                screen.blit(lap3, (600, 300))
                screen.blit(lap4, (600, 325))
                screen.blit(finishTime, (600, 350))

                    
            pygame.display.update()

            if laps == 5 and speed < 5:
                pygame.time.wait(5000)
                GameStart = "Menu"
                pygame.quit()


    while (GameStart == "Drag"):
        if (setVariables == 0):
            degree = 270
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
            maxBoost = 100
            raceFinishSec = 0
            raceFinishMilli = 0
            speed = 0.0
            maxSpeed = 180
            checkpoint1 = False
            checkpoint2 = False
            grassRect = []
            playerSettings = [windowWidth/2-50,windowHeight/2,0,0]
            display = (800, 400)
            screen = pygame.display.set_mode(display)


            smallFont = pygame.font.SysFont(None, 20)
            basicFont = pygame.font.SysFont(None, 24)
            normalFont = pygame.font.SysFont(None, 30)
            guessFont = pygame.font.SysFont(None, 36)



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

            trackBG = pygame.image.load("graphics/NeonBackground2.png").convert_alpha()
            playerImage = pygame.image.load('graphics/TronCar2.0.png').convert_alpha()
            
            trackImage11 = pygame.image.load('graphics/Neon1-1.png').convert_alpha()
            trackImage21 = pygame.image.load('graphics/Neon2-1.png').convert_alpha()
            trackImage31 = pygame.image.load('graphics/Neon3-1.png').convert_alpha()
            trackImage41 = pygame.image.load('graphics/Neon4-1.png').convert_alpha()
            trackImage5 = pygame.image.load('graphics/StNeon7.png').convert_alpha()
            trackImage51 = pygame.image.load('graphics/StNeon8.png').convert_alpha()
            trackImage52 = pygame.image.load('graphics/StNeon9.png').convert_alpha()
            trackImage53 = pygame.image.load('graphics/StNeon10.png').convert_alpha()
            trackImage54 = pygame.image.load('graphics/StNeon11.png').convert_alpha()
            trackImage6 = pygame.image.load('graphics/StNeon-1.png').convert_alpha()
            trackImage61 = pygame.image.load('graphics/StNeon3.png').convert_alpha()
            trackImage62 = pygame.image.load('graphics/StNeon4.png').convert_alpha()
            trackImage63 = pygame.image.load('graphics/StNeon5.png').convert_alpha()
            trackImage64 = pygame.image.load('graphics/StNeon6.png').convert_alpha()
            trackImage12 = pygame.image.load('graphics/Neon1-2.png').convert_alpha()
            trackImage22 = pygame.image.load('graphics/Neon2-2.png').convert_alpha()
            trackImage32 = pygame.image.load('graphics/Neon3-2.png').convert_alpha()
            trackImage42 = pygame.image.load('graphics/Neon4-2.png').convert_alpha()
            trackImage13 = pygame.image.load('graphics/Neon1-3.png').convert_alpha()
            trackImage23 = pygame.image.load('graphics/Neon2-3.png').convert_alpha()
            trackImage33 = pygame.image.load('graphics/Neon3-3.png').convert_alpha()
            trackImage43 = pygame.image.load('graphics/Neon4-3.png').convert_alpha()
            trackImage14 = pygame.image.load('graphics/Neon1-4.png').convert_alpha()
            trackImage24 = pygame.image.load('graphics/Neon2-4.png').convert_alpha()
            trackImage34 = pygame.image.load('graphics/Neon3-4.png').convert_alpha()
            trackImage44 = pygame.image.load('graphics/Neon4-4.png').convert_alpha()

            sped0 = basicFont.render("0", True, WHITE)
            sped100= basicFont.render("100", True, WHITE)
            sped200= basicFont.render("200", True, WHITE)
            sped300= basicFont.render("300", True, WHITE)
            sped400= basicFont.render("400", True, WHITE)
            sped500= basicFont.render("500", True, WHITE)
        
            setVariables = 2

        screen.fill(LBLUE)
        drawBack(position[0],position[1])
        drawTrack(position[0],position[1])

        #draws speedometer
        pygame.draw.circle(screen, WHITE, (700, 350), 150, 3)
        screen.blit(sped0, (580, 365))
        screen.blit(sped100, (560, 315))
        screen.blit(sped200, (585, 265))
        screen.blit(sped300, (630, 225))
        screen.blit(sped400, (700, 210))
        screen.blit(sped500, (760, 250))




        #detects when a key has been pressed
        for event in pygame.event.get():

            if event.type == QUIT:
                GameStart = "Menu"
                pygame.quit()
            if event.type == KEYDOWN:
                
                if event.key == K_UP or event.key == ord("w"):
                   moveUp = True

            if event.type == KEYUP:

                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False

            
        if moveUp:
            if (speed < maxSpeed):
                speed += 1
            if (speed > maxSpeed):
                speed -= 1
            position = [position[0] + dx *(speed/75), position[1] - dy * (speed/75)]

        
        dx = math.cos(math.radians(degree))
        dy = math.sin(math.radians(degree))
        
        where = playerSettings[0], playerSettings[1]
        playerRotatedImage, rotRect, oldCenter, rotatedSurf = rotation(playerImage, where,degree)
        screen.blit(playerRotatedImage,rotRect)

        pygame.display.update()


