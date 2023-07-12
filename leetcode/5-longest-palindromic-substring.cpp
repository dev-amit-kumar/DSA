// Link: https://leetcode.com/problems/longest-palindromic-substring/

#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(string ss)
{
    int n = ss.length();
    int left = 0;
    int right = n - 1;
    while (left <= right)
    {
        if (ss[left] != ss[right])
            return false;
        left++;
        right--;
    }
    return true;
}

string longestPalindrome(string s)
{
    int i = 0;
    int j = 0;
    int n = s.length();
    string currResult = "";
    while (i < n)
    {
        string temp = s.substr(i, j - i + 1);
        bool result = isPalindrome(temp);
        if (result == true && temp.length() > currResult.length())
            currResult = temp;
        j++;
        if (j == n)
        {
            i++;
            j = i;
        }
    }
    return currResult;
}

int main()
{
    string s = "whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone";
    cout << longestPalindrome(s) << endl;
}