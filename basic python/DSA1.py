def move_zeros(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr=arr[:i]+arr[i+1:]
            arr.append(0)
    return arr
  
print(move_zeros([0,1,0,3,12]))
print(move_zeros([0]))
