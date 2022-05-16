# Program name: myGame
# Author: Iri Zink
# Date: May 15, 2022
# Summary: The main file controlling the functionality of my text-based rpg

"""The main python file for my final project: a text-based rpg."""
from location import Location
from breezypythongui import EasyFrame

#Other key terms that can be entered
keyTerms = ['help', 'info', 'instructions', 'inspect', 'look', 'where', 'lost', 'leave', 'back']

#Game Instructions
INSTRUCTIONS = """Type what you'd like to do from the prompts given.
\n You are always free to look around at your surroundings to make an informed decision by typing inspect or look.
\n You can go back one location, but need to restart the game to go back more, type restart to do so.
\n You can be reminded of your current location by typing lost or where.
\n Key terms are: """ + str(keyTerms)

#ERROR MSG for incorrect input
ERMSG = "That answer was not recognized, please pick from the options given."

#All Game Locations
# name, directions, prompt, description, enter phrase
Start = Location("Start",
                 ("walk", "bus"),
                 "You've just got out of work, would you like to walk home or take the bus?",
                 """You're standing outside a nondescript building, you just got out of there for the day and are not eager to return before you need to.
                 \n You see the path home that you can walk in about 45 minutes and can be refreshing on a clear day.
                 \n The sky is clouded over and the air feels heavy with rain and so you eye the nearby bustop that says your bus home will be here any minute.""",
                 "This is the starting location.")
Walk = Location("Walk",
                ("bus", "home"),
                "As you start down your path heavy drops of rain hit the top of your head. \n Do you power through it home or turn back to try and make your bus?",
                "The path is mostly empty as everyone else has taken shelter from the incoming storm. \n You are likely to be soaking wet by the time you get home.",
                "You decide that the fresh air will be good from you and you're in no rush to get home.")
Bus = Location("Bus",
               ("off", "stay"),
               "Do you get off at this stop or stay on to go home?",
                "The forest seems to be calling you to get off the bus. \n You get the feeling you will never get the opportunity to find out what this is if you stay on the bus.",
               """You decide it's best to get out of this weather and take the bus home.
                \n Surely enough the bus pulls up just in time to shield you from the rain.
                \n You hurry to get on and out of the cold.
                \n As it carries on its way a particular stop that is not yours catches your interest.""")
Stay = Location("Stay on Bus",
                ("home"),
                "You are headed home now. Hit enter to continue.",
                "You've stayed on the bus and are headed home",
                "You decide it best not to brave the elements for the strange call from the forest and stay on the bus.")
Home = Location("Home",
                (),
                "This is is it, you are home. \n You settle in for the night. \n Type restart to try again or exit.",
                """Over a warm cup of cocoa you look out the window towards the calling as in gentlely fades into the night.
                \n You know you'll never find out what it was and that is just fine with you.""",
                "Finally, you have reached your home.")
Off = Location("Get off at busstop",
               ("home", "forest"),
               "Do you answer the call and enter the forest or turn away and try to make it back home from here?",
               "You're standing at the bus stop all alone. \n You'll either have to walk home from here of go into the forest.",
               "You quickly signal the bus to stop and get off. \n It pulls away, leaving you in the pouring rain to gaze into the darkness of the forest as it beckons you in.")
Forest = Location("Forest",
                  ("bus", "pool", "overpass", "trees"),
                  """There seems to be three distictive spots you can head towards:
                    \n a small pool of water, \n a large overpass that towers above the trees,
                    \n and an interesting outlet of trees that don't look like the rest.
                    \n Which do you head towards?""",
                  "The pool seems to have a mystical glint to it.",
                  "You're already soaking wet, why abandon the call now. You enter the forest.")
Pool = Location("Pool",
                ("forest", "overpass", "trees", "water"),
                "Would you like to enter the water or go to one of the other spots?",
                """ The pouring rain seems to lighten as you walk here.
                    \n The shimmering water looks a deep blue, nothing like the muddy puddle you expected it to be, much deeper than it realistically could ever be.
                    \n As you circle the outside a glimmer in the depths seems to get stronger and stronger, pulsing just as your own heartbeat seems to be getting deafening.
                    \n This is the call, it wants you to step into the water.""",
                "You go to the pool of water and it would seem awfully nice to dip your feet in.")
Overpass = Location("Overpass",
                    ("forest", "pool", "trees"),
                    "Would you like to go to one of the other spots?",
                    "The rumbling of cars and pouring rain mix as you get a bit of shelter from the weather. There's bits of trash scattered around the area and the call gets quieter.",
                    "You go to the overpass and see nothing out of the ordinary.")
