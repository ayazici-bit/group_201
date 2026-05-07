""" A Python version of the card game 'Conquian' where the user plays against
a computer player.
"""
import random

class Player:
    """Creates a player that can access the game class to play.
    Attributes:
        name(str): Name of the player
        hand(list of tuples): Cards in player's hand
        melds(list of lists of tuples): The melds the player has completed
        count_melds(int): Number of melds player has acquired
    """
    def __init__(self, name, game):
        """_summary_

        Args:
            name(str): Name of the player
            game(Game object): Game surrently being played
        """
        self.name = name
        self.game = game
        self.hand = []
        self.melds = []
        self.count_melds = 0
        
    def deal_hand(self):
        """
        Deals cards from draw pile to player's hand
        """
        while len(self.hand) < 10:
            self.hand.append(self.game.draw_pile.pop())
            
    def draw_card(self, draw_pile, discard_pile):
        """
        Draw a card from the draw pile and add card to hand if applicable.

        Aleyna Yazici: 
            Technique: Composition of two custome classes
        Args:
            draw_pile (list of tuples): A list containing the draw pile’s number and
            suit, such as ('7', 'hearts').

        Returns:
            str: The card that was drawn.

        Raises:
            ValueError: If the draw pile is empty. 

        Side Effects:
            Appends the drawn card to the player’s hand/meld.
            Changes the draw pile state.
            Changes the player's hand state.
        """
        if len(draw_pile) == 0:
            raise ValueError("Draw pile is empty")
        
        drawn_card = draw_pile.pop()
        print(f'Drawn card: {drawn_card}')
        #hand will be the player's hand attribute which will be a list of tuples
        #checking a 4-card meld
        for i in range(len(self.hand)):
            for j in range(i + 1, len(self.hand)):
                for k in range(j + 1, len(self.hand)):
                    test_meld = [self.hand[i], self.hand[j], self.hand[k], drawn_card]
                    
                    if validate_meld(test_meld):
                        card1 = self.hand[i]
                        card2 = self.hand[j]
                        card3 = self.hand[k] 
                        
                        #remove meld from hand
                        self.hand.remove(card1)
                        self.hand.remove(card2)
                        self.hand.remove(card3)
                        
                        return f"New meld: {test_meld}" 
        #check 3-card meld
        for i in range(len(self.hand)):
            for j in range(i + 1, len(self.hand)):
                test_meld = [self.hand[i], self.hand[j], drawn_card]
                
                if validate_meld(test_meld):
                    card1 = self.hand[i]
                    card2 = self.hand[j]
                        
                    #remove meld from hand
                    self.hand.remove(card1)
                    self.hand.remove(card2)
                        
                    return f"New meld: {test_meld}"
        
        print(f"No melds possible, discarding: {drawn_card}")  
        #added to the discard pile (which will be list of tuples) instead
        self.game.discard_pile.append(drawn_card)           
        return None
    
    def show_hand(self):
        """
        Shows the player's completed melds.

        Returns:
            list of lists: All valid melds found, largest first.
                          Empty list if no melds are possible. 
        """
        possible_melds = find_possible_melds(self.hand)
        self.melds.append(possible_melds)
        return possible_melds
        
    def number_of_melds(self):
        """
        Shows the amount of the player's completed melds.
        
        Returns:
            int: The number of melds in player's hand
        """
        if len(self.hand) < 2:
            raise ValueError
        number = len(find_possible_melds(self.hand))
        self.count_melds + number
        return number
    
card_rankings = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, 
                 "J": 8, "Q": 9, "K": 10}
