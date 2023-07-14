#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - a func that checks palindrome of singly linked list
 * @head: pointer to pointer to the first node of listint_t list
 *
 * Return: return 1, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - funct to know if is palindrome
 * @head: head list
 * @end: end list
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
