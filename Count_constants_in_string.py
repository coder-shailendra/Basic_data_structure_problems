text = "hello world"
consonants = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z"
count = 0

for ch in text:
    if ch in consonants:
        count += 1

print("Number of consonants:", count)