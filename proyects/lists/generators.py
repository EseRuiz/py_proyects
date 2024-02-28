"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ['A','B','C','D']
    nume = 0
    for num in range(number):
        if nume >= len(letters):
            nume = 0
        yield letters[nume]
        nume += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = ['A','B','C','D']
    numbers = [num for num in range(1,number+1)]
    nume = 0
    aux = 1
    for num in numbers:
        if nume >= len(letters):
            nume = 0
            aux += 1
            if aux == 13:
                aux = 14
        yield str(aux) + letters[nume]
        nume += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    numbers = len(passengers)
    list_seats = (generate_seats(numbers))
    assign = {}
    for user in passengers:
        assign[user]=next(list_seats)
    return assign

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    
    for seat in range(len(seat_numbers)):
        zeros = 12 -(len(seat_numbers[seat])+len(flight_id))
        yield seat_numbers[seat] + flight_id + str(0)*zeros
     

a = generate_seat_letters(5)
for combo in generate_seat_letters(8):
    print(combo)

b = generate_codes(["12A", "38B", "69C", "102B"],"KL1022")
print(next(b))
print(next(b))
print(next(b))
print(next(b))