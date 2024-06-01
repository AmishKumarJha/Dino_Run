def gcd(m,n):
    print("called")
    (a,b)=(max(m,n),min(m,n))
    if a%b==0:
        return(b)
    else:
        return(gcd(b,a%b))
print(gcd(24,130))