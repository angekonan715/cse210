#Prove03 : Jumper Specification
#Prove03 : Jumper Specification

## PlayerParachute Object
It creates a parachute using a list called parachute.
It also display the elements of the parachute list in a column.
It has two methods namely pararachuteList and dispalay parachute

## Puzzle object
puzzle object use the build-in mathods random and strings.
Its main reaponsibility is to create a random list of 5 letters chosen from [a-z] alphabet.
It has one a member variable called puzzle which is hidden from the user and stores an initial empty list.
It has an hidden mathod called secretWordList which purpose is to return a random list of letters.

## Player object
Its main responsibility is to get an input from the user and store it in hidden class variable
called playerGuess.
It has a method call player_input

## Diectory Object
It has the responsibility to evaluate the user guess , compares it to the item in the puzzle list 
and play the game. 
- If the guess is correct, the letter is revealed.
- If the guess is incorrect, a line is cut on the player's parachute.
- If the puzzle is solved the game is over.
- If the player has no more parachute the game is over.
It has two methods namely guess_r( is the guess of the user right?) and startPlaying game.
