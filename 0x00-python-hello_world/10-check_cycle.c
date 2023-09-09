#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *temp = list;

	if (list == NULL)
		return (0);
	while (list->next != NULL)
	{
		if (list->next == NULL)
			return (0);

		while (temp->next != NULL)
		{
			if (list->next == temp)
				return (1);
			else if (temp == list)
				break;

			temp = temp->next;
		}
		temp = head;
		list = list->next;
	}
	return (0);
}
