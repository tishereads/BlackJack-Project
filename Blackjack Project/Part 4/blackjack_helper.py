from random import randint

def print_card_name(card_rank):
    if card_rank == 1:
        print("Drew an Ace")
    elif card_rank >= 2 and card_rank <= 7 or card_rank >= 9 and card_rank <= 10:
        print("Drew a " + str(card_rank))
    elif card_rank == 8:
        print("Drew an 8")
    elif card_rank == 11:
        print("Drew a Jack")
    elif card_rank == 12:
        print("Drew a Queen")
    elif card_rank == 13:
        print("Drew a King")
    else:
        print("BAD CARD")

def draw_card():
    card_rank = randint(1, 13)
    print_card_name(card_rank)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        return 10
    elif card_rank == 1:
        return 11
    else:
        return card_rank

def print_header(message):
    print("-----------\n{}\n-----------".format(message))

def draw_starting_hand(name):
    print_header(name + " TURN")
    return draw_card() + draw_card()

def print_end_turn_status(hand_value):
    print('Final hand: {}.'.format(hand_value))
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')

def print_end_game_status(user_hand, dealer_hand):
    print("-----------\nGAME RESULT\n-----------")
    if user_hand > 21 or dealer_hand == 21 and user_hand < 21:
        print("Dealer wins!")
    elif dealer_hand == 21 and user_hand == 21:
        print("Push.")
    elif user_hand <= 21 and dealer_hand > 21:
        print("You win!")
    elif user_hand > dealer_hand:
        print("You win!")
    elif dealer_hand > user_hand:
        print("Dealer wins!")
    elif dealer_hand == user_hand:
        print("Push.")


def player_turn():
    total = draw_starting_hand("YOUR")
    loop = True
    while loop and total < 21:
        hit = input("You have {}. Hit (y/n)? ".format(total))
        if hit == "n":
            loop = False
        elif hit == "y":
            total += draw_card()
        else:
            print("Sorry I didn't get that.")
    print_end_turn_status(total)
    return total


def dealer_turn():
    total = draw_starting_hand("DEALER")
    while total < 17:
        print("Dealer has {}.".format(total))
        total += draw_card()
    print_end_turn_status(total)
    return total
