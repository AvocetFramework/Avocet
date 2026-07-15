#include <kernel.h>

#define PAGE_SIZE 4096
#define BITS_PER_INDEX 32

static unsigned int* pmm_bitmap = 0;
static unsigned int  pmm_max_blocks = 0;
static unsigned int  pmm_bitmap_size = 0;

static void pmm_bitmap_set(unsigned int bit_index);
static void pmm_bitmap_clear(unsigned int bit_index);
static int  pmm_bitmap_test(unsigned int bit_index);
static int  pmm_find_first_free_frame(void);

void init_pmm(unsigned long physical_memory_size_kb) {
    unsigned long total_memory_bytes = physical_memory_size_kb * 1024;
    pmm_max_blocks = total_memory_bytes / PAGE_SIZE;
  
    pmm_bitmap_size = pmm_max_blocks / BITS_PER_INDEX;
    if (pmm_max_blocks % BITS_PER_INDEX) {
        pmm_bitmap_size++;
    }

    extern unsigned int end; 
    pmm_bitmap = (unsigned int*)&end;

    for (unsigned int i = 0; i < pmm_bitmap_size; i++) {
        pmm_bitmap[i] = 0xFFFFFFFF;
    }

    unsigned int blocks_to_free = (16 * 1024 * 1024) / PAGE_SIZE;
    for (unsigned int i = 0; i < blocks_to_free; i++) {
        pmm_bitmap_clear(i);
    }
  
    pmm_bitmap_set(0);

    unsigned int bitmap_start_block = ((unsigned int)pmm_bitmap) / PAGE_SIZE;
    unsigned int bitmap_end_block = (((unsigned int)pmm_bitmap) + (pmm_bitmap_size * 4)) / PAGE_SIZE;
    for (unsigned int i = bitmap_start_block; i <= bitmap_end_block; i++) {
        pmm_bitmap_set(i);
    }
}

void* pmm_alloc_frame(void) {
    int free_block_index = pmm_find_first_free_frame();
    if (free_block_index == -1) {
        return 0;
    }

    // Mark block as allocated (1)
    pmm_bitmap_set(free_block_index);

    unsigned int physical_address = free_block_index * PAGE_SIZE;
    return (void*)physical_address;
}

void pmm_free_frame(void* frame_physical_address) {
    unsigned int block_index = ((unsigned int)frame_physical_address) / PAGE_SIZE;
    
    if (block_index < pmm_max_blocks) {
        pmm_bitmap_clear(block_index); 
    }
}

static void pmm_bitmap_set(unsigned int bit_index) {
    pmm_bitmap[bit_index / BITS_PER_INDEX] |= (1 << (bit_index % BITS_PER_INDEX));
}

static void pmm_bitmap_clear(unsigned int bit_index) {
    pmm_bitmap[bit_index / BITS_PER_INDEX] &= ~(1 << (bit_index % BITS_PER_INDEX));
}

static int pmm_bitmap_test(unsigned int bit_index) {
    return pmm_bitmap[bit_index / BITS_PER_INDEX] & (1 << (bit_index % BITS_PER_INDEX));
}

static int pmm_find_first_free_frame(void) {
    for (unsigned int i = 0; i < pmm_bitmap_size; i++) {
      
        if (pmm_bitmap[i] != 0xFFFFFFFF) {
            for (int bit = 0; bit < BITS_PER_INDEX; bit++) {
                unsigned int bit_index = (i * BITS_PER_INDEX) + bit;
                if (!pmm_bitmap_test(bit_index)) {
                    return (int)bit_index;
                }
            }
        }
    }
    return -1; 
}
