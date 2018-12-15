import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 = [ [_, R, M, R, _],
	   [_, _, _, R, _],
	   [M, _, _, _, _],
	   [_, R, R, _, _],
	   [_, _, _, R, M] ]

board3 = [ [_, _, _, M, _],
	   [R, R, _, M, _],
	   [R, _, _, _, _],
	   [_, _, _, _, _],
	   [R, _, _, M, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at((1,1)) == _
    assert at((2,0)) == M
    assert at((4,3)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('A8')
    assert string_to_location('C2') == (2,1)
    assert string_to_location('A1') == (0,0)
    assert string_to_location('E5') == (4,4)

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((10,0))
    with pytest.raises(ValueError):
	location_to_string((2,6))
    assert location_to_string((0,2)) == 'A3'
    assert location_to_string((1,1)) == 'B2'
    assert location_to_string((4,3)) == 'E4'

def test_at():
    set_board(board1)
    assert at((2,3)) == 'R'
    assert at((0,3)) == 'M'
    

def test_all_locations():
    assert len(all_locations()) == 25
    assert all_locations()[1] == (0,1)
    assert all_locations()[12] == (2,2)
    assert all_locations()[20] == (4,4)
    

def test_adjacent_location():
    assert adjacent_location((0,0), 'right') == (0,1)
    assert adjacent_location((2,2), 'left') == (2,1)
    assert adjacent_location((4,4), 'left') == (4,3)
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        at((2,2)) == 'M'
    with pytest.raises(ValueError):
        at((1,3)) == 'M'
    assert is_legal_move_by_musketeer((2,2), 'right') is True
    assert is_legal_move_by_musketeer((1,3), 'right') is not True
    
    
def test_is_legal_move_by_enemy():
    set_board(board2)
    with pytest.raises(ValueError):
        at((1,3)) == 'R'
    with pytest.raises(ValueError):
	at((4,3)) == 'R'
    assert is_legal_move_by_enemy((1,3), 'down') is True
    assert is_legal_move_by_enemy((4,3), 'right') is not True

def test_is_legal_move():
    set_board(board1)	
    assert is_legal_move((4,3), 'down') is not True
    assert is_legal_move((4,3), 'left') is True
    

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((1,3)) is True
    assert can_move_piece_at((0,3)) is not True
    

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True
    set_board(board3)
    asserthas_some_legal_move_somewhere('M') is not True

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((0,3)) == []
    assert possible_moves_from((2,2)) == ['up', 'right', 'left']
    assert possible_moves_from((4,1)) == []
    

def test_is_legal_location():
    assert is_legal_location((1,3)) is True
    assert is_legal_location((5,1)) is not True
    

def test_is_within_board():
    assert is_within_board((0,0), 'up') is not True
    assert is_within_board((2,3), 'right') is True
    

def test_all_possible_moves_for():
    set_board(board2)
    assert all_possible_moves_for('M') == [((0, 1), 'right'), ((0, 1), 'left'), ((4, 4), 'left')]
    set_board(board1)
    assert all_possible_moves_for('R') == [((1, 2), 'up'), ((1, 2), 'left'), ((2, 1), 'up'), 
					  ((2, 1), 'left'), ((2, 3), 'right'), ((2,3), 'down'),
					  ((3, 1), 'right'), ((3, 1), 'down', ((3, 1), 'left'),
					  ((4, 3), 'up'), ((4, 3), 'right'), ((4, 3), 'left')]
    
    
def test_make_move():
    set_board(board1)
    make_move((1, 2), 'up')
    assert board[0][2]) == 'R'
    make_move((2, 2),'right')
    assert board[2][3] == 'M'
    
    
def test_choose_computer_move():
    set_board(board1)
    assert choose_computer_move('M') in all_possible_moves_for('M')
    set_board(board3)
    assert choose_computer_move('R') in all_possible_moves_for('R')
 

def test_is_enemy_win():
    set_board(board3)
    assert is_enemy_win() is True
    set_board(board1)
    assert is_enemy_win() is not True
    


