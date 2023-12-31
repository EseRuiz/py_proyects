"""Functions for implementing the rules of the classic arcade game Pac-Man."""
 
 
def eat_ghost(power_pellet_active, touching_ghost):
    eat_var = False
    """
    Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    if (power_pellet_active is True and touching_ghost is True) :
        eat_var = True
    elif (power_pellet_active is False and touching_ghost is True):
        eat_var = False
    elif (power_pellet_active is True and touching_ghost is False):
        eat_var = False
    return eat_var


def score(touching_power_pellet, touching_dot):
    score_var = False
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if(touching_power_pellet is True and touching_dot is True):
        score_var = True
    elif (touching_power_pellet is False and touching_dot is True):
        score_var = True
    elif (touching_power_pellet is True and touching_dot is False):
        score_var = True
    return score_var


def lose(power_pellet_active, touching_ghost):
    lose_var = False
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if (power_pellet_active is False and touching_ghost is True):
        lose_var = True
    elif (power_pellet_active is True and touching_ghost is False):
        lose_var = False
    elif (power_pellet_active is True and touching_ghost is True):
        lose_var = False

    return lose_var


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    win_var = False
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    if(has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is False):
        win_var = True 
    elif(has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is False):
        win_var = True 
    elif(has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True):
        win_var = True
    elif(has_eaten_all_dots is True and power_pellet_active is False and touching_ghost is True):
        win_var = False

    return win_var