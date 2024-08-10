// CPP program to construct binary
// tree from given array in level
// order fashion Tree Node
#include <iostream>
#include <queue>
using namespace std;

/* A binary tree node has data,
pointer to left child and a
pointer to right child */
struct Node
{
    int data;
    Node *left, *right;
};

/* Helper function that allocates a
new node */
Node *newNode(int data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}

// Function to insert nodes in level order
Node *insertLevelOrder(int arr[], int i, int n)
{
    Node *root = nullptr;
    // Base case for recursion
    if (i < n)
    {
        root = newNode(arr[i]);

        // insert left child
        root->left = insertLevelOrder(arr,
                                      2 * i + 1, n);

        // insert right child
        root->right = insertLevelOrder(arr,
                                       2 * i + 2, n);
    }
    return root;
}

void levelOrderTraversal(Node *root)
{
    queue<Node *> q;
    q.push(root);
    q.push(NULL);
    while (!q.empty())
    {
        Node *temp = q.front();
        q.pop();
        if (temp == NULL)
        {
            // new level started
            cout << endl;
            if (!q.empty()) // deque is not empty
                q.push(NULL);
        }
        else
        {
            cout << temp->data << " ";
            if (temp->left)
                q.push(temp->left);
            if (temp->right)
                q.push(temp->right);
        }
    }
}

int diameter(Node *root, int &ans)
{
    if (root == NULL)
        return 0;
    diameter(root->left, ans);
    diameter(root->right, ans);
    int curr = ans + root->data;
    ans = max(ans, curr);
    return ans;
}

// Driver program to test above function
int main()
{
    int arr[] = {10, 2, -25, 20, 1, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    Node *root = insertLevelOrder(arr, 0, n);
    // cout << endl;
    // levelOrderTraversal(root);
    int ans = INT_MIN;
    diameter(root, ans);
    cout << ans << endl;
}
