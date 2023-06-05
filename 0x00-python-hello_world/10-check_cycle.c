#include "lists.h"

/**
 * node_is_visited - Checks if a node has been visited in a linked list
 * to avoid loops
 * @head: The linked list containing all the nodes
 * @node: A new node to check if it has been visited
 * @prev: The node just before node, this is where to stop the search
 * Return: 1 if the node is in the list, 0 otherwise
 */
int node_is_visited(listint_t *head, listint_t *node, listint_t *prev)
{
	if (prev == NULL || node == NULL)
		return (0);
	while (head != prev)
	{
		if (head == node)
			return (1);
		head = head->next;
	}
	if (head == node)
		return (1);
	return (0);
}

/**
 * check_cycle - Finds the address where the loop begins
 * @list: The lsitint_t
 * Return: The address where the loop begins or NULL
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *prev = NULL;

	while (temp != NULL)
	{
		if (node_is_visited(list, temp, prev))
			return (1);
		prev = temp;
		temp = temp->next;
	}

	return (0);
}
