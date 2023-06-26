#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to a PyObject
 * Return: void
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len;
	Py_ssize_t i;
	char *s;

	puts("[.] bytes object info");
	if (p == NULL || strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}
	s = ((PyBytesObject *) p)->ob_sval;
	len = ((PyVarObject *) p)->ob_size;
	printf("  size: %ld\n", len);
	len = len < 10 ? len + 1 : 10;
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
	fflush(stdout);
}

/**
 * print_python_float - Prints basic info about Python floats
 * @p: Pointer to a PyObject
 * Return: void
*/
void print_python_float(PyObject *p)
{
	char buf[99];
	unsigned int len, i;

	puts("[.] float object info");
	if (p == NULL || strcmp(p->ob_type->tp_name, "float") != 0)
	{
		puts("  [ERROR] Invalid Float Object");
		return;
	}
	sprintf(buf, "%.15lf", ((PyFloatObject *) p)->ob_fval);
	len = strlen(buf);
	for (i = len - 1; buf[i - 1] != '.' && buf[i] == '0'; i--)
	{
		buf[i] = '\0';
	}
	printf("  value: %s\n", buf);
	fflush(stdout);
}


/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to a PyObject
 * Return: void
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *obj;

	if (p == NULL || strcmp(p->ob_type->tp_name, "list") != 0)
	{
		puts("  [ERROR] Invalid List Object");
		return;
	}
	puts("[*] Python list info");
	printf("[*] Size of the Python List = %lu\n",
		((PyVarObject *) p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < ((PyVarObject *) p)->ob_size; i++)
	{
		obj = (PyListObject *) p;
		printf("Element %ld: %s\n", i,
			obj->ob_item[i]->ob_type->tp_name);
		if (strcmp(obj->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(obj->ob_item[i]);
		else if (strcmp(obj->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(obj->ob_item[i]);
	}
	fflush(stdout);
}
