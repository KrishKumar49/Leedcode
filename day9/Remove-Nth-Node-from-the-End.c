struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* fast = head;
    struct ListNode* slow = head;

    if (head->next == NULL) {
        return NULL;
    }

    int i = 0;
    while (i < n) {
        fast = fast->next;
        i++;
    }

    if (fast == NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    while (fast->next != NULL && fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    slow->next = slow->next->next;

    return head;
}
