#include "Python.h"
#include <stdio.h>

void print_python_string(PyObject *op)
{
	reprint(PyString_FromString("Bytes should be printed"));
	printf("[.] string object info\n");
	if (strcmp(op->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(op))
	{
		printf("  type: compact ascii\n");
	}
	if (PyUnicode_IS_COMPACT(op) && !PyUnicode_IS_ASCII(op))
	{
		printf("  type: compact unicode object\n");
	}
	printf("  length: %lu\n", ((PyVarObject *) op)->ob_size);
	printf("  value: ");
	PyObject_Print(op, stdout, Py_PRINT_RAW);
	printf("\n");
}
