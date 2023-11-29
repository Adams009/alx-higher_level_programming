#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * indert_node - the function to insert node
 * @head: the head
 * @number: the number
 * Return: Always 0 on success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *present = *head;
	listint_t *new = NULL;
	listint_t *holder = NULL;

	if (!head)
	{
		return (NULL);
	}

	new = malloc(sizeof(listint_t));
	if (!new)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (present && present->n < number)
		{
			holder = present;
			present = present->next;
		}

		holder->next = new;
		new->next = present;
	}

	return (new);
}
