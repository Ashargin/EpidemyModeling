def simple_eλ(k,l,s,d,P,t,μ,N,x,N2) :
    E=[0]*(N2+1)
    h2=1/N2
    for j in range(N2+1) :
        λ=j*h2
        E[j]=simple_e(k,l,s,d,P,t,λ,μ,N,x)
    X=linspace(0,1,N2+1)
    ax=figure().gca()
    ax.set_ylim(0,1)
    ax.set_xlabel('lambda')
    ax.set_ylabel('e')
    ax.plot(X,E,color=(0,0,0.75),linewidth=5)