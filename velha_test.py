from velha import jogo


def test_1():
    assert jogo([[2,2,2],[2,1,1],[0,1,1]]) == 1 # HORIZONTAL

def test_2():
    assert jogo([[2,1,1],[0,2,1],[1,0,2]]) == 1 # DIAGONAL
    
def test_3():
    assert jogo([[1,2,2],[0,1,2],[0,0,2]]) == 1 # VERTICAL
'''    
def test_3():
    assert jogo([[2,1,2],[2,1,2],[1,2,1]]) == 0
    
def test_4():
    assert jogo([[2,0,0],[0,0,0],[0,0,0]]) == -1
    
def test_5():
    assert jogo([[],[],[]])
'''