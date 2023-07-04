#include "Python.h"
#include <unistd.h>

int _strcmp(const char *s1, const char *s2)
{
	for (; *s1 && *s2; s1++, s2++)
	{
		if (*s1 - *s2 != 0)
			return (*s1 - *s2);
	}
	if (*s1 || *s2)
		return (*s1 - *s2);
	return (0);
}
int _strlen(const char *s)
{
	int len = 0;

	while (*(s + len))
		len++;

	return (len);
}
int unsigned_long_to_string(unsigned long int num, char *str, int depth)
{
        int index;

        if (num == 0)
        {
                if (depth == 0)
                {
                        str[1] = '\0';
                        str[0] = '0';
                        return (1);
                }
                str[depth] = '\0';
                return (0);
        }

        index = unsigned_long_to_string(num / 10, str, depth + 1);
        str[index] = num % 10 + '0';
        return (index + 1);
}
void print(char *buf)
{
	write(STDOUT_FILENO, buf, _strlen(buf));
}
void print_python_string(PyObject *op)
{
	char str[21];

	print("[.] string object info\n");
	if (_strcmp(op->ob_type->tp_name, "str") != 0)
	{
		print("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(op))
	{
		print("  type: compact ascii\n");
	}
	if (PyUnicode_IS_COMPACT(op) && !PyUnicode_IS_ASCII(op))
	{
		print("  type: compact unicode object\n");
	}
	print("  length: ");
	unsigned_long_to_string(((PyVarObject *) op)->ob_size, str, 0);
	print(str);
	print("\n  value: ");
	PyObject_Print(op, stdout, Py_PRINT_RAW);
	fflush(stdout);
	print("\n");
}
