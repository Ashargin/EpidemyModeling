def espace_adj_elieu(K,L,s,D,Id,Dm,N,x,N3,t,λ,μ,p,R0,zlim) :
    E=[0 for i in range(len(R0))]
    Q=[[0 for i in range(N3)] for j in range(N3)]
    I=espace_adj_t(K,L,s,D,Id,Dm,t,N,x,N3,zlim)[1]
    for r in range(len(R0)) :
        r0=R0[r]
        Q=q(N3,p,r0)
        E[r]=espace_adj_e(K,L,s,D,Id,Dm,N,x,N3,t,λ,μ,Q,zlim)
    Sf=espace_adj_t(K,L,s,D,Id,Dm,x,N,x,N3,zlim)[0]
    a=0
    Dtot=0
    for i in range(N3) :
        for j in range(N3) :
            a=a+Sf[i][j]
            Dtot=Dtot+D[i][j]
    Rfinal=1-a/Dtot
    M=0
    R=0
    for r in range(len(R0)) :
        if E[r]>=M :
            M=E[r]
            R=R0[r]
    Q=q(N3,p,R)
    espace_sub_3(I,Q,t,M,Rfinal,N3,zlim)

def espace_sub_3(I,Q,t,M,Rfinal,N3,zlim) :
    X=[0]*(N3**2)
    Y=[0]*(N3**2)
    Z=[0]*(N3**2)
    u=linspace(0,N3-1,N3)
    for i in range(N3) :
        for j in range(N3) :
            X[N3*i+j]=u[i]
            Y[N3*i+j]=u[j]
    Xq=[]
    Yq=[]
    Zq=[]
    for i in range(N3) :
        for j in range(N3) :
            Z[N3*i+j]=I[i][j]
            if Q[i][j]==1 :
                Xq=Xq+[i]
                Yq=Yq+[j]
                Zq=Zq+[zlim]
    fig=figure()
    ax=fig.gca(projection='3d')
    ax.set_zlim3d(0,zlim)
    ax.set_title('t='+str(int(t*100)/100)+' ut'+'                 e='+str(int(M*10**(3-ordredegrandeur(M)))/10**(3-ordredegrandeur(M)))+'                 Rfinal='+str(int(Rfinal*10**(3-ordredegrandeur(Rfinal)))/10**(3-ordredegrandeur(Rfinal))))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.text(N3*0.95,N3*0.75,zlim*1.2,'d(I) (hab/km²)',color=(0,0,0),size=12)
    ax.plot(X,Y,Z,'o',color=(0,0,0.75))
    ax.plot(Xq,Yq,Zq,'o',color=(0,0.75,0))

def ordredegrandeur(M) :
    c=0
    while M<1 :
        M=10*M
        c=c-1
    return(c)