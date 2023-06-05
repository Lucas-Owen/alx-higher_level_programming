#include "lists.h"

#define TABLE_SIZE (0xFF + 1)
/**
 * hash - hash function for the hash table
 * @node: Pointer value to be hashed
 * Return: index to insert to table
 */
int hash(listint_t *node)
{
	return ((((unsigned long) node) >> 4) & (TABLE_SIZE - 1));
}
/**
 * node_is_visited - Checks if a node has been visited in a linked list
 * to avoid loops
 * @lookup_table: The lookup table to add the nodes
 * @node: A new node to check if it has been visited, added to table if absent
 * Return: 1 if the node is in the table, 0 otherwise
 */
int node_is_visited(listint_t **lookup_table, listint_t *node)
{
	int index;

	if (node == NULL)
		return (0);
	index = hash(node);
	if (lookup_table[index] == node)
		return (1);
	lookup_table[index] = node;
	return (0);
}

/**
 * check_cycle - Finds the address where the loop begins
 * @list: The lsitint_t
 * Return: The address where the loop begins or NULL
 */
int check_cycle(listint_t *list)
{
	listint_t *lookup_table[TABLE_SIZE] = {NULL};

	while (list != NULL)
	{
		if (node_is_visited(lookup_table, list))
			return (1);
		list = list->next;
	}

	return (0);
}
