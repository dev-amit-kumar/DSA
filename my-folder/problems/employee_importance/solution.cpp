/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
    void dfs(vector<Employee*> employees, int node, vector<int> &visited,map<int, int> index, int &ans ){
        visited[node] = 1;  
        ans += employees[node] -> importance;
        vector<int> adj = employees[node] -> subordinates;
        for(auto it: adj){
            if(!visited[index[it]]){
                dfs(employees, index[it], visited, index, ans);
            }
        }
    }

public:
    int getImportance(vector<Employee*> employees, int id) {
        vector<int> visited(employees.size(), 0);
        map<int, int> index;
        for(int i = 0; i< employees.size(); i++){
            index[employees[i] -> id] = i;
        }
        int ans = 0;
        dfs(employees, index[id], visited, index, ans );
        return ans;
    }
};