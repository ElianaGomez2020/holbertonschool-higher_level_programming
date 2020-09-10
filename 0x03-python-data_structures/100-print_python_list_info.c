#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python3.4m/Python.h"

void print_python_list_info(PyObject *p)
{
	Py_ssize_t c = 0;
	PyObject *itm = NULL;

	printf("[*] Size of the python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject*)(p))->allocated);
	for(; c < (Py_ssize_t)PyList_Size(p); c++)
	{
		itm = PyList_GetItem(p, c);
		printf("Element %i: %s", (int)c, itm->ob_type->tp_name);
	}
}