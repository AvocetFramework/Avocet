#ifndef VMM_H
#define VMM_H

void init_vmm(void);
void vmm_map_page(void* physical_address, void* virtual_address, unsigned int flags);

#endif
