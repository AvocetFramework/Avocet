# type: ignore
import avocet_core

class AvocetReversi:
    def __init__(self):
        self.board = [["." for _ in range(8)] for _ in range(8)]
        self.board[3][3] = "O"; self.board[4][4] = "O"
        self.board[3][4] = "X"; self.board[4][3] = "X"
        self.cursor = [3, 2]

    def handle_keypress(self, key):
        x, y = self.cursor[0], self.cursor[1]
        if key in ['w', 'W'] and y > 0: self.cursor[1] -= 1
        elif key in ['s', 'S'] and y < 7: self.cursor[1] += 1
        elif key in ['a', 'A'] and x > 0: self.cursor[0] -= 1
        elif key in ['d', 'D'] and x < 7: self.cursor[0] += 1
        elif key == ' ' and self.board[y][x] == ".":
            self.board[y][x] = "X"
            self.bot_move()

    def bot_move(self):
        ticks = avocet_core.get_ticks()
        if (ticks % 100) < 20:
            for y in range(8):
                for x in range(8):
                    if self.board[y][x] == ".":
                        self.board[y][x] = "O"
                        return
        else:
            for y in range(8):
                for x in range(8):
                    if self.board[y][x] == ".":
                        self.board[y][x] = "O"
                        return

    def draw(self):
        avocet_core.draw_rect(0, 0, 80, 2, 0x111111)
        avocet_core.kprint("   Avocet Reversi | WASD: Move | Space: Place Piece (X) | Esc: Exit")
        start_x, start_y = 28, 5
        for y in range(8):
            for x in range(8):
                bg = 0x444444 if self.cursor == [x, y] else 0x004400
                avocet_core.draw_rect(start_x + (x * 3), start_y + y, 2, 1, bg)
                avocet_core.kprint(self.board[y][x])

def main():
    game = AvocetReversi()
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
