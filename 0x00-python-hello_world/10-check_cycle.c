#include "lists.h"

/**
 * check_cycle - checks for cycle in a singly linked list
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
listint_t *ele1 = list;
listint_t *ele2 = list;

if (!list)
return (0);

while (ele2 && ele1 && ele1->next)
{
ele2 = (*ele2).next;
ele1 = ele1->next->next;

if (ele2 == ele1)
return (1);
}

return (0);
}
