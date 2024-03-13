#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number into a stored single linked list
 * @head: double pointer to the linked list
 * @number: the number to add
 * Return: address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *node;
	int x = 0;

	if (head == NULL || *head == NULL)
		return (NULL);
	ptr = *head;
	while (ptr->next != NULL)
	{
		if (number >= ptr->n)
			x++;
		ptr = ptr->next;
	}
	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;
	ptr = *head;
	while (x > 1)
	{
		ptr = ptr->next;
		x--;
	}
	node->next = ptr->next;
	ptr->next = node;
	return (ptr);

}