class cpu_player:    
    def __init__(self):
        """
        Runs to intialize the things needed for the CPU player. This includes their hand,
        the meld_list, and the amount of cards it has melded.

        Attributes:
            cpu_cards (list of tuples): The CPU's hand of unmelded cards. Each card is
            represented as ("rank", "suit").

            cpu_melds (list of lists of tuples): The melds the CPU has completed.

            cpu_melded_cards_count (int): The number of cards the CPU has melded. When
            the value reaches 11 the CPU has won and the game is over.
        """
        self.cpu_cards = []
        self.cpu_melds = []
        self.cpu_melded_cards_count = 0

    def cpu_turn(self, discard_card):
        """
        Executes the CPU's turn. It first tries to make a meld using the discard card. If
        no meld can be formed it will draw a card in an attempt to make melds with that card.
        If no melds can be formed it will discard a card.

        Args:
            discard_card (tuple): The top card on the discard pile.

        Side Effects:
            Can remove cards from cpu_cards and add them to cpu_melds.
            Can increase cpu_melded_cards_count.
            Can remove cards from draw_pile.
            Can remove cards from discard_pile.
            Can append cards to discard_pile.
            Can end program if CPU meets win condition.
        """
        discard_card = discard_pile[0]
        if self.cpu_try_discard(discard_card):
            return
        self.cpu_try_draw()

    def cpu_try_discard(self, discard_card):
        """
        Looks at the top card in the discard pile. If a meld can be made with it, the CPU
        will do so.

        Args:
            discard_card (tuple): The top card on the discard pile.

        Returns:
            A boolean value: True if a meld is made, False if it is not.
        
        Side Effects:
            Can remove cards from cpu_cards and add them to cpu_melds.
            Can increase cpu_melded_cards_count.
            Can remove cards from discard_pile.
            Can end program if CPU meets win condition.
        """
        if discard_pile == 0:
            return False
        cpu_hand_and_discard = self.cpu_cards + [discard_card]
        poss_cpu_melds = find_possible_melds(cpu_hand_and_discard)
        if poss_cpu_melds:
            discard_pile.pop()
            best_cpu_meld = poss_cpu_melds[0]
            for card in best_cpu_meld:
                if card in self.cpu_cards:
                    self.cpu_cards.remove(card)
            self.cpu_melds.append(best_cpu_meld)
            self.cpu_melded_cards_count += len(best_cpu_meld)
            print(f"The CPU has made a meld:{best_cpu_meld}. It used the discard pile" 
                  "to do so. The CPU has now melded {self.cpu_melded_cards_count} cards.")
            if self.cpu_melded_cards_count == 11:
                print("The CPU has melded 11 cards and has beaten you! "
                f"Better luck next time.")
                return "CPU WIN"
            return True
        else:
            return False
    
    def cpu_try_draw(self):
        """
        If the discard card does not work, this function will draw a card and attempt
        to make a meld with it. If the drawn card does not work the card is discarded.

        Returns:
            A boolean value: True if a meld is made, False if it is not.

        Side Effects:
            Can remove cards from cpu_cards and add them to cpu_melds.
            Can remove cards from draw_pile.
            Can increase cpu_melded_cards_count.
            Can append cards to discard_pile.
            Can end program if CPU meets win condition.
        """
        drawn_card = draw_card(draw_pile)
        if type(drawn_card) is not tuple:
            return False
        cpu_hand_and_drawn = self.cpu_cards + [drawn_card]
        poss_cpu_melds = find_possible_melds(cpu_hand_and_drawn)
        if poss_cpu_melds:
            best_cpu_meld = poss_cpu_melds[0]
            for card in best_cpu_meld:
                if card in self.cpu_cards:
                    self.cpu_cards.remove(card)
            self.cpu_melds.append(best_cpu_meld)
            self.cpu_melded_cards_count += len(best_cpu_meld)
            if self.cpu_melded_cards_count == 11:
                print("The CPU has melded 11 cards and has beaten you! "
                "Better luck next time.")
                return "CPU WIN"
        else:
            discard_pile.append(drawn_card)
        return True

def validate_meld(cards):
    """
    Checks if the cards form a valid meld (a set or a sequence).
    
    A valid meld is either:
    - a set: 3 or 4 cards of the same number
    - a sequence: 3 or more cards in order of the same suit

    Args:
        cards (list of tuples): A list where each tuple represents a card in 
        the form of rank and suit, 
        such as ('7', 'hearts'). The list must contain at least three cards.
    
    Paul Gomes:    
    Technique:
        comprehensions - ranks and suits are pulled from the card
        list using list comprehensions.

    Returns:
        bool: True if the cards form a valid meld, False otherwise.

    Side effect:
        Raises ValueError if the input list contains fewer than three cards.
     """ 
    try:
        if len(cards) < 3:
            raise ValueError("A meld must have at least 3 cards.")
    except ValueError:
        return False
    
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    
    same_rank = True
    for rank in ranks:
        if rank != ranks[0]:
            same_rank = False
            break

    if same_rank:
        return True

    same_suit = True
    for suit in suits:
        if suit != suits[0]:
            same_suit = False
            break

    if not same_suit:
        return False

    values = []
    for rank in ranks:
        values.append(card_rankings[rank])
    values.sort()

    for i in range(len(values) - 1):
        if values[i + 1] != values[i] + 1:
            return False

    return True 

def find_possible_melds(hand, max_meld_size=4):
    """
    Finds all valid melds a player could make from their current hand.

    Looks at every possible group of 3 cards and every possible group
    of 4 cards. Keeps the ones that are valid melds. Returns them sorted
    from largest to smallest.

    Paul Gomes:
    Techniques: 
        - comprehensions — valid combinations are found and filtered
          using list comprehensions.
        - optional parameters — max_meld_size has a default value of 4,
          so the caller can limit results to 3-card melds only if needed,
          but does not have to pass anything for normal use.

    Args:
        hand (list of tuples): The player's current unmelded cards.
        max_meld_size (int): The largest meld size to check for.
                             Default is 4. Pass 3 to only find 3-card melds.

    Returns:
        list of lists:All valid melds found, largest first.
                          Empty list if no melds are possible.
    """
    three_card_melds = [
        [hand[i], hand[j], hand[k]]
        for i in range(len(hand))
        for j in range(i + 1, len(hand))
        for k in range(j + 1, len(hand))
        if validate_meld([hand[i], hand[j], hand[k]])]

    four_card_melds = []
    if max_meld_size == 4:
        four_card_melds = [
            [hand[i], hand[j], hand[k], hand[l]]
            for i in range(len(hand))
            for j in range(i + 1, len(hand))
            for k in range(j + 1, len(hand))
            for l in range(k + 1, len(hand))
            if validate_meld([hand[i], hand[j], hand[k], hand[l]])]

    possible_melds = three_card_melds + four_card_melds

    possible_melds.sort(key=lambda meld: len(meld), reverse=True)

    return possible_melds

