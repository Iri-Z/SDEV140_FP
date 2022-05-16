# Program name: location
# Author: Iri Zink
# Date: May 15, 2022
# Summary: Class for locations within my text-based rpg


class Location:

    def __init__(self, name, direct, prompt, descript, enter):
        """Contain all the information needed about any possible location """
        self.name = name
        self.direct = direct
        self.prompt = prompt
        self.descript = descript
        self.enter = enter
    def __str__(self):
        #Returns the name of the location
        return "Name: " + self.name

    def Inspect(self):
        #Returns the further inspection description of location
        statement = "You've decided to look around at your surroundings. \n" + self.descript
        return statement

    def Leave(self):
        #Statement to skip over most dialogue and reach the end
        statement = "You've decided to go straight home and be done with any nonsense. Restart or Exit."
        return statement

    def Lost(self):
        #returns current location
        statement = "You are currently in the " + self.name + " location!"
        return statement
    def Reward(self):
        #returns reward statement for reaching the end of the game
        statement = """Very well, this shall be granted to you. May the outcome be as you dream it.
                    \n You awake in your own bed, drenched, and feeling as though things have been irreversibly altered in your life.
                    \n Restart or Exit"""
        return statement 
    

