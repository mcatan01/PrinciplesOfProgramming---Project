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
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A0') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((10,0))
    assert location_to_string((0,0)) == ('A0')

def test_at():
    assert type(at(board[location[0]][location[1]]) is str
    

def test_all_locations():
    assert len(all_locations()) == 25
    

def test_adjacent_location():
    assert adjacent_location((0,0), 'right') == (0,1)
    
    
def test_is_legal_move_by_musketeer():
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0)) == 'M'
    
    
def test_is_legal_move_by_enemy():
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,0)) == 'R'
    

def test_is_legal_move():
        assert is_legal_move((0,0), 'right') == bool
    

def test_can_move_piece_at():
        assert can_move_piece_at((0,1)) == bool
    

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert type(possible_moves_from((0,0))) is list
    

def test_is_legal_location():
    assert (is_legal_location > (4,4)) is False
    

def test_is_within_board():
    assert is_within_board((0,0), 'left') is False
    

def test_all_possible_moves_for():
    assert type(all_possible_moves_for('M')) is list
    
    
def test_make_move():
    assert make_move((0,0), 'right') == (0, 1)
    
    
def test_choose_computer_move():
    assert type(choose_computer_move('M')) is tuple
    assert type(choose_computer_move('R')) is tuple
    ; should work for both 'M' and 'R'

def test_is_enemy_win():
    assert type(is_enemy_win()) is tuple
    


