# Third-Party Notices and Licenses

The Avocet Framework incorporates, links to, or relies upon third-party software components to build, emulate, and run its custom operating system kernel and desktop environment. This file contains the necessary attributions and licensing notices for those dependencies.

---

## 1. Embedded Python Runtime Engine
The Avocet Framework uses an embedded Python subsystem (`python/` directory) to host the `avocet` toolkit and shell.

*   **Software:** Python
*   **License:** Python Software Foundation (PSF) License Agreement
*   **Notice:** Copyright © 2001-2026 Python Software Foundation. All rights reserved.
*   **Full License Text:** [Python License Terms](https://python.org)

---

## 2. QEMU (System Emulator)
Used to emulate the 32-bit x86 hardware environment and boot the freestanding Avocet kernel.

*   **Software:** QEMU
*   **License:** GNU General Public License v2 (GPLv2) (with various parts under other compatible licenses)
*   **Notice:** Copyright © 2003-2026 Fabrice Bellard and contributors.
*   **Full License Text:** [QEMU Licensing Information](https://qemu.org)

---

## 3. GNU Toolchain (GCC & GNU Make)
Used for the cross-compilation of the 32-bit C kernel core, link scripts, and decentralized build orchestration.

*   **Software:** GNU Compiler Collection (GCC) & GNU Make
*   **License:** GNU General Public License v3 (GPLv3)
*   **Notice:** Copyright © Free Software Foundation, Inc.
*   **Full License Text:** [GNU GPLv3](https://gnu.org)

---

## 4. NASM (Netwide Assembler)
Used to compile the custom Master Boot Record (MBR) bootloader and low-level CPU initialization routines.

*   **Software:** Netwide Assembler (NASM)
*   **License:** 2-Clause BSD License
*   **Notice:** Copyright © 1996-2026 NASM Authors. All rights reserved.
*   **Full License Text:** [NASM License Terms](https://github.com)

---

## 5. Package Managers & Environments (Homebrew & MSYS2)
Used by host systems to fetch compilation dependencies and runtime tools.

*   **Homebrew (macOS Host Engine):** 2-Clause BSD License | Copyright © Homebrew contributors.
*   **MSYS2 (Windows Host Environment):** Various Open Source Licenses (GPL/MIT/BSD) | Copyright © MSYS2 team and contributors.

---

## Disclaimer

The third-party packages listed above are the property of their respective copyright holders. They are distributed under their own independent licenses. The Avocet Framework project team claims no ownership or control over these external utilities.
