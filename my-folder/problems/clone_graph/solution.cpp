/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node *, Node *> visited;
    Node* dfs(Node* node){
        if(!node) return NULL;
        int val = node->val;
        if(visited[node])
            return visited[node];
        Node* copy = new Node (node->val);
        visited[node] = copy;
        for(auto neig: node->neighbors){
            copy ->  neighbors.push_back(cloneGraph(neig));
        }
        return copy;
    }
    Node* cloneGraph(Node* node) {
        return dfs(node);
    }
};