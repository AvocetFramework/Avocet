# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Window, Label

class AvocetSettings(Window):
    def __init__(self):
        super().__init__(44, 14, "Avocet Framework Control Center", 0x333333)
        self.options = [
            "1. Wallpaper Theme: Ubuntu Aubergine",
            "2. Window Borders:  Rounded Minimalist",
            "3. Shell Fallback:  Active (C-Engine)",
            "4. System Telemetry: Live Processing"
        ]
        self.footer_text = "Press 1-4 to Toggle Options | Esc: Exit"

    def draw(self):
        super().draw()
        
        current_y = self.absolute_y + 3
        for opt in self.options:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            opt_lbl = Label(opt, 0xFFFFFF)
            opt_lbl.absolute_x = self.absolute_x + 3
            opt_lbl.absolute_y = current_y
            opt_lbl.draw()
            current_y += 2
            
        avocet_core.draw_rect(self.absolute_x, self.absolute_y + self.height - 1, self.width, 1, 0x111111)
        foot_lbl = Label(self.footer_text, 0xAEA79F)
        foot_lbl.absolute_x = self.absolute_x + 2
        foot_lbl.absolute_y = self.absolute_y + self.height - 1
        foot_lbl.draw()

def main():
    avocet_core.clear_screen()
    settings = AvocetSettings()
    settings.absolute_x = 18
    settings.absolute_y = 5

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        settings.update(18, 5, 44, 14)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char == '\x1b':
            break
            
        avocet_core.sleep(50)

if __name__ == "__main__":
    main()
