import random

# Please do not use these functions for actual gambling. The author does not take any liabilities for any damages or losses, and does not guarantee that the processes are truly random.

money = 100

#Write your game of chance functions here

def valid_bet(bet):
  try:
    float(bet)
  except ValueError:
    print("You did not enter a number as a bet.")
    raise ValueError
  if bet < 0:
    print("You have entered a negative bet. Try again with a positive number.")
    raise ValueError
  if bet > money:
    print("You have insufficient funds. Try entering a bet that is lower than your money.")
    raise ValueError

def generate_outcome(result, bet):
  if result:
    print("You have won ", str(2 * bet), "!\n", sep="")
    return 2*bet
  else:
    print("You have lost ", str(bet), ".\n", sep="")
    return -bet

def money_available():
  print("You now have $", money, " available.", sep="")

def coin_flip(bet, call):
  """Performs a coin flip of a "fair" two-sided coin

    Parameters:
    bet (int): Amount of the bet placed
    call (str): Side called by the player, either "Heads" or "Tails".

    Returns:
    int: Amount won/lost.
  """
  # 0 - heads, 1 - tails
  print("*** Coin Flip! ***\n")
  if call.casefold() in ["heads", "h", "head"]:
    calluni = "Heads"
  elif call.casefold() in ["tails", "t", "tail"]:
    calluni = "Tails"
  else:
    print("You have entered an invalid call. Try 'Heads' or 'Tails'.")
    raise ValueError
  valid_bet(bet)
  print("You have called ", calluni, "!", sep="")
  outcome = random.randint(0,1)
  if outcome == 0:
    print("The coin shows Heads!")
    outstr = "Heads"
  else:
    print("The coin shows Tails!")
    outstr = "Tails"
  result = (calluni == outstr)
  return generate_outcome(result, bet)
  
def cho_han(bet, call):
  """Performs the game "Cho-Han" on two "fair" 6-sided dice. The function adds the results of the two dice together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.

    Parameters:
    bet (int): Amount of the bet placed
    call (str): Call by the player, either "Odd" or "Even".

    Returns:
    int: Amount won/lost.
  """
  # 0 - odd, 1 - even
  print("*** Cho-Han! ***\n")
  if call.casefold() in ["odd", "o"]:
    calluni = "Odd"
  elif call.casefold() in ["even", "e"]:
    calluni = "Even"
  else:
    print("You have entered an invalid call. Try 'odd' or 'even'.")
    raise ValueError
  valid_bet(bet)
  print("You have called ", calluni, "!", sep="")
  die1 = random.randint(1,6)
  print("The first die shows", die1)
  die2 = random.randint(1,6)
  print("The second die shows", die2)
  outcome = die1 + die2
  if outcome % 2 == 0:
    print("The sum is ", outcome, ", which is even!", sep="")
    outstr = "Even"
  else:
    print("The sum is ", outcome, ", which is odd!", sep="")
    outstr = "Odd"
  result = (calluni == outstr)
  return generate_outcome(result, bet)

def card_translator(card):
  descriptive_deck = [False,False,"2","3","4","5","6","7","8","9","J","Q","K","A"]
  try:
    matched_card = descriptive_deck[card]
  except:
    print("Internal error: Error when matching cards in card_translator.")
  if matched_card == False:
    print("Internal error: Error when matching cards in card_translator.")
  return matched_card

def deck_of_cards(bet):
  """Draws "randomly" two cards from a deck of cards. If the value of the first card is higher, the player wins double of their original bet. If it is smaller, the player loses their bet. If there is a draw, the player receives their original bet back.

    Parameters:
    bet (int): Amount of the bet placed

    Returns:
    int: Amount won/lost.
  """
  # 0 - odd, 1 - even
  print("*** Drawing Cards! ***\n")
  valid_bet(bet)
  #constructing the deck
  one_colour = list(range(2,14))
  deck = 4 * one_colour
  card1, card2 = random.sample(deck, k=2)
  print("The first card is", card_translator(card1))
  print("The second card is", card_translator(card2))
  if card1 > card2:
    print("The first card is higher! You've won ", 2 * bet, "!", sep="")
    return 2*bet
  elif card1 == card2:
    print("It's a tie! You've got your bet back! You get ", bet, "!", sep="")
    return bet
  else:
    print("The second card is higher. You've lost ", bet, ".", sep="")
    return -bet



#Call your game of chance functions here

money += coin_flip(25, "heads")
money_available()
money += cho_han(43, "o")
money_available()
money += deck_of_cards(2)
money_available()
