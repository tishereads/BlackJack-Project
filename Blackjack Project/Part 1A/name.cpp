#include<iostream>

using namespace std;

int main()
{
    int card;
    cin >> card;
    if(card == 1){
        cout << "Drew an Ace" << endl;
    } else if(card == 8){
        cout << "Drew an 8" << endl;
    } else if(card >= 2 && card <= 10){
        cout << "Drew a " << card << endl;
    } else if(card == 11){
        cout << "Drew a Jack" << endl;
    } else if(card == 12){
        cout << "Drew a Queen" << endl;
    } else if(card == 13){
        cout << "Drew a King" << endl;
    } else{
        cout << "BAD CARD" << endl;
    }

}
