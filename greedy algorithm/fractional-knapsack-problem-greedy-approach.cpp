#include<iostream>
#include <vector>

using namespace std;

struct Item
{
    int value;
    int weight;
};

bool static comp(Item a, Item b)
{
    double r1 = (double)a.value / (double)a.weight;
    double r2 = (double)b.value / (double)b.weight;
    return r1 > r2;
}

double bruteForce(int W, Item arr[], int n)
{
    sort(arr, arr+n, comp);
    int currWeight = 0;
    double totalValue = 0;

    for(int i = 0 ; i < n ;i++){
        if(currWeight + arr[i].weight <= W){
            currWeight += arr[i].weight;
            totalValue += arr[i].value;
        } 
        else {
            int remain = W - currWeight;
            totalValue += remain * (arr[i].value / arr[i].weight);
            break;
        }
    }
    return totalValue;
}

int main(){
    int n = 3, weight = 50;
    Item arr[n] = {{100, 20}, {60, 10}, {120, 30}};
    cout << "bruteForce" << bruteForce(weight, arr, n) << endl;
    return 0;
}