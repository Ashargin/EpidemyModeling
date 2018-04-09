from numpy import*
from pylab import*
from matplotlib.pyplot import*
from mpl_toolkits.mplot3d import Axes3D

def simple(k,l,s,d,P,N,x) :
    d=d/1000000
    S=[1-1/P]+[0]*N
    I=[1/P]+[0]*N
    R=[0]*(N+1)
    h=x/N
    for i in range(N):
        s1=-k*d*s*S[i]*I[i]
        i1=k*d*s*S[i]*I[i]-l*I[i]
        r1=l*I[i]
        S2=S[i]+(h/2)*s1
        I2=I[i]+(h/2)*i1
        s2=-k*d*s*S2*I2
        i2=k*d*s*S2*I2-l*I2
        r2=l*I2
        S3=S[i]+(h/2)*s2
        I3=I[i]+(h/2)*i2
        s3=-k*d*s*S3*I3
        i3=k*d*s*S3*I3-l*I3
        r3=l*I3
        S4=S[i]+h*s3
        I4=I[i]+h*i3
        s4=-k*d*s*S4*I4
        i4=k*d*s*S4*I4-l*I4
        r4=l*I4
        S[i+1]=S[i]+(h/6)*(s1+2*s2+2*s3+s4)
        I[i+1]=I[i]+(h/6)*(i1+2*i2+2*i3+i4)
        R[i+1]=R[i]+(h/6)*(r1+2*r2+2*r3+r4)
    X=linspace(0,x,N+1)
    ax=figure().gca()
    ax.set_ylim(0,1)
    ax.set_xlabel('t (ut)')
    ax.text(x*0.41,1.05,'S',color=(0,0,0.75),size=30)
    ax.text(x*0.5,1.05,'I',color=(0,0.5,0),size=30)
    ax.text(x*0.57,1.05,'R',color=(0.75,0,0),size=30)
    ax.plot(X,S,color=(0,0,0.75),linewidth=5)
    ax.plot(X,I,color=(0,0.5,0),linewidth=5)
    ax.plot(X,R,color=(0.75,0,0),linewidth=5)

