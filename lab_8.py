from Game import Game
from Num_pic import Num_pic
game = Game(Num_pic())

while True:
    game.reset_game()
    while not game.get_turn():
        pass
    input("Натисніть ентер щоб грати ще раз!!!")