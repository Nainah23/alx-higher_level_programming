#include "lists.h"

/**
 * is_palindrome - checks whether is palindrome
 * @head: list head
 * Return: 0 if fail and 1 for success
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palind(head, *head));
}
/**
 * check_palind - Check is fn is a palindrome
 * @head: list head
 * @end: list end
 */
int check_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
