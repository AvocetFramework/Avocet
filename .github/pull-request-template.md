## 📝 Description
Provide a clear, concise summary of the changes introduced by this pull request. Specify if this affects the kernel, user-space shell, `avocet` UI toolkit, or system utilities.

Fixes # (issue number)

## 🏗️ Type of Change
Select the option that applies to your changes:
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] 🚀 New feature (non-breaking change which adds functionality)
- [ ] 🧹 Refactoring / Code Style (no functional changes)
- [ ] 📚 Documentation update
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)

## 🧩 Subsystem Affected
Which layer of the Avocet Framework does this PR touch?
- [ ] `kernel/` (Bootloader, GDT, IDT, VMM, Allocator)
- [ ] `python/` (`avocet_core` C extension, UI toolkit)
- [ ] `shell/` (Command parsing engine, terminal frontend)
- [ ] `utilities/` (Editors, games, browser, system tools)
- [ ] `Build System` (Root or subsystem Makefiles)

## 🧪 Testing & Verification
Describe how you verified these changes. Include the host environment used for testing.

### Host Environment
- **OS:** [e.g., macOS Sonoma (M1), Windows 11 UCRT64, Ubuntu 24.04]
- **Compiler:** [e.g., GCC cross-compiler, gcc-multilib]

### Verification Checklist
- [ ] Ran `make clean && make run` successfully without compilation warnings.
- [ ] Verified the kernel boots smoothly into QEMU without panics or page faults.
- [ ] Validated Python user-space bindings and toolkit geometry alignment.
- [ ] (For Shell/Utilities) Command output matches expected dual-OS syntax rules.

## 📸 Screenshots / Animations
*If applicable, add screenshots, GIFs, or logs demonstrating the new UI features, terminal outputs, or boot sequences here.*

## 📋 Checklist
- [ ] My code follows the style guidelines of this project.
- [ ] I have performed a self-review of my own code.
- [ ] I have commented my code, particularly in hard-to-understand areas (especially freestanding C kernel code).
- [ ] I have made corresponding changes to the documentation (e.g., `DOCS.md` or `README.md`).
- [ ] My changes generate no new compiler warnings.
