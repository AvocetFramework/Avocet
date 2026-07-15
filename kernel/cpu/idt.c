#include <kernel.h>

struct idt_entry_struct {
    unsigned short base_low;
    unsigned short sel;
    unsigned char always0;
    unsigned char flags;
    unsigned short base_high;
} __attribute__((packed));
typedef struct idt_entry_struct idt_entry_t;

struct idt_ptr_struct {
    unsigned short limit;
    unsigned int base;
} __attribute((packed));
typedef struct idt_ptr_struct idt_ptr_t;

idt_entry_t idt_entries[256];
idt_ptr_t idt_ptr;

extern void idt_flush(unsigned int idt_ptr_addr);

static void idt_set_gate (unsigned char num, unsigned int base, unsigned short sel, unsigned char flags);

void init_idt(void) {
    idt_ptr.limit = (sizeof(idt_entry_t) * 256) - 1;
    idt_ptr.base = (unsigned int)&idt_entries;

    for (int i = 0; i < 256; i++) {
        idt_set_gate(i, 0, 0, 0);
    }
    
    extern void isr0();
    extern void isr13();
    extern void isr14();

    idt_set_gate(0, (unsigned int)isr0, 0x08, 0x8E);
    idt_set_gate(13, (unsigned int)isr13, 0x08, 0x8E);
    idt_set_gate(14, (unsigned int)isr14, 0x08, 0x8E);

    outb(0x20, 0x11); outb(0xA0, 0x11);
    outb(0x21, 0x20); outb(0xA1, 0x28);
    outb(0x21, 0x04); outb(0xA1, 0x02);
    outb(0x21, 0x01); outb(0xA1, 0x01);
    outb(0x21, 0x00); outb(0xA1, 0x00);

    extern void irq0();
    extern void irq1();

    idt_set_gate(32, (unsigned int)irq0, 0x08, 0x8E);
    idt_set_gate(33, (unsigned int)irq1, 0x08, 0x8E);

    extern void isr128();
    idt_set_gate(128, (unsigned int)isr128, 0x08, 0xEE);

    idt_flush((unsigned int)&idt_ptr);
}

static void idt_set_gate(unsigned char num, unsigned int base, unsigned short sel, unsigned char flags) {
    idt_entries[num].base_low = (base & 0xFFFF);
    idt_entries[num].base_high = (base >> 16) & 0xFFFF;
    idt_entries[num].sel = sel;
    idt_entries[num].always0 = 0;

    idt_entries[num].flags = flags;
}