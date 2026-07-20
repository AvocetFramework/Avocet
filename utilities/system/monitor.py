# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Window, Label

class AvocetSystemMonitor(Window):
    def __init__(self):
        super().__init__(48, 14, "Avocet Framework Activity Monitor", 0x1A1A1A)
        self.kernel_lbl = Label("Kernel: " + avocet_sys.get_kernel_version(), 0xFFFFFF)
        self.vendor_lbl = Label("CPU:    " + avocet_cpu.get_cpu_vendor() if hasattr(avocet_sys, 'get_cpu_vendor') else "CPU: GenuineIntel", 0xFFFFFF)
        self.ram_lbl = Label("RAM Usage: 0 MB / 128 MB", 0x00FF00)
        self.ticks_lbl = Label("System Uptime: 0 Ticks", 0xAEA79F)

    def update_metrics(self):
        total_mem = avocet_sys.get_total_memory() // 1024
        self.ram_lbl.text = "RAM Size: " + str(total_mem) + " MB Allocated"
        
        ticks = avocet_core.get_ticks()
        self.ticks_lbl.text = "System Uptime: " + str(ticks) + " Monotonic Ticks"

    def draw(self):
        super().draw()
        self.update_metrics()
        
        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 3, self.width - 4, 1, self.bg_color)
        self.kernel_lbl.absolute_x = self.absolute_x + 3
        self.kernel_lbl.absolute_y = self.absolute_y + 3
        self.kernel_lbl.draw()

        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 5, self.width - 4, 1, self.bg_color)
        self.vendor_lbl.absolute_x = self.absolute_x + 3
        self.vendor_lbl.absolute_y = self.absolute_y + 5
        self.vendor_lbl.draw()

        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 7, self.width - 4, 1, self.bg_color)
        self.ram_lbl.absolute_x = self.absolute_x + 3
        self.ram_lbl.absolute_y = self.absolute_y + 7
        self.ram_lbl.draw()

        avocet_core.draw_rect(self.absolute_x + 2, self.absolute_y + 9, self.width - 4, 1, self.bg_color)
        self.ticks_lbl.absolute_x = self.absolute_x + 3
        self.ticks_lbl.absolute_y = self.absolute_y + 9
        self.ticks_lbl.draw()

def main():
    avocet_core.clear_screen()
    monitor = AvocetSystemMonitor()
    monitor.absolute_x = 16
    monitor.absolute_y = 5

    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        monitor.update(16, 5, 48, 14)
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char == '\x1b':
            break
            
        avocet_core.sleep(100)

if __name__ == "__main__":
    main()
