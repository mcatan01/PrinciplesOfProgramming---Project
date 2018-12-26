# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    global valid_row 
    global valid_col
    global directions
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    valid_row = ["A", "B", "C", "D", "E"]
    valid_col = range(1,6)
    directions = ["down", "left", "up", "right"] 
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    row = s[0].upper()
    col = int(s[1])
    if row not in valid_row or col not in valid_col:
        raise ValueError("Input out of the correct range")
    (a, b) = (valid_row.index(row), valid_col.index(col))
    return (a,b)

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range.
    @param location: 2-tuple location
    @return: string location
    """
    
    if location[0] not in range(0,5) or location[1] not in range(0,5):
        raise ValueError("Location out of range.")
    else:
        return valid_row[location[0]] + str(valid_col[location[1]])

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board.
    @return list
    """
    result = []
    for x in range(0,5):
        for y in range(0,5):
            result.append((x,y))
    return result

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
    @param location: 2-tuple of integers
    @param direction: string
    @return: 2-tuple of integers
    """
    (row, column) = location
    direction = direction.lower()
    if direction == "right":
        return (row, column+1)
    elif direction == "down":
        return (row+1, column)
    elif direction == "left":
        return (row, column-1)
    elif direction == "up":
        return (row-1, column)

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'
    @param location: 2-tuple of integers
    @param direction: string
    @return boolean
    """
    if at(location) != "M":
        raise ValueError("Not 'M' at location")
    if is_within_board(location, direction) is not True:
        raise ValueError("Move is outside board")    
    move_location = adjacent_location(location, direction)
    if at(move_location) == "R":
        return True
    else:
        return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'.
    @param location: 2-tuple integers
    @param direction: string
    @return boolean
    """
    if at(location) != "R":
        raise ValueError("Not 'R' at location")
    if is_within_board(location, direction) is not True:
        raise ValueError("Move is outside board")
    move_location = adjacent_location(location, direction)
    if at(move_location) is "-":
        return True
    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    @param location: 2-tuple integers
    @param direction: string
    @return boolean
    """
    if is_within_board(location, direction) is not True:
        raise ValueError("Move is outside board")
    player = at(location)
    if player == "M":
        return is_legal_move_by_musketeer(location, direction)
    elif player == "R":
        return is_legal_move_by_enemy(location, direction)
    else:
        raise ValueError('No player at location') 

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    ValueError raised if no player at location
    @param location: 2-tuple integers
    @return boolean
    """
    result = False
    if at(location) == "M":
        for _ in directions:
            try:
                if is_legal_move_by_musketeer(location, _) is True:
                    result = True
            except:
                continue
    elif at(location) == "R":
        for _ in directions:
            try:
                if is_legal_move_by_enemy(location, _) is True:
                    result = True
            except:
                continue
    else:
        raise ValueError("No player at location")
    return result


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    @param who: string
    @return boolean
    """
    result = False
    if who is not "M" and who is not "R":
        raise ValueError("input must be either 'M' or 'R'")
    for _ in all_locations():
        if at(_) is who:
            if can_move_piece_at(_) is True:
                result = True
                break
    return result

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
    for the player at location to move. If there is no player at
    location, returns the empty list, [].
    @param location: 2-tuple integers
    @return list
    """
    result = []
    for _ in directions:
        try:
            if is_legal_move(location, _) is True:
                result.append(_)
        except:
            continue
    return result

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will be a pair of integer numbers.
    @param location: 2-tuple integers
    @return boolean
    """
    (row, col) = location
    result = False
    if (row >= 0 and row <= 4) and (col >= 0 and col <= 4):
        result = True
    return result 
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range.
    @param location: 2-tuple integers
    @param direction: string
    @return boolean
    """
    move_location = adjacent_location(location, direction)
    return is_legal_location(move_location)
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
    (location, direction) tuples.
    You can assume that input will always be in correct range.
    @param player: string
    @return list
    """
    result = []
    for loc in all_locations():
        for dir in directions:
            try:
                if at(loc) is player and is_legal_move(loc, dir) is True:
                    result.append((loc, dir))
            except:
                continue
    return result

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range.
    @param location: 2-tuple integers
    @param direction: string
    """
    new_location = adjacent_location(location, direction)
    player = at(location)
    board[new_location[0]][new_location[1]] = player

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
    enemy (who = 'R') and returns it as the tuple (location, direction),
    where a location is a (row, column) tuple as usual.
    You can assume that input will always be in correct range.
    @param who: string
    @return 2-tuple integers
    """
    import random
    all_moves = all_possible_moves_for(who)
    choice = random.randint(0, len(all_moves))
    return all_moves[random.choice(range(0,len(all_moves)))]

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column.
    @return boolean
    """
    result = False
    location_M = []
    for _ in all_locations():
        if at(_) is "M":
            location_M.append(_)
    if (location_M[0][0] == location_M[1][0] == location_M[2][0] or
        location_M[0][1] == location_M[1][1] == location_M[2][1]):
	    result = True
    return result
    	

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
