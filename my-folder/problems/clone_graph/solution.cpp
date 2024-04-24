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
    Node* dfs(Node * original, unordered_map<Node*, Node*>& visited_map){
        vector<Node*> neighbors;
        Node* clone = new Node(original -> val);
        visited_map[original] = clone;

        for(auto it: original->neighbors){
            if(visited_map.find(it) != visited_map.end()){
                neighbors.push_back(visited_map[it]);
            }else
                neighbors.push_back(dfs(it, visited_map));
        }
        clone -> neighbors = neighbors;
        return clone;
    }
public:
    Node* cloneGraph(Node* node) {
        unordered_map<Node*, Node*> visited_map;
        if(node == NULL) return NULL;
        if(node -> neighbors.size() == 0){
            Node* clone = new Node(node -> val);
            return clone;
        }
        return dfs(node, visited_map);
    }
};