from blackjack_helper import *

user_total = draw_starting_hand("YOUR")
loop = True
while loop and user_total < 21:
    hit = input("You have {}. Hit (y/n)? ".format(user_total))
    if hit == "n":
        loop = False
    elif hit == "y":
        user_total += draw_card()
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_total)

dealer_total = draw_starting_hand("DEALER")
while dealer_total < 17:
    print("Dealer has {}.".format(dealer_total))
    dealer_total += draw_card()
print_end_turn_status(dealer_total)

print_end_game_status(user_total, dealer_total)
