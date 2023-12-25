def perm3(s1):
    i=0
    list1=[]
    list1.append(s1[i]+s1[i+1]+s1[i+2])
    list1.append(s1[i]+s1[i+2]+s1[i+1])
    list1.append(s1[i+1]+s1[i]+s1[i+2])
    list1.append(s1[i+1]+s1[i+2]+s1[i])
    list1.append(s1[i+2]+s1[i]+s1[i+1])
    list1.append(s1[::-1])
    return list1
print(perm3("EAT"))




