"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
 

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    val_card = 0
    card_letter = {'J','Q','K'}
    if card in card_letter:
        val_card = 10
        return val_card
    if card == 'A':
        val_card = 1
        return val_card
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    val_card_1 = 0
    val_card_2 = 0
    card_letter = {'J','Q','K'}
          
    if card_one in card_letter:
        val_card_1 = 10
    elif card_one == 'A':
        val_card_1 = 1
    else:
        val_card_1 = int(card_one)
        
    if card_two in card_letter:
        val_card_2 = 10
    elif card_two == 'A':
        val_card_2 = 1
    else:
        val_card_2 = int(card_two)

    if val_card_1 > val_card_2:
        return str(card_one)
    if val_card_1 < val_card_2:
        return str(card_two)
    if val_card_1 == val_card_2:
        return (card_one,card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    ace_val = 1
    val_card_1 = 0
    val_card_2 = 0
    card_letter = {'J','Q','K'}
    if card_one in card_letter:
        val_card_1 = 10
    elif card_one == 'A':
        val_card_1 = 11
    else:
        val_card_1 = int(card_one)
    
    if card_two in card_letter:
        val_card_2 = 10
    elif card_two == 'A':
        val_card_2 = 11
    else:
        val_card_2 = int(card_two)
        
    if (val_card_1 + val_card_2) <= 10 :
        ace_val = 11
    return ace_val


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    black_jack_value = False
    card_letter = {'J','Q','K'}
    if (card_one == 'A' and (card_two in card_letter or card_two == '10')) or ((card_one in (card_letter, '10')) and card_two == 'A'):
        black_jack_value = True
    return black_jack_value   

def can_split_pairs(card_one, card_two):
    split_value = False
    card_letter = {'J','Q','K'}
    if ((card_one == 'A' and card_two in card_letter ) or (card_one == card_letter  and card_two == 'A')
        or (card_one in card_letter and card_two in card_letter) or (card_one == card_two)):
        split_value = True
    return split_value

def can_double_down(card_one, card_two):
    double_val = False
    card_letter = {'J','Q','K'}
    number = {'8','9','10'}
    number_res = {'9','10','11'}
    if (card_one == 'A' and card_two == 'A'):
        double_val = False
    elif ((card_one == 'A' and card_two in card_letter ) or (card_one in  card_letter  and card_two == 'A')
        or (card_one == 'A' and (card_two in number)) or (card_one == number  and card_two == 'A')
        or (str(int(card_one) + int(card_two)) in number_res )):
        double_val = True
    else:
        double_val = False
    return double_val