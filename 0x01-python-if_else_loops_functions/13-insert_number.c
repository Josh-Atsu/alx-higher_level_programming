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
	listint_t *ptr = *head;
	listint_t *node = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!*head || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	else
	{
		while (ptr && ptr->n < number)
		{
			temp = ptr;
			ptr = ptr->next;
		}
		temp->next = node;
		node->next = ptr;
	}
	return (node);

}
