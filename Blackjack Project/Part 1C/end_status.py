current_hand = int(input())
if current_hand == 21:
    print("BLACKJACK!")
elif current_hand >= 22 and current_hand <= 31:
    print("BUST.")
elif current_hand < 4 or current_hand > 31:
    print("BAD HAND VALUE!")
