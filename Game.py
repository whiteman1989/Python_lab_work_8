from Hangman_pic import Hangman_pic
import subprocess

from random import randint

class Game:
    def __init__(self, pic = Hangman_pic()):
        self.words = 'аист акула бабуин барсук бобр бык верблюд'.split()
        self.secret_word = ''
        self.missed_letters = ''
        self.correct_letters = ''
        self.hangman = pic

    def get_random_word(self):
        return self.words[randint(0, len(self.words)-1)]

    def set_random_word(self):
        self.secret_word = self.get_random_word()

    def reset_game(self):
        self.missed_letters = ''
        self.correct_letters = ''
        self.set_random_word()

    def manula_reset_game(self):
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word = input("загадайте слово: ")

    def display_board(self):
        subprocess.call('cls', shell=True) # clear windows 
        print(self.hangman.get_curent_frame())
        print()
        print('Помилкові букви:', self.missed_letters)
        print()
        blanks = '_'*len(self.secret_word)
        for i in range(len(self.secret_word)):
            if self.secret_word[i] in list(self.correct_letters):
                blanks = blanks[:i] + list(self.secret_word)[i] + blanks[i+1:]
        print(' '.join(map(str, list(blanks))))
        print()

    def get_guess(self):
        while True:
            guess = input('Введіть букву: ')
            if len(guess) != 1:
                print("Введіть 1 букву!")
            elif guess in list(self.missed_letters+self.correct_letters):
                print("Ви вже називали цю букву, назвіть іншу!")
            else:
                return guess

    # returns true if game is done
    def get_turn(self):
        self.display_board()
        guess = self.get_guess()
        if guess in self.secret_word:
            self.correct_letters+=guess
            if len(set(self.secret_word)) == len(set(self.secret_word).intersection(set(self.correct_letters))):
                print("Так секретне слово -", self.secret_word, "Ви виграли")
                return True
        else:
            self.missed_letters+=guess
            self.hangman.to_next_frame()
            if len(self.missed_letters) >= self.hangman.get_max_frame_num():
                print("Ви вичерпали усі спроби!")
                print("Не вгадано букв:", len(self.secret_word)-len(self.correct_letters))
                print("Слово:", self.secret_word)
                return True
        return False
