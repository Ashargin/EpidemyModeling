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