from Game import Game

game = Game()

while True:
    game.reset_game()
    while not game.get_turn():
        pass
    input("Натисніть ентер щоб грати ще раз!!!")