"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    current_lista = [0 if num <= 0 else num for num in range (number,number+3)]
    return current_lista


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    concate_list = [val for val in rounds_1+rounds_2]
    return concate_list


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds



def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    average = sum(hand)/len(hand)
    aprox_aver = (hand[0]+hand[len(hand)-1])/2
    return average == aprox_aver or average == hand[int((len(hand)-1)/2)]


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    aver_par = [num for num in hand if num % 2 == 0]
    aver_impar = [num for num in hand if num % 2 != 0]
    if len(aver_par) == 0 or len(aver_impar) == 0:
        return True
    return (sum(aver_par)/len(aver_par))==(sum(aver_impar)/len(aver_impar))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        new_val = hand[0:(len(hand)-1)]
        new_val.append(22)
        return new_val
    return hand

a = get_rounds(25)
b = concatenate_rounds([27, 28, 29], [35, 36])
c =list_contains_round([27, 28, 29, 35, 36], 29)
d = card_average([5, 6, 7])
e = approx_average_is_average([1, 2, 4, 5, 8])
f = average_even_is_average_odd([1, 3, 5, 7, 9])
g = maybe_double_last([1, 2, 11])
print(g)