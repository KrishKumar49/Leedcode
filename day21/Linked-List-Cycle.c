#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

bool hasCycle(struct Linked-List-Cycle)
{
    if (head == NULL || head->next == NULL) {
        return false;
    }

    struct ListNode *slow = head;
    struct ListNode *fast = head->next;
    
    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return true; 
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return false;   
    
};
