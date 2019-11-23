import random
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♠", "♥", "♦", "♣"]

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __lt__(self, other):
        return ranks.index(self.get_rank()) < ranks.index(other.get_rank())
     # lt is an override for > (smaller than) operator. Done to apply "biggest" or "smallest" titles for Python to then sort easily.

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i+1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_double_pair(self):
        pairs = 0
        for i in range(5):
            for p in range(i+1, 5):
                if self.cards[i].get_rank()==self.cards[p].get_rank():
	                    pairs += 1
        if pairs == 2:
            return True
        return False


    def is_four_of_kind(self):
        for i in range(5):
            for l in range(i+1, 5):
                if self.cards[i].rank_it()==self.cards[l].get_rank():
                    for x in range(l+1, 5):
                        if self.cards[i].get_rank()==self.cards[x].get_rank():
                            for y in range(x+1, 5):
                                if self.cards[i].get_rank()== self.cards[y].get_rank():
                                    return True
        return False

    def is_flush(self):
        suit = self.cards[0]
        for i in range(1,5):
            if suit != self.cards[i]:
                return False
        return True

    def is_straight(self):
    #need to sort the hand
        self.cards.sort()
    # special case A 2 3 4 5 (2 3 4 5 A)
        if self.cards[0].get_rank() == "2" and \
            self.cards[1].get_rank() == "3" and \
            self.cards[2].get_rank() == "4" and \
            self.cards[3].get_rank() == "5" and \
            self.cards[4].get_rank() == "A":
            return True
        for i in range(4):
            if ranks.index(self.cards[i].get_rank()) + 1 != ranks.index(self.cards[i+1].get_rank()):
                return False

    def ranking(self):
        if self.is_pair():
            return "A Pair"
        if self.is_double_pair():
            return "A Double Pair"
        if self.is_flush():
            return "A Flush"
        if self.is_straight():
            return "Straight"
        if self.is_four_of_kind():
            return "Four of a kind"
        if self.is_full_house():
            return "Full House"

new_deck = Deck()
for i in range(5):
    new_deck.shuffle()
    print(new_deck)
    hand = Hand(new_deck)
    hand.cards.sort()
    print (hand)


