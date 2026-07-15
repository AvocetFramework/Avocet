HOST_CC = gcc

PYTHON_VERSION = $(shell python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON_CFLAGS = -I/mingw64/include/python$(PYTHON_VERSION) -DMS_WIN64
PYTHON_LDFLAGS = -L/mingw64/lib -lpython$(PYTHON_VERSION)

SRC = src/main.c src/avocet_mod.c src/sys_bindings.c
OBJ = $(SRC:.c=.o)
TARGET = ../build/avocet_desktop.exe

all: $(TARGET)

$(TARGET): $(OBJ)
	$(HOST_CC) $^ -o $@ $(PYTHON_LDFLAGS)

%.o: %.c
	$(HOST_CC) $(PYTHON_CFLAGS) -I../kernel/include -I../shell/include -c $< -o $@

clean:
	rm -f $(OBJ)
