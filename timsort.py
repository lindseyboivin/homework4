# Python3 program to perform basic timSort 
# TimSort implementation taken from this source: https://www.geeksforgeeks.org/timsort/
import copy
from datetime import datetime, date

  
# This function sorts array from left index to 
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1
  
  
# Merge function merges the sorted runs 
def merge(arr, l, m, r): 
      
    # original array is broken in two parts 
    # left and right array 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[l + i]) 
    for i in range(0, len2): 
        right.append(arr[m + 1 + i]) 
  
    i, j, k = 0, 0, l 
      
    # after comparing, we merge those two array 
    # in larger sub array 
    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
  
        else: 
            arr[k] = right[j] 
            j += 1
  
        k += 1
  
    # Copy remaining elements of left, if any 
    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1
  
    # Copy remaining element of right, if any 
    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1
  
  
# Iterative Timsort function to sort the 
# array[0...n-1] (similar to merge sort) 
def timSort(arr,minRun): 
    n = len(arr) 
      
    # Sort individual subarrays of size RUN 
    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 
  
    # Start merging from size RUN (or 32). It will merge 
    # to form size 64, then 128, 256 and so on .... 
    size = minRun 
    while size < n: 
          
        # Pick starting point of left sub array. We 
        # are going to merge arr[left..left+size-1] 
        # and arr[left+size, left+2*size-1] 
        # After every merge, we increase left by 2*size 
        for left in range(0, n, 2 * size): 
  
            # Find ending point of left sub array 
            # mid+1 is starting point of right sub array 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
  
            # Merge sub array arr[left.....mid] & 
            # arr[mid+1....right] 
            merge(arr, left, mid, right) 
  
        size = 2 * size


thouArr60 = [996,402,981,5,78,191,233,764,43,534,678,267,556,711,926,433,108,680,84,125,39,615,472,836,452,296,873,247,326,2,439,738,579,988,743,156,767,604,403,620,303,634,572,256,684,761,847,865,180,118,618,544,88,742,856,749,222,456,994,861,479,241,454,664,672,334,626,427,977,232,98,26,538,839,518,138,358,62,101,782,485,670,574,821,843,48,983,497,94,614,912,471,258,49,752,758,737,91,15,778,291,772,261,872,573,855,430,275,858,944,820,406,353,729,824,669,922,668,514,36,503,837,515,80,978,637,862,720,557,469,226,935,844,142,893,607,268,554,37,320,501,815,622,461,276,458,68,419,418,182,625,423,205,895,531,539,253,507,243,536,245,431,798,568,522,306,386,438,794,955,931,208,804,134,310,8,805,813,848,657,936,349,313,197,47,12,529,645,393,914,340,371,115,195,455,780,278,244,899,773,779,765,508,716,185,590,654,435,775,164,444,184,322,304,473,571,901,640,113,631,624,987,736,541,537,139,530,481,357,343,367,869,816,187,565,259,682,240,653,950,968,19,466,11,877,628,802,905,532,426,721,356,7,273,235,141,199,120,576,525,666,592,361,857,665,505,293,552,44,57,355,906,224,436,389,394,606,511,188,348,152,428,548,564,808,885,945,697,759,589,70,159,883,67,459,777,801,221,175,449,806,841,173,596,513,133,655,984,679,363,750,781,274,719,972,714,198,342,372,167,519,104,829,122,642,404,111,760,526,211,272,859,725,305,792,842,223,41,854,168,287,976,318,85,336,16,840,54,149,17,612,344,603,381,953,681,170,269,900,826,561,486,962,63,189,225,663,980,763,648,708,685,140,875,520,215,674,903,594,845,728,683,61,425,506,540,179,789,319,132,161,150,264,693,608,569,487,502,106,366,409,702,964,597,602,629,493,294,102,793,24,58,301,510,292,124,986,229,577,401,583,341,915,77,768,333,280,204,351,521,698,956,154,957,754,492,451,695,496,277,868,315,480,704,811,549,851,924,165,76,783,918,176,302,992,585,300,399,748,745,727,690,429,365,392,595,866,878,368,71,109,619,218,160,93,51,740,919,42,129,385,441,973,934,925,908,575,13,827,887,242,20,920,390,248,66,822,863,627,443,92,434,605,787,27,377,335,948,864,591,699,688,488,3,388,283,884,546,686,46,414,468,398,74,31,400,705,53,644,896,52,967,239,744,500,923,483,345,959,974,586,850,217,660,982,894,667,907,136,45,73,65,741,807,214,470,34,790,4,747,943,871,491,144,888,643,819,279,360,131,933,616,307,216,410,14,852,623,545,838,282,796,230,40,312,652,123,332,774,611,891,810,563,405,328,251,965,178,833,183,658,69,50,647,257,162,271,314,881,621,96,710,732,97,464,566,424,23,989,407,145,755,89,995,338,59,56,495,609,581,416,932,656,692,1000,25,477,832,157,600,975,599,1,791,963,354,22,174,797,203,567,731,701,712,117,99,90,651,83,10,28,298,130,904,231,309,776,396,846,420,30,266,359,726,81,512,116,114,941,876,453,324,902,547,103,153,886,148,771,550,689,137,143,252,713,709,676,374,489,952,172,254,265,735,397,127,379,448,700,898,694,946,373,9,38,677,633,200,33,325,971,879,64,559,194,193,490,970,938,516,593,542,890,942,158,661,369,474,717,835,339,570,376,739,206,408,598,462,32,562,387,382,551,560,800,786,484,151,753,691,432,421,347,849,769,917,86,295,494,237,169,412,751,147,803,766,814,442,171,227,119,447,960,236,535,757,213,897,649,281,346,105,112,860,478,18,889,100,331,55,954,255,659,909,463,558,985,87,722,391,181,734,234,457,285,110,60,979,228,533,460,262,210,630,527,504,580,498,756,588,991,378,422,415,784,638,553,72,610,817,799,146,632,29,523,834,910,812,639,927,582,509,75,21,155,524,270,6,951,880,966,212,999,95,177,380,587,617,785,219,939,79,723,329,209,411,762,517,913,166,795,867,928,465,958,317,601,417,687,641,297,940,703,990,284,650,202,299,916,578,220,327,636,250,993,706,249,947,555,892,290,882,384,613,528,911,128,107,730,330,370,870,823,853,788,828,289,316,383,35,746,969,724,831,192,440,997,499,311,718,163,350,186,437,635,584,671,190,770,321,825,337,413,937,673,375,323,707,543,696,646,818,482,238,260,352,196,445,450,201,286,475,998,263,921,121,476,288,874,126,246,467,308,82,809,675,135,362,949,733,446,364,662,930,830,929,207,961,715,395]

