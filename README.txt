READ ME 
ZinkIri_FP Folder
Simple RP Game

User Manual

Introduction:
This is a simple text based RPG that wull give the user prompts to decide how they would like to continue the story.

Instructions:
Run myGame.py from the command line or IDLE. 
A window will open and provide prompts.
Type what you'd like to do from the prompts given, the program will search for keywords to move the user to new locations.
You are always free to look around at your surroundings to make an informed decision by typing inspect or look.
You can go back one location, but need to restart the game to go back more, type restart to do so.
You can be reminded of your current location by typing lost or where.
General key terms that can always be used are 'help', 'info', 'instructions', 'inspect', 'look', 'where', 'lost', 'leave', 'back'.
Specific key terms for the current location can be found from clicking the Instructions button or typing help/info/instructions.

Details for operation:
Each location is stored as it's own class object and contains: name, directions, prompt, description, enter phrase.
Based on user input the program will move to new locations and display the enter text and new prompt. If the user decides 
to investigate further then there is an extra description. The directions stores the key terms for moving to new locations from 
the current one. These, along with the genreral terms, are the only phrases that can progress the game to a new location. The final location
has unique responses to input as there are no more locations to move to. 

Layout:
The top row of the GUI is dedicated to the labels that will be changed depending on the prompt for that location.
The second row is dedicated to the text input field that is cleared after input. 
The third row is dedicated to three buttons: back, Instructions, Enter.
	The back button will return you to the last location, but no further.
	Instructions will display the instructions, what the current specific key terms are, and the current prompt again.
	Enter is the only way to submit a user response and must be clicked to progress the game. Cannot use enter key on keyboard.

Key notes:
Can only exit game by closing window manually, there are no key terms to exit. 
Can restart at any time.
Can access instructions at any time. 