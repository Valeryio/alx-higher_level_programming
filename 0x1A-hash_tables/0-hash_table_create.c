#include "hash_tables.h"

/**
 * hash_table_create - creates an hash table
 *
 * @size: (unsigned long int), the size of the hash table
 * Description: This function creates an hash tables and
 * send it.
 * Return: A pointer
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t* table = NULL;

	table = (hash_table_t*) malloc(sizeof(hash_table_t));

	if (!table)
		return (NULL);

	table->size = size;
	table->array = NULL;

	return (table);
}
