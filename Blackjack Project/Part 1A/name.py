card = int(input())
if card == 1:
    print("Drew an Ace")
elif card == 8:
    print("Drew an 8")
elif card >= 2 and card <= 10:
    print("Drew a " + str(card))
elif card == 11:
    print("Drew a Jack")
elif card == 12:
    print("Drew a Queen")
elif card == 13:
    print("Drew a King")
else:
    print("BAD CARD")
