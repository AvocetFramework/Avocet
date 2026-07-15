import avocet_core
import avocet_sys

class AvocetApp:
    def __init__(self):
        self.is_running = False
        self.windows = []
        self.theme = {
            "background": 0x2C001E,
            "panel_bg": 0x111111,
            "accent": 0xE95420,
            "text": 0xFFFFFF,
            "text_dim": 0xAEA79F
        }

    def register_window(self, window):
        self.windows.append(window)

    def unregister_window(self, window):
        if window in self.windows:
            self.windows.remove(window)
        if not self.windows:
            self.quit()

    def init_desktop_environment(self):
        avocet_core.clear_screen()
        avocet_core.kprint("[AVOCET] Loading Desktop Environment...\n")
        self.is_running = True

    def mainloop(self):
        self.init_desktop_environment()
        while self.is_running:
            for window in self.windows:
                if window.visible:
                    window.update()
            avocet_core.flush_frame()
            avocet_core.sleep(10)

    def quit(self):
        self.is_running = False
        avocet_core.clear_screen()
        avocet_core.kprint("[AVOCET] Desktop Environment Terminated Cleanly\n")
