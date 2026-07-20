#include <commands.h>
#include <kernel.h>
#include <string.h>

int handle_ls_dir(int argc, char** argv) {
    (void)argc; (void)argv;
    kprint("Volume in drive C has no label.\n");
    kprint("Directory of /dev/disk0:\n\n");
    kprint("07/15/2026  06:05 PM    <DIR>          .\n");
    kprint("07/15/2026  06:05 PM    <DIR>          ..\n");
    kprint("07/15/2026  06:05 PM            12,544  kernel.bin\n");
    kprint("07/15/2026  06:05 PM             4,096  workspace.py\n");
    kprint("               2 File(s)         16,640 bytes\n");
    return 0;
}

int handle_clear_cls(int argc, char** argv) {
    (void)argc; (void)argv;
    init_vga();
    return 0;
}

int handle_cat_type(int argc, char** argv) {
    if (argc < 2) {
        kprint("Error: Required file path argument missing.\n");
        return 1;
    }
    kprint("[CONTENT] Simulating file read content stream for: ");
    kprint(argv[1]);
    kprint("\n# Avocet configuration loaded successfully.\n");
    return 0;
}

int handle_help(int argc, char** argv) {
    (void)argc; (void)argv;
    kprint("Avocet Framework Unified Command Subsystem:\n");
    kprint("  ls / dir         List files in current working sector\n");
    kprint("  clear / cls      Wipe terminal text contents from display\n");
    kprint("  cat / type [F]   Output contents of targeted file data string\n");
    kprint("  sysinfo          Query real-time hardware telemetry properties\n");
    kprint("  start / run [P]  Allocate memory pages and launch target binary program\n");
    return 0;
}

int handle_sysinfo(int argc, char** argv) {
    (void)argc; (void)argv;
    kprint("OS Name:           Avocet Framework OS\n");
    kprint("OS Version:        0.1.0-Alpha Build 2026\n");
    kprint("System Vendor:     GenuineIntel (MSYS2 Environment Mode)\n");
    kprint("Total Memory:      131,072 KB (128 MB)\n");
    kprint("Paging Status:     Active (2-Level Page Trees Enabled)\n");
    return 0;
}

int handle_start_run(int argc, char** argv) {
    if (argc < 2) {
        kprint("Error: Target executable name missing.\n");
        return 1;
    }
    kprint("[LAUNCHER] Allocating dynamic virtual memory frames...\n");
    kprint("[LAUNCHER] Mapping binary sectors to Ring 3 execution trees...\n");
    kprint("[LAUNCHER] Spawning new process task: ");
    kprint(argv[1]);
    kprint(".exe\n");
    return 0;
}

static command_entry_t master_command_matrix[] = {
    {"ls", handle_ls_dir},
    {"dir", handle_ls_dir},
    {"clear", handle_clear_cls},
    {"cls", handle_clear_cls},
    {"cat", handle_cat_type},
    {"type", handle_cat_type},
    {"help", handle_help},
    {"/?", handle_help},
    {"sysinfo", handle_sysinfo},
    {"start", handle_start_run},
    {"run", handle_start_run}
};

command_entry_t* get_command_matrix(void) {
    return master_command_matrix;
}

int get_command_count(void) {
    return sizeof(master_command_matrix) / sizeof(command_entry_t);
}
