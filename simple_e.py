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