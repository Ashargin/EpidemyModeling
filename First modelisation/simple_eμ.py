def simple_eμ(k,l,s,d,P,t,λ,N,x,N2) :
    E=[0]*N2
    h2=1/N2
    for j in range(N2) :
        μ=j*h2
        E[j]=simple_e(k,l,s,d,P,t,λ,μ,N,x)
    X=linspace(0,1,N2)
    ax=figure().gca()
    ax.set_ylim(0,1)
    ax.set_xlabel('mu')
    ax.set_ylabel('e')
    ax.plot(X,E,color=(0,0,0.75),linewidth=5)