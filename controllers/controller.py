from flask import render_template
from app import app
from model.game import Game
from model.player import Player



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

