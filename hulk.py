n=int(input())
s=""
for i in range(1,n+1):
    if i!=1:
        s+="that "
    if i%2==0:
        s+="I love "
    if i%2!=0:
        s+="I hate "
s+="it "
print(s)
