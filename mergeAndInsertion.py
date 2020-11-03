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

onesevenfiveArr1 = [55,36,72,164,111,57,168,73,89,23,38,162,13,149,138,75,106,156,143,113,110,70,174,25,47,108,76,37,145,165,169,77,140,97,79,39,5,102,175,10,12,120,17,45,56,95,20,74,161,90,126,127,116,83,152,68,98,69,173,157,84,8,64,81,26,160,137,40,87,60,9,94,146,105,59,32,86,65,123,135,18,125,109,144,115,101,124,34,22,42,11,78,52,88,155,31,3,122,30,66,147,24,14,142,119,107,1,28,130,27,129,21,154,53,167,96,80,29,51,133,16,54,71,100,15,150,153,114,35,158,159,33,63,104,85,19,49,58,6,136,61,7,4,128,103,172,48,171,112,46,43,50,82,99,163,131,132,92,91,134,117,93,148,67,121,141,62,41,44,151,170,118,2,166,139]
onesevenfiveArr2 = [55,36,72,164,111,57,168,73,89,23,38,162,13,149,138,75,106,156,143,113,110,70,174,25,47,108,76,37,145,165,169,77,140,97,79,39,5,102,175,10,12,120,17,45,56,95,20,74,161,90,126,127,116,83,152,68,98,69,173,157,84,8,64,81,26,160,137,40,87,60,9,94,146,105,59,32,86,65,123,135,18,125,109,144,115,101,124,34,22,42,11,78,52,88,155,31,3,122,30,66,147,24,14,142,119,107,1,28,130,27,129,21,154,53,167,96,80,29,51,133,16,54,71,100,15,150,153,114,35,158,159,33,63,104,85,19,49,58,6,136,61,7,4,128,103,172,48,171,112,46,43,50,82,99,163,131,132,92,91,134,117,93,148,67,121,141,62,41,44,151,170,118,2,166,139]

onetwofiveArr1 = [106,113,124,98,58,115,82,105,27,42,114,33,66,76,125,49,8,116,28,41,29,87,93,5,86,68,6,45,96,71,50,121,97,122,40,38,99,59,79,73,92,83,91,62,25,12,60,31,46,112,39,15,32,117,3,56,74,77,95,48,100,72,65,19,111,69,47,107,13,120,118,119,101,109,16,57,22,2,30,78,81,123,52,84,44,35,54,85,26,24,10,53,21,102,7,4,63,75,70,9,61,108,89,23,18,43,36,20,67,103,110,1,90,80,17,94,37,88,11,34,64,51,104,14,55]
onetwofiveArr2 = [106,113,124,98,58,115,82,105,27,42,114,33,66,76,125,49,8,116,28,41,29,87,93,5,86,68,6,45,96,71,50,121,97,122,40,38,99,59,79,73,92,83,91,62,25,12,60,31,46,112,39,15,32,117,3,56,74,77,95,48,100,72,65,19,111,69,47,107,13,120,118,119,101,109,16,57,22,2,30,78,81,123,52,84,44,35,54,85,26,24,10,53,21,102,7,4,63,75,70,9,61,108,89,23,18,43,36,20,67,103,110,1,90,80,17,94,37,88,11,34,64,51,104,14,55]

onetenArr1 = [79,60,22,59,8,84,101,40,104,46,100,20,56,27,90,86,95,23,37,89,4,77,16,9,10,28,88,98,33,69,39,2,76,49,75,11,34,94,50,68,97,52,105,47,15,53,71,73,65,44,81,91,83,54,109,1,35,74,58,48,57,30,70,80,66,99,26,7,110,13,85,51,5,24,72,64,32,25,21,106,19,41,17,102,82,45,67,61,93,96,107,78,31,103,62,108,14,3,43,6,92,36,55,87,42,18,29,38,12,63]
onetenArr2 = [79,60,22,59,8,84,101,40,104,46,100,20,56,27,90,86,95,23,37,89,4,77,16,9,10,28,88,98,33,69,39,2,76,49,75,11,34,94,50,68,97,52,105,47,15,53,71,73,65,44,81,91,83,54,109,1,35,74,58,48,57,30,70,80,66,99,26,7,110,13,85,51,5,24,72,64,32,25,21,106,19,41,17,102,82,45,67,61,93,96,107,78,31,103,62,108,14,3,43,6,92,36,55,87,42,18,29,38,12,63]

hundredArr1 = [15,99,24,9,70,17,49,64,71,12,5,94,26,90,75,52,56,76,61,3,10,11,51,43,82,36,31,68,47,4,85,45,60,89,38,22,1,46,19,44,37,91,23,88,69,14,81,30,13,79,93,98,53,40,18,96,42,34,2,83,48,6,92,57,7,97,39,55,67,27,29,100,78,28,74,66,50,21,41,95,86,87,65,35,77,80,32,62,8,16,58,33,73,84,25,63,59,20,72,54]
hundredArr2 = [15,99,24,9,70,17,49,64,71,12,5,94,26,90,75,52,56,76,61,3,10,11,51,43,82,36,31,68,47,4,85,45,60,89,38,22,1,46,19,44,37,91,23,88,69,14,81,30,13,79,93,98,53,40,18,96,42,34,2,83,48,6,92,57,7,97,39,55,67,27,29,100,78,28,74,66,50,21,41,95,86,87,65,35,77,80,32,62,8,16,58,33,73,84,25,63,59,20,72,54]
tenArr1 = [3,9,2,1,7,5,4,10,8,6]
tenArr2 = [3,9,2,1,7,5,4,10,8,6]

print()


#### TESTING N = 175 ####
# Testing merge n = 175

beforeTime = datetime.now().time()

mergeSort(onesevenfiveArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 175: ", totalTime)

# Testing insertion n = 175

beforeTime = datetime.now().time()

insertionSort(onesevenfiveArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 175: ", totalTime)

print()

#### TESTING N = 125 ####
# Testing merge n = 125

beforeTime = datetime.now().time()

mergeSort(onetwofiveArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 125: ", totalTime)

# Testing insertion n = 125

beforeTime = datetime.now().time()

insertionSort(onetwofiveArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 125: ", totalTime)

print()

#### TESTING N = 110 ####
# Testing merge n = 110

beforeTime = datetime.now().time()

mergeSort(onetenArr1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of merge sort n = 110: ", totalTime)

# Testing insertion n = 110

beforeTime = datetime.now().time()

insertionSort(onetenArr2)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print("Duration of insertion sort n = 110: ", totalTime)

print()

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