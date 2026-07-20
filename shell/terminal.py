# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Window, Label

class AvocetTerminal(Window):
    def __init__(self):
        super().__init__(55, 16, "Avocet Framework Shell Console", 0x1E0A22)
        self.prompt = "avocet@root:~# "
        self.input_buffer = ""
        self.history = [
            "Welcome to Avocet Framework Terminal Subsystem",
            "Dual-OS C Engine Backend Active (Linux/Windows Mode)",
            "Type 'help' or '/?' to display available system controls",
            ""
        ]
        self.max_lines = 12

    def append_line(self, text):
        self.history.append(text)
        if len(self.history) > self.max_lines:
            self.history.pop(0)

    def execute_command(self, cmd_string):
        if not cmd_string.strip():
            return
        
        self.append_line(self.prompt + cmd_string)
        
        if cmd_string.strip() in ["clear", "cls"]:
            self.history = [""]
            self.input_buffer = ""
            avocet_core.clear_screen()
            return

        avocet_core.execute_command(cmd_string)
        
        response = "Executed target program task successfully."
        self.append_line(response)

    def handle_keypress(self, character):
        if character == '\n':
            self.execute_command(self.input_buffer)
            self.input_buffer = ""
        elif character == '\b':
            if len(self.input_buffer) > 0:
                self.input_buffer = self.input_buffer[:-1]
        else:
            if len(self.input_buffer) < 45:
                self.input_buffer += character

    def draw(self):
        super().draw()
        
        current_y = self.absolute_y + 2
        for line in self.history:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            label = Label(line, 0xFFFFFF)
            label.absolute_x = self.absolute_x + 2
            label.absolute_y = current_y
            label.draw()
            current_y += 1

        avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
        visible_prompt = self.prompt + self.input_buffer + "_"
        prompt_label = Label(visible_prompt, 0xE95420)
        prompt_label.absolute_x = self.absolute_x + 2
        prompt_label.absolute_y = current_y
        prompt_label.draw()

def main():
    avocet_core.clear_screen()
    terminal = AvocetTerminal()
    terminal.absolute_x = 12
    terminal.absolute_y = 4

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        terminal.update(12, 4, 55, 16)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char:
            terminal.handle_keypress(char)
            
        avocet_core.sleep(30)

if __name__ == "__main__":
    main()
