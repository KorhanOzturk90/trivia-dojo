import io
import pickle
import random
from contextlib import redirect_stdout

from trivia import Game

def test_trivia_game():
    input_file = open(f"input.txt", "rb")
    game_output_file = open(f"output.txt", "r")
    game_input = pickle.load(input_file)
    expected_output = game_output_file.read()
    print("\nInput:")
    print(game_input)
    game = Game()

    for player in game_input["players"]:
        game.add(player)
    random.seed(game_input["seed"])

    f = io.StringIO()
    with redirect_stdout(f):
        while True:
            game.roll(random.randrange(5) + 1)

            if random.randrange(9) == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.was_correctly_answered()

            if not not_a_winner: break
    game_output = f.getvalue()

    print("\ngame_output:")
    print(game_output)
    print("\nExpected output:")
    print(expected_output)

    assert game_output == expected_output