def simple_impact(k,l,s,d,P,t,λ,μ,N,x) :
    d=d/1000000
    S=[1-1/P]+[0]*N
    I=[1/P]+[0]*N
    R=[0]*(N+1)
    Si=[1-1/P]+[0]*N
    Ii=[1/P]+[0]*N
    Ri=[0]*(N+1)
    h=x/N
    i=0
    while i<t/h :
        s1=-k*d*s*S[i]*I[i]
        i1=k*d*s*S[i]*I[i]-l*I[i]
        r1=l*I[i]
        S2=S[i]+(h/2)*s1
        I2=I[i]+(h/2)*i1
        s2=-k*d*s*S2*I2
        i2=k*d*s*S2*I2-l*I2
        r2=l*I2
        S3=S[i]+(h/2)*s2
        I3=I[i]+(h/2)*i2
        s3=-k*d*s*S3*I3
        i3=k*d*s*S3*I3-l*I3
        r3=l*I3
        S4=S[i]+h*s3
        I4=I[i]+h*i3
        s4=-k*d*s*S4*I4
        i4=k*d*s*S4*I4-l*I4
        r4=l*I4
        S[i+1]=S[i]+(h/6)*(s1+2*s2+2*s3+s4)
        I[i+1]=I[i]+(h/6)*(i1+2*i2+2*i3+i4)
        R[i+1]=R[i]+(h/6)*(r1+2*r2+2*r3+r4)
        Si[i+1]=S[i+1]
        Ii[i+1]=I[i+1]
        Ri[i+1]=R[i+1]
        i=i+1
    ki=k*(1-λ)
    li=l/(1-μ)
    while i<N :
        s1=-k*d*s*S[i]*I[i]
        i1=k*d*s*S[i]*I[i]-l*I[i]
        r1=l*I[i]
        S2=S[i]+(h/2)*s1
        I2=I[i]+(h/2)*i1
        s2=-k*d*s*S2*I2
        i2=k*d*s*S2*I2-l*I2
        r2=l*I2
        S3=S[i]+(h/2)*s2
        I3=I[i]+(h/2)*i2
        s3=-k*d*s*S3*I3
        i3=k*d*s*S3*I3-l*I3
        r3=l*I3
        S4=S[i]+h*s3
        I4=I[i]+h*i3
        s4=-k*d*s*S4*I4
        i4=k*d*s*S4*I4-l*I4
        r4=l*I4
        S[i+1]=S[i]+(h/6)*(s1+2*s2+2*s3+s4)
        I[i+1]=I[i]+(h/6)*(i1+2*i2+2*i3+i4)
        R[i+1]=R[i]+(h/6)*(r1+2*r2+2*r3+r4)
        s1=-ki*d*s*Si[i]*Ii[i]
        i1=ki*d*s*Si[i]*Ii[i]-li*Ii[i]
        r1=li*Ii[i]
        S2=Si[i]+(h/2)*s1
        I2=Ii[i]+(h/2)*i1
        s2=-ki*d*s*S2*I2
        i2=ki*d*s*S2*I2-li*I2
        r2=li*I2
        S3=Si[i]+(h/2)*s2
        I3=Ii[i]+(h/2)*i2
        s3=-ki*d*s*S3*I3
        i3=ki*d*s*S3*I3-li*I3
        r3=li*I3
        S4=Si[i]+h*s3
        I4=Ii[i]+h*i3
        s4=-ki*d*s*S4*I4
        i4=ki*d*s*S4*I4-li*I4
        r4=li*I4
        Si[i+1]=Si[i]+(h/6)*(s1+2*s2+2*s3+s4)
        Ii[i+1]=Ii[i]+(h/6)*(i1+2*i2+2*i3+i4)
        Ri[i+1]=Ri[i]+(h/6)*(r1+2*r2+2*r3+r4)
        i=i+1
    X=linspace(0,x,N+1)
    ax=figure().gca()
    ax.set_ylim(0,1)
    ax.set_xlabel('t (ut)')
    ax.text(x*0.24,1.05,'S',color=(0,0,0.75),size=30)
    ax.text(x*0.32,1.05,'I',color=(0,0.5,0),size=30)
    ax.text(x*0.38,1.05,'R',color=(0.75,0,0),size=30)
    ax.text(x*0.46,1.05,'Si',color=(0.8,0,1),size=30)
    ax.text(x*0.58,1.05,'Ii',color=(0,0,0),size=30)
    ax.text(x*0.68,1.05,'Ri',color=(1,0.7,0),size=30)
    ax.plot(X,Si,color=(0.8,0,1),linewidth=3)
    ax.plot(X,Ii,color=(0,0,0),linewidth=3)
    ax.plot(X,Ri,color=(1,0.7,0),linewidth=3)
    ax.plot(X,S,color=(0,0,0.75),linewidth=3)
    ax.plot(X,I,color=(0,0.5,0),linewidth=3)
    ax.plot(X,R,color=(0.75,0,0),linewidth=3)
    ax.plot([t,t],[0,1],color=(0,0,0),linewidth=2)

