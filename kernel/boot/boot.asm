[org 0x7c00]

start:
    cli
    cld

    xor ax, ax
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    mov ss, ax
    mov bp, 0x7c00
    mov sp, bp

    mov [BOOT_DRIVE], dl

check_cpu:
    pusfd
    pop eax
    mov ecx, eax
    xor eax, 0x00200000
    push eax
    popfd
    pushfd
    pop eax
    xor eax, ecx
    jz cpu_error

load_kernel:
    mov ah, 0x02
    mov al, 15
    mov ch, 0x00
    mov dh, 0x00
    mov cl, 0x02
    mov dl, [BOOT_DRIVE]
    mov bx, 0x1000
    int 0x13
    jc disk_error

activate_a20:
    in al, 0x92
    or al, 2
    out 0x92, al

load_gdt:
    lgdt[gdt_descriptor]

switch_pm: 
    mov eax, cr0
    or eax, 0x1
    mov cr0, eax

    jmp CODE_SEG:init_pm

cpu_error:
    mov si, MSG_CPU_ERR
    jmp print_string

print_string: 
    mov ah, 0x0e
.loop:
    lodsb
    or al, al
    jz .done
    int 0x10
    jmp .loop
.done:
    cli
    hlt

MSG_CPU_ERR db "CPU Unsupported!", 0
MSG_DISK_ERR db "Disk Read Failed!", 0

gdt_start:
gdt_null:
    dd 0x0, 0x0
gdt_code:
    dw 0xffff, 0x0, 0x9a00, 0x00cf
gdt_data:
    dw 0xffff, 0x0, 0x9200, 0x00cf
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt-start

CODE_SEG equ gdt_code - gdt_start
DATA_SEG equ gdt_data - gdt_start

[bits 32]
init_pm
    mov ax, DATA_SEG
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax

    mov ebp, 0x90000
    mov esp, ebp
    
    call 0x1000
    jmp $

BOOT_DRIVE db 0

times 510-($-$$) db 0
dw 0xaa55