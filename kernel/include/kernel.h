#ifndef KERNEL_H
#define KERNEL_H

#include "cpu/gdt.h"
#include "cpu/idt.h"
#include "drivers/screen.h"
#include "drivers/keyboard.h"
#include "drivers/timer.h"

void kernel_entry(void);
void kmain(void);

void kprint_hex(unsigned int value);
void kprint_dec(unsigned long value);

static inline void outb(unsigned short port, unsigned char data) {
    __asm__ __volatile__("outb %0, %1" : : "a"(data), "Nd"(port));
}

static inline unsigned char inb(unsigned short port) {
    unsigned char result;
    __asm__ __volatile__("inb %1, %0" : "=a"(result) : "Nd"(port));
    return result;
}

void init_pmm(unsigned long physical_memory_size_kb);
void* pmm_alloc_frame(void);
void pmm_free_frame(void* frame_physical_address);

void init_vmm(void);
void vmm_map_page(void* physical_address, void* virtual_address, unsigned int flags);

void init_heap(void);
void* kmalloc(unsigned int size);
void kfree(void* ptr);

#endif
