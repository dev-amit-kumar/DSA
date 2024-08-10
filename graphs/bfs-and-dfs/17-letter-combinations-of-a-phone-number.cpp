// Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

void letterCombinations(string digits, vector<string>& output, string &temp, vector<string>& pad, int index){
    if(index == digits.size()){
        output.push_back(temp);
        return;
    }
    string value = pad[digits[index]-'0'];
    for(int i=0; i<value.size(); i++){
        temp.push_back(value[i]);
        letterCombinations(digits, output, temp, pad, index+1);
        temp.pop_back();
    }
}

vector<string> letterCombinations(string digits) {
    if(digits.empty())
        return {};
    vector<string> pad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> output;
    string temp;
    letterCombinations(digits, output, temp, pad, 0);
    return output;
}

int main()
{
    string digits = "23";
    vector<string> pad = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> result = letterCombinations(digits);
    for (int i = 0; i < result.size(); i++)
        cout << result[i] << (i != result.size() - 1 ? ", " : "\n") ;
    cout << result.size() << endl;
}