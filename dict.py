from datetime import datetime, date
# Binary tree implementation provided by this source: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
# Python program to insert element in binary tree 
class newNode(): 
 
    def __init__(self, data): 
        self.key = data
        self.left = None
        self.right = None
         
""" Inorder traversal of a binary tree"""
def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left) 
    print(temp.key,end = " ")
    inorder(temp.right) 
 
 
"""function to insert element in binary tree """
def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = [] 
    q.append(temp) 
 
    # Do level order traversal until we find 
    # an empty place. 
    while (len(q)): 
        temp = q[0] 
        q.pop(0) 
 
        if (not temp.left):
            temp.left = newNode(key) 
            break
        else:
            q.append(temp.left) 
 
        if (not temp.right):
            temp.right = newNode(key) 
            break
        else:
            q.append(temp.right) 
     

root = newNode(-10) 
root.left = newNode(-11) 
root.left.left = newNode(-7) 
root.right = newNode(-9) 
root.right.left = newNode(-15) 
root.right.right = newNode(-8)  

hashDict = dict()
hashDict[-10] = -10
hashDict[-11] = -11
hashDict[-7] = -7
hashDict[-9] = -9
hashDict[-15] = -15
hashDict[-8] = -8

###### TESTING BINARY TREE ########
## Testing n = 10
beforeTime = datetime.now().time()

for i in range(10):
    insert(root,i)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of binary tree insertion n = 10: ", totalTime)


## Testing n = 100
beforeTime = datetime.now().time()

for i in range(10,110):
    insert(root,i)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of binary tree insertion n = 100: ", totalTime)  


## Testing n = 1,000
beforeTime = datetime.now().time()

for i in range(110,1110):
    insert(root,i)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of binary tree insertion n = 1,000: ", totalTime)


## Testing n = 10,000
beforeTime = datetime.now().time()


for i in range(1110,11110):
    insert(root,i)


afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of binary tree insertion n = 10,000: ", totalTime)






############## TESTING HASH TABLE ####################
## Testing n = 10
beforeTime = datetime.now().time()

for i in range(10):
    hashDict[i] = i

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of hash table insertion n = 10: ", totalTime)


## Testing n = 100
beforeTime = datetime.now().time()

for i in range(10,110):
    hashDict[i] = i

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of hash table insertion n = 100: ", totalTime)  


## Testing n = 1,000
beforeTime = datetime.now().time()

for i in range(110,1110):
    hashDict[i] = i

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of hash table insertion n = 1,000: ", totalTime)


## Testing n = 10,000
beforeTime = datetime.now().time()

for i in range(1110,11110):
    hashDict[i] = i

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of hash table insertion n = 10,000: ", totalTime)