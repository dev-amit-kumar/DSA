#include <iostream>
#include <queue>
#include <stack>
using namespace std;

class node
{
public:
    int data;
    node *left;
    node *right;

    node(int d)
    {
        this->data = d;
        this->left = NULL;
        this->right = NULL;
    }
};

node *buildTree(node *root)
{
    cout << "Enter the data for Node" << endl;
    int data;
    cin >> data;
    root = new node(data);
    if (data == -1)
        return NULL;

    cout << "Enter data left of " << data << endl;
    root->left = buildTree(root->left);

    cout << "Enter data right of " << data << endl;
    root->right = buildTree(root->right);

    return root;
}

void levelOrderTraversal(node *root)
{
    queue<node *> q;
    q.push(root);
    q.push(NULL);
    while (!q.empty())
    {
        node *temp = q.front();
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

void reverseLevelOrderTraversal(node *root)
{
    queue<node *> q;
    stack<int> s;
    q.push(root);
    q.push(NULL);
    while (!q.empty())
    {
        node *temp = q.front();
        q.pop();
        if (temp == NULL)
        {
            // new level started
            if (!q.empty())
            {
                // deque is not empty
                q.push(NULL);
                s.push(-1);
            }
        }
        else
        {
            s.push(temp->data);
            if (temp->right)
                q.push(temp->right);
            if (temp->left)
                q.push(temp->left);
        }
    }
    int temp;
    while (!s.empty())
    {
        temp = s.top();
        s.pop();
        if (temp != -1)
            cout << temp << " ";
        else
            cout << endl;
    }
}

void inOrder(node *root)
{
    if (root == NULL)
        return;
    inOrder(root->left);
    cout << root->data << " ";
    inOrder(root->right);
}

void preOrder(node *root)
{
    if (root == NULL)
        return;
    cout << root->data << " ";
    inOrder(root->left);
    inOrder(root->right);
}

void postOrder(node *root)
{
    if (root == NULL)
        return;
    inOrder(root->left);
    inOrder(root->right);
    cout << root->data << " ";
}

int main()
{
    node *root = NULL;
    // create a binary tree
    root = buildTree(root);

    // 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1

    // level order
    cout << "levelOrderTraversal" << endl;
    levelOrderTraversal(root);
    cout << "reverseLevelOrderTraversal" << endl;
    reverseLevelOrderTraversal(root);

    cout << endl
         << "inOrder -> ";
    inOrder(root);

    cout
        << endl
        << "preOrder -> ";
    preOrder(root);

    cout << endl
         << "postOrder -> ";
    postOrder(root);

    // return
    return 0;
}