import random

money = 100



#Write your game of chance functions here
def coin_flip(coin, bet):
  global money
  comp = None
  while coin != 'quit':
    random_coin_flip = random.randint(1,2)
    if random_coin_flip == 1:
      comp = 'heads'
    else:
      comp = 'tails'
    while str(coin) != 'heads' and str(coin) != 'tails':
      print('Invalid choice. Please choose again.')
      coin = str(input('Please type heads or tails: '))
    while bet > money:
      print(f'You do no have enough money. You only have {money} dollars left')
      bet = int(input())
    if coin == comp:
      money += bet
      print(f'You have a match! You made {bet} dollars')
      print(f'Money left: {money}')
      coin = str(input('Please type heads or tails: '))
      bet = int(input(f'Place a bet between 1 and {money}: '))
    else:
      money -= bet
      print(f'Oh no! You did not match and lost {bet} dollars')
      print(f'Money left: {money}')
      if money <= 0:
        print('Gameover! Try again!')
        break
      coin = str(input('Please type heads or tails: '))
      bet = int(input(f'Place a bet between 1 and {money}: '))

def cho_han(guess, bet):
  global money
  while guess != 'quit' and money > 0:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice_add = die1 + die2
    o_or_e = None
    if dice_add % 2 == 0:
      o_or_e = 'evens'
    elif dice_add % 2 != 0:
      o_or_e = 'odds'
    if guess == o_or_e:
      money += bet
      print(f'You have a match! You made {bet} dollars')
      print(f'Money left: {money}')
      guess = input('Please choose again odds or evens: ')
      if guess == 'quit':
        break
      bet = int(input(f'Please another bet between 1 and {money}: '))
    if money == 0:
      print('Game over!')
      break
    else:
      money -= bet
      print(f'Ouch! It was {o_or_e} You lost {bet} dollars')
      print(f'Money left: {money}')
      guess = input('Please choose again odds or evens: ')
      bet = int(input(f'Please another bet between 1 and {money}: '))




#Call your game of chance functions here

# coin_flip(str(input('Please type heads or tails: ')), int(input(f'Place a bet between 1 and {money}: ')))

cho_han(str(input('Please type odds or evens: ')), int(input(f'Please please a bet between 1 and {money}: ')))