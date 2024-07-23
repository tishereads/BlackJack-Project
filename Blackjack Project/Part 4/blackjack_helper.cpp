#include<iostream>
#include<time.h>

using namespace std;

void print_card_name(int card_rank){
    if(card_rank == 1){
        cout << "Drew an Ace" << endl;
    } else if(card_rank == 8){
        cout << "Drew an 8" << endl;
    } else if(card_rank >= 2 && card_rank <= 10){
        cout << "Drew a " << card_rank << endl;
    } else if(card_rank == 11){
        cout << "Drew a Jack" << endl;
    } else if(card_rank == 12){
        cout << "Drew a Queen" << endl;
    } else if(card_rank == 13){
        cout << "Drew a King" << endl;
    } else{
        cout << "BAD CARD" << endl;
    }
}

int draw_card(){
    int card_rank = rand() % 13 + 1;
    print_card_name(card_rank);
    if(card_rank == 11 || card_rank == 12 || card_rank == 13){
        return 10;
    } else if(card_rank == 1){
        return 11;
    } else{
        return card_rank;
    }
}

void print_header(string message){
    cout << "-----------\n" << message << "\n-----------" << endl;
}

int draw_starting_hand(string name){
    print_header(name + " TURN");
    return draw_card() + draw_card();
}

void print_end_turn_status(int hand_value){
    cout << "Final hand: " << hand_value << '.' << endl;
    if(hand_value == 21){
        cout << "BLACKJACK!" << endl;
    } else if(hand_value > 21){
        cout << "BUST." << endl;
    }
}

void print_end_game_status(int user_hand, int dealer_hand){
    cout << "-----------\nGAME RESULT\n-----------" << endl;
    if(user_hand > 21 || dealer_hand == 21 && user_hand < 21){
        cout << "Dealer wins!" << endl;
    } else if (dealer_hand == 21 && user_hand == 21){
        cout << "Push." << endl;
    } else if (user_hand <= 21 && dealer_hand > 21){
        cout << "You win!" << endl;
    } else if (user_hand > dealer_hand){
        cout << "You win!" << endl;
    } else if (dealer_hand > user_hand){
        cout << "Dealer wins!" << endl;
    } else if (dealer_hand == user_hand){
        cout << "Push." << endl;
    }
}

int main()
{
    srand(time(0));
    int user_total = draw_starting_hand("YOUR");
    bool loop = true;
    while(loop && user_total < 21){
        string hit;
        cout << "You have " << user_total << ". Hit (y/n)? ";
        cin >> hit;
        if(hit == "n"){
            loop = false;
        } else if(hit == "y"){
            user_total += draw_card();
        } else{
            cout << "Sorry I didn't get that." << endl;
        }
    }
    print_end_turn_status(user_total);
    int dealer_total = draw_starting_hand("DEALER");
    while(dealer_total < 17){
        cout << "Dealer has " << dealer_total << "." << endl;
        dealer_total += draw_card();
    }
    print_end_turn_status(dealer_total);
    print_end_game_status(user_total, dealer_total);
    return 0;
}
