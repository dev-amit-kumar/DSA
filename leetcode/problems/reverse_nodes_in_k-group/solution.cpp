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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode * first = head;
        ListNode * second = head;
        vector<int> values;
        while(second){
            count++;
            values.push_back(second -> val);
            if(count == k){
                for(int i = k-1; i >= 0; i--){
                    first -> val = values[i];
                    values.pop_back();
                    first = first -> next;
                }
                count = 0;
            }
            second = second -> next;
        }
        return head;
    }
};