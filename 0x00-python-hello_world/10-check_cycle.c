#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	if (!list)
		return (0);

	current = list;
	while (current != NULL)
	{
		if (current->next == list)
			return (1);

		current = current->next;
	}

	return (0);
}
