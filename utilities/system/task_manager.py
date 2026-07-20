# type: ignore
import avocet_core
import avocet_sys
from avocet.widgets import Window, Label

class AvocetTaskManager(Window):
    def __init__(self):
        super().__init__(46, 14, "Avocet Process Task Manager", 0x1E1E1E)
        self.headers = "PID   PROCESS NAME     STATUS       PRIVILEGE"
        self.tasks = [
            "000   kinitial_core    RUNNING      RING 0",
            "001   avocet_desktop   RUNNING      RING 3",
            "002   shell_backend    IDLE         RING 3",
            "003   task_manager     ACTIVE       RING 3"
        ]

    def draw(self):
        super().draw()
        avocet_core.draw_rect(self.absolute_x + 1, self.absolute_y + 2, self.width - 2, 1, 0x111111)
        head_lbl = Label(self.headers, 0xE95420)
        head_lbl.absolute_x = self.absolute_x + 2
        head_lbl.absolute_y = self.absolute_y + 2
        head_lbl.draw()
        
        current_y = self.absolute_y + 4
        for task in self.tasks:
            avocet_core.draw_rect(self.absolute_x + 1, current_y, self.width - 2, 1, self.bg_color)
            task_lbl = Label(task, 0xFFFFFF)
            task_lbl.absolute_x = self.absolute_x + 2
            task_lbl.absolute_y = current_y
            task_lbl.draw()
            current_y += 1

def main():
    avocet_core.clear_screen()
    mgr = AvocetTaskManager()
    mgr.absolute_x = 17
    mgr.absolute_y = 5
    while True:
        avocet_core.draw_rect(0, 0, 80, 25, 0x2C001E)
        mgr.update(17, 5, 46, 14)
        avocet_core.flush_frame()
        char = avocet_core.getc()
        if char == '\x1b': break
        avocet_core.sleep(100)

if __name__ == "__main__":
    main()
