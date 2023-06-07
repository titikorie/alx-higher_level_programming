#include "lists.h"

/**
 * check_cycle - check for loop in LL
 * @list: pointer to the beginning of the node
 * Return: if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = slow->next;

	while (slow != NULL && fast->next != NULL
		&& fast->next->next != NULL)
	{
		if (slow ==fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
