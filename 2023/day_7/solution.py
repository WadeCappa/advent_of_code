from enum import IntEnum
import sys

class HandType(IntEnum):
    FIVE_KIND = 1
    FOUR_KIND = 2
    FULL_HOUSE = 3
    THREE_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

values = {
    'A':2,
    'K':3,
    'Q':4,
    'T':6,
    '9':7,
    '8':8,
    '7':9,
    '6':10,
    '5':11,
    '4':12,
    '3':13,
    '2':14,
    'J':15,
}

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        freq = {}
        for c in cards:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        jokers = 0
        if 'J' in freq:
            jokers = freq['J']

        highestCombo = 0
        for c, v in freq.items():
            if c != 'J':
                highestCombo = max(highestCombo, v)
        highestCombo += jokers
        
        if highestCombo == 5:
            self.type = HandType.FIVE_KIND
        elif highestCombo == 4:
            self.type = HandType.FOUR_KIND
        elif highestCombo == 3:
            if (len(freq) == 3 and 'J' in freq) or (len(freq) == 2 and 'J' not in freq):
                self.type = HandType.FULL_HOUSE
            else:
                self.type = HandType.THREE_KIND
        elif highestCombo == 2:
            if len(freq) == 3:
                self.type = HandType.TWO_PAIR
            else:
                self.type = HandType.ONE_PAIR
        else:
            self.type = HandType.HIGH_CARD
        self.ordering = [k for k, v in sorted(freq.items(), key=lambda x:(x[1] * 1000) - values[x[0]])][::-1]
        self.freq = freq

    def __repr__(self): 
        return self.cards
        # res = []
        # for c in self.ordering:
            # f = self.freq[c]
            # for _ in range(f):
                # res.append(c)
        # return "".join(res)

    def __lt__(self, other):
        if self.type == other.type:
            p = 0
            
            # The commented solution here is more correct. But the rules of day-7 say just go through 
            # the ordering of the cards as from the game input, not based on pairing
            while p < len(self.cards):
                if self.cards[p] != other.cards[p]:
                    return values[self.cards[p]] < values[other.cards[p]]

                # if self.freq[self.ordering[p]] != other.freq[other.ordering[p]]:
                    # print("incorrect comparison of hands")
                # if self.ordering[p] != other.ordering[p]:
                    # return values[self.ordering[p]] < values[other.ordering[p]]
                p += 1
            print(f"could not find ordering for {self.cards} and {other.cards}")

        return self.type < other.type

def buildHand(line):
    cards, bid = line.split()
    return Hand(cards, int(bid))

if __name__ == "__main__":
    input = sys.argv[1]
    hands = []
    with open(input) as f:
        for l in f:
            hands.append(buildHand(l))

    hands.sort()
    print(hands)
    res = 0
    for i, h in enumerate(hands[::-1]):
        # print(f"{h.cards}, with bid {h.bid} in place {i + 1}")
        res += h.bid * (i + 1)
    print(res)