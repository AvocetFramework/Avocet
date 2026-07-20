#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <kernel.h>

static PyObject* sys_get_total_memory(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    unsigned long memory_kb = 128 * 1024;
    return PyLong_FromUnsignedLong(memory_kb);
}

static PyObject* sys_get_kernel_version(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    return PyUnicode_FromString("Avocet Kernel v0.1.0-Alpha (MSYS2-Simulated-Ring3)");
}

static PyObject* sys_get_cpu_vendor(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    return PyUnicode_FromString("GenuineIntel (Emulated)");
}

static PyObject* sys_reboot(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    kprint("[AVOCET SYSTEM] Reboot signal caught by Python host engine.\n");
    exit(0);
    Py_RETURN_NONE;
}

static PyObject* sys_shutdown(PyObject* self, PyObject* args) {
    (void)self;
    (void)args;
    kprint("[AVOCET SYSTEM] Shutdown signal caught by Python host engine.\n");
    exit(0);
    Py_RETURN_NONE;
}

static PyMethodDef SysBindingsMethods[] = {
    {"get_total_memory", sys_get_total_memory, METH_NOARGS, NULL},
    {"get_kernel_version", sys_get_kernel_version, METH_NOARGS, NULL},
    {"get_cpu_vendor", sys_get_cpu_vendor, METH_NOARGS, NULL},
    {"reboot", sys_reboot, METH_NOARGS, NULL},
    {"shutdown", sys_shutdown, METH_NOARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sysbindingsmodule = {
    PyModuleDef_HEAD_INIT,
    "avocet_sys",
    NULL,
    -1,
    SysBindingsMethods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_avocet_sys(void) {
    return PyModule_Create(&sysbindingsmodule);
}
