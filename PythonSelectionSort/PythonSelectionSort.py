import sys

def selectionSort(nums):
    for i,n in enumerate(nums):
        mn = min(range(i,len(nums)), key=nums.__getitem__)
        nums[i], nums[mn] = nums[mn], n

def binarySearch(lst,item,start,end):
    if(start == end):
        if(lst[start] > item):
            return start
        else:
            return start + 1
    if(start > end):
        return start
    mid = (start + end) // 2
    if(lst[mid] < item):
        return binarySearch(lst,item,mid+1,end)
    elif(lst[mid] > item):
        return binarySearch(lst,item,start,mid-1)
    else:
        return mid

def insertionSort(lst):
    length = len(lst)
    for index in range(1,length):
        value = lst[index]
        pos = binarySearch(lst,value,0,index-1)
        lst = lst[:pos] + [value] + lst[pos:index] + lst[index+1:]
    return lst

def merge(left,right):
    if(not left):
        return right
    if(not right):
        return left
    if(left[0] < right[0]):
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left,right[1:])

def timeSort(lst):
    runs,sortedRuns = [],[]
    length = len(lst)
    newRun = [lst[0]]
    sortedArray = []
    for i in range(1,length):
        if(i == length - 1):
            newRun.append(lst[i])
            runs.append(newRun)
            break
        if(lst[i] < lst[i-1]):
            if(not newRun):
                runs.append([lst[i-1]])
                newRun.append(lst[i])
            else:
                runs.append(newRun)
                newRun = []
        else:
            newRun.append(lst[i])
    for run in runs:
        sortedRuns.append(insertionSort(run))
    for run in sortedRuns:
        sortedarray = merge(sortedArray,run)
    return sortedArray


































