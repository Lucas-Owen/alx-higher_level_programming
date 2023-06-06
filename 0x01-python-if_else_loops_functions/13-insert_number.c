#include "lists.h"

/**
 * insert_node - insert a node to a sorted linked list
 * @head: Head of the linked list
 * @number: value of the node
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL, *curr;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
		return (add_nodeint_end(head, number));
	curr = *head;
	while (curr)
	{
		if (number > curr->n)
		{
			prev = curr;
			curr = curr->next;
			continue;
		}
		break;
	}
	if (prev == NULL)
	{
		add_nodeint_end(&prev, number);
		if (prev)
		{
			prev->next = *head;
			*head = prev;
		}
		return (prev);
	}
	prev->next = NULL;
	if (add_nodeint_end(&prev->next, number))
		prev->next->next = curr;
	else
	{
		prev->next = curr;
	}
	return (prev->next);
}
