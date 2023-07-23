def modArray(array,base):
    res=0
    for i in range(len(array)):
        res=(res*10+array[i])%base
    return res

array=list(map(int, input().split()))
base=int(input())
print(modArray(array,base))