thouArr1 = copy.deepcopy(thouArr60)
thouArr20 = copy.deepcopy(thouArr60)
thouArr40 = copy.deepcopy(thouArr60)
thouArr80 = copy.deepcopy(thouArr60)
thouArr100 = copy.deepcopy(thouArr60)
thouArr120 = copy.deepcopy(thouArr60)
thouArr140 = copy.deepcopy(thouArr60)
thouArr160 = copy.deepcopy(thouArr60)

# Testing k = 1
beforeTime = datetime.now().time()

timSort(thouArr1,1)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 1: ", totalTime)


# Testing k = 20
beforeTime = datetime.now().time()

timSort(thouArr20,20)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 20: ", totalTime)

# Testing k = 40
beforeTime = datetime.now().time()

timSort(thouArr40,40)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 40: ", totalTime)


# Testing k = 60
beforeTime = datetime.now().time()

timSort(thouArr60,60)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 60: ", totalTime)

# Testing k = 80
beforeTime = datetime.now().time()

timSort(thouArr80,80)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 80: ", totalTime)

# Testing k = 100
beforeTime = datetime.now().time()

timSort(thouArr100,100)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 100: ", totalTime)

# Testing k = 120
beforeTime = datetime.now().time()

timSort(thouArr120,120)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 120: ", totalTime)

# Testing k = 140
beforeTime = datetime.now().time()

timSort(thouArr140,140)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 140: ", totalTime)

# Testing k = 160
beforeTime = datetime.now().time()

timSort(thouArr160,160)

afterTime = datetime.now().time()

totalTime = str(datetime.combine(date.min, afterTime) - datetime.combine(date.min, beforeTime))

print ("Duration of tim sort k = 160: ", totalTime)

