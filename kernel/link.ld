OUTPUT_FORMAT("binary")
ENTRY(kernel_entry)

SECTIONS
{
    . = 0x1000;

    .text : ALIGN(4096)
    {
        *(.text)
    }

    .rodata : ALIGN(4096)
    {
        *(.rodata)
    }

    .data : ALIGN(4096)
    {
        *(.data)
    }

    .bss : ALIGN(4096)
    {
        *(.COMMON)
        *(.bss)
    }

    end = .;
}
