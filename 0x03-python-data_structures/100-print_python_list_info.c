#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info -function
 * @p: pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	unsigned int c;
	
	printf("[*] Size of the python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (c = 0; c < Py_SIZE(p); c++)
	{
		printf("Element %i: %s\n", c, Py_TYPE(PyList_GetItem(p, c))->tp_name);
	}
}
