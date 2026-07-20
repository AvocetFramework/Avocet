# 📖 Avocet Framework Setup & Troubleshooting Guide

This document provides exhaustive installation workflows for all supported operating systems, details target environments, and lists troubleshooting steps for common compilation, linking, and emulator failures.

## 🛠️ Complete Installation Methods

### 🪟 Windows (via MSYS2)
First, download and install the core installer from the [MSYS2 Official Website](https://msys2.org). Launch the specific environment terminal shell matching your architectural choice below to run the package manager.

#### 🟩 UCRT64 Environment (Recommended Default)
Modern Windows environment utilizing the Universal C Runtime and GCC.
```bash
pacman -S --needed base-devel \
  mingw-w64-ucrt-x86_64-toolchain \
  mingw-w64-ucrt-x86_64-gcc \
  mingw-w64-ucrt-x86_64-python \
  mingw-w64-ucrt-x86_64-qemu
```

#### 🟦 CLANG64 Environment
Modern native LLVM/Clang-focused toolchain using UCRT.
```bash
pacman -S --needed base-devel \
  mingw-w64-clang-x86_64-toolchain \
  mingw-w64-clang-x86_64-clang \
  mingw-w64-clang-x86_64-python \
  mingw-w64-clang-x86_64-qemu
```

#### 🟨 MINGW64 Environment
Legacy native 64-bit environment using MSVCRT.
```bash
pacman -S --needed base-devel \
  mingw-w64-x86_64-toolchain \
  mingw-w64-x86_64-gcc \
  mingw-w64-x86_64-python \
  mingw-w64-x86_64-qemu
```

#### 🟧 MINGW32 Environment
Legacy native 32-bit environment using MSVCRT.
```bash
pacman -S --needed base-devel \
  mingw-w64-i686-toolchain \
  mingw-w64-i686-gcc \
  mingw-w64-i686-python \
  mingw-w64-i686-qemu
```

#### 🟪 CLANGARM64 Environment
Native LLVM/Clang environment targeted for Windows on ARM hardware (Qualcomm Snapdragon, etc.).
```bash
pacman -S --needed base-devel \
  mingw-w64-clang-aarch64-toolchain \
  mingw-w64-clang-aarch64-clang \
  mingw-w64-clang-aarch64-python \
  mingw-w64-clang-aarch64-qemu
```

#### 🟥 MSYS2 General Environment
POSIX-emulated fallback environment. Note that applications built here rely on `msys-2.0.dll` and are not fully native Windows binaries.
```bash
pacman -S --needed base-devel \
  gcc \
  python3 \
  qemu
```

---

### 🐧 Linux Environments
Because Avocet targets a freestanding 32-bit architecture, 64-bit Linux distributions must install multilib development tools to properly handle the `-m32` flags during compilation.

#### 📦 Debian / Ubuntu / Linux Mint
```bash
sudo apt update && sudo apt install -y \
  build-essential \
  gcc-multilib \
  g++-multilib \
  python3-dev \
  qemu-system-x86 \
  nasm
```

#### ⚙️ Fedora / RHEL / CentOS
```bash
sudo dnf groupinstall -y "Development Tools" && sudo dnf install -y \
  glibc-devel.i686 \
  libgcc.i686 \
  python3-devel \
  qemu-system-x86 \
  nasm
```

#### 🏔️ Arch Linux / Manjaro
Ensure your `/etc/pacman.conf` has the `[multilib]` repository enabled before running:
```bash
sudo pacman -Syy --needed \
  base-devel \
  multilib-devel \
  python \
  qemu-system-x86 \
  nasm
```

#### 🦎 openSUSE Tumbleweed / Leap
```bash
sudo zypper refresh && sudo zypper install -t pattern devel_basis && sudo zypper install -y \
  glibc-devel-32bit \
  python3-devel \
  qemu-x86 \
  nasm
```


## 🔍 Troubleshooting & Resolution

### 1. Toolchain & Compilation Failures

#### ❌ Error: `sys/cdefs.h: No such file or directory` or missing 32-bit headers
* **Cause**: Your 64-bit Linux host environment is missing the multi-architecture development libraries required to build 32-bit targets.
* **Fix**: Re-run your distribution package installation command and explicitly verify that `gcc-multilib` (Debian/Ubuntu), `glibc-devel.i686` (Fedora), or `multilib-devel` (Arch) successfully installed.

#### ❌ Error: `nasm: command not found`
* **Cause**: The Netwide Assembler is missing from the environment path, preventing assembly of the MBR bootloader code.
* **Fix**: Install `nasm` using your specific host OS package manager listed above.

#### ❌ Error: `Python.h: No such file or directory`
* **Cause**: The C compilation stage for the embedded engine cannot locate the Python framework header files.
* **Fix**: Ensure you installed the development flavor of Python (`python3-dev` on Debian/Ubuntu or `python3-devel` on Fedora). If using MSYS2, make sure you launched the exact terminal corresponding to your installed package prefix (e.g., UCRT64 shell for UCRT packages).

---

### 2. Linking Errors

#### ❌ Error: `i386 architecture of input file is incompatible with i386:x86-64 output`
* **Cause**: The linker is trying to combine the freestanding 32-bit assembly/C kernel objects into a host-native 64-bit binary layout.
* **Fix**: Explicitly pass `-m elf_i386` to your `ld` linker arguments inside the `kernel/Makefile`. Ensure your C compiler flags utilize `-m32`.

#### ❌ Error: Undefined reference to standard library symbols (e.g., `memset`, `memcpy`, `malloc`)
* **Cause**: The kernel is compiled with `-ffreestanding`, meaning standard host C libraries are excluded.
* **Fix**: Ensure that custom, low-level implementations for basic operations are linked inside the `kernel/memory/` directory. Do not use standard host headers inside freestanding source paths.

---

### 3. Emulator & Virtualization Errors (QEMU)

#### ❌ Error: QEMU boots to a black screen or hangs at `Booting from Hard Disk...`
* **Cause**: The compiled kernel exceeded the size boundaries expected by the early sector bootloader, or the MBR magic signature (`0xAA55`) is misaligned.
* **Fix**: Check `kernel/link.ld` to ensure sections map correctly. Run `make clean && make run` to clear corrupt artifacts.

#### ❌ Error: `Could not initialize SDL / GTK / Display output`
* **Cause**: QEMU is running inside a headless environment or SSH session without graphical display forwarding.
* **Fix**: Append a fallback display argument to your QEMU execution line inside the root `Makefile`:
  ```bash
  qemu-system-x86_64 -drive format=raw,file=avocet.bin -display sdl
  ```
  If working completely headless, use `-nographic` or `-vnc :1` to interact via a network client.

#### ❌ Error: `KVM: Failed to initialize / Permission Denied`
* **Cause**: Your Linux user account lacks direct read/write privileges to the hardware acceleration node `/dev/kvm`.
* **Fix**: Append your user to the KVM group, then log out and back in:
  ```bash
  sudo usermod -aG kvm \$USER
  ```

## Running Avocet Framework
To run the Avocet Framework, simply run the commands below on the root directory:
```bash
# Build the entire framework and boot the OS in QEMU
make run

# Build only the desktop environment
make desktop

# Remove compiled binaries and artifacts
make clean
```
