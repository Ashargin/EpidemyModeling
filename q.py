def tri(R) :
    n=len(R)
    if n==1 :
        return(R)
    else :
        a=int((n+1)/2)
        A=R[:a]
        B=R[a:]
        A2=tri(A)
        B2=tri(B)
        C=[]
        p=0
        q=0
        for i in range(n) :
            if p==a :
                C=C+[B2[q]]
                q=q+1
            elif q==n-a :
                C=C+[A2[p]]
                p=p+1
            else :
                u=A2[p][0]
                v=B2[q][0]
                if u<=v :
                    C=C+[A2[p]]
                    p=p+1
                else :
                    C=C+[B2[q]]
                    q=q+1
        return(C)

def q(N3,p,r0) :
    Qres=[[0 for i in range(N3)] for j in range(N3)]
    N4=int(p*N3**2)
    R=[0 for i in range(N3**2)]
    a=int((N3-1)/2)
    for i in range(N3) :
        for j in range(N3) :
            R[i*N3+j]=[sqrt((i-a)**2+(j-a)**2),i,j]
    R2=tri(R)
    n=0
    while R2[n][0]<r0 :
        n=n+1
    if n>=N3**2-N4+1 :
        return(False)
    else :
        for m in range(n,n+N4) :
            i=R2[m][1]
            j=R2[m][2]
            Qres[i][j]=1
    return(Qres)