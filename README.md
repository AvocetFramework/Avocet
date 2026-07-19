# 🐦 Avocet Framework

A custom, freestanding 32-bit operating system kernel and high-fidelity desktop ecosystem that bridges low-level C architecture with an embedded Python user space. Inspired by the premium aesthetics of mainstream distributions like Ubuntu and Debian, Avocet implements its own user-space shell, system utilities, and games. These run on top of a custom, lightweight graphical toolkit named `avocet`, drawing inspiration from both `tkinter` and `customtkinter`.

## 🚀 Key Architectural Features

- **Freestanding Kernel Core**: Implements a dedicated MBR bootloader, Global Descriptor Table (GDT), Interrupt Descriptor Table (IDT), 2-level paging Virtual Memory Manager (VMM), and a dynamic kernel heap allocator.
- **Embedded Python Subsystem**: Links low-level C hardware graphics, clock timers, and keyboard interrupt streams directly to a Python runtime environment using a native C extension bridge (`avocet_core`).
- **`avocet` UI Toolkit Clone**: A modular, object-oriented user interface framework that handles geometry mapping, alignment calculations, and standard desktop color palettes.
- **Dual-OS Backend Terminal**: A hybrid terminal console matching command syntaxes from both Linux (`ls`, `clear`, `cat`) and Windows (`dir`, `cls`, `type`).
- **Rich Utility Ecosystem**: Features a standalone text-based HTML browser, markdown text editors, process task managers, and bot-driven desktop leisure games.

## 📂 Repository Structure

Avocet uses an organized architecture that cleanly separates the OS foundation (kernel and shell) from the application layers (Python-based utilities and UI).

```text
Avocet/
├── .github/
├── .vscode/
├── kernel/                 # Freestanding x86 C kernel & bootloader
│   ├── boot/
│   ├── cpu/
│   ├── drivers/
│   ├── memory/
│   ├── include/
│   ├── Makefile
|   ├── kprint.c
|   ├── link.ld
|   └── main.c
├── python/                 # Python C embedding engine host & 'avocet' toolkit library
│   ├── desktop/
│   ├── lib/
│   ├── src/
│   └── Makefile
├── shell/                  # Dual-OS command parsing engine & Python terminal frontend
│   ├── include/
│   ├── src/
│   ├── terminal.py
│   └── Makefile
├── utilities/              # System tools, content editors, and retro games
│   ├── editors/
│   ├── games/
│   ├── system/
│   └── Makefile
└── Makefile                # Master orchestration build script
```

## 🛠️ Prerequisites & Installation

### Windows Hosts
The **MSYS2 MinGW64** environment is highly recommended to compile this repository on Windows. 

1. Download and install from the [MSYS2 Official Website](https://msys2.org).
2. Open your MSYS2 MinGW64 terminal.
3. Install the required compiler tools and dependencies:

```bash
pacman -S --needed base-devel \
  mingw-w64-x86_64-toolchain \
  mingw-w64-x86_64-gcc \
  mingw-w64-x86_64-python \
  mingw-w64-x86_64-qemu
```

### Linux Hosts
Alternatively, for Debian/Ubuntu-based Linux distributions, install the standard GNU toolchain, Python development headers, and QEMU:

```bash
sudo apt update && sudo apt install -y \
  build-essential \
  gcc \
  python3-dev \
  qemu-system-x86
```

## 💻 Building and Running

Avocet employs a decentralized build system with a primary `Makefile` centralized at the root. Run compilation targets directly from your workspace root:

```bash
# Build the entire framework and boot the OS in QEMU
make run

# Build only the desktop environment
make desktop

# Remove compiled binaries and artifacts
make clean
```
