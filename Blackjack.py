import re
import random as r





s = '23456789TJQKA'
Cards = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10,'A':(1,11)}
wallet = 0

DealerCards =[]
PlayerCards =[]






def geUserInfo():
    global wallet
    print('Welcome To BlackJack')
    name,age = input('Enter you Name,Age').split()
    wallet = int(input('Enter the total amount of money you wish to Gamble'))

def getBet():
    var = True
    while var:
        print('Amounts to be bet are multiples of 10 ')
        bet = int(input('Enter you bet amount '))
        if bet%10 == 0:
            var = False
        else:
            print('Enter correct bet')
def DealerCardAdd(n):
    global DealerCards
    for i in range(n):
        DealerCards.append(Cards[s[r.randint(0,13)]])

def PlayerCardAdd(n):
    global PlayerCards
    for i in range(n):
        PlayerCards.append(Cards[s[r.randint(0,13)]])

def addition(arr):
    sum = 0
    for element in arr:
        if isinstance(element,int):
            sum += element

        else:
            tup = element
            if(sum<=10):
                sum+=11
                
            else:
                sum+=1

    return sum

def isBlackjack(s):
    if(s==21):
        return True


def Options():
    print('Enter H --> Hit/n S--> Stand /n ')


def startGame():
    DealerCardAdd(2)
    PlayerCardAdd(2)
    if(isBlackjack(addition(DealerCardAdd))==True):
        print("You lose")
    elif(isBlackjack(addition(PlayerCardAdd))==True):
        print("You Win")
    else:





