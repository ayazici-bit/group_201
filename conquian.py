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

def computer_player():
	"""
	Represents the opponent the user is playing against. Like the user, it has its own (randomized) hand and will make decisions based on it. 
	Like the user, it aims to meld cards by choosing from its own hand, the stock, or the discarded cards. 
	The computer player will make this meld by taking out tuples (cards) from its own hand and stock/discard and adding them to the “cards” variable to be scored.

	Attributes:
		cpu_cards (list of tuples): A list of tuples where each represents a card the computer player has drawn.
	
	Side Effects:
		Adds tuples to the “cards” variable based on what would score the most points for that turn.
	"""

def validate_meld(cards):
    """
    Checks if the cards form a valid meld (a set or a sequence).
    
    A valid meld is either:
    - a set: 3 or 4 cards of the same number
    - a sequence: 3 or more cards in order of the same suit

    Args:
        cards (list of tuples): A list where each tuple represents a card in the form of rank and suit, 
        such as ('7', 'hearts'). The list must contain at least three cards.

    Returns:
        bool: True if the cards form a valid meld, False otherwise.

    Side effect:
        Raises ValueError if the input list contains fewer than three cards.---(a game shouldn’t show the exception because it will look like the game crashed, it should be invisible to the user. So if there is a error raised, the program should handle it, without the game crashing)
     ""” 

def check_win_condition(player_melds):
    """
    Checks whether a player has won the game by reaching exactly 11 cards in melds.

        Args:
        player_melds (list of lists of tuples): A list containing the player’s melds.
        Each meld is a list of card tuples, and each card is stored in the form
        (rank, suit), such as (7, "clubs").

    Returns:
        bool: True if the player has exactly 11 cards in melds, False otherwise.

    Side Effects:
        Raises ValueError if the meld list is empty or if one of the melds is not in
        the correct format.
    """

