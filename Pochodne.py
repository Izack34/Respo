def HornerPochodne(n,A,c):
    i=A[0]
    tab=[]
    for x in range(1,len(A)):
        tab.append(i)
        i=c*i+A[x]
        
    return [n-1,tab,i]
    
def HornerPochodne_k(n,A,c,k):
    i=A[0]
    tab=[]
    
    for x in range(1,len(A)):
        tab.append(i)
        i=c*i+A[x]
        
    if k == 0:
        return i
    if k == 1:
        return [n-1,tab,i]
    
    
    return HornerPochodne_k(n-1,tab,c,k-1)


def HornerPochodneOdwrotne(n,A,c):
    i=A[-1]
    tab=[]
    for x in range(2,n+1):        
        tab.append(i)
        i=c*i+A[-x]
        
    return [n-1,tab,i]


def HornerPochodne_kOdwrotne(n,A,c,k):
    i=A[-1]
    tab=[]
    for x in range(2,n+1):
        tab.append(i)
        i=c*i+A[-x]
        
    if k == 0:
        return i
    if k == 1:
        return [n-1,tab,i]
    
    
    return HornerPochodne_k(n-1,tab,c,k-1)
