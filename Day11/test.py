# from day11_blackJack import Deck, Player, Game, Turn, Card, revealCards
#
# print("\n🔍 TEST: Deck Initialization and Size")
# deck = Deck()
# print("Deck size:", deck.getDeckSize())  # Expect 52
# print("Top 3 cards:", deck.getDeck()[:3])
#
# print("\n🎲 TEST: Shuffling")
# deck.shuffle_deck()
# print("Shuffled top 3 cards:", deck.getDeck()[:3])
#
# print("\n🃏 TEST: Drawing One Card")
# card1 = deck.drawOneCard()
# print("Drew one card:", card1)
# print("Deck size now:", deck.getDeckSize())
#
# print("\n🃏 TEST: Drawing Multiple Cards")
# cards2 = deck.drawNCards(3)
# print("Drew 3 cards:", cards2)
# print("Deck size now:", deck.getDeckSize())
#
# print("\n👤 TEST: Player Initialization and Card Management")
# player = Player(type=1)
# print("Initial turn:", player.getTurn())
# player.incrementTurn()
# print("After increment turn:", player.getTurn())
#
# print("Initial score:", player.getScore())
# player.incrementScore()
# print("After increment score:", player.getScore())
#
# print("Adding one card...")
# player.addCard({'suit': 'spades', 'value': 10})
# print("Player cards:", player.getPlayerCards())
#
# print("Adding multiple cards...")
# player.addnCards([{'suit': 'hearts', 'value': 2}, {'suit': 'clubs', 'value': 5}])
# print("Player cards:", player.getPlayerCards())
#
# print("\n🧩 TEST: Round Setup")
# human = Player(1)
# dealer = Player(0)
# deck = Deck()
# deck.shuffle_deck()
# round1 = Turn(human, dealer, deck)
# round1.incrementTurnCount()
# print("Round count after increment:", round1.getTurn())
#
# print("\n▶️ TEST: Game Logic")
# deck = Deck()
# deck.shuffle_deck()
# game = Game(deck, human, dealer)
# print("Game initialized.")
# game.startGame()
# print("Shuffled deck started.")
# print("Game winning status:", game.isWinning())
#
# print("Appending a round to game...")
# game.appendRound(round1)
# print("Total rounds in game:", len(game.rounds))