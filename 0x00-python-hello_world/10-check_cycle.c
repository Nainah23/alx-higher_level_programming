#include "lists.h"
/**
 * check_cycle - Checks whether or not the list has a cycle
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (!list || !list->next)
		return (0);
	a = list;
	b = list;

	while (b != NULL && a != NULL && a->next != NULL)
	{
		b = b->next;
		a = a->next->next;
		if (b == a)
			return (1);
	}
	return (0);
}