Trees = Location("Trees",
                 ("forest", "pool", "overpass"),
                 "Would you like to go to the other spots?",
                 """On closer inspection, there doesn't seem to be anything unusual about them, other than the shadows being thrown by the passing traffic.
                 \n You do start to notice how dark it is getting and how the cold is settling into you.
                 \n Best to hurry out of this weather.""",
                 "You go to the clearing of strange trees.")
Water = Location("Water",
                 ("leave"),
                 "What would you like?",
                 "It seems that you are being offered anything you could dream of: power, money, anything. What is it that you desire?",
                 "You enter the water. Everything seems still for a moment. Suddenly the water rushes upwards, enveloping you, and you hear a voice.")
End = Location("End",
               (),
               "",
               "",
               "")

#Code begins here
#Class for GUI display
class GameGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Game", width = 850, height = 250)

        self.start = True
        self.current = Start
        self.last = Start
        self.answer = ''
        #Divide screen into sections
        dataPanel = self.addPanel(row= 0, column=0)
        textPanel = self.addPanel(row= 1, column=0)
        buttonPanel = self.addPanel(row = 2, column = 0)
        #Create labels so that all text is in correct locations
        dataPanel.addLabel(text='', row=0, column=0)
        textPanel.addLabel(text='', row=0, column=0)
        #label for all game instructions
        self.textLabel = dataPanel.addLabel(text = "Welcome to the game! \n Type next to start:", row=0, column = 1, sticky = 'W')
        #Text field for answers
        self.inputField = textPanel.addTextField(text = "", row=0, column=1, width=60, sticky = "N" + "W")
        #Create all buttons
        self.enter_button = buttonPanel.addButton(text = "Enter", row = 0, column = 2, command = self.loopControl)
        self.help_button = buttonPanel.addButton(text = "Instructions", row = 0, column = 1, command = self.getHelp)
        self.back_button = buttonPanel.addButton(text = "Back", row = 0, column = 0, command = self.back)

    def loopControl(self, progress=False):
        #Determines what if the input is correct and moves to new location
        if self.start:
            self.textLabel['text'] = (self.current.enter + '\n' + self.current.prompt)
            self.in_Progress = True
            self.start= False
            self.inputField.setText("")
            if any(str_ in self.answer.lower() for str_ in keyTerms):
                self.keyTerms()
        else:
            self.answer = self.inputField.getText()
            self.inputField.setText("")
            if self.current == Water:
                if any(str_ in self.answer.lower() for str_ in keyTerms):
                    self.keyTerms()
                else: 
                    self.textLabel['text']= self.current.Reward()
                    self.current = End
            elif self.current == Stay:
                self.current = Home
                self.textLabel['text']= (self.current.enter + '\n' + self.current.prompt)
            elif any(str_ in self.answer.lower() for str_ in self.current.direct):
                for i in self.current.direct:
                    if i in self.answer.lower():
                        self.last = self.current
                        self.current = eval(i.capitalize())
                        self.textLabel['text']= (self.current.enter + '\n' + self.current.prompt)
            elif any(str_ in self.answer.lower() for str_ in keyTerms):
                self.keyTerms()
            elif self.answer.lower() == "restart":
                self.textLabel['text']= self.RestartGame()
            else:
                self.textLabel['text']= ERMSG + "\n The current key terms for new locations are: " + str(self.current.direct) + "\n" + self.current.prompt


    def getHelp(self):
        #Displays the instructions
        self.textLabel['text']= (INSTRUCTIONS + "\n The current key terms for new locations are: " + str(self.current.direct)) + "\n" + self.current.prompt
        return
    
    def back(self):
        #Sets the current location to the last one
        self.current = self.last
        self.textLabel['text']= (self.current.prompt)
        return
    
    def keyTerms(self):
        #Finds which keyterm was used and returns appropriate info
        if keyTerms[0] in self.answer.lower() or keyTerms[1] in self.answer.lower() or keyTerms[2] in self.answer.lower():
            self.getHelp()
        elif keyTerms[3] in self.answer.lower() or keyTerms[4] in self.answer.lower():
            self.textLabel['text']= self.current.Inspect() + "\n" + self.current.prompt
        elif keyTerms[5] in self.answer.lower() or keyTerms[6] in self.answer.lower():
            self.textLabel['text']= self.current.Lost() + "\n" + self.current.prompt
        elif keyTerms[7] in self.answer.lower():
            self.textLabel['text']= self.current.Leave
        elif keyTerms[8] in self.answer.lower():
            self.textLabelself.textLabel['text']= ("You went back to " + current.name + " location.")
            self.back()
    
    def RestartGame(self):
        #Restarts the game at the starting location
        self.textLabel['text'] = "You've restarted the game! \n Type next to continue:"
        self.start = True
        self.current = Start
        self.last = Start

def main():
    GameGUI().mainloop()

main()

        
