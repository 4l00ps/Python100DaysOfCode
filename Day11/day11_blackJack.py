import random

HUMANPLAYER = 1
COMPUTERPLAYER = 2


def revealCards(cards):
    for card in cards:
        print(f"{card['value']} of {card['suit']}")


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getCard(self):
        return {'suit': self.suit, 'value': self.value}


class Deck:
    def __init__(self):
        self.suits = ["hearts", "spades", "clover", "diamonds"]
        self.values = list(range(1, 14))  # 1 (Ace) to 13 (King)
        self.deck = self._initialize_deck()

    def _initialize_deck(self):
        deck = []
        for suit in self.suits:
            for value in self.values:
                playingCard = Card(suit, value)
                deck.append(playingCard.getCard())
        return deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def drawNCards(self, n):
        return [self.deck.pop() for _ in range(n) if self.deck]

    def drawOneCard(self):
        return self.deck.pop() if self.deck else None

    def getDeckSize(self):
        return len(self.deck)

    def canPlayMore(self):
        return self.getDeckSize() >= 4  # Enough for at least 2 players


class Player:
    def __init__(self, player_type):
        self.type = player_type
        self.score = 0
        self.roundCards = []

    def getScore(self):
        return self.score

    def incrementScore(self):
        self.score += 10

    def addCard(self, card):
        self.roundCards.append(card)

    def addnCards(self, cards):
        self.roundCards.extend(cards)

    def getPlayerCards(self):
        return self.roundCards

    def flushRoundCards(self):
        self.roundCards.clear()


class Round:
    def __init__(self, humanPlayer, computerPlayer, deck):
        self.human = humanPlayer
        self.dealer = computerPlayer
        self.deck = deck
        self.winner = None

    def getCardValue(self, card):
        value = card['value']
        if value >= 10:
            return 10
        elif value == 1:
            return 11 if self.getHandSum([card]) + 11 <= 21 else 1
        return value

    def getHandSum(self, cards):
        total = 0
        aces = 0
        for card in cards:
            if card['value'] == 1:
                aces += 1
            elif card['value'] >= 10:
                total += 10
            else:
                total += card['value']

        for _ in range(aces):
            total += 11 if total + 11 <= 21 else 1

        return total

    def play(self):
        self.human.flushRoundCards()
        self.dealer.flushRoundCards()

        self.human.addnCards(self.deck.drawNCards(2))
        self.dealer.addnCards(self.deck.drawNCards(2))

        print("\nYour cards:")
        revealCards(self.human.getPlayerCards())

        while self.getHandSum(self.human.getPlayerCards()) < 21:
            action = input("Hit or stand? (h/s): ").strip().lower()
            if action == 'h':
                self.human.addCard(self.deck.drawOneCard())
                print("\nYour cards:")
                revealCards(self.human.getPlayerCards())
            else:
                break

        human_sum = self.getHandSum(self.human.getPlayerCards())
        if human_sum > 21:
            print("You busted. Dealer wins.")
            self.dealer.incrementScore()
            return

        print("\nDealer's turn:")
        revealCards(self.dealer.getPlayerCards())

        while self.getHandSum(self.dealer.getPlayerCards()) < 17:
            self.dealer.addCard(self.deck.drawOneCard())
            revealCards(self.dealer.getPlayerCards())

        dealer_sum = self.getHandSum(self.dealer.getPlayerCards())

        print(f"\nYour total: {human_sum} | Dealer total: {dealer_sum}")

        if dealer_sum > 21 or human_sum > dealer_sum:
            print("You win!")
            self.human.incrementScore()
        elif dealer_sum > human_sum:
            print("Dealer wins.")
            self.dealer.incrementScore()
        else:
            print("It's a tie!")

        print(f"Remaining cards in deck: {self.deck.getDeckSize()}")


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.human = Player(HUMANPLAYER)
        self.dealer = Player(COMPUTERPLAYER)

    def startGame(self):
        while self.deck.canPlayMore():
            round_ = Round(self.human, self.dealer, self.deck)
            round_.play()
            print(f"\nScore → You: {self.human.getScore()} | Dealer: {self.dealer.getScore()}\n")
            again = input("Play another round? (y/n): ").strip().lower()
            if again != 'y':
                break
        print("\nThanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.startGame()