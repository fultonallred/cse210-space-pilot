Space Pilot

Getting Started:

	Have Python 3.11 or newer and Raylib Python CFFI 3.7 installed.
	
	Open a terminal and browse to the source code file (Space_Pilot) and run py __main__.py
	Alternatively, run __main__.py from your IDE.

File Structure:

root
Space_Pilot (source code)
	game (specific game classes)
		casting
		directing
		scripting
		services
		shared
	__main__.py (entry point)
	constants.py
	README.txt

How to play:
	The goal is to stay alive by avoiding colliding with minerals and the (maybe not so occasional) asteroid.
	Move with WASD. Collect red stationary cells to gain power. Press space to fire yoru lasers when you have power. 
	Minerals will die in one shot, but asteroids will take a few more. Shooting minerals will improve the power cells you
	pick up. Currently asteroids destroyed is logged in the terminal. See how many you can kill!

Authors:
	Fulton Allred (all21037@byui.edu)
	based on code from Cycle written by Matt Manley (manleym@byui.edu).