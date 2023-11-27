#include "lists.h"

/**
 * check_cycle - function to check cycle
 * @list: list
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *forward;
	listint_t *backward;

	if (!list || !list->next)
	{
		return (0);
	}

	forward = list;
	backward = list;

	while (backward != NULL && forward != NULL && forward->next != NULL)
	{
		backward = backward->next;
		forward = forward->next->next;

		if (backward == forward)
		{
			return (1);
		}
	}
	return (0);
}
