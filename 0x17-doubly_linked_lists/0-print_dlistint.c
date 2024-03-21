#include "lists.h"

/**
 * print_dlistint - print the nodes of a list
 * @h: the list
 *
 * Description: This function prints all the nodes
 * of a list
 * Return: A number
 */

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *node = NULL;
	size_t number_of_nodes = 0;

	node = (void *) h;
	while (node != NULL)
	{
		number_of_nodes++;
		printf("%d\n", node->n);
		node = node->next;
	}

	return (number_of_nodes);
}
