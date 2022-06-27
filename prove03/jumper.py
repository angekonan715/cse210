import random
import string
class PlayerParachute:
    
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
    
    def displayParachute(self):
        print("")
        for i in self.parachute:
            print(i, sep = '')
        print("")
        print('^^^^^^^^')

class Puzzle:
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
    
    def secretWord(self):
        secretWord = ''.join(self._puzzle)
        return secretWord

class Player:
    
    def __init__(self):
        self.playerGuess = ''
        self.is_guess_r = True
        
    def player_input(self):
        self.playerGuess = input("Guess a letter [a - z]: ").lower()
        return self.playerGuess
    
    
       
                

class Directory:
    
    def __init__(self):
        self._player = Player()
        self._puzzle = Puzzle()
        self._playerParachute = PlayerParachute()
        self._hiddenWord = ['_','_','_','_','_']
        
        
    def guess_r(self, puzzle, guess):
        for item in puzzle:
            if item == guess:
                return True
                
    
        
        
    def startPlaying(self):
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
                self._playerParachute.displayParachute()
                print(puzzle)
            else:
                index_item = puzzle.index(guess)
                self._hiddenWord[index_item]= guess
        print("")
        print("============ Game is over =============")


def main():
    director = Directory()
    director.startPlaying()
if __name__ == "__main__":
    main()
