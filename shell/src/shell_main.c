#include <shell_ui.h>
#include <commands.h>
#include <kernel.h>
#include <string.h>

static shell_session_t global_session;

void init_shell_session(shell_session_t* session) {
    if (!session) return;
    strcpy(session->current_path, "C:\\");
    session->terminal_fg_color = 0xE95420;
    session->terminal_bg_color = 0x1E0A22;
    session->echo_active = 1;
    session->running_process_id = 0;
}

int parse_and_execute(const char* raw_input_line) {
    if (!raw_input_line || strlen(raw_input_line) == 0) {
        return 0;
    }

    char input_copy[MAX_COMMAND_LENGTH];
    strncpy(input_copy, raw_input_line, MAX_COMMAND_LENGTH - 1);
    input_copy[MAX_COMMAND_LENGTH - 1] = '\0';

    char* argv[MAX_ARGUMENTS];
    int argc = 0;

    char* token = strtok(input_copy, " \t\r\n");
    while (token != NULL && argc < MAX_ARGUMENTS) {
        argv[argc++] = token;
        token = strtok(NULL, " \t\r\n");
    }

    if (argc == 0) {
        return 0;
    }

    command_entry_t* matrix = get_command_matrix();
    int count = get_command_count();

    for (int i = 0; i < count; i++) {
        if (strcmp(argv[0], matrix[i].name) == 0) {
            return matrix[i].function(argc, argv);
        }
    }

    kprint("avocet-shell: command not found: ");
    kprint(argv[0]);
    kprint("\nType 'help' or '/?' to view active system commands.\n");
    return -1;
}

void shell_main(void) {
    init_shell_session(&global_session);
    kprint("[SHELL] C Backend Routing Subsystem Ready.\n");

    char test_buffer[MAX_COMMAND_LENGTH];
    int idx = 0;

    while (1) {
        char c = kgetc();
        if (c == '\n') {
            test_buffer[idx] = '\0';
            kprint("\n");
            parse_and_execute(test_buffer);
            idx = 0;
            kprint("avocet@root:~# ");
        } else if (c == '\b') {
            if (idx > 0) {
                idx--;
                kprint_char('\b');
            }
        } else {
            if (idx < MAX_COMMAND_LENGTH - 1) {
                test_buffer[idx++] = c;
                kprint_char(c);
            }
        }
    }
}
