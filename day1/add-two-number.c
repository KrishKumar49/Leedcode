#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* l3 = malloc(sizeof(struct ListNode));
    struct ListNode *head = l3;

    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int val1 = 0;
        int val2 = 0;

        if (l1 != NULL) {
            val1 = l1->val;
            l1 = l1->next;
        }

        if (l2 != NULL) {
            val2 = l2->val;
            l2 = l2->next;
        }

        int sum = val1 + val2 + carry;
        int digit = sum % 10;
        carry = sum / 10;  // <-- FIXED: No 'int' here

        l3->val = digit;

        if (l1 != NULL || l2 != NULL || carry != 0) {
            l3->next = malloc(sizeof(struct ListNode));
            l3 = l3->next;
        } else {
            l3->next = NULL;
        }
    }

    return head;
}
