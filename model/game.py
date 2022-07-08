from model.player import Player


class Game:
    def __init__(self, input_p1, input_p2):  
        self.player1 = input_p1
        self.player2 = input_p2


    def play_game(self):
        if self.player1.choice == 'rock' and self.player2.choice == 'rock':
            return 

        if self.player1.choice == 'rock' and self.player2.choice == 'paper':
            return self.player2

        if self.player1.choice == 'rock' and self.player2.choice == 'scissor':
            return self.player1

        if self.player1.choice == 'paper' and self.player2.choice == 'paper':
            return 

        if self.player1.choice == 'paper' and self.player2.choice == 'rock':
            return self.player1

        if self.player1.choice == 'paper' and self.player2.choice == 'scissor':
            return self.player2

        if self.player1.choice == 'scissor' and self.player2.choice == 'scissor':
            return 

        if self.player1.choice == 'scissor' and self.player2.choice == 'rock':
            return self.player2
        if self.player1.choice == 'scissor' and self.player2.choice == 'paper':
            return self.player1