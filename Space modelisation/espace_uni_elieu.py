def espace_uni_elieu(k,l,s,d,P,dm,N,x,N3,t,λ,μ,p,R0,zlim) :
    E=[0 for i in range(len(R0))]
    Q=[[0 for i in range(N3)] for j in range(N3)]
    I=espace_uni_t(k,l,s,d,P,dm,t,N,x,N3,zlim)[1]
    for r in range(len(R0)) :
        r0=R0[r]
        Q=q(N3,p,r0)
        E[r]=espace_uni_e(k,l,s,d,P,dm,N,x,N3,t,λ,μ,Q,zlim)
    Sf=espace_uni_t(k,l,s,d,P,dm,x,N,x,N3,zlim)[0]
    a=0
    Dtot=d*N3**2
    for i in range(N3) :
        for j in range(N3) :
            a=a+Sf[i][j]
    Rfinal=1-a/Dtot
    M=0
    R=0
    for r in range(len(R0)) :
        if E[r]>=M :
            M=E[r]
            R=R0[r]
    Q=q(N3,p,R)
    espace_sub_3(I,Q,t,M,Rfinal,N3,zlim)