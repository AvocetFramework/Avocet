#ifndef KHEAP_H
#define VMM_H

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

void init_heap(void);
void* kmalloc(unsigned int size);
void kfree(void* ptr);

#endif
