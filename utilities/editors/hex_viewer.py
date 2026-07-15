# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetHexViewer(Window):
    def __init__(self):
        super().__init__(52, 14, "Avocet Binary Hex Viewer", 0x1A252C)
        self.hex_dump_rows = [
            "00000000:  7F 45 4C 46  01 01 01 00  .ELF....",
            "00000008:  00 00 00 00  00 00 00 00  ........",
            "00000010:  02 00 03 00  01 00 00 00  ........",
            "00000018:  54 80 04 08  34 00 00 00  T...4...",
            "00000020:  00 00 00 00  00 00 00 00  ........",
            "00000028:  34 00 20 00  01 00 28 00  4. ..._."
        ]
        self.status_text = "Viewing: /bin/kernel.bin | Esc: Close"

    def draw(self):
        super().draw()
        
        current_y = self.absolute_y + 3
        for row in self.hex_dump_rows:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            dump_label = Label(row, 0x00FF00)  
            dump_label.absolute_x = self.absolute_x + 2
            dump_label.absolute_y = current_y
            dump_label.draw()
            current_y += 1
            
        avocet_core.draw_rect(self.absolute_x, self.absolute_y + self.height - 1, self.width, 1, 0x111111)
        info_label = Label(self.status_text, 0xAEA79F)
        info_label.absolute_x = self.absolute_x + 2
        info_label.absolute_y = self.absolute_y + self.height - 1
        info_label.draw()

def main():
    avocet_core.clear_screen()
    viewer = AvocetHexViewer()
    viewer.absolute_x = 14
    viewer.absolute_y = 5

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        viewer.update(14, 5, 52, 14)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char == '\x1b': 
            break
            
        avocet_core.sleep(50)

if __name__ == "__main__":
    main()
