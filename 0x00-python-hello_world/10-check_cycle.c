#include "lists.h"

/**
 * check_cycle - function to check if cycle.
 * @list: Pointer to head
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list, *temp2 = list;

	while (temp != NULL && temp2 != NULL)
	{
		temp = temp->next;
		if (temp == NULL)
			return (0);
		temp = temp->next;
		temp2 = temp2->next;

		if (temp == temp2)
			return (1);
	}
	return (0);
}
