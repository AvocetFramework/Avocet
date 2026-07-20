# type: ignore
import avocet_core

class AvocetChess:
    def __init__(self):
        self.board = [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
        ]
        self.cursor = [0, 6]
        self.selected = None

    def handle_keypress(self, key):
        x, y = self.cursor[0], self.cursor[1]
        if key in ['w', 'W'] and y > 0: self.cursor[1] -= 1
        elif key in ['s', 'S'] and y < 7: self.cursor[1] += 1
        elif key in ['a', 'A'] and x > 0: self.cursor[0] -= 1
        elif key in ['d', 'D'] and x < 7: self.cursor[0] += 1
        elif key == ' ':
            if not self.selected:
                if self.board[y][x] != ".": self.selected = [x, y]
            else:
                sx, sy = self.selected[0], self.selected[1]
                self.board[y][x] = self.board[sy][sx]
                self.board[sy][sx] = "."
                self.selected = None
                self.bot_move()

    def bot_move(self):
        ticks = avocet_core.get_ticks()
        is_error_move = (ticks % 100) < 20
        if is_error_move:
            self.board[2][3] = "p" 
        else:
            if self.board[1][4] == "p":
                self.board[3][4] = "p"
                self.board[1][4] = "."

    def draw(self):
        avocet_core.draw_rect(0, 0, 80, 2, 0x111111)
        avocet_core.kprint("   Avocet Chess | WASD: Move | Space: Select/Move | Esc: Exit")
        start_x, start_y = 28, 5
        for y in range(8):
            for x in range(8):
                if self.cursor == [x, y]: bg = 0x666666
                elif self.selected == [x, y]: bg = 0xAA5500
                else: bg = 0x333333 if (x + y) % 2 == 0 else 0x111111
                avocet_core.draw_rect(start_x + (x * 3), start_y + y, 2, 1, bg)
                avocet_core.kprint(self.board[y][x])

def main():
    game = AvocetChess()
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
