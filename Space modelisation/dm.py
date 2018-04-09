def dm(D,m) :
    N3=len(D)
    Dm=[[[[0 for i in range(N3)] for j in range(N3)] for t in range(N3)] for u in range(N3)]
    Dm[0][0][0][1]=m*max(D[0][0],D[0][1])
    Dm[0][0][1][0]=m*max(D[0][0],D[1][0])
    Dm[0][N3-1][1][N3-1]=m*max(D[0][N3-1],D[1][N3-1])
    Dm[N3-1][0][N3-1][1]=m*max(D[N3-1][0],D[N3-1][1])
    for j in range(1,N3-1) :
        Dm[0][j][0][j+1]=m*max(D[0][j],D[0][j+1])
        Dm[0][j][1][j]=m*max(D[0][j],D[1][j])
        Dm[N3-1][j][N3-1][j+1]=m*max(D[N3-1][j],D[N3-1][j+1])
    for i in range(1,N3-1) :
        Dm[i][0][i+1][0]=m*max(D[i][0],D[i+1][0])
        Dm[i][0][i][1]=m*max(D[i][0],D[i][1])
        Dm[i][N3-1][i+1][N3-1]=m*max(D[i][N3-1],D[i+1][N3-1])
    for i in range(1,N3-1) :
        for j in range(1,N3-1) :
            Dm[i][j][i+1][j]=m*max(D[i][j],D[i+1][j])
            Dm[i][j][i][j+1]=m*max(D[i][j],D[i][j+1])
    return(Dm)