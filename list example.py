#블랙잭 게임

import random

cardPattern = ['Spade', 'Heart', 'Diamond', 'Club']
print(cardPattern[2][6])
print(cardPattern[2][2])

cardNum = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

cardDeck = [] #빈list
for pattern in cardPattern:
    for num in cardNum:
        card = [pattern, num]
        cardDeck.append(card)

print(cardDeck[0])

random.shuffle(cardDeck)


class player:
    def __init__(self,userName, credit=1000):
        self._name = userName
        self._credit = credit
        self.holdingCard = []
        self.score = 0

    def hit(self):
        self.holdingCard.append(cardDeck.pop())
        self.calcScore()

    def calcScore(self):
        self.score = 0
        for card in self.holdingCard:
            if card[1] == 'A' or card[1] == 'K' or card[1] == 'Q' or card[1] == 'J':   #card[0]=pattern
                self.score += 10
            else:
                self.score += card[1]
    def showPlayerInfo(self):
        print('='*50)
        print('[Player' + self._name+ ']' + 'Score: '+ str(self.score))
        for card in self.holdingCard:
            print(card)
        print('='*50)


class Dealer(player):
    def dealer_rule(self):
        self.calcScore()
        #딜러는 16이하이면 무조건 카드를 받아야한다.
        if self.score <= 16:
            print('딜러가 카드를 한 장 받습니다.')
            self.hit()

        else:
            print('딜러가 Stay 합니다.')

    def showPlayerInfo(self):
        print('' * 50 + '='*50)
        print('' * 50 +'[ Player' + self._name + ']' + 'Score: '+ str(self.score))
        for card in self.holdingCard:
            print(""*49, end="")
            print(card)
        print('' * 50 + '='*50)

p1 = player('강현우')
dealer = Dealer('Dealer')

print("게임시작")
print("카드를 한 장 받는다.")

p1.hit()
dealer.hit()

userInput = None

while userInput != 'q':
    dealer.showPlayerInfo()
    p1.showPlayerInfo()

    userInput = input("h or s? : ")

    if userInput == "h":
        print("플레이어 {0}이 카드를 받습니다.". format(p1._name))
        dealer.dealer_rule()
        p1.hit()

    elif userInput == 's':
        print('점수를 계산합니다')
        dealer.dealer_rule()
        break

    else:
        print('잘못된 입력입니다.')


print('\n점수를 계산합니다.')

dealer.showPlayerInfo()
p1.showPlayerInfo()

if dealer.score > 21:
    print('딜러 버스트! 모든 플레이어 Win')

elif p1.score == 21:
    print('플레이어 {0} Black Jack!'.format(p1._name))

elif p1.score > dealer.score:
    print('플레이어 {0} 승리'.format(p1._name))

elif p1.score ==dealer.score:
    print('무승부')

else:
    print("딜러 승")


# def hit():
#     card = cardDeck.pop()
#     if card[1] == 'A' or card[1] == 'K' or card[1] == 'Q' or card[1] == 'J':
#         return 10
#     else:
#         return card[1]
#
# print("게임시작")
# print("카드를 한 장 받는다.")
# score = hit()
#
# userlnput = None
#
# while userlnput != 'q':
#     print("현재 점수는 {0}입니다.".format(score))
#     userlnput = input("카드를 한장 더 받으시겠습니까? Hit:h/ Stay:s")
#
#     if userlnput == 'h':
#         print("hit")
#         score += hit()
#
#     elif userlnput == 's':
#         print("점수를 계산한다")
#         print("최종 점수는 {0}".format(score))
#         print("게임을 종료")
#         break
#     else:
#         print("잘못된 입력입니다.")
#
