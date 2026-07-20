# type: ignore
import avocet_core

class AvocetTicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.cursor = 0
        self.turn = "X"
        self.winner = None

    def handle_keypress(self, key):
        if self.winner: return
        if key in ['w', 'W'] and self.cursor >= 3: self.cursor -= 3
        elif key in ['s', 'S'] and self.cursor <= 5: self.cursor += 3
        elif key in ['a', 'A'] and self.cursor % 3 > 0: self.cursor -= 1
        elif key in ['d', 'D'] and self.cursor % 3 < 2: self.cursor += 1
        elif key == ' ' and self.board[self.cursor] == " ":
            self.board[self.cursor] = "X"
            self.check_winner()
            if not self.winner:
                self.turn = "O"
                self.bot_move()

    def bot_move(self):
        empty = [i for i, v in enumerate(self.board) if v == " "]
        if not empty: return
        ticks = avocet_core.get_ticks()
        if (ticks % 100) < 20:
            move = empty[ticks % len(empty)]
        else:
            for win_line in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
                vals = [self.board[i] for i in win_line]
                if vals.count("O") == 2 and vals.count(" ") == 1:
                    move = win_line[vals.index(" ")]
                    break
            else:
                move = empty[0]
        self.board[move] = "O"
        self.check_winner()
        self.turn = "X"

    def check_winner(self):
        for l in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if self.board[l[0]] == self.board[l[1]] == self.board[l[2]] != " ":
                self.winner = self.board[l[0]]
        if " " not in self.board and not self.winner: self.winner = "Draw"

    def draw(self):
        avocet_core.draw_rect(0, 0, 80, 2, 0x111111)
        avocet_core.kprint("   Tic-Tac-Toe | WASD: Move | Space: Place X | Esc: Exit")
        start_x, start_y = 34, 8
        for i in range(9):
            x, y = i % 3, i // 3
            bg = 0x555555 if self.cursor == i else 0x222222
            avocet_core.draw_rect(start_x + (x * 4), start_y + (y * 3), 3, 2, bg)
            avocet_core.kprint(self.board[i])
        if self.winner:
            avocet_core.draw_rect(30, 20, 20, 1, 0xE95420)
            avocet_core.kprint(" Winner: " + self.winner)

def main():
    game = AvocetTicTacToe()
    avocet_core.clear_screen()
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        game.draw()
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        if char: game.handle_keypress(char)
        avocet_core.sleep(40)

if __name__ == "__main__":
    main()
