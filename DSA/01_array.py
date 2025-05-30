# Array is a module {array.py}
# we can "import array" but we need to do (array.__) to access
from array import *
array1=array("i",[1,2,3,4])
for i in array1:
  print(i)
for i in range(4):
  print(array1[i],end="")
print("")
#mutable
array1[0]=9
#append
array1.append(20)
print(array1)

#count
print(array1.count(1))

#extend
array1.extend([21,22,23,24])
print(array1)

#fromList
array1.fromlist([45,46,47])
print(array1)

#index
print(array1.index(24))

#pop
print(array1.pop())
print(array1)

#insert
array1.insert(12,48)
print(array1)

#remove
print(array1.remove(48))
print(array1)

#reverse
print(array1.reverse())
print(array1)

#tolist
print(array1.tolist())