def simple_e(k,l,s,d,P,t,λ,μ,N,x) :
    d=d/1000000
    S=[1-1/P]+[0]*N
    I=[1/P]+[0]*N
    Si=[1-1/P]+[0]*N
    Ii=[1/P]+[0]*N
    h=x/N
    i=0
    while i<t/h :
        s1=-k*d*s*S[i]*I[i]
        i1=k*d*s*S[i]*I[i]-l*I[i]
        S2=S[i]+(h/2)*s1
        I2=I[i]+(h/2)*i1
        s2=-k*d*s*S2*I2
        i2=k*d*s*S2*I2-l*I2
        S3=S[i]+(h/2)*s2
        I3=I[i]+(h/2)*i2
        s3=-k*d*s*S3*I3
        i3=k*d*s*S3*I3-l*I3
        S4=S[i]+h*s3
        I4=I[i]+h*i3
        s4=-k*d*s*S4*I4
        i4=k*d*s*S4*I4-l*I4
        S[i+1]=S[i]+(h/6)*(s1+2*s2+2*s3+s4)
        I[i+1]=I[i]+(h/6)*(i1+2*i2+2*i3+i4)
        Si[i+1]=S[i+1]
        Ii[i+1]=I[i+1]
        i=i+1
    ki=k*(1-λ)
    li=l/(1-μ)
    while i<N :
        s1=-k*d*s*S[i]*I[i]
        i1=k*d*s*S[i]*I[i]-l*I[i]
        S2=S[i]+(h/2)*s1
        I2=I[i]+(h/2)*i1
        s2=-k*d*s*S2*I2
        i2=k*d*s*S2*I2-l*I2
        S3=S[i]+(h/2)*s2
        I3=I[i]+(h/2)*i2
        s3=-k*d*s*S3*I3
        i3=k*d*s*S3*I3-l*I3
        S4=S[i]+h*s3
        I4=I[i]+h*i3
        s4=-k*d*s*S4*I4
        i4=k*d*s*S4*I4-l*I4
        S[i+1]=S[i]+(h/6)*(s1+2*s2+2*s3+s4)
        I[i+1]=I[i]+(h/6)*(i1+2*i2+2*i3+i4)
        s1=-ki*d*s*Si[i]*Ii[i]
        i1=ki*d*s*Si[i]*Ii[i]-li*Ii[i]
        S2=Si[i]+(h/2)*s1
        I2=Ii[i]+(h/2)*i1
        s2=-ki*d*s*S2*I2
        i2=ki*d*s*S2*I2-li*I2
        S3=Si[i]+(h/2)*s2
        I3=Ii[i]+(h/2)*i2
        s3=-ki*d*s*S3*I3
        i3=ki*d*s*S3*I3-li*I3
        S4=Si[i]+h*s3
        I4=Ii[i]+h*i3
        s4=-ki*d*s*S4*I4
        i4=ki*d*s*S4*I4-li*I4
        Si[i+1]=Si[i]+(h/6)*(s1+2*s2+2*s3+s4)
        Ii[i+1]=Ii[i]+(h/6)*(i1+2*i2+2*i3+i4)
        i=i+1
    return(Si[N]-S[N])

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

def espace_adj(K,L,s,D,Id,Dm,T,N,x,N3,zlim) :
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
            S[N][i][j]=D[i][j]*S[N][i][j]
            I[N][i][j]=D[i][j]*I[N][i][j]
    n=len(T)
    for q in range(n) :
        p=int(T[q]/h)
        espace_sub(I,X,Y,p,h,N3,zlim)

def espace_uni(k,l,s,d,P,dm,T,N,x,N3,zlim) :
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
    for i in range(N3) :
        for j in range(N3) :
            X[N3*i+j]=u[i]
            Y[N3*i+j]=u[j]
            S[0][i][j]=1-I[0][i][j]
    for p in range(N) :
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
    for i in range(N3) :
        for j in range(N3) :
            S[N][i][j]=d*S[N][i][j]*1000000
            I[N][i][j]=d*I[N][i][j]*1000000
    n=len(T)
    for q in range(n) :
        p=int(T[q]/h)
        espace_sub(I,X,Y,p,h,N3,zlim)

def espace_adj_impact(K,L,s,D,Id,Dm,T,N,x,N3,t,λ,μ,Q,zlim) :
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
    n=len(T)
    for q in range(n) :
        if T[q]<=t :
            p=int(T[q]/h)
            espace_sub(I,X,Y,p,h,N3,zlim)
        else :
            p=int(T[q]/h)
            espace_sub_2(I,Ii,X,Y,p,h,N3,zlim)

def espace_sub_2(I,Ii,X,Y,p,h,N3,zlim) :
    Z=[0]*(N3**2)
    Zi=[0]*(N3**2)
    for i in range(N3) :
        for j in range(N3) :
            Z[N3*i+j]=I[p][i][j]
            Zi[N3*i+j]=Ii[p][i][j]
    fig=figure()
    ax=fig.gca(projection='3d')
    ax.set_zlim3d(0,zlim)
    ax.set_title('t='+(str(int(p*h*100)/100)+' ut'))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.text(N3*0.95,N3*0.75,zlim*1.2,'d(I) (hab/km²)',color=(0,0,0),size=12)
    ax.plot(X,Y,Zi,'o',color=(0,0.75,0))
    ax.plot(X,Y,Z,'o',color=(0,0,0.75))

def espace_uni_impact(k,l,s,d,P,dm,T,N,x,N3,t,λ,μ,Q,zlim) :
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
    n=len(T)
    for q in range(n) :
        if T[q]<=t :
            p=int(T[q]/h)
            espace_sub(I,X,Y,p,h,N3,zlim)
        else :
            p=int(T[q]/h)
            espace_sub_2(I,Ii,X,Y,p,h,N3,zlim)

