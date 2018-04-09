def simple_etλ(k,l,s,d,P,μ,N,x,N2,x2) :
    d=d/1000000
    fig=figure()
    ax=fig.gca(projection='3d')
    u=linspace(0,x2,N2)
    v=linspace(0,1,N2)
    X=zeros((N2,N2))
    Y=zeros((N2,N2))
    Z=zeros((N2,N2))
    for p in range(N2) :
        for q in range(N2) :
            X[p][q]=u[p]
            Y[p][q]=v[q]
            t=u[p]
            λ=v[q]
            Z[p][q]=simple_e(k,l,s,d,P,t,λ,μ,N,x)
    ax.set_zlim3d(0,1)
    ax.set_xlabel('t (ut)')
    ax.set_ylabel('lambda')
    ax.set_zlabel('e')
    ax.plot_surface(X,Y,Z,color=(0,0,0.75))