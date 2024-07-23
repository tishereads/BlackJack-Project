from random import randint

print("-----------\nYOUR TURN\n-----------")

user_start = randint(1, 13)
if user_start == 1:
  print("Drew an Ace")
  user_total = 11
elif user_start == 8:
  print("Drew an 8")
  user_total = 8
elif user_start >= 2 and user_start <= 10:
  print("Drew a " + str(user_start))
  user_total = user_start
elif user_start == 11:
  print("Drew a Jack")
  user_total = 10
elif user_start == 12:
  print("Drew a Queen")
  user_total = 10
elif user_start == 13:
  print("Drew a King")
  user_total = 10

loop = True
while loop:
  user_hand = randint(1, 13)
  if user_hand == 1:
    print("Drew an Ace")
    user_total = user_total + 11
  elif user_hand == 8:
    print("Drew an 8")
    user_total = user_total + 8
  elif user_hand >= 2 and user_hand <= 10:
    print("Drew a " + str(user_hand))
    user_total = user_total + user_hand
  elif user_hand == 11:
    print("Drew a Jack")
    user_total = user_total + 10
  elif user_hand == 12:
    print("Drew a Queen")
    user_total = user_total + 10
  elif user_hand == 13:
    print("Drew a King")
    user_total = user_total + 10
  
  if user_total == 21:
    print("Final hand: {}.".format(user_total))
    print('BLACKJACK!')
    loop = False
  elif user_total > 21 and user_total <= 31:
    print("Final hand: {}.".format(user_total))
    print('BUST.')
    loop = False
  else:
    # This code asks if the user wants to hit or not.
    typo = True
    while typo:
      hit = input("You have {}. Hit (y/n)? ".format(user_total))
      # It checks that it inputs either y or n.
      # It repeats the question if not answered properly.
      if hit == "n":
        print("Final hand: {}.".format(user_total))
        typo = False
        loop = False
      elif hit == "y":
        typo = False
      else:
        print("Sorry I didn't get that.")

print("-----------\nDEALER TURN\n-----------")

# First card being dealt
dealer_start = randint(1, 13)
if dealer_start == 1:
  print("Drew an Ace")
  dealer_total = 11
elif dealer_start == 8:
  print("Drew an 8")
  dealer_total = 8
elif dealer_start >= 2 and dealer_start <= 10:
  print("Drew a " + str(dealer_start))
  dealer_total = dealer_start
elif dealer_start == 11:
  print("Drew a Jack")
  dealer_total = 10
elif dealer_start == 12:
  print("Drew a Queen")
  dealer_total = 10
elif dealer_start == 13:
  print("Drew a King")
  dealer_total = 10

# The first run of the loop is the second dealer hand
# After that it loops until it reaches 17, blackjack, or it busts
while dealer_total < 17:
  dealer_hand = randint(1, 13)
  if dealer_hand == 1:
    print("Drew an Ace")
    dealer_total = dealer_total + 11
  elif dealer_hand == 8:
    print("Drew an 8")
    dealer_total = dealer_total + 8
  elif dealer_hand >= 2 and dealer_hand <= 10:
    print("Drew a " + str(dealer_hand))
    dealer_total = dealer_total + dealer_hand
  elif dealer_hand == 11:
    print("Drew a Jack")
    dealer_total = dealer_total + 10
  elif dealer_hand == 12:
    print("Drew a Queen")
    dealer_total = dealer_total + 10
  elif dealer_hand == 13:
    print("Drew a King")
    dealer_total = dealer_total + 10

  # To determine the result of each hit.
  if dealer_total >= 17 and dealer_total < 21:
    print("Final hand: {}.".format(dealer_total))
  elif dealer_total == 21:
    print("Final hand: {}.".format(dealer_total))
    print('BLACKJACK!')
  elif dealer_total > 21 and dealer_total <= 31:
    print("Final hand: {}.".format(dealer_total))
    print('BUST.')
  else:
    print("Dealer has {}.".format(dealer_total))

print("-----------\nGAME RESULT\n-----------")

if user_total > 21 or dealer_total == 21 and user_total < 21:
  print("Dealer wins!")
elif dealer_total == 21 and user_total == 21:
  print("Push.")
elif user_total <= 21 and dealer_total > 21:
  print("You win!")
elif user_total > dealer_total:
  print("You win!")
elif dealer_total > user_total:
  print("Dealer wins!")
elif dealer_total == user_total:
  print("Push.")
