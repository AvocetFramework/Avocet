# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetCalculator(Window):
    def __init__(self):
        super().__init__(40, 14, "Avocet Grid Calculator", 0x252525)
        self.expression = ""
        self.result = "0"
        self.ui_grid = [
            "[ 7 ]  [ 8 ]  [ 9 ]  [ / ]",
            "[ 4 ]  [ 5 ]  [ 6 ]  [ * ]",
            "[ 1 ]  [ 2 ]  [ 3 ]  [ - ]",
            "[ C ]  [ 0 ]  [ = ]  [ + ]"
        ]

    def handle_keypress(self, key):
        if key in "0123456789+-*/":
            if len(self.expression) < 18:
                self.expression += key
        elif key in ["\n", "="]:
            self.result = "125"  
            self.expression = ""
        elif key in ["c", "C"]:
            self.expression = ""
            self.result = "0"

    def draw(self):
        super().draw()
        
        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 2, self.width - 4, 2, 0x000000)
        
        display_str = self.expression if self.expression else self.result
        expr_lbl = Label(display_str, 0x00FF00)
        expr_lbl.absolute_x = self.absolute_x + 4
        expr_lbl.absolute_y = self.absolute_y + 2
        expr_lbl.draw()

        current_y = self.absolute_y + 5
        for row in self.ui_grid:
            avocet_core.draw_rect(self.absolute_x + 2, current_y, self.width - 4, 1, self.bg_color)
            row_lbl = Label(row, 0xFFFFFF)
            row_lbl.absolute_x = self.absolute_x + 6
            row_lbl.absolute_y = current_y
            row_lbl.draw()
            current_y += 2

def main():
    avocet_core.clear_screen()
    calc = AvocetCalculator()
    calc.absolute_x = 20
    calc.absolute_y = 5

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        calc.update(20, 5, 40, 14)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char == '\x1b':
            break
        if char:
            calc.handle_keypress(char)
            
        avocet_core.sleep(30)

if __name__ == "__main__":
    main()
