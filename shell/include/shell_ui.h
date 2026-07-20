#ifndef SHELL_UI_H
#define SHELL_UI_H

#define MAX_COMMAND_LENGTH 256
#define MAX_ARGUMENTS      16

struct shell_session {
    char current_path[MAX_COMMAND_LENGTH];
    unsigned int terminal_fg_color;
    unsigned int terminal_bg_color;
    int echo_active;
    unsigned long running_process_id;
};
typedef struct shell_session shell_session_t;

void init_shell_session(shell_session_t* session);
int parse_and_execute(const char* raw_input_line);
void shell_main(void);

#endif
