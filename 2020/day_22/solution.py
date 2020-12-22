from collections import deque


def read_data(path="input.data"):
    is_player1 = True
    player1, player2 = [], []
    with open(path) as fobj:
        for line in map(str.rstrip, fobj):
            if ":" in line:
                continue
            if not line:
                is_player1 = False
                continue

            if is_player1:
                player1.append(int(line))
            else:
                player2.append(int(line))
    return player1, player2


def play(player1, player2):
    player1, player2 = map(deque, (player1, player2))
    while True:
        card1 = player1.popleft()
        card2 = player2.popleft()

        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])

        if not player1:
            return player2

        if not player2:
            return player1


def play_recursive(player1, player2, previous_decks=None):
    if previous_decks is None:
        previous_decks = (set(), set())

    player1, player2 = map(deque, [player1, player2])

    while True:
        # if there was a previous round in this game
        # that had exactly the same cards in the same order in the same players' decks,
        # the game instantly ends in a win for player 1.
        # Previous rounds from other games are not considered.
        previous_deck1 = tuple(player1)
        previous_deck2 = tuple(player2)

        if previous_deck1 in previous_decks[0] and previous_deck2 in previous_decks[1]:
            return 1, player1

        previous_decks[0].add(previous_deck1)
        previous_decks[1].add(previous_deck2)

        card1 = player1.popleft()
        card2 = player2.popleft()

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew,
        # the winner of the round is determined by playing a new game of Recursive Combat
        if len(player1) >= card1 and len(player2) >= card2:
            # To play a sub-game of Recursive Combat,
            # each player creates a new deck by making a *copy* of the next cards in their deck
            # (the quantity of cards copied is equal to *the number on the card they drew*
            # to trigger the sub-game).
            winner, _ = play_recursive(tuple(player1)[:card1], tuple(player2)[:card2])
            if winner == 1:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        else:
            if card1 > card2:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])

        if not player1:
            return 2, player2

        if not player2:
            return 1, player1


def score(deck):
    return sum(e * i for i, e in enumerate(reversed(deck), 1))


def solution_01(path="input.data"):
    player1, player2 = deque(read_data(path))
    result = play(player1, player2)
    return score(result)


def solution_02(path="input.data"):
    player1, player2 = read_data(path)
    _, result = play_recursive(player1, player2)
    return score(result)


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
