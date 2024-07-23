#include<iostream>
#include<time.h>

using namespace std;

int main()
{
    // First card being dealt
    srand(time(0));
    int total_hand;
    int start = rand() % 13 + 1;

    if(start == 1){
        cout << "Drew an Ace" << endl;
        total_hand = 11;
    } else if(start == 8){
        cout << "Drew an 8" << endl;
        total_hand = 8;
    } else if(start >= 2 && start <= 10){
        cout << "Drew a " << start << endl;
        total_hand = start;
    } else if(start == 11){
        cout << "Drew a Jack" << endl;
        total_hand = 10;
    } else if(start == 12){
        cout << "Drew a Queen" << endl;
        total_hand = 10;
    } else if(start == 13){
        cout << "Drew a King" << endl;
        total_hand = 10;
    }
    
    // The first run of the loop is the second dealer hand
    // After that it loops until it reaches 17, blackjack, or it busts
    while(total_hand < 17){
        int hand = rand() % 13 + 1;
        if(hand == 1){
            cout << "Drew an Ace" << endl;
            total_hand += 11;
        } else if(hand == 8){
            cout << "Drew an 8" << endl;
            total_hand += 8;
        } else if(hand >= 2 && hand <= 10){
            cout << "Drew a " << hand << endl;
            total_hand += hand;
        } else if(hand == 11){
            cout << "Drew a Jack" << endl;
            total_hand += 10;
        } else if(hand == 12){
            cout << "Drew a Queen" << endl;
            total_hand += 10;
        } else if(hand == 13){
            cout << "Drew a King" << endl;
            total_hand += 10;
        }

        // To determine the result of each hit.
        if(total_hand >= 17 and total_hand < 21){
            cout << "Final hand: " << total_hand << "." << endl;
        } else if(total_hand == 21){
            cout << "Final hand: " << total_hand << "." << endl;
            cout << "BLACKJACK!" << endl;
        } else if(total_hand >= 21 and total_hand <= 31){
            cout << "Final hand: " << total_hand << "." << endl;
            cout << "BUST." << endl;
        } else{
            cout << "Dealer has " << total_hand << "." << endl;
        }
    }

}
