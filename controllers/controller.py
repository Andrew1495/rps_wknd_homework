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
        p1_picked= f"{player1.name} picked: {player1.choice}"
        p2_picked = f"{player2.name} picked: {player2.choice}"
        win = f"Its a draw"
    else:
        p1_picked= f"{player1.name} picked: {player1.choice}"
        p2_picked = f"{player2.name} picked: {player2.choice}"
        win = f"The winner is: {winner.name}"
        
    return render_template("index.html", win=win, p1_picked=p1_picked, p2_picked=p2_picked)

@app.route('/rules')
def rule():
    return render_template("rules.html")

@app.route('/computer')
def computer():
    return render_template("computer.html")

@app.route('/computer',  methods=["POST"])
def computers():


    random_number = random.randint(1, 3)
    if random_number == 1:
        cp_choice = "rock"
    elif random_number == 2:
        cp_choice = "paper"
    else:
        cp_choice = "scissors"


    computer = Player("Computer", cp_choice)
    player_name = request.form['name']
    player_choice = request.form['choose']

    user = Player(player_name, player_choice)

    game1 = Game(user, computer)
    winner = game1.play_game()
    if winner == None:
        p1_picked= f"{user.name} picked: {user.choice}"
        p2_picked = f"{computer.name} picked: {computer.choice}"
        win = f"Its a draw, play again"
        return render_template("draw.html", win=win ,p1_picked=p1_picked, p2_picked=p2_picked)
    elif winner == computer:
        p1_picked= f"{user.name} picked: {user.choice}"
        p2_picked = f"{computer.name} picked: {computer.choice}"
        win = f"The winner is: {winner.name}"
        return render_template("comp_win.html", win=win ,p1_picked=p1_picked, p2_picked=p2_picked)
    elif winner == user:
        p1_picked= f"{user.name} picked: {user.choice}"
        p2_picked = f"{computer.name} picked: {computer.choice}"
        win = f"The winner is: {winner.name}"
        return render_template("user_win.html", win=win ,p1_picked=p1_picked, p2_picked=p2_picked)



