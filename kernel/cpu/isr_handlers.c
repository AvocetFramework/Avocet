#include <kernel.h>

typedef struct {
    unsigned int ds;
    unsigned int edi, esi, ebp, esp, ebx, edx, ecx, eax;
    unsigned int int_no, err_code;
    unsigned int eip, cs, eflags, useresp, ss;
} __attribute__((packed)) registers_t;

typedef void (*isr_t)(registers_t*);
static isr_t interrupt_handlers[256] = {0};

void register_interrupt_handler(unsigned char n, isr_t handler) {
    interrupt_handlers[n] = handler;
}

void isr_handler(registers_t* regs) {
    if (interrupt_handlers[regs->int_no] != 0) {
        isr_t handler = interrupt_handlers[regs->int_no];
        handler(regs);
    } else {
        kprint("CRITICAL CPU EXCEPTION UNHANDLED: ");
        kprint_hex(regs->int_no);
        kprint("\nError Code:");
        kprint_hex(regs->err_code);
        kprint("\nInstruction Pointer (EIP)");
        kprint_hex(regs->eip);
        kprint("\n");

        while(1) {
            __asm__ __volatile__("cli; hlt");
        }
    }
}

void irq_handler(registers_t* regs) {
    if (regs->int_no >= 40) {
        outb(0xA0, 0x20);
    }

    outb(0x20, 0x20);

    if (interrupt_handlers[regs->int_no] != 0) {
        isr_t handler = interrupt_handlers[regs->int_no];
        handler(regs);
    }
}

void syscall_handler(registers_t* regs) {
    unsigned int syscall_id = regs->eax;
    
    kprint("System Call Request Received. ID:");
    kprint_hex(syscall_id);
    kprint("\n");

    regs->eax = 0;
}