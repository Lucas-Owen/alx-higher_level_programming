#include <Python.h>
#include "structmember.h"
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about Python lists
 * @p: Pointer to a PyObject
 * Return: void
*/
void print_python_list(PyObject *p)
{
    Py_ssize_t i;

    if (p == NULL || !PyList_Check(p))
        return;
    printf("[*] Size of the Python List = %lu\n",
		((PyVarObject *) p)->ob_size);
    printf("[*] Allocated = %lu\n", ((PyListObject *) p)->allocated);
    for (i = 0; i < ((PyVarObject *) p)->ob_size; i++)
        printf("Element %ld: %s\n", i,
			((PyListObject *) p)->ob_item[i]->ob_type->tp_name);
}

/**
 * print_python_bytes - Prints basic info about Python lists and
 * Python bytes objects
 * @p: Pointer to a PyObject
 * Return: void
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len;
	Py_ssize_t i;
	char *s;

	puts("[.] bytes object info");
	if (p == NULL || !PyBytes_CheckExact(p))
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}
	PyBytes_AsStringAndSize(p, &s, &len);
	printf("  size: %ld\n", len);
	len = len <= 10 ? len : 10;
	printf("  trying string: %s\n", s);
	printf("  first %ld bytes: ", len);
	for (i = 0; i < len; i++)
	{
		printf("%02hhx", s[i]);
		if (i != len - 1)
			putchar(' ');
		else
			putchar('\n');
	}
}
