#include <kernel.h>

static const char scancode_ascii_map[] = {
    0,  27, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\b',
  '\t', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\n',   
    0,  'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', '`',   0,   
 '\\', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',   0, '*',   0, ' '
};

#define KEYBOARD_BUFFER_SIZE 256
static char keyboard_ring_buffer[KEYBOARD_BUFFER_SIZE];
static int buffer_head = 0;
static int buffer_tail = 0;

static int shift_active = 0;
static int caps_lock_active = 0;

typedef struct {
    unsigned int ds;
    unsigned int edi, esi, ebp, esp, ebx, edx, ecx, eax;
    unsigned int int_no, err_code;
    unsigned int eip, cs, eflags, useresp, ss;
} __attribute__((packed)) registers_t;

static void keyboard_callback(registers_t* regs);

void init_keyboard(void) {
    register_interrupt_handler(33, keyboard_callback);
}

static void keyboard_callback(registers_t* regs) {
    (void)regs;

    unsigned char scancode = inb(0x60);

    if (scancode & 0x80) {
        scancode &= 0x7F;

        if (scancode == 0x2A || scancode == 0x36) {
            shift_active = 1;
            return;
        }

        if (scancode == 0x3A) {
            caps_lock_active = !caps_lock_active;
            return;
        }

        if (scancode < sizeof(scancode_ascii_map)) {
            char ascii = scancode_ascii_map[scancode];

            if (ascii >= 'a' && ascii <= 'z') {
                ascii -= 32;
            }

            if (ascii != 0) {
                int next_head = (buffer_head + 1) % KEYBOARD_BUFFER_SIZE;
                if (next_head != buffer_tail) {
                    keyboard_ring_buffer[buffer_head] = ascii;
                    buffer_head = next_head;
                }

                kprint_char(ascii);

            }
        }
    }
}

char kgetc(void) {
    while (buffer_head == buffer_tail) {
        __asm__ __volatile__ ("hlt");
    }

    char ascii = keyboard_ring_buffer[buffer_tail];
    buffer_tail = (buffer_tail + 1) % KEYBOARD_BUFFER_SIZE;
    return ascii;
}