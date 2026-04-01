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
