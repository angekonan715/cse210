import random
import string
class PlayerParachute:
    """create a playerParachute oject
    
    responsibility: create and display  a parachute

    Attributes:
        parachute: list( of letter)
        
    """
    
    def __init__(self):
        self.parachute = []
        
    def parachuteList(self):
        
        parachute = [
            "  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
            "   o   ",
            "  /|\  " ,
            "  / \  "   
        ]
        self.parachute = parachute
        return self.parachute
    
    
    # display paracute
    def displayParachute(self):
        print("")
        for i in self.parachute:
            print(i, sep = '')
        print("")
        print('^^^^^^^^')

class Puzzle:
    """create a Puzzle oject
    
    responsibility: create a list of letters, randomly choose 5 letters within that list and append
                    to the list

    Attributes:
        puzzle(hidden) : list
        
    """
    def __init__(self):
        self._puzzle = []
    
    def _secretWordList(self):
        alphabet_string = string.ascii_lowercase
        letters_list = list(alphabet_string)
        i= 0
        while i < 5:
            self._puzzle.append(random.choice(letters_list))
            i += 1
        return self._puzzle
    
class Player:
    """create a Player oject
    
    responsibility: get an input letter from the user

    Attributes:
        playerGuess(hidden) : string
        
    """
    
    def __init__(self):
        self._playerGuess = ''
        
    def player_input(self):
        self._playerGuess = input("Guess a letter [a - z]: ").lower()
        return self._playerGuess
    
    
       
                

class Directory:
    """create a Directory oject
    
    Responsibilities: evaluate user guess and play the game

    Attributes:
        player(hidden): Player()
        puzzle(hidden): Puzzle()
        playerParachute(hidden): playerParachute()
        hiddenWord(hidden): list
        
    """
    
    def __init__(self):
        self._player = Player()
        self._puzzle = Puzzle()
        self._playerParachute = PlayerParachute()
        self._hiddenWord = ['_','_','_','_','_']
        
        
    def guess_r(self, puzzle, guess):
        for item in puzzle:
            if item == guess:
                return True
        
        
    def _startPlaying(self):
        parachute = self._playerParachute.parachuteList()
        puzzle = self._puzzle._secretWordList()
        while (len(parachute) > 3 and puzzle != self._hiddenWord):
            for j in self._hiddenWord:
                print(j, end = ' ')
            print('')
            self._playerParachute.displayParachute()
            guess = self._player.player_input()
            
            is_guess_true = self.guess_r(puzzle, guess)
            if not (is_guess_true):
                del parachute[0]
            else:
                index_item = puzzle.index(guess)
                self._hiddenWord[index_item]= guess
        print("")
        print("============ Game is over =============")


def main():
    director = Directory()
    director._startPlaying()
if __name__ == "__main__":
    main()
