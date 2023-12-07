from collections import Counter

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def transform_card_values(hand, joker):
    transformations = {'T': chr(ord('9') + 1), 'J': chr(ord('2') - 1) if joker else chr(ord('9') + 2),
                       'Q': chr(ord('9') + 3), 'K': chr(ord('9') + 4), 'A': chr(ord('9') + 5)}

    for old_value, new_value in transformations.items():
        hand = hand.replace(old_value, new_value)

    return hand

def calculate_strength(hand, joker):
    hand = transform_card_values(hand, joker)
    card_counts = Counter(hand)

    if joker:
        target = max(card_counts, key=card_counts.get)
        for card, count in card_counts.items():
            if card != '1':
                if count > card_counts[target] or target == '1':
                    target = card

        assert target != '1' or list(card_counts.keys()) == ['1']
        if '1' in card_counts and target != '1':
            card_counts[target] += card_counts['1']
            del card_counts['1']
        assert '1' not in card_counts or list(card_counts.keys()) == ['1'], f'{card_counts} {hand}'

    sorted_counts = sorted(card_counts.values())

    if sorted_counts == [5]:
        return 10, hand
    elif sorted_counts == [1, 4]:
        return 9, hand
    elif sorted_counts == [2, 3]:
        return 8, hand
    elif sorted_counts == [1, 1, 3]:
        return 7, hand
    elif sorted_counts == [1, 2, 2]:
        return 6, hand
    elif sorted_counts == [1, 1, 1, 2]:
        return 5, hand
    elif sorted_counts == [1, 1, 1, 1, 1]:
        return 4, hand
    else:
        assert False, f'{card_counts} {hand} {sorted_counts}'

def main():
    input_file = "input.in.txt"
    lines = read_input(input_file)
    joker = True

    hands_and_bids = [(line.split()[0], int(line.split()[1])) for line in lines]
    sorted_hands = sorted(hands_and_bids, key=lambda hb: calculate_strength(hb[0], joker))

    total_winnings = 0
    for i, (hand, bid) in enumerate(sorted_hands):
        total_winnings += (i + 1) * bid

    print('Total winnings: ', total_winnings)

if __name__ == "__main__":
    main()
