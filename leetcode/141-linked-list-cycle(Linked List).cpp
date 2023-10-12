// https://leetcode.com/problems/linked-list-cycle/

#include <iostream>
#include <unordered_set>
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
    bool hasCycle(ListNode *head)
    {
        unordered_set<ListNode *> temp;
        while (head)
        {
            if (temp.find(head) != temp.end())
                return true;
            temp.insert(head);
            head = head->next;
        }
        return false;
    }
};