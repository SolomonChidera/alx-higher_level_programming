#include "lists.h"

/**
 * check_cycle - checks to see if a list has a cycle in it.
 * @list: the list to check
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *track = list;
	listint_t *seek = list;

	if (list == NULL)
		return (0);

	while (track && track->next)
	{
		seek = seek->next;
		track = track->next->next;

		if (seek == track)
			return (1);
	}
	return (0);
}
