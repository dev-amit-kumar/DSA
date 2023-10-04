// https://leetcode.com/problems/reverse-linked-list/description/

// Definition for singly-linked list.
struct ListNode{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr){}
    ListNode(int x) : val(x), next(nullptr){}
    ListNode(int x, ListNode *next) : val(x), next(next){}
};

class Solution{
public:
    ListNode *reverseList(ListNode *head){
        ListNode *newLL = nullptr;
        while(head != nullptr){
            ListNode *tempNext = head -> next;
            head -> next = newLL;
            newLL = head;
            head = tempNext;
        }
        return newLL;
    }
};