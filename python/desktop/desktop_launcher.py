# type: ignore
import avocet_core
from lock_screen import AvocetLockScreen
from workspace import AvocetDesktop

def main():
    avocet_core.clear_screen()
    
    lock_screen = AvocetLockScreen()
    while lock_screen.is_locked:
        lock_screen.render()
        avocet_core.flush_frame()
        
        char = avocet_core.getc()
        if char:
            lock_screen.handle_input(char)
        avocet_core.sleep(20)
        
    avocet_core.clear_screen()
    avocet_core.kprint("[AVOCET Launcher] Authenticated. Loading Shell Environment...\n")
    avocet_core.sleep(500)
    
    desktop = AvocetDesktop()
    while True:
        desktop.render()
        avocet_core.flush_frame()
        avocet_core.sleep(30)

if __name__ == "__main__":
    main()
