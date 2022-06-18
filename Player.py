

class Player:
    def __init__(self, game, name, hand_size):
        self.game = game
        self.name = name
        self.possible_cards = game.possible_cards
        self.guess_sets = []
        self.known_cards = []
        self.hand_size = hand_size

    def eliminate_card(self, *args):
        for card in args:
            if card in self.possible_cards:
                self.possible_cards.remove(card)

            for guess_set in self.guess_sets:
                if card in guess_set:
                    guess_set.remove(card)
                    if len(guess_set) == 1:
                        self.reveal_card(guess_set[0])
                        self.guess_sets.remove(guess_set)

        if self.hand_size - len(self.known_cards) == len(self.possible_cards):
            for card in self.possible_cards:
                self.reveal_card(card)

    def reveal_card(self, *args):
        self.game.eliminate_card(*args)
        for card in args:
            self.known_cards.append(card)
            self.remove_by_name(card)
            self.game.eliminate_from_others(self, card)

            for guess in self.guess_sets:
                if card in guess:
                    self.guess_sets.remove(guess)

    def remove_by_name(self, card_name):
        for card in self.possible_cards:
            if card.name == card_name:
                self.possible_cards.remove(card)

    def add_guess_set(self, cards):
        for card in cards:
            if card in self.known_cards:
                return

        guess = []
        for card in cards:
            if card in self.possible_cards:
                guess.append(card)

        if len(guess) > 1:
            self.guess_sets.append(guess)

        elif len(guess) == 1:
            self.reveal_card(guess[0])
