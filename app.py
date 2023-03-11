from flask import Flask, request, render_template, jsonify
from uuid import uuid4


from boggle import BoggleGame



app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    game_data = {"gameId": game_id, "board": game.board}
    return jsonify(game_data)

@app.post("/api/score-word")
def score_word():
    """Check if word is valid and score.
    Accepts JSON of game ID and word"""
    word = request.json["word"]
    game_id = request.json["gameId"]
    print("word", word)
    #request.json
    #is_word_in_word_list(word)
    #check_word_on_board(word)
    #is_word_not_a_dup(word)
    #play_and_score_word(word)
    game = games[game_id]
    game.is_word_in_word_list(word)
    game.check_word_on_board(word)
    game.is_word_not_a_dup(word)
    game.play_and_score_word(word)
    
    if not game.is_word_in_word_list(word):
        return jsonify(result:"not-word")
    elif not game.check_word_on_board(word):
        return jsonify(result:"not-on-board")
    elif not game.is_word_not_a_dup(word):
        return jsonify(result:"is-duplicate")
    else game.play_and_score_word(word):
        return jsonify(result: )