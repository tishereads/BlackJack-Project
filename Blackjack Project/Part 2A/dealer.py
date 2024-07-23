from random import randint

# First card being dealt
start = randint(1, 13)
if start == 1:
  print("Drew an Ace")
  total_hand = 11
elif start == 8:
  print("Drew an 8")
  total_hand = 8
elif start >= 2 and start <= 10:
  print("Drew a " + str(start))
  total_hand = start
elif start == 11:
  print("Drew a Jack")
  total_hand = 10
elif start == 12:
  print("Drew a Queen")
  total_hand = 10
elif start == 13:
  print("Drew a King")
  total_hand = 10

# The first run of the loop is the second dealer hand
# After that it loops until it reaches 17, blackjack, or it busts
while total_hand < 17:
  hand = randint(1, 13)
  if hand == 1:
    print("Drew an Ace")
    total_hand = total_hand + 11
  elif hand == 8:
    print("Drew an 8")
    total_hand = total_hand + 8
  elif hand >= 2 and hand <= 10:
    print("Drew a " + str(hand))
    total_hand = total_hand + hand
  elif hand == 11:
    print("Drew a Jack")
    total_hand = total_hand + 10
  elif hand == 12:
    print("Drew a Queen")
    total_hand = total_hand + 10
  elif hand == 13:
    print("Drew a King")
    total_hand = total_hand + 10

  # To determine the result of each hit.
  if total_hand >= 17 and total_hand < 21:
    print("Final hand: {}.".format(total_hand))
  elif total_hand == 21:
    print("Final hand: {}.".format(total_hand))
    print('BLACKJACK!')
  elif total_hand > 21 and total_hand <= 31:
    print("Final hand: {}.".format(total_hand))
    print('BUST.')
  else:
    print("Dealer has {}.".format(total_hand))
