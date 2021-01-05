from flask import Flask, render_template, flash, request, redirect, session
from flask_session import Session
import game

app = Flask(__name__)
app.secret_key = "kinghorn"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route("/")
def home():
  return render_template('home.html')

#On first load of this page (no players yet)
@app.route("/add-players")
def add_players():
  session['players'] = []
  session['num_players'] = 0
  return render_template('add_players.html')

#Every further load of this page
@app.route("/add",  methods=["GET","POST"])
def add():
  Name = request.form['name']
  players = session.get('players')
  new = game.player(Name)
  session['players'].append(new)
  session['num_players'] = len(players)
  return render_template('add_players.html', players = players)

@app.route("/scoreboard", methods=["GET","POST"])
def add_point():
  num_players = session.get('num_players')
  players = session.get('players')
  x =  game.random(num_players)
  winner = players[x].name
  players[x].add_points(2)
  return render_template('scoreboard.html', players = players)


  

if __name__ == "__main__":
  app.run()