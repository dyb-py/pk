#1 选 或  不选

arr = [1,2,4,1,7,8,3]

def rec_opt(arr,i):
    if i==0:
        return arr[00]
    elif i==1:
        return max(arr[0],arr[1])
    else:
        A = arr[i]+rec_opt(arr,i-2)
        B =rec_opt(arr,i-1)
        return max(A,B)


def opt(arr):
    o=[0 for i in range(len(arr))]
    o[0]=arr[0]
    o[1]=arr[1]
    for i in range(2,len(arr)):
        A=arr[i]+o[i-2]
        B=o[i-1]
        o[i]=max(A,B)
    return o[len(arr)-1]
# print(rec_opt(arr,6))

# print(opt(arr))


