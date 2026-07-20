# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Label, Button, Window

class AvocetLockScreen:
    def __init__(self):
        self.background_color = 0x2C001E
        self.panel_color = 0x111111
        self.is_locked = True
        
        self.clock_label = Label("17:45", 0xFFFFFF)
        self.clock_label.x = 32
        self.clock_label.y = 6
        self.date_label = Label("Wednesday, July 15", 0xAEA79F)
        self.date_label.x = 26
        self.date_label.y = 8
        
        self.auth_window = Window(20, 12, 40, 8, "System Authentication", 0x1E1E1E)
        self.prompt_label = Label("Password for root:", 0xFFFFFF)
        self.prompt_label.x = 22
        self.prompt_label.y = 14
        self.input_box = Window(22, 16, 36, 1)
        self.login_button = Button(34, 18, 12, 1, "Unlock")
        
        self.password_buffer = ""

    def render(self):
        avocet_core.draw_rect(0, 0, 80, 25, self.background_color)
        
        self.clock_label.update()
        self.date_label.update()
        
        self.auth_window.update()
        self.prompt_label.update()
        self.input_box.update()
        
        avocet_core.draw_rect(34, 18, 12, 1, 0xE95420)
        avocet_core.kprint("   [Unlock]   ")

    def handle_input(self, character):
        if character == '\n':
            if self.password_buffer == "root":
                self.is_locked = False
            else:
                self.password_buffer = ""
                avocet_core.clear_screen()
                avocet_core.kprint("[AUTH] Incorrect Password! Try again.\n")
                avocet_core.sleep(1000)
        elif character == '\b':
            if len(self.password_buffer) > 0:
                self.password_buffer = self.password_buffer[:-1]
        else:
            if len(self.password_buffer) < 20:
                self.password_buffer += character

def main():
    lock_screen = AvocetLockScreen()
    avocet_core.clear_screen()
    
    while lock_screen.is_locked:
        lock_screen.render()
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char:
            lock_screen.handle_input(char)
            
        avocet_core.sleep(20)
        
    avocet_core.clear_screen()
    avocet_core.kprint("[AUTH] Authentication Successful. Loading Desktop Workspace...\n")

if __name__ == "__main__":
    main()
