class Hangman_pic:
    def __init__(self):
        self.curent_frame = 0
        self.pictures = ['''
+---+
    |
    |
    |
   ===''','''
+---+
  0 |
    |
    |
   ===''','''
+---+
  0 |
  | |
    |
   ===''','''
+---+
  0 |
 /| |
    |
   ===''','''
+---+
  0 |
 /|\|
    |
   ===''','''
+---+
  0 |
 /|\|
 /  |
   ===''','''
+---+
  0 |
 /|\|
 / \|
   ===''']

    def get_frame(self, n):
        return self.pictures[n]

    def get_curent_frame(self):
        return self.pictures[self.curent_frame]

    def to_next_frame(self):
        self.curent_frame += 1
        if self.curent_frame >= len(self.pictures):
            self.curent_frame = 0
        return self.curent_frame

    def get_curent_frame_index(self):
        return self.curent_frame

    def reset_frame(self):
        self.curent_frame = 0

    def get_max_frame_num(self):
        return len(self.pictures)