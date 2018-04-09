def espace(K,L,s,D,Id,Dm,T,N,x,N3,zlim) :
    u=linspace(0,N3-1,N3)
    h=x/N
    X=[0]*(N3**2)
    Y=[0]*(N3**2)
    S=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I=[Id]+[[[0 for i in range(N3)] for j in range(N3)] for i in range(N)]
    S0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    for i in range(N3) :
        for j in range(N3) :
            X[N3*i+j]=u[i]
            Y[N3*i+j]=u[j]
            S[0][i][j]=1-I[0][i][j]
    for p in range(N) :
        for i in range(N3) :
            for j in range(N3) :
                k=K[i][j]
                l=L[i][j]
                d=D[i][j]/1000000
                s1=-k*d*s*S[p][i][j]*I[p][i][j]
                i1=k*d*s*S[p][i][j]*I[p][i][j]-l*I[p][i][j]
                S2=S[p][i][j]+(h/2)*s1
                I2=I[p][i][j]+(h/2)*i1
                s2=-k*d*s*S2*I2
                i2=k*d*s*S2*I2-l*I2
                S3=S[p][i][j]+(h/2)*s2
                I3=I[p][i][j]+(h/2)*i2
                s3=-k*d*s*S3*I3
                i3=k*d*s*S3*I3-l*I3
                S4=S[p][i][j]+h*s3
                I4=I[p][i][j]+h*i3
                s4=-k*d*s*S4*I4
                i4=k*d*s*S4*I4-l*I4
                S0[p+1][i][j]=S[p][i][j]+(h/6)*(s1+2*s2+2*s3+s4)
                I0[p+1][i][j]=I[p][i][j]+(h/6)*(i1+2*i2+2*i3+i4)
                S[p+1][i][j]=S0[p+1][i][j]
                I[p+1][i][j]=I0[p+1][i][j]
                S[p][i][j]=D[i][j]*S[p][i][j]
                I[p][i][j]=D[i][j]*I[p][i][j]
        for i in range(N3) :
            for j in range(N3) :
                for i2 in range(i,N3) :
                    for j2 in range(N3) :
                        if (i2>i or (i2==i and j2>j)) :
                            dm=Dm[i][j][i2][j2]/1000000
                            d1=D[i][j]/1000000
                            d2=D[i2][j2]/1000000
                            S[p+1][i][j]=S[p+1][i][j]+(dm/d1)*(S0[p+1][i2][j2]-S0[p+1][i][j])
                            I[p+1][i][j]=I[p+1][i][j]+(dm/d1)*(I0[p+1][i2][j2]-I0[p+1][i][j])
                            S[p+1][i2][j2]=S[p+1][i2][j2]+(dm/d2)*(S0[p+1][i][j]-S0[p+1][i2][j2])
                            I[p+1][i2][j2]=I[p+1][i2][j2]+(dm/d2)*(I0[p+1][i][j]-I0[p+1][i2][j2])
    for i in range(N3) :
        for j in range(N3) :
            S[N][i][j]=D[i][j]*S[N][i][j]
            I[N][i][j]=D[i][j]*I[N][i][j]
    n=len(T)
    for q in range(n) :
        p=int(T[q]/h)
        espace_sub(I,X,Y,p,h,N3,zlim)

def espace_sub(I,X,Y,p,h,N3,zlim) :
    Z=[0]*(N3**2)
    for i in range(N3) :
        for j in range(N3) :
            Z[N3*i+j]=I[p][i][j]
    fig=figure()
    ax=fig.gca(projection='3d')
    ax.set_zlim3d(0,zlim)
    ax.set_title('t='+(str(int(p*h*100)/100)+' ut'))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.text(N3*0.95,N3*0.75,zlim*1.2,'d(I) (hab/km²)',color=(0,0,0),size=12)
    ax.plot(X,Y,Z,'o',color=(0,0,0.75))