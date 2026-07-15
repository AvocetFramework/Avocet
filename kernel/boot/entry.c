void init_gdt(void);
void init_idt(void);
void init_pmm(unsigned long mem_size);
void init_vmm(void);
void init_heap(void);
void init_vga(void);
void init_keyboard(void);
void init_timer(unsigned int frequency);
void kmain(void);

typedef struct {
    unsigned long boot_drive;
    unsigned long memory_size_kb;
} boot_info_t;

void kernel_entry(boot_info_t* info) {
    init_vga();
    init_gdt();
    init_idt();
    unsigned long target_mem = (info) ? info->memory_size_kb : (128 * 1024);
    init_pmm(target_mem);
    init_vmm();
    init_timer(100);
    init_keyboard();
    kmain();

    while(1) {
        __asm__ __volatile__("hlt");
    }
}

void init_vga(void) {}
void init_gdt(void) {}
void init_idt(void) {}
void init_pmm(unsigned long mem) {}
void init_vmm(void) {}
void init_heap(void) {}
void init_timer(unsigned int freq) { (void)freq; }
void init_keyboard(void) {}