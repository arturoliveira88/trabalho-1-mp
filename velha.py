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
    
    
    # CRITERIOS PARA ESTAR INDEFINIDO ------------------------------
    
    if cont_X + cont_O < 5:
        return -1
    
    # CRITERIO PARA X VENCER ---------------------------------------------
    
    if matriz[0][0] == 2 and matriz[0][1] == 2 and matriz[0][2] == 2:
        return 1
    
    elif matriz[1][0] == 2 and matriz[1][1] == 2 and matriz[1][2] == 2:
        return 1
    
    elif matriz[2][0] == 2 and matriz[2][1] == 2 and matriz[2][2] == 2:
        return 1
    
    elif matriz[0][0] == 2 and matriz[1][1] == 2 and matriz[2][2] == 2:
        return 1
    
    elif matriz[0][2] == 2 and matriz[1][1] == 2 and matriz[2][0] == 2:
        return 1
