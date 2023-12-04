if __name__ == "__main__":
    with open("day4.txt", "r") as f:
        scratch_cards = []
        for card in f.readlines():
            winning, play = card.split("|")
            scratch_cards.append([set(winning.split()[2:]), set(play.split())])

    total = 0
    for winning, play in scratch_cards:
        num_matches = len(winning.intersection(play))
        if num_matches > 0:
            total += 2**(num_matches - 1)

    print(f"Part 1: {total}")

    card_wins = {}
    card_counts = {i: 1 for i in range(len(scratch_cards))}
    for card_num, (winning, play) in enumerate(scratch_cards):
        if card_num not in card_wins:
            num_matches = len(winning.intersection(play))
            card_wins[card_num] = num_matches
    
        for i in range(card_wins[card_num]):
            card_counts[card_num + i + 1] += card_counts[card_num]

    print(f"Part 2: {sum(card_counts.values())}")