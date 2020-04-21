Jumana's Mastermind \0/

My project is an implementation of the famour board game Mastermind. 
Mastermind is a code breaking game for two players, a code setter and a codebreaker. The code is a pattern of four colored pegs. 
The code breaker attempts to guess the code and receives a score on the accuracy of his/her guess. The score is represented as black and white pegs. 
Black pegs represent the number of colored pegs in their correct position and white pegs represent the number of correct pegs that are not in the correct position. 
The goal of the game is to break the code using the minimum number of guess possible without exceeding ten attempts.
My game gives the player two options, either be code breaker or code setter. 
When codebreaker is selected, the computer genertes a random hidden board and the player starts guessing. After each guess, the player recieves a score.
When codesetter is selected, the player is prompted to enter the code he wants the computer to guess. After each guess, the player assigns the computer a score.

*For my project to work, the following is needed:
1 - Ensure you are using python 64-bit and not 34-bit, you also need to have visual studio installed or run it on mac or linux! (im sorry its complicated)!
2- Have the following libraires installed: 
	- pygame: to install using cmd prompt, type 'pip install pygame'
	- keras: using cmd prompt, type 'pip install keras'
	- tensorflow: using cmd prompt, type 'pip install tensorflow'
	- pandas: using cmd prompt, type 'pip install pandas'
	- numpy: using cmd prompt, type 'pip install numpy'
	- tkinter

If you are using pycharm (aka the best IDE), simply go to file >> settings >> project >> project interpreter >> '+' sign, 
	then lookup any library you wish to install and click 'install package'.

*To run my project after installing all the libraires, open the file mastermind.py and simply click run.

Enjoy the game :)