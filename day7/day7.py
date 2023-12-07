from collections import Counter

def group_hand(most_common):
    if most_common[0][1] == 5:
        return 7
    elif most_common[0][1] == 4:
        return 6
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        return 5
    elif most_common[0][1] == 3:
        return 4
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        return 3
    elif most_common[0][1] == 2:
        return 2
    else:
        return 1

def rank_cards(hand_types):
    hand_types = {hand_type: sorted(hands) for hand_type, hands in hand_types.items()}
    print(hand_types.keys())
    card_ranks = hand_types["hc"] + hand_types["p"] + hand_types["2p"] + hand_types["3ok"] + hand_types["fh"] + hand_types["4ok"] + hand_types["5ok"]
    return card_ranks

if __name__ == "__main__":
    with open("day7.txt", "r") as f:
        hands = [
            (hand.split()[0], int(hand.split()[1])) 
            for hand in f.readlines()
        ]

    card_ranks = []
    for cards, bid in hands:
        most_common = Counter(cards).most_common()
        cards = cards.replace("T", "B").replace("J", "C").replace("Q", "D").replace("K", "E").replace("A", "F")
        
        card_ranks.append((group_hand(most_common), cards, bid))

    winnings = sum([(i+1)*bid for i, (_, _, bid) in enumerate(sorted(card_ranks))])
    print(f"Part 1: {winnings}")

    card_ranks = []
    for cards, bid in hands:
        card_counts = Counter(cards)
        num_jokers = card_counts["J"]
        card_counts["J"] = 0
        card_counts[card_counts.most_common(1)[0][0]] += num_jokers
        most_common = card_counts.most_common()
        cards = cards.replace("T", "B").replace("J", "0").replace("Q", "C").replace("K", "D").replace("A", "E")
        
        card_ranks.append((group_hand(most_common), cards, bid))

    winnings = sum([(i+1)*bid for i, (_, _, bid) in enumerate(sorted(card_ranks))])
    print(f"Part 2: {winnings}")