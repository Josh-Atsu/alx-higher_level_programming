#include "lists.h"

/**
 * check_cycle - Check if a linked lists has a cycle
 * @list: Contains the linked lists
 * Return: 0 if no cycle or 1 if there  is
 */

int check_cycle(listint_t *list)
{
	listint_t *node, *ptr;

	if (!list || !list->next)
		return (0);
	node =  list; ptr = list;

	while (ptr != NULL && node != NULL && ptr->next != NULL)
	{
		ptr = ptr->next;
		node = node->next->next;
		if (ptr == node)
			return (1);
	}
	return (0);
}
