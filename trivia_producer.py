import pickle
import random

from trivia import Game
import contextlib

if __name__ == '__main__':
    player_pool = ["Robert", "Andy", "Sam", "Korhan"]
    input = {"seed": 41, "players": player_pool}
    # seed_pool = [7, 11, 31]
    # players = random.choices(player_pool, weights=[10, 1, 1, 1], k=random.randint(2, 4))
    seed = 41
    with open('input.txt', 'wb') as f_inp:
        # f_inp.write(player_pool + "\n" + seed)
        pickle.dump(input, f_inp)
    with open('output.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            game = Game()
            for player in player_pool:
                game.add(player)

            random.seed(seed)
            while True:
                game.roll(random.randrange(5) + 1)

                if random.randrange(9) == 7:
                    not_a_winner = game.wrong_answer()
                else:
                    not_a_winner = game.was_correctly_answered()

                if not not_a_winner: break