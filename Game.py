from Player import Player


class Card:
    def __init__(self, name, card_type):
        self.name = name
        self.card_type = card_type


class Game:
    def __init__(self):
        self.ordered_players = []
        self.cards = []
        self.load_cards()
        self.possible_cards = self.cards
        self.confirmed_weapon = None
        self.confirmed_character = None
        self.confirmed_room = None
        self.number_of_cards = len(self.cards)
        self.play_game()

    def play_game(self):
        card_amount = 0
        while self.get_input("Add Player? (y/n): ", ['y', 'n']).upper() == 'Y':
            player_name = input("Player Name: ")
            player_hand_size = int(input("Hand_Size: "))
            card_amount += player_hand_size

            self.ordered_players.append(Player(self, player_name, player_hand_size))

        if card_amount != len(self.cards) - 3:
            print("CARD NUMBER NOT VALID")
            return

        your_player = self.player_by_name(self.get_input("Which player are you?: ", [player.name for player in self.ordered_players]))

        print("What cards do you have?: ")
        while len(your_player.known_cards) < your_player.hand_size:

            card_name = self.get_input("Card Name: ", [card.name for card in self.cards]).upper()

            your_player.reveal_card(self.card_by_name(card_name))

        your_player.possible_cards = []

        player_iter = 0
        while not self.check_confirmed():
            if self.get_input(f"{self.ordered_players[player_iter].name} guessed? (y/n): ", ['y', 'n']).upper() == 'Y':

                character_guess = self.card_by_name(self.get_input(
                    "Character guessed: ", [card.name for card in self.cards if card.card_type == "CHARACTER"]).upper())

                weapon_guess = self.card_by_name(self.get_input(
                    "Weapon guessed: ", [card.name for card in self.cards if card.card_type == "WEAPON"]).upper())

                room_guess = self.card_by_name(self.get_input(
                    "Room guessed: ", [card.name for card in self.cards if card.card_type == "ROOM"]).upper())

                show_iter = (player_iter + 1) % len(self.ordered_players)

                while True:
                    if self.get_input(f"{self.ordered_players[show_iter].name} showed? (y/n): ", ['y', 'n']).upper() == 'N':
                        self.ordered_players[show_iter].eliminate_card(weapon_guess, character_guess, room_guess)
                        show_iter = (show_iter + 1) % len(self.ordered_players)
                        if show_iter == player_iter:
                            break

                    else:
                        self.ordered_players[show_iter].add_guess_set([weapon_guess, character_guess, room_guess])
                        break

            self.print_info()
            player_iter = (player_iter + 1) % len(self.ordered_players)

        self.provide_answer()
        self.provide_answer()
        self.provide_answer()

    @staticmethod
    def get_input(prompt, valid_answers=None):
        while True:
            answer = input(prompt)
            if valid_answers:
                if answer.upper() not in [answer.upper() for answer in valid_answers]:
                    print("INVALID ANSWER")
                    continue

            return answer

    def player_by_name(self, name):
        for player in self.ordered_players:
            if player.name == name:
                return player

    def card_by_name(self, name):
        for card in self.cards:
            if card.name == name:
                return card

    def add_player(self, *args):
        pass

    def eliminate_card(self, *args):
        for card in args:
            self.possible_cards.remove(card)

    def check_confirmed(self):
        weapons = [x for x in self.possible_cards if x.card_type == "WEAPON"]
        characters = [x for x in self.possible_cards if x.card_type == "CHARACTER"]
        rooms = [x for x in self.possible_cards if x.card_type == "ROOM"]

        if len(weapons) == 1:
            self.confirmed_weapon = weapons[0]

        if len(characters) == 1:
            self.confirmed_character = characters[0]

        if len(rooms) == 1:
            self.confirmed_room = rooms[0]

        if self.confirmed_weapon is not None and self.confirmed_character is not None and self.confirmed_room is not None:
            return True

        else:
            return False

    def provide_answer(self):
        print(
            f"Weapon: {self.confirmed_weapon.name}, Character: {self.confirmed_character.name}, Room: {self.confirmed_room.name}")

    def eliminate_from_others(self, player, card):
        for other in self.ordered_players:
            if other == player:
                continue
            other.eliminate_card(card)

    def load_cards(self):
        self.cards.append(Card("REVOLVER", "WEAPON"))
        self.cards.append(Card("KNIFE", "WEAPON"))
        self.cards.append(Card("LEAD PIPE", "WEAPON"))
        self.cards.append(Card("ROPE", "WEAPON"))
        self.cards.append(Card("CANDLESTICK", "WEAPON"))
        self.cards.append(Card("WRENCH", "WEAPON"))

        self.cards.append(Card("MRS PEACOCK", "CHARACTER"))
        self.cards.append(Card("MISS SCARLET", "CHARACTER"))
        self.cards.append(Card("COLONEL MUSTARD", "CHARACTER"))
        self.cards.append(Card("MR GREEN", "CHARACTER"))
        self.cards.append(Card("MRS WHITE", "CHARACTER"))
        self.cards.append(Card("PROFESSOR PLUM", "CHARACTER"))

        self.cards.append(Card("BILLIARD ROOM", "ROOM"))
        self.cards.append(Card("STUDY", "ROOM"))
        self.cards.append(Card("HALL", "ROOM"))
        self.cards.append(Card("LOUNGE", "ROOM"))
        self.cards.append(Card("DINING ROOM", "ROOM"))
        self.cards.append(Card("BALLROOM", "ROOM"))
        self.cards.append(Card("CONSERVATORY", "ROOM"))
        self.cards.append(Card("LIBRARY", "ROOM"))
        self.cards.append(Card("KITCHEN", "ROOM"))

    def new_guess(self):
        pass

    def print_info(self):
        print([x.name for x in self.possible_cards])
