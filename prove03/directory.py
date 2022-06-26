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
        self.is_guessRight = True
        
    def player_input(self):
        self.playerGuess = input("Guess a letter [a - z]: ").lower()
        return self.playerGuess
    
    def guess_r(self):
        return self.is_guess
    
    def guess_w(self):
        self.is_guessRight = False
        return self.is_guessRight
                

class Directory:
    
    def __init__(self):
        self._player = Player()
        self._puzzle = Puzzle()
        self._playerParachute = PlayerParachute()
        self._hiddenWord = ['_','_','_','_','_']
        
    def startPlaying(self):
        
        parachute = self._playerParachute.parachuteList()
        puzzle = self._puzzle._secretWordList()
        for j in self._hiddenWord:
            print(j, end = ' ')
        print('')
        for s in parachute:
            print(s, sep = '')
        print('^^^^^^^^')
        guess = self._player.player_input()
        for item in puzzle:
            if (item != guess):
                parachute = parachute
            else:
                index_item = puzzle.index(guess)
                print(index_item)
                self._hiddenWord[index_item]= guess
        print(self._hiddenWord)
        print(puzzle)
                
                
               
                
        
        
        
d = Directory()
d.startPlaying()

