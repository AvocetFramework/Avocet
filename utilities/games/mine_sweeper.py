# type: ignore
import avocet_core

class AvocetMinesweeper:
    def __init__(self):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.revealed = [[False for _ in range(8)] for _ in range(8)]
        self.cursor = [0, 0]
        self.grid[1][2] = -1; self.grid[3][5] = -1; self.grid[6][4] = -1
        self.game_over = False

    def handle_keypress(self, key):
        if key in ['w', 'W'] and self.cursor[1] > 0: self.cursor[1] -= 1
        elif key in ['s', 'S'] and self.cursor[1] < 7: self.cursor[1] += 1
        elif key in ['a', 'A'] and self.cursor[0] > 0: self.cursor[0] -= 1
        elif key in ['d', 'D'] and self.cursor[0] < 7: self.cursor[0] += 1
        elif key == ' ':
            self.revealed[self.cursor[0]][self.cursor[1]] = True
            if self.grid[self.cursor[0]][self.cursor[1]] == -1: self.game_over = True

    def draw(self):
        avocet_core.draw_rect(0, 0, 80, 2, 0x111111)
        avocet_core.kprint("   Avocet Minesweeper | WASD: Navigate | Space: Reveal | Esc: Exit")
        start_x = 28
        start_y = 6
        for y in range(8):
            for x in range(8):
                bg = 0x555555 if self.cursor == [x, y] else (0x222222 if self.revealed[x][y] else 0x444444)
                avocet_core.draw_rect(start_x + (x * 3), start_y + (y * 2), 2, 1, bg)
                if self.revealed[x][y]:
                    char = "*" if self.grid[x][y] == -1 else str(self.grid[x][y])
                    avocet_core.kprint(char)
        if self.game_over:
            avocet_core.draw_rect(30, 22, 20, 1, 0xFF0000)
            avocet_core.kprint("   BOOM! GAME OVER   ")

def main():
    game = AvocetMinesweeper()
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
