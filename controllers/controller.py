from flask import render_template , redirect, request
from app import app
from model.game import Game
from model.player import Player
import random


@app.route('/game')
def index():
    return render_template('index.html')


@app.route('/<p1_choice>/<p2_choice>')
def play(p1_choice, p2_choice):
    player1 = Player("player1", p1_choice)
    player2 = Player("player2", p2_choice)
    game = Game(player1, player2)
    winner = game.play_game()
    if winner == None:
        win = f"Its a draw"
    else:
        win = f"The winner is:{winner.name}"
    return render_template("index.html", win=win)

@app.route('/rules')
def rule():
    return render_template("rules.html")

@app.route('/computer')
def computer():
    return render_template("computer.html")

@app.route('/computers',  methods=["GET", "POST"])
def computers():
    random_number = random.randint(1, 3)
    if random_number == 1:
        cp_choice = "rock"
    elif random_number == 2:
        cp_choice = "paper"
    else:
        cp_choice = "scissors"
    player2 = Player("Computer", cp_choice)
    player_name = request.form['name']
    player_choice = request.form['choose']

    player1 = Player(player_name, player_choice)

    game = Game(player1, player2)
    if winner == None:
        win = f"Its a draw"
    else:
        win = f"The winner is:{winner.name}"
    return render_template("computer.html", win=win)


