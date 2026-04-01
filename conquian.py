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
