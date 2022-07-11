from velha import jogo


def test_1():
    assert jogo([[2,2,2],[2,1,1],[0,1,1]]) == 1 # HORIZONTAL x GANHA 

def test_2():
    assert jogo([[2,1,1],[0,2,1],[1,0,2]]) == 1 # DIAGONAL X GANHA
    
def test_3():
    assert jogo([[1,2,2],[0,1,2],[1,0,2]]) == 1 # VERTICAL X GANHA
    
def test_4():
    assert jogo([[2,0,1],[0,2,1],[2,0,1]]) == 2 # VERTICAL O GANHA
    
def test_5():
    assert jogo([[2,1,2],[2,2,0],[1,1,1]]) == 2 # HORIZONTAL O GANHA
    
def test_6():
    assert jogo([[1,0,2],[2,1,0],[2,0,1]]) == 2 # DIAGONAL O GANHA
    
def test_7():
    assert jogo([[2,1,2],[2,1,2],[1,2,1]]) == 0 # EMPATE
    
def test_8():
    assert jogo([[2,0,0],[0,0,0],[0,0,0]]) == -1 # INDEFINIDO
    
def test_8():
    assert jogo([[2,2,2],[2,2,2],[2,2,2]]) # IMPOSSÍVEL
