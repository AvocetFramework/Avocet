# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetIniEditor(Window):
    def __init__(self):
        super().__init__(46, 14, "Avocet System Configuration Workspace", 0x2E2E2E)
        self.config_keys = [
            "[BOOT_LOADER]",
            "timeout = 5",
            "default = avocet_kernel_v1",
            "",
            "[GRAPHICS_DISPLAY]",
            "resolution_x = 80",
            "resolution_y = 25",
            "theme_profile = ubuntu_aubergine"
        ]
        self.cursor_idx = 1

    def handle_keypress(self, key):
        if key in ['w', 'W'] and self.cursor_idx > 1: self.cursor_idx -= 1
        elif key in ['s', 'S'] and self.cursor_idx < len(self.config_keys) - 1: self.cursor_idx += 1

    def draw(self):
        super().draw()
        current_y = self.absolute_y + 3
        for i, row in enumerate(self.config_keys):
            bg = 0x444444 if i == self.cursor_idx else self.bg_color
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, bg)
            color = 0x00FF00 if row.startswith("[") else 0xFFFFFF
            lbl = Label(row, color)
            lbl.absolute_x = self.absolute_x + 3
            lbl.absolute_y = current_y
            lbl.draw()
            current_y += 1
        avocet_core.draw_rect(self.absolute_x, self.absolute_y + self.height - 1, self.width, 1, 0x111111)
        ctrl_lbl = Label("WS: Navigate Parameters | Esc: Close", 0xAEA79F)
        ctrl_lbl.absolute_x = self.absolute_x + 2
        ctrl_lbl.absolute_y = self.absolute_y + self.height - 1
        ctrl_lbl.draw()

def main():
    avocet_core.clear_screen()
    editor = AvocetIniEditor()
    editor.absolute_x = 17
    editor.absolute_y = 5
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        editor.update(17, 5, 46, 14)
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        if char: editor.handle_keypress(char)
        avocet_core.sleep(40)

if __name__ == "__main__":
    main()
