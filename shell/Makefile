CC = i686-elf-gcc
CFLAGS = -ffreestanding -O2 -Wall -Wextra -Iinclude -I../kernel/include -fno-pie -fno-stack-protector -m32

SRC = src/commands.c src/shell_main.c
OBJ = $(SRC:.c=.o)

all: $(OBJ)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)
