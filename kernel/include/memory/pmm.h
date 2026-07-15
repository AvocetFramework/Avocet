#ifndef PMM_H
#define PMM_H

void init_pmm(unsigned long physical_memory_size_kb);
void* pmm_alloc_frame(void);
void pmm_free_frame(void* frame_physical_address);

#endif
