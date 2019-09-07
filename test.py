import random as r

s = '23456789TJQKA'
Cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10,
         'A': (1, 11)}
Suits = ['Diamond', 'Hearts', 'Club', 'Spade']
wallet = 0
bet = 0
DealerCards = []
PlayerCards = []
DealerCardKey = []
PlayerCardKey = []


def getUserInfo():
    global wallet
    print('Welcome To BlackJack')
    name, age = input('Enter you Name,Age ').split()
    print("Hello ", name)
    wallet = int(input('Enter the total amount of money you wish to Gamble '))


def getBet():
    global bet
    global wallet
    var = True
    
    print('Amounts to be bet are multiples of 10 $ ')
    while var:
        bet = int(input('Enter you bet amount '))
        if bet <= wallet:
             if bet % 10 == 0:
                var = False
            
             else:
                print('Enter correct bet')
        else:
            print('You cannot bet due to insufficient balance') 


def DealerCardAdd(n):
    global DealerCards
    for i in range(n):
        j = s[r.randint(0, 12)]
        DealerCards.append(Cards[j])
        x = Suits[r.randint(0, 3)]
        DealerCardKey.append([x, j])


def PlayerCardAdd(n):
    global PlayerCards
    for i in range(n):
        j = s[r.randint(0, 12)]
        PlayerCards.append(Cards[j])
        x = Suits[r.randint(0, 3)]
        PlayerCardKey.append([x, j])


def display(n):
    print('\nDealer\'s cards are',end =' ')
    if n == 0:
        for i in DealerCardKey:
            print(" {}({})".format(i[0],i[1]),end=' ')
        print('||Sum --> {}'.format(addition(DealerCards)))
    if n == 1:
        for i in range(1):
            print("{}({})".format(DealerCardKey[0][0],DealerCardKey[0][1]))
       
    print('\nYour cards are ',end=' ')
    for i in PlayerCardKey:
        print(" {}({})".format(i[0],i[1]),end=' ')
    print('||Sum --> {}'.format(addition(PlayerCards)))
    print('\n')
    


def addition(arr):
    sum = 0
    for element in arr:
        if isinstance(element, int):
            sum += element

        else:
            if (sum <= 10):
                sum += 11

            else:
                sum += 1

    return sum


def isBlackjack(s):
    if (s == 21):
        print("BLACKJACK!!")
        return True
    else:
        return False


def isBusted(s):
    if (s > 21):
        print("BUSTED")
        return True
    else:
        return False


def options():
    global PlayerCards
    x = 0
    print('Enter \n H --> Hit\n S--> Stand \n')
    if len(PlayerCards) == 2:
        print(' D --> DoubleDown\n')
        x = 2
    elif len(PlayerCards) == 2 and PlayerCards[0] == PlayerCards[1]:
        print('P --> Split')
        x = 1
    o = input("Please enter your option ")
    if o == 'H' or o == 'h':
        hit()
    elif o == 'S' or o == 's':
        stand()
    elif o == 'p' or o == 'P' and x == 1:
        split()
    elif o == 'D' or o == 'd' and x == 2:
        doubleDown()
    else:
        print("Please enter only valid values. \n Try again")
    


def startGame():
    getBet()
    DealerCardAdd(2)
    PlayerCardAdd(2)
    if isBlackjack(addition(PlayerCards)) and not isBlackjack(addition(DealerCards)):
        display(0)
        print("You Win")
    else:
        display(1)
        options()


def hit(a):
    global wallet
    PlayerCardAdd(1)
    display(1)
    if isBlackjack(addition(PlayerCards)):
        victory()

    elif isBusted(addition(PlayerCards)):
        display(0)
        loss()
    elif a == 1:
        stand()
    else:
        options()


def stand():
    r = 0
    global DealerCards
    while addition(DealerCards) < 17 or isSoftSeventeen():
        DealerCardAdd(1)
        display(0)
        if isBlackjack(addition(DealerCards)):
            r = 1
            loss()
        elif isBusted(addition(DealerCards)):
            r = 1
            victory()
    if r == 0:
        display(0)
        if addition(DealerCards) > addition(PlayerCards):
            loss()
        elif addition(DealerCards) < addition(PlayerCards):
            victory()
        else:
            print("PUSH")
            wishToContinue()


def isSoftSeventeen():
    try:
        if addition(DealerCards) == 17 and (DealerCards.index(2) + 1) * (DealerCards.index(4) + 1) * (
                DealerCards.index(11)
                + 1) >= 0:
            return True
    except ValueError:
        return False


def victory():
    global wallet
    global bet
    print("You Win")
    wallet += (1.5 * bet)
    print("Game Over.You have {0} $ in your wallet".format(wallet))
    wishToContinue()


def loss():
    global wallet
    global bet
    print("You Lose")
    wallet -= bet
    print("Game Over.You have {0} $ in your wallet".format(wallet))
    if wallet <= 0:
        print("Sorry you are out of the game")
    else:
        wishToContinue()


def wishToContinue():
    global DealerCards, PlayerCards, DealerCardKey, PlayerCardKey
    a = input("Do you wish to continue to play Y/N ")
    if a == 'Y' or a == 'y':
        DealerCards = []
        PlayerCards = []
        DealerCardKey = []
        PlayerCardKey = []
        startGame()
    else:
        print("Goodbye from the LA Python CASINO")


def doubleDown():
    global bet
    bet *= 2
    hit(1)
    


def split():
    global PlayerCards
    global wallet
    w = wallet
    y = PlayerCards[1]
    i = 0
    if i == 0:
        PlayerCardAdd(1)
        PlayerCards.remove(y)
        options()
        if w >= wallet:
            i += 1
    if i == 1:
        PlayerCards = [y]
        PlayerCardAdd(1)
        options()


getUserInfo()
startGame()
