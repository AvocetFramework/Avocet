# type: ignore
import avocet_core
from avocet.widgets import Window, Label

class AvocetLogViewer(Window):
    def __init__(self):
        super().__init__(54, 14, "Avocet Core Diagnostics Event Log", 0x1A1E24)
        self.logs = [
            "[00:00:01] [INFO]  GDT segment registers re-mapped atomially.",
            "[00:00:02] [INFO]  IDT interrupt service traps flushed safely.",
            "[00:00:03] [WARN]  A20 Fast gate pin high-voltage checked.",
            "[00:00:05] [INFO]  PMM initialization bitmap generated past &end.",
            "[00:00:06] [DEBUG] MMU 2-level directory trees generated.",
            "[00:00:08] [FATAL] User test heap allocations completed successfully."
        ]

    def draw(self):
        super().draw()
        current_y = self.absolute_y + 3
        for log in self.logs:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            color = 0xFF0000 if "FATAL" in log else (0xFFFF00 if "WARN" in log else 0x00FF00)
            lbl = Label(log, color)
            lbl.absolute_x = self.absolute_x + 2
            lbl.absolute_y = current_y
            lbl.draw()
            current_y += 1

def main():
    avocet_core.clear_screen()
    viewer = AvocetLogViewer()
    viewer.absolute_x = 13
    viewer.absolute_y = 5
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        viewer.update(13, 5, 54, 14)
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        avocet_core.sleep(50)

if __name__ == "__main__":
    main()
