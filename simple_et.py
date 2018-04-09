def simple_et(k,l,s,d,P,λ,μ,N,x,N2,x2) :
    E=[0]*(N2+1)
    h2=x2/N2
    for j in range(N2+1) :
        t=j*h2
        E[j]=simple_e(k,l,s,d,P,t,λ,μ,N,x)
    X=linspace(0,x2,N2+1)
    ax=figure().gca()
    ax.set_ylim(0,1)
    ax.set_xlabel('t (ut)')
    ax.set_ylabel('e')
    ax.plot(X,E,color=(0,0,0.75),linewidth=5)