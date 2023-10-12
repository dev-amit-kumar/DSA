// https://leetcode.com/problems/intersection-of-two-linked-lists/

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
    ListNode *bruteForce(ListNode *headA, ListNode *headB)
    {
        while (headA != NULL)
        {
            ListNode *temp = headB;
            while (temp != NULL)
            {
                // if both nodes are same
                if (temp == headA)
                    return headA;
                temp = temp->next;
            }
            headA = headA->next;
        }
        // intersection is not present between the lists return null
        return NULL;
    }

    ListNode *hashing(ListNode *headA, ListNode *headB){
        unordered_set<ListNode *> st;
        while (headA != NULL)
        {
            st.insert(headA);
            headA = headA->next;
        }
        while (headB != NULL)
        {
            if (st.find(headB) != st.end())
                return headB;
            headB = headB->next;
        }
        return NULL;
    }
};