// https://leetcode.com/problems/rotate-list/description/

#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *rotateRight(ListNode *head, int k)
    {
        if (head == NULL || head->next == NULL || k == 0)
            return head;
        ListNode *temp = head;
        int length = 1;
        while (temp->next)
        {
            temp = temp->next;
            ++length;
        }
        temp->next = head;
        k = k % length;
        int n = length - k;
        while (n--)
        {
            temp = temp->next;
        }
        head = temp->next;
        temp->next = NULL;
        return head;
    }
};