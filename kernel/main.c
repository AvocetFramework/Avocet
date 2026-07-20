#include <kernel.h>

void kmain(void) {
    kprint("========================================\n");
    kprint("            AVOCET FRAMEWORK            \n");
    kprint("========================================\n");
    kprint("[AVOCET] System Core Boot Successful\n");
    
    unsigned long current_ticks = kget_ticks();
    kprint("[AVOCET] Initial Clock Tick Count: ");
    kprint_dec(current_ticks);
    kprint("\n");

    kprint("[AVOCET] Testing Kernel Heap Allocator...\n");
    int* test_ptr1 = (int*)kmalloc(sizeof(int) * 10);
    int* test_ptr2 = (int*)kmalloc(sizeof(int) * 20);

    if (test_ptr1 && test_ptr2) {
        kprint("[AVOCET] Heap Allocation: SUCCESS\n");
        kprint("[AVOCET] Address Block 1: ");
        kprint_hex((unsigned int)test_ptr1);
        kprint("\n");
    } else {
        kprint("[AVOCET] Heap Allocation: FAILED\n");
    }

    kfree(test_ptr1);
    kfree(test_ptr2);
    kprint("[AVOCET] Heap Free Routine: COMPLETE\n");

    kprint("[AVOCET] Launching Interactive Subsystems...\n");
    kprint("avocet@root:~# ");

    while(1) {
        char input_char = kgetc();
        if (input_char == '\n') {
            kprint("avocet@root:~# ");
        }
    }
}
