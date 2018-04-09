def gauss_ex(A,B,C) :
    D=[[0 for i in range(41)] for j in range(41)]
    for i in range(41) :
        for j in range(41) :
            if j<15 :
                if i<12 :
                    D[i][j]=A*exp(-(((i-3)**2)/B)-(((j-7)**2)/B))+C
                elif i<29 :
                    D[i][j]=A*exp(-(((i-20)**2)/B)-(((j-7)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-37)**2)/B)-(((j-7)**2)/B))+C
            elif j<30 :
                if i<21 :
                    D[i][j]=A*exp(-(((i-12)**2)/B)-(((j-22)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-28)**2)/B)-(((j-22)**2)/B))+C
            else :
                if i<12 :
                    D[i][j]=A*exp(-(((i-3)**2)/B)-(((j-37)**2)/B))+C
                elif i<29 :
                    D[i][j]=A*exp(-(((i-20)**2)/B)-(((j-37)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-37)**2)/B)-(((j-37)**2)/B))+C
    return(D)