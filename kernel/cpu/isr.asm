[bits 32]

global idt_flush
global gdt_flush
global isr0
global isr13
global isr14
global irq0
global isr128

extern isr_handler
extern irq_handler

isr0:
    push byte 0
    push byte 0
    jmp isr_common_stub

isr13:
    push byte 13
    jmp isr_common_stub

isr14:
    push byte 14
    jmp isr_common_stub

irq0:
    push byte 0
    push byte 32
    jmp irq_common_stub

isr128:
    push byte 0
    push byte 128
    jmp isr_common_stub

isr_common_stub
    pusha
    mov ax, ds
    push eax

    mov ax, 0x08
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    call isr_handler

    pop eax
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    popa
    add esp, 8
    iret

irq_common_stub:
    pusha
    mov ax, ds
    push eax

    mov ax, 0x08
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    call irq_handler

    pop eax
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    popa
    add esp, 8
    iret

idt_flush:
    mov eax, [esp+4]
    lidt [eax]
    ret

gdt_flush:
    mov eax, [esp+4]
    lgdt [eax]
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax
    jmp 0x08:.flush
.flush
    ret