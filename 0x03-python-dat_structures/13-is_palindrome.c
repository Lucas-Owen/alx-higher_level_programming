#include "lists.h"

/**
 * is_palindrome_iterative - Checks if a linked list is a palindrome
 * Reverses the list then begins checking
 * @head: Head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome_iterative(listint_t **head)
{
	listint_t *rev_head = NULL, *curr, *temp = NULL;
	int len = 1;

	if (head == NULL || *head == NULL)
		return (0);
	add_nodeint_end(&rev_head, (*head)->n);
	curr = (*head)->next;
	/* Reverse copy the list */
	while (curr)
	{
		add_nodeint_end(&temp, curr->n);
		temp->next = rev_head;
		rev_head = temp;
		curr = curr->next;
		temp = NULL;
		++len;
	}
	temp = *head;
	curr = rev_head;
	len /= 2;
	while (len >= 0)
	{
		if (temp->n != curr->n)
			return (0);
		temp = temp->next;
		curr = curr->next;
		len--;
	}
	free_listint(rev_head);

	return (1);
}

/**
 * is_palindrome_recursive - Checks if a linked list is a palindrome
 * Recurses the list until the end then begins checking
 * @head: Head of the linked list
 * @tail: Initially as head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome_recursive(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	is_palindrome_recursive(head, tail->next);
	if ((*head)->n != tail->n)
		return (0);
	*head = (*head)->next;
	return (1);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;

	if (head == NULL)
		return (1);
	temp = *head;
	return is_palindrome_recursive(&temp, temp);
}
