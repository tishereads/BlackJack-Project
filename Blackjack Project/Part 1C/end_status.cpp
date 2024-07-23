#include<iostream>

using namespace std;

int main()
{
    int current_hand;
    cin >> current_hand;
    if(current_hand == 21){
        cout << "BLACKJACK!"<< endl;
    } else if(current_hand >= 21 && current_hand <= 31){
        cout << "BUST." << endl;
    } else if(current_hand < 4 || current_hand > 31){
        cout << "BAD HAND VALUE!" << endl;
    }
}
