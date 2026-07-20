#include <kernel.h>

#define KHEAP_START 0x01000000
#define KHEAP_INITIAL_SIZE 0x00100000
#define HEAP_MAGIC 0x12345678

struct kheap_header {
    unsigned int magic;
    unsigned char is_allocated;
    unsigned int size;
};
typedef struct kheap_header kheap_header_t;

struct kheap_footer {
    unsigned int magic;
};
typedef struct kheap_footer kheap_footer_t;

static unsigned int heap_start_address = KHEAP_START;
static unsigned int heap_end_address = KHEAP_START + KHEAP_INITIAL_SIZE;

void init_heap(void) {
    kheap_header_t* init_header = (kheap_header_t*)heap_start_address;
    init_header->magic = HEAP_MAGIC;
    init_header->is_allocated = 0;
    init_header->size = KHEAP_INITIAL_SIZE - sizeof(kheap_header_t) - sizeof(kheap_footer_t);

    kheap_footer_t* init_footer = (kheap_footer_t*)(heap_end_address - sizeof(kheap_footer_t));
    init_footer->magic = HEAP_MAGIC;
}

void* kmalloc(unsigned int size) {
    unsigned int current_address = heap_start_address;

    while (current_address < heap_end_address) {
        kheap_header_t* header = (kheap_header_t*)current_address;

        if (header->magic != HEAP_MAGIC) {
            return 0;
        }

        if (!header->is_allocated && header->size >= size) {
            unsigned int requested_total_size = size + sizeof(kheap_header_t) + sizeof(kheap_footer_t);
            
            if (header->size >= requested_total_size + 32) {
                unsigned int next_block_address = current_address + requested_total_size;
                kheap_header_t* next_header = (kheap_header_t*)next_block_address;
                next_header->magic = HEAP_MAGIC;
                next_header->is_allocated = 0;
                next_header->size = header->size - requested_total_size;

                kheap_footer_t* next_footer = (kheap_footer_t*)(next_block_address + sizeof(kheap_header_t) + next_header->size);
                next_footer->magic = HEAP_MAGIC;

                header->size = size;
            }

            header->is_allocated = 1;

            kheap_footer_t* footer = (kheap_footer_t*)(current_address + sizeof(kheap_header_t) + header->size);
            footer->magic = HEAP_MAGIC;

            return (void*)(current_address + sizeof(kheap_header_t));
        }

        current_address += sizeof(kheap_header_t) + header->size + sizeof(kheap_footer_t);
    }

    return 0;
}

void kfree(void* ptr) {
    if (!ptr) {
        return;
    }

    unsigned int header_address = (unsigned int)ptr - sizeof(kheap_header_t);
    kheap_header_t* header = (kheap_header_t*)header_address;

    if (header->magic != HEAP_MAGIC) {
        return;
    }

    header->is_allocated = 0;

    unsigned int next_block_address = header_address + sizeof(kheap_header_t) + header->size + sizeof(kheap_footer_t);
    if (next_block_address < heap_end_address) {
        kheap_header_t* next_header = (kheap_header_t*)next_block_address;
        if (next_header->magic == HEAP_MAGIC && !next_header->is_allocated) {
            header->size += sizeof(kheap_header_t) + next_header->size + sizeof(kheap_footer_t);
            kheap_footer_t* footer = (kheap_footer_t*)(header_address + sizeof(kheap_header_t) + header->size);
            footer->magic = HEAP_MAGIC;
        }
    }
}
