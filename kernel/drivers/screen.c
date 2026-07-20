#include <kernel.h>

#define VIDEO_ADDRESS 0xB8000
#define MAX_ROWS 25
#define MAX_COLS 80
#define WHITE_ON_BLACK 0x0F

#define REG_SCREEN_CTRL 0x3D4
#define REG_SCREEN_DATA 0x3D5

static int cursor_row = 0;
static int cursor_col = 0;

static int get_cursor_offset(void);
static void set_cursor_offset(int offset);
static void scroll_screen(void);

void init_vga(void) {
    unsigned char* video_memory = (unsigned char*)VIDEO_ADDRESS;

    for (int i = 0; i < MAX_ROWS * MAX_COLS * 2; i+=2) {
        video_memory[i] = ' ';
        video_memory[i + 1] = WHITE_ON_BLACK;
    }

    cursor_row = 0;
    cursor_col = 0;
    set_cursor_offset(0);
}

void kprint_char(char character) {
    unsigned char* video_memory = (unsigned char*)VIDEO_ADDRESS;

    if (character == '\n') {
        cursor_col = 0;
        cursor_row++;
    }

    else if (character == '\b') {
        if (cursor_col > 0) {
            cursor_col--;
        } else if (cursor_row > 0) {
            cursor_row--;
            cursor_col = MAX_COLS - 1;
        }
        int offset = (cursor_row * MAX_COLS + cursor_col) * 2;
        video_memory[offset] = ' ';
        video_memory[offset+1] = WHITE_ON_BLACK;
    }

    else {
        int offset = (cursor_row * MAX_COLS + cursor_col) * 2;
        video_memory[offset] = character;
        video_memory[offset + 1] = WHITE_ON_BLACK;
        cursor_col++;
    }

    if (cursor_col >= MAX_COLS) {
        cursor_col = 0;
        cursor_row++;
    }

    set_cursor_offset(cursor_row * MAX_COLS + cursor_col);
}

void krping(const char* message) {
    int i = 0;
    while (message[i] != 0) {
        kprint_char(message[i]);
        i++;
    }
}

static void scroll_screen(void) {
    unsigned char* video_memory = (unsigned char*)VIDEO_ADDRESS;

    for (int i = 1; i < MAX_ROWS; i++) {
        for (int j = 0; j < MAX_COLS * 2; j++) {
            int target_offset = ((i - 1) * MAX_COLS * 2) + j;
            int source_offset = (i * MAX_COLS * 2) + j;
            video_memory[target_offset] = video_memory[source_offset];
        }
    }

    int bottom_row_start = (MAX_ROWS - 1) * MAX_COLS * 2;
    for (int j = 0; j < MAX_COLS * 2; j += 2) {
        video_memory[bottom_row_start + j] = ' ';
        video_memory[bottom_row_start + j + 1] = WHITE_ON_BLACK;
    }

    cursor_row = MAX_ROWS - 1;
}

static void set_cursor_offset(int offset) {
    outb(REG_SCREEN_CTRL, 14);
    outb(REG_SCREEN_DATA, (unsigned char)(offset >> 8) & 0xFF);

    outb(REG_SCREEN_CTRL, 15);
    outb(REG_SCREEN_DATA, (unsigned char)(offset & 0xFF));
}