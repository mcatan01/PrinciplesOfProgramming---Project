import pickle 
import three_musketeers
 
filename = 'saved_board_file'



def save_board():
    """Give choice to user, after his turn, to save the current board"""

    choice = input("Do you want to save the current board (Y) or not (N) ?").upper().replace(' ', '')
    if choice == 'Y':
        outfile = open(filename, 'wb')
        pickle.dump(three_musketeers.get_board(), outfile)
        outfile.close()
        print('Game saved')
        print()



def create_retrieve_board():
    """ This function assigns global variable board (instead of create_board()).
    Try to open any saved board. If file does not exist, load a default board.
    If previous board saved, give choice to user to retrieve it.
    @return: list (board)
    """
    
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]
    try:
        infile = open(filename, 'rb')
    except:
        print()
        print('No saved game found')
        print()
        return board
    loaded_board = pickle.load(infile)
    infile.close()
    choice = input("Do you want to retrieve the previous game (Y) or not (N) ?").upper().replace(' ', '') 
    if choice == "Y":
        print('You play now on the previous board')
        board = loaded_board
        return board
    else:
        return board
