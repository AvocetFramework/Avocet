#ifndef IDT_H
#define IDT_H

struct idt_entry_struct {
    unsigned short base_low;
    unsigned short sel;
    unsigned char  always0;
    unsigned char  flags;
    unsigned short base_high;
} __attribute__((packed));
typedef struct idt_entry_struct idt_entry_t;

struct idt_ptr_struct {
    unsigned short limit;
    unsigned int   base;
} __attribute__((packed));
typedef struct idt_ptr_struct idt_ptr_t;

struct registers_struct {
    unsigned int ds;
    unsigned int edi, esi, ebp, esp, ebx, edx, ecx, eax;
    unsigned int int_no, err_code;
    unsigned int eip, cs, eflags, useresp, ss;
} __attribute__((packed));
typedef struct registers_struct registers_t;

typedef void (*isr_t)(registers_t*);

void init_idt(void);
void register_interrupt_handler(unsigned char n, isr_t handler);

#endif
