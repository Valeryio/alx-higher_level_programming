#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL, *iNode = NULL;

	if (!head)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);

	/*Initialisation of the new node*/
	newNode->n = number;
	newNode->next = NULL;

	iNode = *head;
	while (iNode != NULL)
	{
		if (iNode->n >= newNode->n)
		{
			newNode->next = iNode->next;
			iNode->next = newNode;
			break;
		}

		if ((iNode->n <= newNode->n) && (iNode->next == NULL))
		{
			newNode->next = iNode->next;
			iNode->next = newNode;
			break;
		}

/*		printf("NOus avons : %d <= %d <= %d\n", iNode->n, newNode->n, iNode->next->n);
*/
		if ((iNode->n <= newNode->n) && (newNode->n <= iNode->next->n))
		{
			newNode->next = iNode->next;
			iNode->next = newNode;
			break;
		}

		iNode = iNode->next;
	}

	return newNode;
}
