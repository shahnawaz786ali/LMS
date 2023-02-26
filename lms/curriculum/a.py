a=[(1,6),(2,7),(3,6),(4,8),(5,6)]

b=dict(a)
print(b)
c={}

for i in a:
    if i[0] not in c:
        c[i[1]]=[i[0]]
    else:
       c[i[1]].append(i[0])        
print(c)
    
    