def check_win_condition(player_melds):
    """
    Checks whether a player has won the game by reaching exactly 11 cards in melds.

    Args:
        player_melds (list of lists of tuples): A list containing the players melds.
        Each meld is a list of card tuples, and each card is stored in the form
        (rank, suit), such as (7, "clubs").

    Returns:
        bool: True if the player has exactly 11 cards in melds, False otherwise.

    Side Effects:
        Raises ValueError if the meld list is empty or if one of the melds is not in
        the correct format.
    """

    if not isinstance(player_melds, list):
        raise TypeError("player_melds must be a list.")

    if len(player_melds) == 0:
        raise ValueError("player_melds cannot be empty.")

    total_cards = 0

    for meld in player_melds:
        if not isinstance(meld, list):
            raise ValueError("Each meld must be a list of card tuples.")

        for card in meld:
            if not isinstance(card, tuple):
                raise TypeError("Each card must be stored as a tuple.")

            rank, suit = card
            total_cards += 1

    return True if total_cards == 11 else False

def player_turn():
    """

    """
    if len(discard_pile) == 0:
        drawn_card = draw_card(draw_pile)
        if type(drawn_card) is not tuple:
                return
        hand.append(drawn_card)
    else:
        discard_card = discard_pile[0]    
        dis_or_draw = input(f"Would you like to use the discard card: {discard_card}" 
                            "(d) or draw a card (c)?").lower()
        if dis_or_draw == "c":
            drawn_card = draw_card(draw_pile)
            if type(drawn_card) is not tuple:
                return
            hand.append(drawn_card)
        elif dis_or_draw == "d":
            discard_pile.pop(0)
            hand.append(discard_card)
    i = 0
    while i < len(hand):
        print(f"{i}: {hand[i]}")
        i += 1
    choice = input("Choose what cards you would like to add to a meld,"
    " list the cards by index seperated by spaces(ex: 0 4 8).")
    indices = choice.split()
    indices = [int(i) for i in indices]
    chosen_cards = []
    for index in indices:
        chosen_cards.append(hand[index])
    if validate_meld(chosen_cards):
        print("Good meld!")
        for card in chosen_cards:
            hand.remove(card)
        player_melds.append(chosen_cards)
        if check_win_condition(player_melds):
            return "PLAYER WINS"
    else:
        print("Invalid meld")
    i = 0
    while i < len(hand):
        print(f"{i}: {hand[i]}")
        i += 1
        chosen_discard = int(input("What card would you like to discard? (Choose by index)"))
        hand.remove(hand[chosen_discard])
        discard_pile.append(hand[chosen_discard])

class Game:
    """
    Stores the game state.
    
    """
    def __init__(self):
        """
        Creates game object. 
        Attributes:
            player(Player object): The player playing
            cpu(cpu_player): The computer player playing
            player_turn(str): Tracking whose turn it is
            cards(list of tuples): The playing cards used in conquian
            draw_pile(list of tuples): Shuffled deck
            discard_pile(list of tuples): Discarded cards pile
        """
        self.player = Player()
        self.cpu = cpu_player()
        self.player_turn = "Human Player"
        
        self.cards = [('Ace', 'Diamonds'), ('2', 'Diamonds'), ('3', 'Diamonds'), 
             ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'),
             ('7', 'Diamonds'),('Jack', 'Diamonds'),('Queen', 'Diamonds'),
             ('King', 'Diamonds'), ('Ace', 'Clubs'), ('2', 'Clubs'),
             ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'),
             ('7', 'Clubs'), ('Jack', 'Clubs'),('Queen', 'Clubs'),
             ('King', 'Clubs'), ('Ace', 'Hearts'), ('2', 'Hearts'),
             ('3', 'Hearts'), ('4', 'Hearts'), ('5', 'Hearts'), ('6', 'Hearts'),
             ('7', 'Hearts'), ('Jack', 'Hearts'), ('Queen', 'Hearts'),
             ('King', 'Hearts'), ('Ace', 'Spades'), ('2', 'Spades'),
             ('3', 'Spades'), ('4', 'Spades'), ('5', 'Spades'), ('6', 'Spades'),
             ('7', 'Spades'), ('Jack', 'Spades'), ('Queen', 'Spades'),
             ('King', 'Spades')
             ]
        self.draw_pile = self.cards.copy()
        random.shuffle(self.draw_pile)
        self.discard_pile = []
    
    def play_game(self):
        if self.turn == "Human Player":
            

if __name__ == "__main__":
    game = Game()
    game.play_game()
