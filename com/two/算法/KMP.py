def prefix_table(pattern,n):
    prefix=[0 for i in range(n)]
    l=0
    i=1
    while(i<n):
        if(pattern[i]==pattern[l]):
            l+=1
            prefix[i]=l
            i+=1
        else:
            if(l>0):
                l=prefix[l-1]
            else:
                prefix[i]=0
                i+=1
    return prefix
pattern='ABABCABAA'
prefix=prefix_table(pattern, len(pattern))
for i in range(8,0,-1):
    prefix[i]=prefix[i-1]
prefix[0]=-1
for i in prefix:
    print(i)
