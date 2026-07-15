#ifndef COMMANDS_H
#define COMMANDS_H

struct command_entry {
    const char* name;
    int (*function)(int argc, char** argv);
};
typedef struct command_entry command_entry_t;

int handle_ls_dir(int argc, char** argv);
int handle_clear_cls(int argc, char** argv);
int handle_cat_type(int argc, char** argv);
int handle_help(int argc, char** argv);
int handle_sysinfo(int argc, char** argv);
int handle_start_run(int argc, char** argv);

command_entry_t* get_command_matrix(void);
int get_command_count(void);

#endif
