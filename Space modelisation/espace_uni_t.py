def espace_uni_t(k,l,s,d,P,dm,t,N,x,N3,zlim) :
    d=d/1000000
    dm=dm/1000000
    Id=[[0 for i in range(N3)] for j in range(N3)]
    a=int((N3-1)/2)
    Id[a][a]=(N3**2)/P
    h=x/N
    S=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I=[Id]+[[[0 for i in range(N3)] for j in range(N3)] for t in range(N)]
    S0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    for i in range(N3) :
        for j in range(N3) :
            S[0][i][j]=1-I[0][i][j]
    p=0
    while p<t/h :
        for i in range(N3) :
            for j in range(N3) :
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
                S[p][i][j]=d*S[p][i][j]*1000000
                I[p][i][j]=d*I[p][i][j]*1000000
        S[p+1][0][0]=S[p+1][0][0]+(dm/d)*(S0[p+1][1][0]+S0[p+1][0][1]-2*S0[p+1][0][0])
        I[p+1][0][0]=I[p+1][0][0]+(dm/d)*(I0[p+1][1][0]+I0[p+1][0][1]-2*I0[p+1][0][0])
        S[p+1][0][N3-1]=S[p+1][0][N3-1]+(dm/d)*(S0[p+1][1][N3-1]+S0[p+1][0][N3-2]-2*S0[p+1][0][N3-1])
        I[p+1][0][N3-1]=I[p+1][0][N3-1]+(dm/d)*(I0[p+1][1][N3-1]+I0[p+1][0][N3-2]-2*I0[p+1][0][N3-1])
        S[p+1][N3-1][0]=S[p+1][N3-1][0]+(dm/d)*(S0[p+1][N3-1][1]+S0[p+1][N3-2][0]-2*S0[p+1][N3-1][0])
        I[p+1][N3-1][0]=I[p+1][N3-1][0]+(dm/d)*(I0[p+1][N3-1][1]+I0[p+1][N3-2][0]-2*I0[p+1][N3-1][0])
        S[p+1][N3-1][N3-1]=S[p+1][N3-1][N3-1]+(dm/d)*(S0[p+1][N3-1][N3-2]+S0[p+1][N3-2][N3-1]-2*S0[p+1][N3-1][N3-1])
        I[p+1][N3-1][N3-1]=I[p+1][N3-1][N3-1]+(dm/d)*(I0[p+1][N3-1][N3-2]+I0[p+1][N3-2][N3-1]-2*I0[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            S[p+1][0][j]=S[p+1][0][j]+(dm/d)*(S0[p+1][0][j-1]+S0[p+1][0][j+1]+S0[p+1][1][j]-3*S0[p+1][0][j])
            I[p+1][0][j]=I[p+1][0][j]+(dm/d)*(I0[p+1][0][j-1]+I0[p+1][0][j+1]+I0[p+1][1][j]-3*I0[p+1][0][j])
            S[p+1][N3-1][j]=S[p+1][N3-1][j]+(dm/d)*(S0[p+1][N3-1][j-1]+S0[p+1][N3-1][j+1]+S0[p+1][N3-2][j]-3*S0[p+1][N3-1][j])
            I[p+1][N3-1][j]=I[p+1][N3-1][j]+(dm/d)*(I0[p+1][N3-1][j-1]+I0[p+1][N3-1][j+1]+I0[p+1][N3-2][j]-3*I0[p+1][N3-1][j])
        for i in range(1,N3-1) :
            S[p+1][i][0]=S[p+1][i][0]+(dm/d)*(S0[p+1][i-1][0]+S0[p+1][i+1][0]+S0[p+1][i][1]-3*S0[p+1][i][0])
            I[p+1][i][0]=I[p+1][i][0]+(dm/d)*(I0[p+1][i-1][0]+I0[p+1][i+1][0]+I0[p+1][i][1]-3*I0[p+1][i][0])
            S[p+1][i][N3-1]=S[p+1][i][N3-1]+(dm/d)*(S0[p+1][i-1][N3-1]+S0[p+1][i+1][N3-1]+S0[p+1][i][N3-2]-3*S0[p+1][i][N3-1])
            I[p+1][i][N3-1]=I[p+1][i][N3-1]+(dm/d)*(I0[p+1][i-1][N3-1]+I0[p+1][i+1][N3-1]+I0[p+1][i][N3-2]-3*I0[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                S[p+1][i][j]=S[p+1][i][j]+(dm/d)*(S0[p+1][i-1][j]+S0[p+1][i+1][j]+S0[p+1][i][j-1]+S0[p+1][i][j+1]-4*S0[p+1][i][j])
                I[p+1][i][j]=I[p+1][i][j]+(dm/d)*(I0[p+1][i-1][j]+I0[p+1][i+1][j]+I0[p+1][i][j-1]+I0[p+1][i][j+1]-4*I0[p+1][i][j])
        p=p+1
    for i in range(N3) :
        for j in range(N3) :
            S[p][i][j]=d*S[p][i][j]*1000000
            I[p][i][j]=d*I[p][i][j]*1000000
    return(S[p],I[p])