def q(N3,p,r0) :
    Qres=[[0 for i in range(N3)] for j in range(N3)]
    N4=int(p*N3**2)
    R=[0 for i in range(N3**2)]
    a=int((N3-1)/2)
    for i in range(N3) :
        for j in range(N3) :
            R[i*N3+j]=[sqrt((i-a)**2+(j-a)**2),i,j]
    R2=tri(R)
    n=0
    while R2[n][0]<r0 :
        n=n+1
    if n>=N3**2-N4+1 :
        return(False)
    else :
        for m in range(n,n+N4) :
            i=R2[m][1]
            j=R2[m][2]
            Qres[i][j]=1
    return(Qres)

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

def espace_adj_t(K,L,s,D,Id,Dm,t,N,x,N3,zlim) :
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
        p=p+1
    for i in range(N3) :
        for j in range(N3) :
            S[p][i][j]=D[i][j]*S[p][i][j]
            I[p][i][j]=D[i][j]*I[p][i][j]
    return(S[p],I[p])

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

def dm(D,m) :
    N3=len(D)
    Dm=[[[[0 for i in range(N3)] for j in range(N3)] for t in range(N3)] for u in range(N3)]
    Dm[0][0][0][1]=m*max(D[0][0],D[0][1])
    Dm[0][0][1][0]=m*max(D[0][0],D[1][0])
    Dm[0][N3-1][1][N3-1]=m*max(D[0][N3-1],D[1][N3-1])
    Dm[N3-1][0][N3-1][1]=m*max(D[N3-1][0],D[N3-1][1])
    for j in range(1,N3-1) :
        Dm[0][j][0][j+1]=m*max(D[0][j],D[0][j+1])
        Dm[0][j][1][j]=m*max(D[0][j],D[1][j])
        Dm[N3-1][j][N3-1][j+1]=m*max(D[N3-1][j],D[N3-1][j+1])
    for i in range(1,N3-1) :
        Dm[i][0][i+1][0]=m*max(D[i][0],D[i+1][0])
        Dm[i][0][i][1]=m*max(D[i][0],D[i][1])
        Dm[i][N3-1][i+1][N3-1]=m*max(D[i][N3-1],D[i+1][N3-1])
    for i in range(1,N3-1) :
        for j in range(1,N3-1) :
            Dm[i][j][i+1][j]=m*max(D[i][j],D[i+1][j])
            Dm[i][j][i][j+1]=m*max(D[i][j],D[i][j+1])
    return(Dm)

def gauss_ex(A,B,C) :
    D=[[0 for i in range(41)] for j in range(41)]
    for i in range(41) :
        for j in range(41) :
            if j<15 :
                if i<12 :
                    D[i][j]=A*exp(-(((i-3)**2)/B)-(((j-7)**2)/B))+C
                elif i<29 :
                    D[i][j]=A*exp(-(((i-20)**2)/B)-(((j-7)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-37)**2)/B)-(((j-7)**2)/B))+C
            elif j<30 :
                if i<21 :
                    D[i][j]=A*exp(-(((i-12)**2)/B)-(((j-22)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-28)**2)/B)-(((j-22)**2)/B))+C
            else :
                if i<12 :
                    D[i][j]=A*exp(-(((i-3)**2)/B)-(((j-37)**2)/B))+C
                elif i<29 :
                    D[i][j]=A*exp(-(((i-20)**2)/B)-(((j-37)**2)/B))+C
                else :
                    D[i][j]=A*exp(-(((i-37)**2)/B)-(((j-37)**2)/B))+C
    return(D)

def tri(R) :
    n=len(R)
    if n==1 :
        return(R)
    else :
        a=int((n+1)/2)
        A=R[:a]
        B=R[a:]
        A2=tri(A)
        B2=tri(B)
        C=[]
        p=0
        q=0
        for i in range(n) :
            if p==a :
                C=C+[B2[q]]
                q=q+1
            elif q==n-a :
                C=C+[A2[p]]
                p=p+1
            else :
                u=A2[p][0]
                v=B2[q][0]
                if u<=v :
                    C=C+[A2[p]]
                    p=p+1
                else :
                    C=C+[B2[q]]
                    q=q+1
        return(C)