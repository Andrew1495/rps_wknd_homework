import unittest
from model.game import Game
from model.player import Player

class TestGame(unittest.TestCase):

    def test_rock_rock(self):
        self.player1 = Player("bob", "rock")
        self.player2 = Player("frank", "rock")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(None, winner)

    def test_rock_paper(self):
        self.player1 = Player("bob", "rock")
        self.player2 = Player("frank", "paper")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player2, winner)

    def test_rock_scissor(self):
        self.player1 = Player("bob", "rock")
        self.player2 = Player("frank", "scissors")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player1, winner)

    def test_paper_paper(self):
        self.player1 = Player("bob", "paper")
        self.player2 = Player("frank", "paper")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(None, winner)

    def test_paper_rock(self):
        self.player1 = Player("bob", "paper")
        self.player2 = Player("frank", "rock")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player1, winner)

    def test_paper_scissors(self):
        self.player1 = Player("bob", "paper")
        self.player2 = Player("frank", "scissors")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player2, winner)

    def test_scissors_scissors(self):
        self.player1 = Player("bob", "scissors")
        self.player2 = Player("frank", "scissors")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(None, winner)

    def test_scissors_rock(self):
        self.player1 = Player("bob", "scissors")
        self.player2 = Player("frank", "rock")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player2, winner)

    def test_scissors_paper(self):
        self.player1 = Player("bob", "scissors")
        self.player2 = Player("frank", "paper")
        self.game = Game(self.player1, self.player2)
        winner = self.game.play_game()
        self.assertEqual(self.player1, winner)