# Avocet Framework

A custom, freestanding 32-bit operating system kernel and high-fidelity desktop ecosystem that bridges low-level C architecture with an embedded Python user space. Inspired by the premium aesthetics of mainstream Linux distributions like Ubuntu and Fedora, Avocet implements its own user-space shell, system utilities, and games using a custom lightweight graphical toolkit clone, inspired in both `tkinter` and `customtkinter`, named `avocet`.

## 🚀 Key Architectural Features

- **Freestanding Kernel Core**: Implements a dedicated MBR bootloader, Global Descriptor Table (GDT), Interrupt Descriptor Table (IDT), 2-level paging Virtual Memory Manager (VMM), and a dynamic kernel heap allocator.
- **Embedded Python Subsystem**: Links low-level C hardware graphics, clock timers, and keyboard interrupt streams directly to a Python runtime environment using a native C extension bridge (`avocet_core`).
- **`avocet` UI Toolkit Clone**: A modular, object-oriented user interface framework that handles geometry mapping, alignment calculations, and Linux color palettes.
- **Dual-OS Backend Terminal**: A hybrid terminal console matching command syntaxes from both Linux (`ls`, `clear`, `cat`) and Windows (`dir`, `cls`, `type`).
- **Rich Utility Ecosystem**: Features a standalone text-based HTML browser, markdown text editors, process task managers, and bot-driven desktop leisure games.

## 📂 Repository Structure

```text
Avocet/
├── kernel/             # Freestanding x86 C kernel & bootloader
├── shell/              # Dual-OS backend command parsing engine & Python terminal frontend
├── python/             # Python C embedding engine host & 'avocet' toolkit library
├── utilities/          # System tools, content editors, and retro games
└── Makefile            # Master orchestration build script
```

## 🛠️ Prerequisites & Installation

To compile the repository on a Windows host using the **MSYS2 MinGW64** environment, open your terminal and install the required compiler tools and dependencies:

```bash
pacman -S --needed base-devel mingw-w64-x86_64-toolchain
pacman -S --needed base-devel mingw-w64-x86_64-gcc
pacman -S --needed base-devel mingw-w64-x86_64-python mingw-w64-x86_64-qemu
```

## 💻 Building and Running

Avocet employs a decentralized build system, using a Makefile centralized for each folder. Run compilation targets directly from the root workspace folder:

```bash
make run
make desktop
make clean
```
