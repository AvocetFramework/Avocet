# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Widget, Label, Toolbar

class AvocetPanel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 80
        self.height = 1
        self.bg_color = 0x111111

        self.container = Toolbar(self.x, self.y, self.width)
        self.title_label = Label("Avocet OS", 0xE95420)
        self.title_label.x = 2
        self.title_label.y = 0
        self.clock_label = Label("12:00", 0xFFFFFF)
        self.clock_label.x = 36
        self.clock_label.y = 0
        self.mem_label = Label("MEM: 000M", 0xAEA79F)
        self.mem_label.x = 62
        self.mem_label.y = 0

    def update_metrics(self):
        ticks = avocet_core.get_ticks()
        minutes = (ticks // 6000) % 60
        hours = (ticks // 360000) % 24
        
        min_str = str(minutes) if minutes >= 10 else "0" + str(minutes)
        hr_str = str(hours) if hours >= 10 else "0" + str(hours)
        self.clock_label.text = hr_str + ":" + min_str

        total_mem = avocet_sys.get_total_memory() // 1024
        self.mem_label.text = "RAM: " + str(total_mem) + "MB"

    def render(self):
        self.container.update()
        self.update_metrics()
        
        self.title_label.update()
        self.clock_label.update()
        self.mem_label.update()

def main():
    avocet_core.clear_screen()
    panel = AvocetPanel()
    
    while True:
        panel.render()
        avocet_core.flush_frame()
        avocet_core.sleep(100)

if __name__ == "__main__":
    main()
