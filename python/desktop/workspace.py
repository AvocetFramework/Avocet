import avocet_core
import avocet_sys
from avocet.widgets import Window, Toolbar, Label, Button

class AvocetDesktop:
    def __init__(self):
        self.background_color = 0x2C001E
        self.panel_color = 0x111111
        
        self.top_bar = Toolbar(0, 0, 80, 24, self.panel_color)
        self.side_dock = Toolbar(0, 24, 24, 25, self.panel_color)
        
        self.system_label = Label(2, 4, "Avocet OS")
        self.version_label = Label(60, 4, "v0.1.0")
        
        self.main_window = Window(30, 40, 45, 18)

    def render(self):
        avocet_core.draw_rect(0, 0, 80, 25, self.background_color)
        
        self.top_bar.update()
        self.side_dock.update()
        
        avocet_core.draw_rect(0, 0, 80, 24, self.panel_color)
        self.system_label.update()
        self.version_label.update()
        
        self.main_window.update()

def main():
    desktop = AvocetDesktop()
    avocet_core.clear_screen()
    
    while True:
        desktop.render()
        avocet_core.flush_frame()
        avocet_core.sleep(30)

if __name__ == "__main__":
    main()
