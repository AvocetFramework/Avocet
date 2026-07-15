# Contributing to Avocet Framework

Thank you for choosing to contribute to the Avocet Framework! This layout guides developers through submitting enhancements, debugging low-level memory maps, and maintaining clean code standards across the workspace.

## 📜 Behavioral Code of Conduct
By participating in this operating system development workspace, you agree to treat all contributors with respect, maintain a helpful attitude, and prioritize content helpfulness and software design stability.

## 🛠️ Local Environment Workspace Configuration

Ensure you are working inside the correct development environment matching the baseline cross-compilers:
1. Fork the repository and sync your target development branch locally.
2. If working on a Windows host machine, execute compilation routines purely from the **MSYS2 MinGW64 terminal window**.
3. Verify changes compile without layout warnings before committing.

## ✒️ Development Code Styles

### Low-Level C Standards (`kernel/`, `shell/src/`)
- Adhere strictly to bare-metal freestanding guidelines (`-ffreestanding`).
- Avoid using external library headers. Use primitive platform definitions provided inside `kernel.h`.
- Protect newly added headers with explicit preprocessor macro guards.

### High-Level Python Standards (`python/`, `utilities/`)
- All user applications must inherit structural attributes directly from the core `Widget` layout blueprints inside `widgets.py`.
- Apply a `# type: ignore` directive to python file entries calling native `avocet_core` extensions to prevent local syntax analyzer highlighting failures.

## 📥 Pull Request (PR) Submission Pipelines

1. Create a dedicated feature branch containing your changes: `git checkout -b feature/your-subsystem-fix`.
2. Clean out old executable testing files locally before initiating pushes: `make clean`.
3. Submit a comprehensive PR description detailing:
   - The targeted folder workspace being modified.
   - Evidence showing the changes compile correctly.
   - An explanation of how the modification impacts core kernel memory protection bounds or UI geometry trees.
4. Ensure your branch clears the integrated **GitHub Actions Build CI Workflow** checks before asking for reviewer sign-off.
