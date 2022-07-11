def jogo(matriz):
    
    # CONTAGEM --------------------------------------------------
    
    cont_X = 0
    cont_O = 0
    
    for i in matriz: # CONTA OS SIMBOLOS
        for j in i:
            if j == 2:
                cont_X += 1
            if j == 1:
                cont_O += 1
    
    # CRITERIOS PARA SER IMPOSSIVEL -------------------------------------
    
    if abs(cont_O - cont_X) > 1:
        return -2
    
    # CRITERIOS PARA ESTAR INDEFINIDO ----------------------------------
    
    if cont_X + cont_O < 5:
        return -1
    
    # CRITERIO PARA ESTAR EMPATADO ---------------------------------------
    
    if cont_X == 5 and cont_O == 4:
        return 0
    
    # CRITERIOS PARA X VENCER ---------------------------------------------
    
    if matriz[0][0] == 2 and matriz[0][1] == 2 and matriz[0][2] == 2: # HORIZONTAL
        return 1
    
    elif matriz[1][0] == 2 and matriz[1][1] == 2 and matriz[1][2] == 2: # HORIZONTAL
        return 1
    
    elif matriz[2][0] == 2 and matriz[2][1] == 2 and matriz[2][2] == 2: # HORIZONTAL
        return 1
    
    elif matriz[0][0] == 2 and matriz[1][0] == 2 and matriz[2][0] == 2: # VERTICAL
        return 1
    
    elif matriz[0][1] == 2 and matriz[1][1] == 2 and matriz[2][1] == 2: # VERTICAL
        return 1
    
    elif matriz[0][2] == 2 and matriz[1][2] == 2 and matriz[2][2] == 2: # VERTICAL
        return 1
    
    elif matriz[0][0] == 2 and matriz[1][1] == 2 and matriz[2][2] == 2: # DIAGONAL
        return 1
    
    elif matriz[0][2] == 2 and matriz[1][1] == 2 and matriz[2][0] == 2: # DIAGONAL
        return 1
    
    # CRITERIOS PARA O VENCER ---------------------------------------------
    
    if matriz[0][0] == 1 and matriz[0][1] == 1 and matriz[0][2] == 1: # HORIZONTAL
        return 2
    
    elif matriz[1][0] == 1 and matriz[1][1] == 1 and matriz[1][2] == 1: # HORIZONTAL
        return 2
    
    elif matriz[2][0] == 1 and matriz[2][1] == 1 and matriz[2][2] == 1: # HORIZONTAL
        return 2
    
    elif matriz[0][0] == 1 and matriz[1][0] == 1 and matriz[2][0] == 1: # VERTICAL
        return 2
    
    elif matriz[0][1] == 1 and matriz[1][1] == 1 and matriz[2][1] == 1: # VERTICAL
        return 2
    
    elif matriz[0][2] == 1 and matriz[1][2] == 1 and matriz[2][2] == 1: # VERTICAL
        return 2
    
    elif matriz[0][0] == 1 and matriz[1][1] == 1 and matriz[2][2] == 1: # DIAGONAL
        return 2
    
    elif matriz[0][2] == 1 and matriz[1][1] == 1 and matriz[2][0] == 1: # DIAGONAL
        return 2
    
