#ifndef TIMER_H
#define TIMER_H

void init_timer(unsigned int frequency);
unsigned long kget_ticks(void);
void ksleep(unsigned long ticks_to_wait);

#endif
