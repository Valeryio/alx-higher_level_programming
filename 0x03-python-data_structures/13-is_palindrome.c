#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - find a palindrome data structure
 * @head: the list
 *
 * Description: This function verify if all the parameters
 * of a linked list form a palindrome
 *
 * Return: 1 on success, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int *palInt = NULL, i = 0, listLength = 0, result = 0;
	listint_t *iterator = NULL;

	/*Return a 0 if the linked list is empty*/
	if (!head)
		return (0);

	/*Getting the length of the linked list*/
	iterator = *head;
	while (iterator != NULL)
	{
		listLength++;
		iterator = iterator->next;
	}

	palInt = malloc(sizeof(int) * listLength);
	if (!palInt)
	{
		free(palInt);
		return (0);
	}
	iterator = *head;

	/*Attribution of the right value to the dynamic table data structure */
	for (; i < listLength; i++)
	{
		palInt[i] = iterator->n;
		iterator = iterator->next;
	}

	/*Comparing different values*/
	for (i = 0; i < listLength / 2; i++)
		if (palInt[i] == palInt[listLength - (i + 1)])
			result++;

	/*Verification and returning the result*/
	if (result == (listLength / 2))
		return (1);
	else
		return (0);

	free(palInt);
}
