# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetFileBrowser(Window):
    def __init__(self):
        super().__init__(44, 14, "Avocet Virtual Storage Explorer", 0x222C33)
        self.files = [
            " [DIR]  ..",
            " [DIR]  avocet_ui_lib",
            " [DIR]  desktop_shell",
            " [FILE] link.ld  (1 KB)",
            " [FILE] main.c   (2 KB)",
            " [FILE] boot.asm (3 KB)"
        ]
        self.cursor = 1

    def handle_keypress(self, key):
        if key in ['w', 'W'] and self.cursor > 0: self.cursor -= 1
        elif key in ['s', 'S'] and self.cursor < len(self.files) - 1: self.cursor += 1

    def draw(self):
        super().draw()
        current_y = self.absolute_y + 3
        for i, f in enumerate(self.files):
            bg = 0x555555 if i == self.cursor else self.bg_color
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, bg)
            color = 0x00FFFF if "[DIR]" in f else 0xFFFFFF
            lbl = Label(f, color)
            lbl.absolute_x = self.absolute_x + 3
            lbl.absolute_y = current_y
            lbl.draw()
            current_y += 1

def main():
    avocet_core.clear_screen()
    browser = AvocetFileBrowser()
    browser.absolute_x = 18
    browser.absolute_y = 5
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        browser.update(18, 5, 44, 14)
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        if char: browser.handle_keypress(char)
        avocet_core.sleep(40)

if __name__ == "__main__":
    main()
