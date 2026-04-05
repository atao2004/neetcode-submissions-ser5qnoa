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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* node = &dummy;

        while(list1 && list2) {
            if(list1->val < list2->val) {
                node->next=list1;
                list1 = list1->next;
            } else {
                node->next = list2;
                list2 = list2->next;
            }
            node=node->next;
        }
        while(list1 || list2) {
            if(list1) {
                node->next = list1;
                list1=list1->next;
            } else {
                node->next = list2;
                list2=list2->next;
            }
            node=node->next;
        }
        return dummy.next;
        // ListNode* head;
    //     ListNode* curr1 = list1;
    //     ListNode* curr2 = list2;
    //     if(list1 && list2 && list1 > list2) {
    //         head = list2;
    //     } else {
    //         head = list1;
    //     }

    //     while(curr1 && curr2) {
    //         if(curr1->val > curr2->val) {
    //             ListNode* temp2 = curr2->next;
    //             head->next = curr1;
    //             curr1 = curr1->next;
    //             curr2 = temp2;
    //             head = head->next;
    //         } else {
    //             ListNode* temp1 = curr1->next;
    //             curr1->next = curr2;
    //             curr2 = curr2->next;
    //             curr1 = temp1;
    //             head = head->next;
    //         }
    //     }
    //     return head;
    }


};
