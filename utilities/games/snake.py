# type: ignore
import avocet_core

class AvocetSnake:
    def __init__(self):
        self.snake = [[15, 10], [14, 10], [13, 10]]
        self.direction = [1, 0]
        self.apple = [25, 12]
        self.score = 0
        self.game_over = False

    def handle_keypress(self, key):
        if key in ['w', 'W'] and self.direction !=: self.direction = [0, -1]
        elif key in ['s', 'S'] and self.direction != [0, -1]: self.direction = [0, 1]
        elif key in ['a', 'A'] and self.direction !=: self.direction = [-1, 0]
        elif key in ['d', 'D'] and self.direction != [-1, 0]: self.direction = [1, 0]

    def update(self):
        if self.game_over: return
        new_head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
        if new_head[0] < 2 or new_head[0] >= 78 or new_head[1] < 4 or new_head[1] >= 22 or new_head in self.snake:
            self.game_over = True
            return
        self.snake.insert(0, new_head)
        if new_head == self.apple:
            self.score += 10
            self.apple = [(new_head[0] * 7 + 13) % 74 + 2, (new_head[1] * 3 + 7) % 17 + 4]
        else:
            self.snake.pop()

    def draw(self):
        avocet_core.draw_rect(2, 4, 76, 18, 0x1A1A1A)
        avocet_core.draw_rect(self.apple[0], self.apple[1], 1, 1, 0xFF0000)
        for segment in self.snake:
            avocet_core.draw_rect(segment[0], segment[1], 1, 1, 0x00FF00)
        avocet_core.draw_rect(0, 0, 80, 2, 0x111111)
        avocet_core.kprint("   Avocet Snake | Score: " + str(self.score) + " | WASD to Move | Esc: Exit")
        if self.game_over:
            avocet_core.draw_rect(30, 10, 20, 3, 0x000000)
            avocet_core.kprint("    GAME OVER!   ")

def main():
    game = AvocetSnake()
    avocet_core.clear_screen()
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        game.draw()
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        if char: game.handle_keypress(char)
        game.update()
        avocet_core.sleep(100)

if __name__ == "__main__":
    main()
