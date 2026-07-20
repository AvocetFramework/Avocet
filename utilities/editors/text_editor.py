# type: ignore
import avocet_core
from avocet.widgets import Window, Label, Widget

class AvocetTextEditor(Window):
    def __init__(self):
        super().__init__(50, 14, "Avocet Text Editor v1.0", 0x2A2A2A)
        self.text_buffer = ""
        self.cursor_char = "_"
        self.status_msg = "Ctrl+S: Save | Ctrl+Q: Exit"
        self.max_chars = 40

    def handle_keypress(self, character):
        if character == '\n':
            if len(self.text_buffer) < self.max_chars - 10:
                self.text_buffer += " [NEWLINE] "
        elif character == '\b':
            if len(self.text_buffer) > 0:
                self.text_buffer = self.text_buffer[:-1]
        else:
            if len(self.text_buffer) < self.max_chars:
                self.text_buffer += character

    def draw(self):
        super().draw()
        
        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 3, self.width - 4, 6, 0x1E1E1E)
        
        display_text = self.text_buffer + self.cursor_char
        content_label = Label(display_text, 0xFFFFFF)
        content_label.absolute_x = self.absolute_x + 3
        content_label.absolute_y = self.absolute_y + 4
        content_label.draw()
        
        avocet_core.draw_rect(self.absolute_x, self.absolute_y + self.height - 1, self.width, 1, 0x111111)
        status_label = Label(self.status_msg, 0xAEA79F)
        status_label.absolute_x = self.absolute_x + 2
        status_label.absolute_y = self.absolute_y + self.height - 1
        status_label.draw()

def main():
    avocet_core.clear_screen()
    editor = AvocetTextEditor()
    editor.absolute_x = 15
    editor.absolute_y = 5

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        editor.update(15, 5, 50, 14)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char:
            if char == '\x11': 
                break
            editor.handle_keypress(char)
            
        avocet_core.sleep(30)

if __name__ == "__main__":
    main()
