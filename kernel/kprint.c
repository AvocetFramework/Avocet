#include <kernel.h>

void kprint_hex(unsigned int value) {
    char hex_chars[] = "0123456789ABCDEF";
    char buffer[11];
    int i = 8;

    buffer[0] = '0';
    buffer[1] = 'x';
    buffer[10] = '\0';

    while (i > 0) {
        buffer[i + 1] = hex_chars[value & 0xF];
        value >>= 4;
        i--;
    }

    kprint(buffer);
}

void kprint_dec(unsigned long value) {
    char buffer[21];
    int i = 19;

    buffer[20] = '\0';

    if (value == 0) {
        kprint("0");
        return;
    }

    while (value > 0) {
        buffer[i] = (char)('0' + (value % 10));
        value /= 10;
        i--;
    }

    kprint(&buffer[i + 1]);
}
