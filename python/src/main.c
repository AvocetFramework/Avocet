#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

extern PyMODINIT_FUNC PyInit_avocet_core(void);
extern PyMODINIT_FUNC PyInit_avocet_sys(void);

int main(int argc, char* argv[]) {
    (void)argc;
    (void)argv;

    if (PyImport_AppendInittab("avocet_core", PyInit_avocet_core) == -1) {
        return -1;
    }
    if (PyImport_AppendInittab("avocet_sys", PyInit_avocet_sys) == -1) {
        return -1;
    }

    Py_Initialize();

    PyRun_SimpleString(
        "import sys\n"
        "sys.path.append('python/lib')\n"
        "sys.path.append('python/desktop')\n"
        "sys.path.append('shell')\n" // ADDED: Allows workspace.py to see terminal.py
    );

    FILE* fp = fopen("python/desktop/workspace.py", "r");
    if (fp) {
        PyRun_SimpleFile(fp, "python/desktop/workspace.py");
        fclose(fp);
    } else {
        PyRun_SimpleString("print('[AVOCET ERROR] Desktop workspace.py script not found!')\n");
    }

    Py_Finalize();
    return 0;
}
