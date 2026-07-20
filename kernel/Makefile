CC = i686-elf-gcc
LD = i686-elf-ld
ASM = nasm

CFLAGS = -ffreestanding -O2 -Wall -Wextra -Iinclude -Ishell/include -fno-pie -fno-stack-protector -m32
LDFLAGS = -T link.ld

KERNEL_OBJ = boot/entry.o \
             cpu/gdt.o \
             cpu/idt.o \
             cpu/isr_handlers.o \
             cpu/isr.o \
             drivers/keyboard.o \
             drivers/screen.o \
             drivers/timer.o \
             kprint.o \
             memory/pmm.o \
             memory/vmm.o \
             memory/kheap.o \
             main.o

SHELL_OBJ = ../shell/src/commands.o \
            ../shell/src/shell_main.o

all: boot/boot.bin ../build/kernel.bin

../build/kernel.bin: $(KERNEL_OBJ) $(SHELL_OBJ)
	$(LD) $(LDFLAGS) -o $@ $^ --oformat binary

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

boot/boot.bin: boot/boot.asm
	$(ASM) $< -f bin -o $@

cpu/isr.o: cpu/isr.asm
	$(ASM) $< -f elf32 -o $@

clean:
	rm -f boot/boot.bin
	rm -f $(KERNEL_OBJ)
