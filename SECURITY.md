# Security Policy — Avocet Framework

This document outlines the security procedures, supported versions, and vulnerability reporting mechanisms for the Avocet Framework ecosystem.

---

## Supported Versions

Only the latest commit on the main development branch is actively supported and maintained with security updates. A new version of the software is published after every one month, each with twelve versions, so the software must be kept under update every at least one year.

| Version | Supported |
| :--- | :--- |
| **0.1.x** | Actively Supported |
| **< 0.1.0** | End of Life (EOL) |

---

## Reporting a Vulnerability

As a bare-metal operating system executing code directly in x86 Protected Mode, memory safety and privilege separation are critical. Security bugs require discrete handling to safeguard downstream system builds.

### Critical Vulnerability Vectors
Please report any flaw that allows unauthorized execution, breaks ring privileges, or maliciously crashes host instances, including:
* **Ring-Bridging Faults**: User-space Python programs bypassing the `VMM` or `GDT` page/segment limits to execute code directly at Ring 0.
* **Buffer Overflows**: Any payload inside the C backend shell tokenizer (`shell_main.c`) or print engines (`kprint.c`) that triggers an unhandled memory corruption.
* **Interrupt Hijacking**: Exploits where user programs rewrite the Interrupt Descriptor Table (`IDT`) exception trap doors.
* **Host Sandbox Escapes**: Flaws within the native `avocet_core` or `avocet_sys` Python C extensions that allow a script to break out of the simulated runtime engine and run arbitrary code on the developer's Windows/MSYS2, macOS/Homebrew, or Linux host machine.

### Submission Process
1. **Do Not Open a Public Issue**: To prevent exposing system flaws publicly before an official patch is deployed, do not use the public GitHub Issue tracker for security bugs.
2. **Discrete Report**: Email a detailed write-up of the exploit directly to the maintainer's primary contact email or submit a confidential advisory directly through the GitHub Security tab.
3. **Provide a Proof of Concept (PoC)**: Include the exact minimal Python widget script, raw shell string inputs, or kernel setup configurations required to reproduce the exploit.

---

## Vulnerability Triage and Patch Timeline

* **Acknowledgement**: You will receive a verification response acknowledging receipt of the security report within **48 hours**.
* **Remediation**: The core architecture will be analyzed against the reported exploit vector. A private patch branch will be opened to harden memory boundaries or structure tracking tables.
* **Coordination**: We will coordinate with you to publish a Security Advisory alongside credit for discovering the vulnerability, after which the patch will be merged directly into the main trunk.
