#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t i;

    if (!PyList_Check(p))
        return;
    printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
    printf("[*] Allocated = %lu\n", ((PyListObject *) p)->allocated);
    for (i = 0; i < Py_SIZE(p); i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
