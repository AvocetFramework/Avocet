# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetMarkdownViewer(Window):
    def __init__(self):
        super().__init__(54, 14, "Avocet Markdown Reader v1.0", 0x222222)
        self.doc_lines = [
            "# AVOCET OS FRAMEWORK",
            "=====================",
            "* Core Language: Python & C Engine",
            "* Architecture: Freestanding 32-Bit Protected Mode",
            "* Graphics Layer: Avocet UI Toolkit Clone Layout",
            "",
            "## Getting Started",
            "Type 'help' in the terminal window to query commands."
        ]
        self.status = "File: README.md | Esc: Quit"

    def draw(self):
        super().draw()
        current_y = self.absolute_y + 3
        for line in self.doc_lines:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            color = 0xE95420 if line.startswith("#") else (0xAEA79F if line.startswith("*") else 0xFFFFFF)
            lbl = Label(line, color)
            lbl.absolute_x = self.absolute_x + 3
            lbl.absolute_y = current_y
            lbl.draw()
            current_y += 1
        avocet_core.draw_rect(self.absolute_x, self.absolute_y + self.height - 1, self.width, 1, 0x111111)
        stat_lbl = Label(self.status, 0xAEA79F)
        stat_lbl.absolute_x = self.absolute_x + 2
        stat_lbl.absolute_y = self.absolute_y + self.height - 1
        stat_lbl.draw()

def main():
    avocet_core.clear_screen()
    viewer = AvocetMarkdownViewer()
    viewer.absolute_x = 13
    viewer.absolute_y = 5
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        viewer.update(13, 5, 54, 14)
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        avocet_core.sleep(50)

if __name__ == "__main__":
    main()
