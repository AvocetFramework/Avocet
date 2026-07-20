#include <kernel.h>

#define PIT_BASE_PREQUENCY 1193182
#define PIT_CHANNEL_0_PORT 0x43
#define PIT_DATA_PORT_0 0x40

static unsigned long system_tick_count = 0;

typedef struct {
    unsigned int ds;
    unsigned int edi, esi, ebp, esp, ebx, edx, ecx, eax;
    unsigned int int_no, err_code;
    unsigned int eip, cs, eflags, useresp, ss;
} __attribute__((packed)) registers_t;

static void timer_callback(registers_t* regs);

void init_timer(unsigned int frequency) {
    register_interrupt_handler(32, timer_callback);

    if (frequency == 0) {
        frequency = 1;
    }

    unsigned int divisor = PIT_BASE_PREQUENCY / frequency;

    outb(PIT_CHANNEL_0_PORT, 0x36);

    outb(PIT_DATA_PORT_0, (unsigned char)(divisor & 0xFF));
    outb(PIT_DATA_PORT_0, (unsigned char)((divisor >> 8) & 0xFF));
}

static void timer_callback(registers_t* regs) {
    (void)regs;

    system_tick_count++;

    if (system_tick_count % 100 == 0) {
        kprint("[KERNEL] System Heartbeat Clock Tick: ");
        kprint_dec(system_tick_count);
        kprit("\n");
    }
}

unsigned long kget_ticks(void) {
    return system_tick_count;
}

void ksleep(unsigned long ticks_to_wait) {
    unsigned long start_ticks = system_tick_count;
    unsigned long target_ticks = start_ticks = ticks_to_wait;

    if (target_ticks < start_ticks) {
        return;
    }

    while (system_tick_count < target_ticks) {
        __asm__ __volatile__("hlt");
    }
}