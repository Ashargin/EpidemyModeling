def espace_adj_e(K,L,s,D,Id,Dm,N,x,N3,t,λ,μ,Q,zlim) :
    if Q==False :
        return(0)
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
        S[p+1][0][0]=S[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(S0[p+1][1][0]-S0[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(S0[p+1][0][1]-S0[p+1][0][0])
        I[p+1][0][0]=I[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(I0[p+1][1][0]-I0[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(I0[p+1][0][1]-I0[p+1][0][0])
        S[p+1][0][N3-1]=S[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(S0[p+1][1][N3-1]-S0[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(S0[p+1][0][N3-2]-S0[p+1][0][N3-1])
        I[p+1][0][N3-1]=I[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(I0[p+1][1][N3-1]-I0[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(I0[p+1][0][N3-2]-I0[p+1][0][N3-1])
        S[p+1][N3-1][0]=S[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(S0[p+1][N3-1][1]-S0[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(S0[p+1][N3-2][0]-S0[p+1][N3-1][0])
        I[p+1][N3-1][0]=I[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(I0[p+1][N3-1][1]-I0[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(I0[p+1][N3-2][0]-I0[p+1][N3-1][0])
        S[p+1][N3-1][N3-1]=S[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(S0[p+1][N3-1][N3-2]-S0[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(S0[p+1][N3-2][N3-1]-S0[p+1][N3-1][N3-1])
        I[p+1][N3-1][N3-1]=I[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(I0[p+1][N3-1][N3-2]-I0[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(I0[p+1][N3-2][N3-1]-I0[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            S[p+1][0][j]=S[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(S0[p+1][0][j-1]-S0[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(S0[p+1][0][j+1]-S0[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(S0[p+1][1][j]-S0[p+1][0][j])
            I[p+1][0][j]=I[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(I0[p+1][0][j-1]-I0[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(I0[p+1][0][j+1]-I0[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(I0[p+1][1][j]-I0[p+1][0][j])
            S[p+1][N3-1][j]=S[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(S0[p+1][N3-1][j-1]-S0[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(S0[p+1][N3-1][j+1]-S0[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(S0[p+1][N3-2][j]-S0[p+1][N3-1][j])
            I[p+1][N3-1][j]=I[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(I0[p+1][N3-1][j-1]-I0[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(I0[p+1][N3-1][j+1]-I0[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(I0[p+1][N3-2][j]-I0[p+1][N3-1][j])
        for i in range(1,N3-1) :
            S[p+1][i][0]=S[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(S0[p+1][i-1][0]-S0[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(S0[p+1][i+1][0]-S0[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(S0[p+1][i][1]-S0[p+1][i][0])
            I[p+1][i][0]=I[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(I0[p+1][i-1][0]-I0[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(I0[p+1][i+1][0]-I0[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(I0[p+1][i][1]-I0[p+1][i][0])
            S[p+1][i][N3-1]=S[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(S0[p+1][i-1][N3-1]-S0[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(S0[p+1][i+1][N3-1]-S0[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(S0[p+1][i][N3-2]-S0[p+1][i][N3-1])
            I[p+1][i][N3-1]=I[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(I0[p+1][i-1][N3-1]-I0[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(I0[p+1][i+1][N3-1]-I0[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(I0[p+1][i][N3-2]-I0[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                S[p+1][i][j]=S[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(S0[p+1][i-1][j]-S0[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(S0[p+1][i+1][j]-S0[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(S0[p+1][i][j-1]-S0[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(S0[p+1][i][j+1]-S0[p+1][i][j])
                I[p+1][i][j]=I[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(I0[p+1][i-1][j]-I0[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(I0[p+1][i+1][j]-I0[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(I0[p+1][i][j-1]-I0[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(I0[p+1][i][j+1]-I0[p+1][i][j])
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
                Ki[i][j]=K[i][j]*(1-λ)
                Li[i][j]=L[i][j]/(1-μ)
            else :
                Ki[i][j]=K[i][j]
                Li[i][j]=L[i][j]
    while p<N :
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
        S[p+1][0][0]=S[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(S0[p+1][1][0]-S0[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(S0[p+1][0][1]-S0[p+1][0][0])
        I[p+1][0][0]=I[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(I0[p+1][1][0]-I0[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(I0[p+1][0][1]-I0[p+1][0][0])
        S[p+1][0][N3-1]=S[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(S0[p+1][1][N3-1]-S0[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(S0[p+1][0][N3-2]-S0[p+1][0][N3-1])
        I[p+1][0][N3-1]=I[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(I0[p+1][1][N3-1]-I0[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(I0[p+1][0][N3-2]-I0[p+1][0][N3-1])
        S[p+1][N3-1][0]=S[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(S0[p+1][N3-1][1]-S0[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(S0[p+1][N3-2][0]-S0[p+1][N3-1][0])
        I[p+1][N3-1][0]=I[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(I0[p+1][N3-1][1]-I0[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(I0[p+1][N3-2][0]-I0[p+1][N3-1][0])
        S[p+1][N3-1][N3-1]=S[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(S0[p+1][N3-1][N3-2]-S0[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(S0[p+1][N3-2][N3-1]-S0[p+1][N3-1][N3-1])
        I[p+1][N3-1][N3-1]=I[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(I0[p+1][N3-1][N3-2]-I0[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(I0[p+1][N3-2][N3-1]-I0[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            S[p+1][0][j]=S[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(S0[p+1][0][j-1]-S0[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(S0[p+1][0][j+1]-S0[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(S0[p+1][1][j]-S0[p+1][0][j])
            I[p+1][0][j]=I[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(I0[p+1][0][j-1]-I0[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(I0[p+1][0][j+1]-I0[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(I0[p+1][1][j]-I0[p+1][0][j])
            S[p+1][N3-1][j]=S[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(S0[p+1][N3-1][j-1]-S0[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(S0[p+1][N3-1][j+1]-S0[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(S0[p+1][N3-2][j]-S0[p+1][N3-1][j])
            I[p+1][N3-1][j]=I[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(I0[p+1][N3-1][j-1]-I0[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(I0[p+1][N3-1][j+1]-I0[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(I0[p+1][N3-2][j]-I0[p+1][N3-1][j])
        for i in range(1,N3-1) :
            S[p+1][i][0]=S[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(S0[p+1][i-1][0]-S0[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(S0[p+1][i+1][0]-S0[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(S0[p+1][i][1]-S0[p+1][i][0])
            I[p+1][i][0]=I[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(I0[p+1][i-1][0]-I0[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(I0[p+1][i+1][0]-I0[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(I0[p+1][i][1]-I0[p+1][i][0])
            S[p+1][i][N3-1]=S[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(S0[p+1][i-1][N3-1]-S0[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(S0[p+1][i+1][N3-1]-S0[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(S0[p+1][i][N3-2]-S0[p+1][i][N3-1])
            I[p+1][i][N3-1]=I[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(I0[p+1][i-1][N3-1]-I0[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(I0[p+1][i+1][N3-1]-I0[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(I0[p+1][i][N3-2]-I0[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                S[p+1][i][j]=S[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(S0[p+1][i-1][j]-S0[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(S0[p+1][i+1][j]-S0[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(S0[p+1][i][j-1]-S0[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(S0[p+1][i][j+1]-S0[p+1][i][j])
                I[p+1][i][j]=I[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(I0[p+1][i-1][j]-I0[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(I0[p+1][i+1][j]-I0[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(I0[p+1][i][j-1]-I0[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(I0[p+1][i][j+1]-I0[p+1][i][j])
        for i in range(N3) :
            for j in range(N3) :
                ki=Ki[i][j]
                li=Li[i][j]
                d=D[i][j]/1000000
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
                Si[p][i][j]=D[i][j]*Si[p][i][j]
                Ii[p][i][j]=D[i][j]*Ii[p][i][j]
        Si[p+1][0][0]=Si[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(S0i[p+1][1][0]-S0i[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(S0i[p+1][0][1]-S0i[p+1][0][0])
        Ii[p+1][0][0]=Ii[p+1][0][0]+(Dm[0][0][1][0]/D[0][0])*(I0i[p+1][1][0]-I0i[p+1][0][0])+(Dm[0][0][0][1]/D[0][0])*(I0i[p+1][0][1]-I0i[p+1][0][0])
        Si[p+1][0][N3-1]=Si[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(S0i[p+1][1][N3-1]-S0i[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(S0i[p+1][0][N3-2]-S0i[p+1][0][N3-1])
        Ii[p+1][0][N3-1]=Ii[p+1][0][N3-1]+(Dm[0][N3-1][1][N3-1]/D[0][N3-1])*(I0i[p+1][1][N3-1]-I0i[p+1][0][N3-1])+(Dm[0][N3-2][0][N3-1]/D[0][N3-1])*(I0i[p+1][0][N3-2]-I0i[p+1][0][N3-1])
        Si[p+1][N3-1][0]=Si[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(S0i[p+1][N3-1][1]-S0i[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(S0i[p+1][N3-2][0]-S0i[p+1][N3-1][0])
        Ii[p+1][N3-1][0]=Ii[p+1][N3-1][0]+(Dm[N3-1][0][N3-1][1]/D[N3-1][0])*(I0i[p+1][N3-1][1]-I0i[p+1][N3-1][0])+(Dm[N3-2][0][N3-1][0]/D[N3-1][0])*(I0i[p+1][N3-2][0]-I0i[p+1][N3-1][0])
        Si[p+1][N3-1][N3-1]=Si[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(S0i[p+1][N3-1][N3-2]-S0i[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(S0i[p+1][N3-2][N3-1]-S0i[p+1][N3-1][N3-1])
        Ii[p+1][N3-1][N3-1]=Ii[p+1][N3-1][N3-1]+(Dm[N3-1][N3-2][N3-1][N3-1]/D[N3-1][N3-1])*(I0i[p+1][N3-1][N3-2]-I0i[p+1][N3-1][N3-1])+(Dm[N3-2][N3-1][N3-1][N3-1]/D[N3-1][N3-1])*(I0i[p+1][N3-2][N3-1]-I0i[p+1][N3-1][N3-1])
        for j in range(1,N3-1) :
            Si[p+1][0][j]=Si[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(S0i[p+1][0][j-1]-S0i[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(S0i[p+1][0][j+1]-S0i[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(S0i[p+1][1][j]-S0i[p+1][0][j])
            Ii[p+1][0][j]=Ii[p+1][0][j]+(Dm[0][j-1][0][j]/D[0][j])*(I0i[p+1][0][j-1]-I0i[p+1][0][j])+(Dm[0][j][0][j+1]/D[0][j])*(I0i[p+1][0][j+1]-I0i[p+1][0][j])+(Dm[0][j][1][j]/D[0][j])*(I0i[p+1][1][j]-I0i[p+1][0][j])
            Si[p+1][N3-1][j]=Si[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(S0i[p+1][N3-1][j-1]-S0i[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(S0i[p+1][N3-1][j+1]-S0i[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(S0i[p+1][N3-2][j]-S0i[p+1][N3-1][j])
            Ii[p+1][N3-1][j]=Ii[p+1][N3-1][j]+(Dm[N3-1][j-1][N3-1][j]/D[N3-1][j])*(I0i[p+1][N3-1][j-1]-I0i[p+1][N3-1][j])+(Dm[N3-1][j][N3-1][j+1]/D[N3-1][j])*(I0i[p+1][N3-1][j+1]-I0i[p+1][N3-1][j])+(Dm[N3-2][j][N3-1][j]/D[N3-1][j])*(I0i[p+1][N3-2][j]-I0i[p+1][N3-1][j])
        for i in range(1,N3-1) :
            Si[p+1][i][0]=Si[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(S0i[p+1][i-1][0]-S0i[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(S0i[p+1][i+1][0]-S0i[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(S0i[p+1][i][1]-S0i[p+1][i][0])
            Ii[p+1][i][0]=Ii[p+1][i][0]+(Dm[i-1][0][i][0]/D[i][0])*(I0i[p+1][i-1][0]-I0i[p+1][i][0])+(Dm[i][0][i+1][0]/D[i][0])*(I0i[p+1][i+1][0]-I0i[p+1][i][0])+(Dm[i][0][i][1]/D[i][0])*(I0i[p+1][i][1]-I0i[p+1][i][0])
            Si[p+1][i][N3-1]=Si[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(S0i[p+1][i-1][N3-1]-S0i[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(S0i[p+1][i+1][N3-1]-S0i[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(S0i[p+1][i][N3-2]-S0i[p+1][i][N3-1])
            Ii[p+1][i][N3-1]=Ii[p+1][i][N3-1]+(Dm[i-1][N3-1][i][N3-1]/D[i][N3-1])*(I0i[p+1][i-1][N3-1]-I0i[p+1][i][N3-1])+(Dm[i][N3-1][i+1][N3-1]/D[i][N3-1])*(I0i[p+1][i+1][N3-1]-I0i[p+1][i][N3-1])+(Dm[i][N3-2][i][N3-1]/D[i][N3-1])*(I0i[p+1][i][N3-2]-I0i[p+1][i][N3-1])
        for i in range(1,N3-1) :
            for j in range(1,N3-1) :
                Si[p+1][i][j]=Si[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(S0i[p+1][i-1][j]-S0i[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(S0i[p+1][i+1][j]-S0i[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(S0i[p+1][i][j-1]-S0i[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(S0i[p+1][i][j+1]-S0i[p+1][i][j])
                Ii[p+1][i][j]=Ii[p+1][i][j]+(Dm[i-1][j][i][j]/D[i][j])*(I0i[p+1][i-1][j]-I0i[p+1][i][j])+(Dm[i][j][i+1][j]/D[i][j])*(I0i[p+1][i+1][j]-I0i[p+1][i][j])+(Dm[i][j-1][i][j]/D[i][j])*(I0i[p+1][i][j-1]-I0i[p+1][i][j])+(Dm[i][j][i][j+1]/D[i][j])*(I0i[p+1][i][j+1]-I0i[p+1][i][j])
        p=p+1
    for i in range(N3) :
        for j in range(N3) :
            S[N][i][j]=D[i][j]*S[N][i][j]
            I[N][i][j]=D[i][j]*I[N][i][j]
            Si[N][i][j]=D[i][j]*Si[N][i][j]
            Ii[N][i][j]=D[i][j]*Ii[N][i][j]
    E=0
    Dtot=0
    for i in range(N3) :
        for j in range(N3) :
            Dtot=Dtot+D[i][j]
    for i in range(N3) :
        for j in range(N3) :
            E=E+(Si[N][i][j]-S[N][i][j])/Dtot
    return(E)