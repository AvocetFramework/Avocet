#include <kernel.h>

#define PAGE_PRESENT  0x1
#define PAGE_WRITE    0x2
#define PAGE_USER     0x4

#define PAGE_SIZE     4096
#define ENTRIES_PER_TABLE 1024

static unsigned int kernel_page_directory[ENTRIES_PER_TABLE] __attribute__((aligned(4096)));
static unsigned int kernel_page_table[ENTRIES_PER_TABLE]     __attribute__((aligned(4096)));

extern void vmm_switch_page_directory(unsigned int directory_address);
extern void vmm_enable_paging(void);

void init_vmm(void) {
    for (int i = 0; i  22;
    unsigned int table_index     = (virt_addr_int >> 12) & 0x3FF;

    if (!(kernel_page_directory[directory_index] & PAGE_PRESENT)) {
        return; 
    }

    unsigned int* target_page_table = (unsigned int*)(kernel_page_directory[directory_index] & 0xFFFFF000);

    target_page_table[table_index] = (phys_addr_int & 0xFFFFF000) | flags;

    __asm__ __volatile__("mov %%cr3, %%eax; mov %%eax, %%cr3" ::: "eax");
}
