
import Tkinter as tk
import pygame


LARGE_FONT= ("Verdana", 12)


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

        global manual
        manual = tk.PhotoImage(file = "manual.gif")

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

##def MakeTrack():
    
    
menu = Menu()

windowWidth = 800
windowHeight = 400
display = (windowWidth, windowHeight)

# sets up the window for pygame
gameDisplay = pygame.display.set_mode(display)

playGame = 1
while(playGame):

    menu.mainloop()
    MGet()
##    gameDisplay.blit("grass.gif",
