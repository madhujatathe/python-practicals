import array
arr = array.array('i',[1,2,3])
print("original array: ",arr)
#original array: array('i',[1,2,3])
arr.append(4)
print("array after append update: ",arr)
#array after append update: array('i',l[1,2,3,4])
arr.insert(4,5)
print("array after insert update: ",arr)
#array after insert update: array('i',[1,2,3,4,5])
arr[1]=0
print("array after index update: ",arr)
#array after index update: array ('i',[1,0,3,4,5])
arr.pop(1)  #0
print("array after pop: ",arr)
#array after index update: array ('i',[1,3,4,5])
arr.remove(4)
print("array after remove: ",arr)
#array after remove: array('i',[1,3,5])
len(arr)   #3
print(len(arr))
print(arr.index(3))  #1
arr.reverse()
print("array after reverse: ",arr)
#array after reverse: array('i',[5,3,1])
