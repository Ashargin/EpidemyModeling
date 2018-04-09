def espace_uni_e(k,l,s,d,P,dm,N,x,N3,t,λ,μ,Q,zlim) :
    if Q==False :
        return(0)
    d=d/1000000
    dm=dm/1000000
    Id=[[0 for i in range(N3)] for j in range(N3)]
    a=int((N3-1)/2)
    Id[a][a]=(N3**2)/P
    u=linspace(0,N3-1,N3)
    h=x/N
    X=[0]*(N3**2)
    Y=[0]*(N3**2)
    S=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I=[Id]+[[[0 for i in range(N3)] for j in range(N3)] for i in range(N)]
    S0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I0=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    Si=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    Ii=[Id]+[[[0 for i in range(N3)] for j in range(N3)] for i in range(N)]
    S0i=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    I0i=[[[0 for i in range(N3)] for j in range(N3)] for t in range(N+1)]
    for i in range(N3) :
        for j in range(N3) :
            X[N3*i+j]=u[i]
            Y[N3*i+j]=u[j]
            S[0][i][j]=1-I[0][i][j]
            Si[0][i][j]=1-I[0][i][j]
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
        S[p+1][0][0]=S[p+1][0][0]+(dm/d)*(S0[p+1][1][0]-S0[p+1][0][0])+(dm/d)*(S0[p+1][0][1]-S0[p+1][0][0])
        I[p+1][0][0]=I[p+1][0][0]+(dm/d)*(I0[p+1][1][0]-I0[p+1][0][0])+(dm/d)*(I0[p+1][0][1]-I0[p+1][0][0])
        S[p+1][0][N3-1]=S[p+1][0][N3-1]+(dm/d)*(S0[p+1][1][N3-1]-S0[p+1][0][N3-1])+(dm/d)*(S0[p+1][0][N3-2]-S0[p+1][0][N3-1])
        I[p+1][0][N3-1]=I[p+1][0][N3-1]+(dm/d)*(I0[p+1][1][N3-1]-I0[p+1][0][N3-1])+(dm/d)*(I0[p+1][0][N3-2]-I0[p+1][0][N3-1])
        S[p+1][N3-1][0]=S[p+1][N3-1][0]+(dm/d)*(S0[p+1][N3-1][1]-S0[p+1][N3-1][0])+(dm/d)*(S0[p+1][N3-2][0]-S0[p+1][N3-1][0])
        I[p+1][N3-1][0]=I[p+1][N3-1][0]+(dm/d)*(I0[p+1][N3-1][1]-I0[p+1][N3-1][0])+(dm/d)*(I0[p+1][N3-2][0]-I0[p+1][N3-1][0])
        S[p+1][N3-1][N3-1]=S[p+1][N3-1][N3-1]+(dm/d)*(S0[p+1][N3-1][N3-2]-S0[p+1][N3-1][N3-1])+(dm/d)*(S0[p+1][N3-2][N3-1]-S0[p+1][N3-1][N3-1])
        I[p+1][N3-1][N3-1]=I[p+1][N3-1][N3-1]+(dm/d)*(I0[p+1][N3-1][N3-2]-I0[p+1][N3-1][N3-1])+(dm/d)*(I0[p+1][N3-2][N3-1]-I0[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            S[p+1][0][j]=S[p+1][0][j]+(dm/d)*(S0[p+1][0][j-1]-S0[p+1][0][j])+(dm/d)*(S0[p+1][0][j+1]-S0[p+1][0][j])+(dm/d)*(S0[p+1][1][j]-S0[p+1][0][j])
            I[p+1][0][j]=I[p+1][0][j]+(dm/d)*(I0[p+1][0][j-1]-I0[p+1][0][j])+(dm/d)*(I0[p+1][0][j+1]-I0[p+1][0][j])+(dm/d)*(I0[p+1][1][j]-I0[p+1][0][j])
            S[p+1][N3-1][j]=S[p+1][N3-1][j]+(dm/d)*(S0[p+1][N3-1][j-1]-S0[p+1][N3-1][j])+(dm/d)*(S0[p+1][N3-1][j+1]-S0[p+1][N3-1][j])+(dm/d)*(S0[p+1][N3-2][j]-S0[p+1][N3-1][j])
            I[p+1][N3-1][j]=I[p+1][N3-1][j]+(dm/d)*(I0[p+1][N3-1][j-1]-I0[p+1][N3-1][j])+(dm/d)*(I0[p+1][N3-1][j+1]-I0[p+1][N3-1][j])+(dm/d)*(I0[p+1][N3-2][j]-I0[p+1][N3-1][j])
        for i in range(1,N3-1) :
            S[p+1][i][0]=S[p+1][i][0]+(dm/d)*(S0[p+1][i-1][0]-S0[p+1][i][0])+(dm/d)*(S0[p+1][i+1][0]-S0[p+1][i][0])+(dm/d)*(S0[p+1][i][1]-S0[p+1][i][0])
            I[p+1][i][0]=I[p+1][i][0]+(dm/d)*(I0[p+1][i-1][0]-I0[p+1][i][0])+(dm/d)*(I0[p+1][i+1][0]-I0[p+1][i][0])+(dm/d)*(I0[p+1][i][1]-I0[p+1][i][0])
            S[p+1][i][N3-1]=S[p+1][i][N3-1]+(dm/d)*(S0[p+1][i-1][N3-1]-S0[p+1][i][N3-1])+(dm/d)*(S0[p+1][i+1][N3-1]-S0[p+1][i][N3-1])+(dm/d)*(S0[p+1][i][N3-2]-S0[p+1][i][N3-1])
            I[p+1][i][N3-1]=I[p+1][i][N3-1]+(dm/d)*(I0[p+1][i-1][N3-1]-I0[p+1][i][N3-1])+(dm/d)*(I0[p+1][i+1][N3-1]-I0[p+1][i][N3-1])+(dm/d)*(I0[p+1][i][N3-2]-I0[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                S[p+1][i][j]=S[p+1][i][j]+(dm/d)*(S0[p+1][i-1][j]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i+1][j]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i][j-1]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i][j+1]-S0[p+1][i][j])
                I[p+1][i][j]=I[p+1][i][j]+(dm/d)*(I0[p+1][i-1][j]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i+1][j]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i][j-1]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i][j+1]-I0[p+1][i][j])
        for i in range(N3) :
            for j in range(N3) :
                S0i[p+1][i][j]=S0[p+1][i][j]
                I0i[p+1][i][j]=I0[p+1][i][j]
                Si[p+1][i][j]=S[p+1][i][j]
                Ii[p+1][i][j]=I[p+1][i][j]
                Si[p][i][j]=S[p][i][j]
                Ii[p][i][j]=I[p][i][j]
        p=p+1
    Ki=[[0 for i in range(N3)] for j in range(N3)]
    Li=[[0 for i in range(N3)] for j in range(N3)]
    for i in range(N3) :
        for j in range(N3) :
            if Q[i][j]==1 :
                Ki[i][j]=k*(1-λ)
                Li[i][j]=l/(1-μ)
            else :
                Ki[i][j]=k
                Li[i][j]=l
    while p<N :
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
        S[p+1][0][0]=S[p+1][0][0]+(dm/d)*(S0[p+1][1][0]-S0[p+1][0][0])+(dm/d)*(S0[p+1][0][1]-S0[p+1][0][0])
        I[p+1][0][0]=I[p+1][0][0]+(dm/d)*(I0[p+1][1][0]-I0[p+1][0][0])+(dm/d)*(I0[p+1][0][1]-I0[p+1][0][0])
        S[p+1][0][N3-1]=S[p+1][0][N3-1]+(dm/d)*(S0[p+1][1][N3-1]-S0[p+1][0][N3-1])+(dm/d)*(S0[p+1][0][N3-2]-S0[p+1][0][N3-1])
        I[p+1][0][N3-1]=I[p+1][0][N3-1]+(dm/d)*(I0[p+1][1][N3-1]-I0[p+1][0][N3-1])+(dm/d)*(I0[p+1][0][N3-2]-I0[p+1][0][N3-1])
        S[p+1][N3-1][0]=S[p+1][N3-1][0]+(dm/d)*(S0[p+1][N3-1][1]-S0[p+1][N3-1][0])+(dm/d)*(S0[p+1][N3-2][0]-S0[p+1][N3-1][0])
        I[p+1][N3-1][0]=I[p+1][N3-1][0]+(dm/d)*(I0[p+1][N3-1][1]-I0[p+1][N3-1][0])+(dm/d)*(I0[p+1][N3-2][0]-I0[p+1][N3-1][0])
        S[p+1][N3-1][N3-1]=S[p+1][N3-1][N3-1]+(dm/d)*(S0[p+1][N3-1][N3-2]-S0[p+1][N3-1][N3-1])+(dm/d)*(S0[p+1][N3-2][N3-1]-S0[p+1][N3-1][N3-1])
        I[p+1][N3-1][N3-1]=I[p+1][N3-1][N3-1]+(dm/d)*(I0[p+1][N3-1][N3-2]-I0[p+1][N3-1][N3-1])+(dm/d)*(I0[p+1][N3-2][N3-1]-I0[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            S[p+1][0][j]=S[p+1][0][j]+(dm/d)*(S0[p+1][0][j-1]-S0[p+1][0][j])+(dm/d)*(S0[p+1][0][j+1]-S0[p+1][0][j])+(dm/d)*(S0[p+1][1][j]-S0[p+1][0][j])
            I[p+1][0][j]=I[p+1][0][j]+(dm/d)*(I0[p+1][0][j-1]-I0[p+1][0][j])+(dm/d)*(I0[p+1][0][j+1]-I0[p+1][0][j])+(dm/d)*(I0[p+1][1][j]-I0[p+1][0][j])
            S[p+1][N3-1][j]=S[p+1][N3-1][j]+(dm/d)*(S0[p+1][N3-1][j-1]-S0[p+1][N3-1][j])+(dm/d)*(S0[p+1][N3-1][j+1]-S0[p+1][N3-1][j])+(dm/d)*(S0[p+1][N3-2][j]-S0[p+1][N3-1][j])
            I[p+1][N3-1][j]=I[p+1][N3-1][j]+(dm/d)*(I0[p+1][N3-1][j-1]-I0[p+1][N3-1][j])+(dm/d)*(I0[p+1][N3-1][j+1]-I0[p+1][N3-1][j])+(dm/d)*(I0[p+1][N3-2][j]-I0[p+1][N3-1][j])
        for i in range(1,N3-1) :
            S[p+1][i][0]=S[p+1][i][0]+(dm/d)*(S0[p+1][i-1][0]-S0[p+1][i][0])+(dm/d)*(S0[p+1][i+1][0]-S0[p+1][i][0])+(dm/d)*(S0[p+1][i][1]-S0[p+1][i][0])
            I[p+1][i][0]=I[p+1][i][0]+(dm/d)*(I0[p+1][i-1][0]-I0[p+1][i][0])+(dm/d)*(I0[p+1][i+1][0]-I0[p+1][i][0])+(dm/d)*(I0[p+1][i][1]-I0[p+1][i][0])
            S[p+1][i][N3-1]=S[p+1][i][N3-1]+(dm/d)*(S0[p+1][i-1][N3-1]-S0[p+1][i][N3-1])+(dm/d)*(S0[p+1][i+1][N3-1]-S0[p+1][i][N3-1])+(dm/d)*(S0[p+1][i][N3-2]-S0[p+1][i][N3-1])
            I[p+1][i][N3-1]=I[p+1][i][N3-1]+(dm/d)*(I0[p+1][i-1][N3-1]-I0[p+1][i][N3-1])+(dm/d)*(I0[p+1][i+1][N3-1]-I0[p+1][i][N3-1])+(dm/d)*(I0[p+1][i][N3-2]-I0[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                S[p+1][i][j]=S[p+1][i][j]+(dm/d)*(S0[p+1][i-1][j]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i+1][j]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i][j-1]-S0[p+1][i][j])+(dm/d)*(S0[p+1][i][j+1]-S0[p+1][i][j])
                I[p+1][i][j]=I[p+1][i][j]+(dm/d)*(I0[p+1][i-1][j]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i+1][j]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i][j-1]-I0[p+1][i][j])+(dm/d)*(I0[p+1][i][j+1]-I0[p+1][i][j])
        for i in range(N3) :
            for j in range(N3) :
                ki=Ki[i][j]
                li=Li[i][j]
                s1=-ki*d*s*Si[p][i][j]*Ii[p][i][j]
                i1=ki*d*s*Si[p][i][j]*Ii[p][i][j]-li*Ii[p][i][j]
                S2=Si[p][i][j]+(h/2)*s1
                I2=Ii[p][i][j]+(h/2)*i1
                s2=-ki*d*s*S2*I2
                i2=ki*d*s*S2*I2-li*I2
                S3=Si[p][i][j]+(h/2)*s2
                I3=Ii[p][i][j]+(h/2)*i2
                s3=-ki*d*s*S3*I3
                i3=ki*d*s*S3*I3-li*I3
                S4=Si[p][i][j]+h*s3
                I4=Ii[p][i][j]+h*i3
                s4=-ki*d*s*S4*I4
                i4=ki*d*s*S4*I4-li*I4
                S0i[p+1][i][j]=Si[p][i][j]+(h/6)*(s1+2*s2+2*s3+s4)
                I0i[p+1][i][j]=Ii[p][i][j]+(h/6)*(i1+2*i2+2*i3+i4)
                Si[p+1][i][j]=S0i[p+1][i][j]
                Ii[p+1][i][j]=I0i[p+1][i][j]
                Si[p][i][j]=d*Si[p][i][j]*1000000  
                Ii[p][i][j]=d*Ii[p][i][j]*1000000
        Si[p+1][0][0]=Si[p+1][0][0]+(dm/d)*(S0i[p+1][1][0]-S0i[p+1][0][0])+(dm/d)*(S0i[p+1][0][1]-S0i[p+1][0][0])
        Ii[p+1][0][0]=Ii[p+1][0][0]+(dm/d)*(I0i[p+1][1][0]-I0i[p+1][0][0])+(dm/d)*(I0i[p+1][0][1]-I0i[p+1][0][0])
        Si[p+1][0][N3-1]=Si[p+1][0][N3-1]+(dm/d)*(S0i[p+1][1][N3-1]-S0i[p+1][0][N3-1])+(dm/d)*(S0i[p+1][0][N3-2]-S0i[p+1][0][N3-1])
        Ii[p+1][0][N3-1]=Ii[p+1][0][N3-1]+(dm/d)*(I0i[p+1][1][N3-1]-I0i[p+1][0][N3-1])+(dm/d)*(I0i[p+1][0][N3-2]-I0i[p+1][0][N3-1])
        Si[p+1][N3-1][0]=Si[p+1][N3-1][0]+(dm/d)*(S0i[p+1][N3-1][1]-S0i[p+1][N3-1][0])+(dm/d)*(S0i[p+1][N3-2][0]-S0i[p+1][N3-1][0])
        Ii[p+1][N3-1][0]=Ii[p+1][N3-1][0]+(dm/d)*(I0i[p+1][N3-1][1]-I0i[p+1][N3-1][0])+(dm/d)*(I0i[p+1][N3-2][0]-I0i[p+1][N3-1][0])
        Si[p+1][N3-1][N3-1]=Si[p+1][N3-1][N3-1]+(dm/d)*(S0i[p+1][N3-1][N3-2]-S0i[p+1][N3-1][N3-1])+(dm/d)*(S0i[p+1][N3-2][N3-1]-S0i[p+1][N3-1][N3-1])
        Ii[p+1][N3-1][N3-1]=Ii[p+1][N3-1][N3-1]+(dm/d)*(I0i[p+1][N3-1][N3-2]-I0i[p+1][N3-1][N3-1])+(dm/d)*(I0i[p+1][N3-2][N3-1]-I0i[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            Si[p+1][0][j]=Si[p+1][0][j]+(dm/d)*(S0i[p+1][0][j-1]-S0i[p+1][0][j])+(dm/d)*(S0i[p+1][0][j+1]-S0i[p+1][0][j])+(dm/d)*(S0i[p+1][1][j]-S0i[p+1][0][j])
            Ii[p+1][0][j]=Ii[p+1][0][j]+(dm/d)*(I0i[p+1][0][j-1]-I0i[p+1][0][j])+(dm/d)*(I0i[p+1][0][j+1]-I0i[p+1][0][j])+(dm/d)*(I0i[p+1][1][j]-I0i[p+1][0][j])
            Si[p+1][N3-1][j]=Si[p+1][N3-1][j]+(dm/d)*(S0i[p+1][N3-1][j-1]-S0i[p+1][N3-1][j])+(dm/d)*(S0i[p+1][N3-1][j+1]-S0i[p+1][N3-1][j])+(dm/d)*(S0i[p+1][N3-2][j]-S0i[p+1][N3-1][j])
            Ii[p+1][N3-1][j]=Ii[p+1][N3-1][j]+(dm/d)*(I0i[p+1][N3-1][j-1]-I0i[p+1][N3-1][j])+(dm/d)*(I0i[p+1][N3-1][j+1]-I0i[p+1][N3-1][j])+(dm/d)*(I0i[p+1][N3-2][j]-I0i[p+1][N3-1][j])
        for i in range(1,N3-1) :
            Si[p+1][i][0]=Si[p+1][i][0]+(dm/d)*(S0i[p+1][i-1][0]-S0i[p+1][i][0])+(dm/d)*(S0i[p+1][i+1][0]-S0i[p+1][i][0])+(dm/d)*(S0i[p+1][i][1]-S0i[p+1][i][0])
            Ii[p+1][i][0]=Ii[p+1][i][0]+(dm/d)*(I0i[p+1][i-1][0]-I0i[p+1][i][0])+(dm/d)*(I0i[p+1][i+1][0]-I0i[p+1][i][0])+(dm/d)*(I0i[p+1][i][1]-I0i[p+1][i][0])
            Si[p+1][i][N3-1]=Si[p+1][i][N3-1]+(dm/d)*(S0i[p+1][i-1][N3-1]-S0i[p+1][i][N3-1])+(dm/d)*(S0i[p+1][i+1][N3-1]-S0i[p+1][i][N3-1])+(dm/d)*(S0i[p+1][i][N3-2]-S0i[p+1][i][N3-1])
            Ii[p+1][i][N3-1]=Ii[p+1][i][N3-1]+(dm/d)*(I0i[p+1][i-1][N3-1]-I0i[p+1][i][N3-1])+(dm/d)*(I0i[p+1][i+1][N3-1]-I0i[p+1][i][N3-1])+(dm/d)*(I0i[p+1][i][N3-2]-I0i[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                Si[p+1][i][j]=Si[p+1][i][j]+(dm/d)*(S0i[p+1][i-1][j]-S0i[p+1][i][j])+(dm/d)*(S0i[p+1][i+1][j]-S0i[p+1][i][j])+(dm/d)*(S0i[p+1][i][j-1]-S0i[p+1][i][j])+(dm/d)*(S0i[p+1][i][j+1]-S0i[p+1][i][j])
                Ii[p+1][i][j]=Ii[p+1][i][j]+(dm/d)*(I0i[p+1][i-1][j]-I0i[p+1][i][j])+(dm/d)*(I0i[p+1][i+1][j]-I0i[p+1][i][j])+(dm/d)*(I0i[p+1][i][j-1]-I0i[p+1][i][j])+(dm/d)*(I0i[p+1][i][j+1]-I0i[p+1][i][j])
        p=p+1
    for i in range(N3) :
        for j in range(N3) :
            S[N][i][j]=d*S[N][i][j]*1000000
            I[N][i][j]=d*I[N][i][j]*1000000
            Si[N][i][j]=d*Si[N][i][j]*1000000
            Ii[N][i][j]=d*Ii[N][i][j]*1000000
    E=0
    Dtot=d*N3**2*1000000
    for i in range(N3) :
        for j in range(N3) :
            E=E+(Si[N][i][j]-S[N][i][j])/Dtot
    return(E)