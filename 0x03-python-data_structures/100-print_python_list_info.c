#include <Python.h>

/**
 * print_python_list_info - Prints information about Python lists
 * @p: PyObject pointer to a Python list
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, alloc, i;

	size = Py_SIZE(p);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	for (i = 0; i < size; ++i)
	{
		 printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
