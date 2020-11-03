from datetime import datetime, date

# Python program for implementation of MergeSort
# Function below taken from this source: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

# Function to do insertion sort 
# Function below taken from this source: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key



hundredArr1 = [15,99,24,9,70,17,49,64,71,12,5,94,26,90,75,52,56,76,61,3,10,11,51,43,82,36,31,68,47,4,85,45,60,89,38,22,1,46,19,44,37,91,23,88,69,14,81,30,13,79,93,98,53,40,18,96,42,34,2,83,48,6,92,57,7,97,39,55,67,27,29,100,78,28,74,66,50,21,41,95,86,87,65,35,77,80,32,62,8,16,58,33,73,84,25,63,59,20,72,54]
hundredArr2 = [15,99,24,9,70,17,49,64,71,12,5,94,26,90,75,52,56,76,61,3,10,11,51,43,82,36,31,68,47,4,85,45,60,89,38,22,1,46,19,44,37,91,23,88,69,14,81,30,13,79,93,98,53,40,18,96,42,34,2,83,48,6,92,57,7,97,39,55,67,27,29,100,78,28,74,66,50,21,41,95,86,87,65,35,77,80,32,62,8,16,58,33,73,84,25,63,59,20,72,54]
tenArr1 = [3,9,2,1,7,5,4,10,8,6]
tenArr2 = [3,9,2,1,7,5,4,10,8,6]
fiveArr1 = [1,5,3,4,2]
fiveArr2 = [1,5,3,4,2]
oneArr1 = [1]
oneArr2 = [1]
zeroArr1 = []
zeroArr2 = []

#### TESTING N = 100 ####
# Testing merge n = 100

beforeTime = datetime.now().time()

mergeSort(hundredArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 100: ", totalTime)

# Testing insertion n = 100

beforeTime = datetime.now().time()

insertionSort(hundredArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 100: ", totalTime)

print()

#### TESTING N = 10 ####
# Testing merge n = 10

beforeTime = datetime.now().time()

mergeSort(tenArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 10: ", totalTime)

# Testing insertion n = 10

beforeTime = datetime.now().time()

insertionSort(tenArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of insertion sort n = 10: ", totalTime)
print()

#### TESTING N = 5 ####
# Testing merge n = 5

beforeTime = datetime.now().time()

mergeSort(fiveArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 5: ", totalTime)

# Testing insertion n = 5

beforeTime = datetime.now().time()

insertionSort(fiveArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 5: ", totalTime)

print()

#### TESTING N = 1 ####
# Testing merge n = 1

beforeTime = datetime.now().time()

mergeSort(oneArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 1: ", totalTime)

# Testing insertion n = 1

beforeTime = datetime.now().time()

insertionSort(oneArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 1: ", totalTime)
print()

#### TESTING N = 0 ####
# Testing merge n = 0

beforeTime = datetime.now().time()

mergeSort(zeroArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 0: ", totalTime)

# Testing insertion n = 0

beforeTime = datetime.now().time()

insertionSort(zeroArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 0: ", totalTime)

print()