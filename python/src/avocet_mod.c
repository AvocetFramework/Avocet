#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <kernel.h>
#include <shell_ui.h>

static PyObject* avocet_kprint(PyObject* self, PyObject* args) {
    const char* message;
    if (!PyArg_ParseTuple(args, "s", &message)) {
        return NULL;
    }
    kprint(message);
    Py_RETURN_NONE;
}

static PyObject* avocet_clear_screen(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    init_vga();
    Py_RETURN_NONE;
}

static PyObject* avocet_get_ticks(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    unsigned long ticks = kget_ticks();
    return PyLong_FromUnsignedLong(ticks);
}

static PyObject* avocet_sleep(PyObject* self, PyObject* args) {
    unsigned long ticks;
    if (!PyArg_ParseTuple(args, "k", &ticks)) {
        return NULL;
    }
    ksleep(ticks);
    Py_RETURN_NONE;
}

static PyObject* avocet_getc(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    char c = kgetc();
    return PyUnicode_FromStringAndSize(&c, 1);
}

static PyObject* avocet_draw_rect(PyObject* self, PyObject* args) {
    int x, y, width, height;
    unsigned int color;
    if (!PyArg_ParseTuple(args, "iiiii", &x, &y, &width, &height, &color)) {
        return NULL;
    }
    (void)x; (void)y; (void)width; (void)height; (void)color;
    Py_RETURN_NONE;
}

static PyObject* avocet_draw_pixel(PyObject* self, PyObject* args) {
    int x, y;
    unsigned int color;
    if (!PyArg_ParseTuple(args, "iii", &x, &y, &color)) {
        return NULL;
    }
    (void)x; (void)y; (void)color;
    Py_RETURN_NONE;
}

static PyObject* avocet_flush_frame(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    Py_RETURN_NONE;
}

static PyObject* avocet_execute_command(PyObject* self, PyObject* args) {
    const char* cmd_string;
    if (!PyArg_ParseTuple(args, "s", &cmd_string)) {
        return NULL;
    }
    int result = parse_and_execute(cmd_string);
    return PyLong_FromLong(result);
}

static PyMethodDef AvocetMethods[] = {
    {"kprint", avocet_kprint, METH_VARARGS, NULL},
    {"clear_screen", avocet_clear_screen, METH_NOARGS, NULL},
    {"get_ticks", avocet_get_ticks, METH_NOARGS, NULL},
    {"sleep", avocet_sleep, METH_VARARGS, NULL},
    {"getc", avocet_getc, METH_NOARGS, NULL},
    {"draw_rect", avocet_draw_rect, METH_VARARGS, NULL},
    {"draw_pixel", avocet_draw_pixel, METH_VARARGS, NULL},
    {"flush_frame", avocet_flush_frame, METH_NOARGS, NULL},
    {"execute_command", avocet_execute_command, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef avocetmodule = {
    PyModuleDef_HEAD_INIT,
    "avocet_core",
    NULL,
    -1,
    AvocetMethods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_avocet_core(void) {
    return PyModule_Create(&avocetmodule);
}
