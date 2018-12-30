import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ ['-','-', '-', 'M', '-'],
            ['-', '-', 'R', 'M', '-'],
            ['-', 'R', 'M', 'R', '-'],
            ['-', 'R', '-', '-', '-'],
            ['-', '-', '-', 'R', '-'] ]

board2 = [ ['-', 'R', 'M', 'R', '-'],
	   ['-', '-', '-', 'R', '-'],
	   ['M', '-', '-', '-', '-'],
	   ['-', 'R', 'R', '-', '-'],
	   ['-', '-', '-', 'R', 'M'] ]

board3 = [ ['-', '-', '-', 'M', '-'],
	   ['R', '-', '-', 'M', 'R'],
	   ['R', '-', '-', '-', '-'],
	   ['-', '-', '-', '-', '-'],
	   ['R', '-', '-', 'M', '-'] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((2,2)) == M
    assert at((4,0)) == M
    assert at ((4,4)) == R

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    set_board(board2)
    assert at((1,1)) == _
    assert at((2,0)) == M
    assert at((4,3)) == R
    set_board(board3)
    assert at((0,1)) == _
    assert at((2,0)) == R
    assert at((1,3)) == M

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()
    set_board(board3)
    assert board3 == get_board()

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
    assert all_locations()[17] == (3,2)
    assert all_locations()[24] == (4,4)
    

def test_adjacent_location():
    assert adjacent_location((0,0), 'right') == (0,1)
    assert adjacent_location((2,2), 'left') == (2,1)
    assert adjacent_location((4,4), 'left') == (4,3)
    assert adjacent_location((0,2), 'down') == (1,2)
    assert adjacent_location((4,2), 'up') == (3,2)
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((3,1), 'up')
    assert is_legal_move_by_musketeer((2,2), 'right') is True
    assert is_legal_move_by_musketeer((1,3), 'right') is not True
    set_board(board2)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((2,1), 'right')
    assert is_legal_move_by_musketeer((0,2), 'right') is True
    assert is_legal_move_by_musketeer((4,4), 'up') is not True
    set_board(board3)
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((2,2), 'up')
    assert is_legal_move_by_musketeer((1,3), 'right') is True
    assert is_legal_move_by_musketeer((4,3), 'right') is not True
    
def test_is_legal_move_by_enemy():
    set_board(board1)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((3,2), 'down')
    assert is_legal_move_by_enemy((2,1), 'up') is True
    assert is_legal_move_by_enemy((2,3), 'left') is not True
    set_board(board2)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,2), 'down')
    assert is_legal_move_by_enemy((1,3), 'down') is True
    assert is_legal_move_by_enemy((4,3), 'right') is not True
    set_board(board3)
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,3), 'right')
    assert is_legal_move_by_enemy((2,0), 'right') is True
    assert is_legal_move_by_enemy((4,0), 'left') is not True

def test_is_legal_move():
    set_board(board1)	
    assert is_legal_move((0,3), 'right') is not True
    assert is_legal_move((4,3), 'left') is True
    set_board(board2)
    assert is_legal_move((0,2), 'right') is True
    assert is_legal_move((4,4), 'up') is not True
    set_board(board3)
    assert is_legal_move((4,0), 'right') is True
    assert is_legal_move((0,3), 'up') is not True
    

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((1,3)) is True
    assert can_move_piece_at((0,3)) is not True
    set_board(board2)
    assert can_move_piece_at((0,2)) is True
    assert can_move_piece_at((2,0)) is not True
    set_board(board3)
    assert can_move_piece_at((4,0)) is True
    assert can_move_piece_at((0,3)) is not True
    
    
def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True
    set_board(board3)
    assert has_some_legal_move_somewhere('M') is True
    assert has_some_legal_move_somewhere('R') is True

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((0,3)) == []
    assert possible_moves_from((2,2)) == sorted(['left', 'up', 'right'])
    set_board(board2)
    assert possible_moves_from((2,0)) == []
    assert possible_moves_from((3,2)) == sorted(['up','right','down'])
    set_board(board3)
    assert possible_moves_from((4,3)) == []
    assert possible_moves_from((4,0)) == sorted(['up','right'])
    

def test_is_legal_location():
    assert is_legal_location((1,3)) is True
    assert is_legal_location((0,0)) is True
    assert is_legal_location((4,2)) is True
    assert is_legal_location((5,1)) is not True
    assert is_legal_location((-2,4)) is not True
    assert is_legal_location((1,7)) is not True
    
def test_is_within_board():
    assert is_within_board((0,0), 'up') is not True
    assert is_within_board((4,4), 'right') is not True
    assert is_within_board((4,2),'down') is not True
    assert is_within_board((2,3), 'right') is True
    assert is_within_board((1,2), 'down') is True
    assert is_within_board((3,4), 'left') is True

def test_all_possible_moves_for():
    set_board(board2)
    assert all_possible_moves_for('M') == sorted([((0, 2), 'right'), ((0, 2), 'left'), ((4, 4), 'left')])
    set_board(board1)
    assert all_possible_moves_for('R') == sorted([((1, 2), 'up'), ((1, 2), 'left'), ((2, 1), 'up'),((2, 1), 'left'), ((2, 3), 'right'), ((2,3), 'down'),((3, 1), 'right'), ((3, 1), 'down'), ((3, 1), 'left'),((4, 3), 'up'), ((4, 3), 'right'), ((4, 3), 'left')])
    set_board(board3)
    assert all_possible_moves_for('M') == sorted([((1,3), 'right')])
    
def test_make_move():
    set_board(board1)
    make_move((1, 2), 'up')
    assert board1[0][2] == 'R'
    assert board1[1][2] == '-'
    set_board(board2)
    make_move((0, 2),'right')
    assert board2[0][3] == 'M'
    assert board2[0][2] == '-'
    set_board(board3)
    make_move((4,0), 'up')
    assert board3[3][0] == 'R'
    assert board3[4][0] == '-'
    
    
def test_choose_computer_move():
    set_board(board1)
    assert choose_computer_move('M') in all_possible_moves_for('M')
    set_board(board3)
    assert choose_computer_move('R') in all_possible_moves_for('R')
 

def test_is_enemy_win():
    set_board(board2)
    assert is_enemy_win() is not True
    set_board(board3)
    assert is_enemy_win() is True
    set_board(board1)
    assert is_enemy_win() is not True
    


