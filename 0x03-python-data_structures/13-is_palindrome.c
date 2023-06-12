
#include "lists.h"

/**
 * reverse_list - Reverses a singly-linked list
 * @head: Pointer to the starting node of the list.
 * Return: Pointer to reversed list.
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a plaindrome.
 * @head: Pointer to the starting node of the linked list.
 * Return: 0 if linked list not a palindrome.
 *         1 if linked lisr is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *mid;
	size_t length = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		length++;
		temp = temp->next;
	}

	temp = *head;

	for (j = 0; j < (length / 2) - 1; j++)
		temp = temp->next;

	if ((length % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reverse = reverse_list(&temp);
	mid = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_list(&mid);

	return (1);
}
