""" A Python version of the card game 'Conquian' where the user plays against
a computer player.
"""
def draw_card(draw_pile):
    """ Draw a card from the draw pile and add card to hand if applicable.

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
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                test_meld = [hand[i], hand[j], hand[k], drawn_card]
                
                if validate_meld(test_meld):
                    card1 = hand[i]
                    card2 = hand[j]
                    card3 = hand[k] 
                    
                    #remove meld from hand
                    hand.remove(card1)
                    hand.remove(card2)
                    hand.remove(card3)
                    
                    return f"New meld: {test_meld}" 
    #check 3-card meld
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            test_meld = [hand[i], hand[j], drawn_card]
            
            if validate_meld(test_meld):
                card1 = hand[i]
                card2 = hand[j]
                    
                #remove meld from hand
                hand.remove(card1)
                hand.remove(card2)
                    
                return f"New meld: {test_meld}"
    
    print(f"No melds possible, discarding: {drawn_card}")  
    #added to the discard pile (which will be list of tuples) instead
    discard_pile.append(drawn_card)           
    return None
	
hand = []
discard_pile = []    
card_rankings = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, 
                 "J": 8, "Q": 9, "K": 10}
class cpu_player:    
    def __init__(self):
        self.cpu_cards = []
        self.cpu_melds = []
        self.melded_cards_count = 0

    def cpu_turn(self, discard_card):
        """
        Enables the computer opponent to take a turn. Decisions are made based on
        the hand the computer has and the top card in the discard pile.
        
        Args:
            cpu_cards (list of tuples): A list where each tuple represents an
            unmelded card in the hand of the cpu. Formatted as ("value", suit").
            
            discard_card (tuple): Represents the top card on the discard pile.
        """
        # Checking for runs using the discarded card
        
        sorted_cpu_cards = sorted(self.cpu_cards, key = 
                                    lambda x:(x[1], card_rankings[x[0]]))

        suit_match = []
        suit_match.append(discard_card)
        for card in sorted_cpu_cards:
            if discard_card[1] == card[1]:
                suit_match.append(card)
        sequence = []
        sorted_suit_match_dis = sorted(suit_match, key = lambda x: card_rankings[x[0]])
        if len(sorted_suit_match_dis) >= 3:
            for i in range(1, len(sorted_suit_match_dis)):
                c1 = card_rankings[sorted_suit_match_dis[i][0]]
                c2 = card_rankings[sorted_suit_match_dis[i-1][0]]
                if c1 == c2 + 1:
                    sequence.append(sorted_suit_match_dis[i])
                    if len(sequence) >= 3:
                        for card in sequence:
                            self.cpu_cards.remove(card)
                        self.cpu_melds.append(sequence)
                        self.melded_cards_count += len(sequence)
                        # Also need to go back one in the discard pile here, not
                        # going to write this code now as it will depend on other
                        # functions to understand how the discard pile will be
                        # implemented.
                elif len(sequence) < 3:
                    same_rank_cards = []
                    same_rank_cards.append(discard_card)
                    for card in self.cpu_cards:
                        if card[0] == discard_card[0]:
                            same_rank_cards.append(card)
                    if len(same_rank_cards) >= 3:
                        for card in same_rank_cards:
                            self.cpu_cards.remove(card)
                            self.cpu_melds.append(same_rank_cards)
                            self.melded_cards_count += len(same_rank_cards)
        else:
            # Need to implement the drawing of a random card from stock deck
            # Again will do when how this will be implemented is known
            # Most likely will be calling another function here
            suit_match = []
            suit_match.append(drawn_card)
            for card in self.cpu_cards:
                if drawn_card[1] == card[1]:
                    suit_match.append(card)
                    sequence = []
        sorted_suit_match_draw = sorted(suit_match, key = 
                                        lambda x: card_rankings[x[0]])
        if len(sorted_suit_match_draw) >= 3:
            for i in range(1, len(sorted_suit_match_draw)):
                c1 = card_rankings[sorted_suit_match_draw[i][0]]
                c2 = card_rankings[sorted_suit_match_draw[i-1][0]]
                if c1 == c2 + 1:
                    sequence.append(sorted_suit_match_draw[i])
                    if len(sequence) >= 3:
                        for card in sequence:
                            self.cpu_cards.remove(card)
                        self.cpu_melds.append(sequence)
                        self.melded_cards_count += len(sequence)
                elif len(sequence) < 3:
                    same_rank_cards = []
                    same_rank_cards.append(drawn_card)
                    for card in self.cpu_cards:
                        if card[0] == drawn_card[0]:
                            same_rank_cards.append(card)
                    if len(same_rank_cards) >= 3:
                        for card in same_rank_cards:
                            self.cpu_cards.remove(card)
                            self.cpu_melds.append(same_rank_cards)
                            self.melded_cards_count += len(same_rank_cards)
                    # Meld logic within this function is a place holder and will ultimately be deferred to the validate_meld function.
                    # Likely by calling it within the cpu_turn function

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
	            total_cards += 1
	
	    if total_cards == 11:
	        return True
	    else:
	        return False
