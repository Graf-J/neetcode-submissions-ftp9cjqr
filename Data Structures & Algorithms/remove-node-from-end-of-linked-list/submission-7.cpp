/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        while (n > 0) {
            fast = fast->next;
            n--;
        }

        ListNode dummy(0, head);
        ListNode* slow = &dummy;
        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;

        return dummy.next;
    }
};



// d -> 1 -> 2 -> 3 -> 4 -> nullptr
//                            f
//           s

// d -> 5 -> nullptr
//             f
// s