class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        count = collections.Counter(hand)
        hand.sort()

        for card in hand:
            if count[card] > 0:
                for i in range(card, card + groupSize):
                    if count[i] == 0:
                        return False
                    else:
                        count[i] -= 1
        return True