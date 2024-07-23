#include<iostream>

using namespace std;

int main()
{
    int card;
    cin >> card;
    if(card == 1){
        cout << "Your hand value is 11." << endl;
    } else if(card >= 2 && card <= 10){
        cout << "Your hand value is " << card << "." << endl;
    } else if(card >= 11 && card <= 13){
        cout << "Your hand value is 10." << endl;
    } else{
        cout << "BAD CARD";
    }
    return 0;
}