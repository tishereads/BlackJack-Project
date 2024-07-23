card = int(input())
if card == 1:
    print("Your hand value is 11.")
elif card >= 2 and card <= 10:
    print("Your hand value is " + str(card) + ".")
elif card >= 11 and card <= 13:
    print("Your hand value is 10.")
else:
    print("BAD CARD")
