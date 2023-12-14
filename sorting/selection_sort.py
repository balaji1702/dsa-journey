
"""selects the minimum element and swap to the first value after the sorted one """

def selection_sort(arr:list):

    for i in range(len(arr)):

        min_idx=i
        for j in range(i+1,len(arr)):

            if arr[j] < arr[min_idx]:
                min_idx=j
        
        arr[i],arr[min_idx]=arr[min_idx],arr[i]


arr=[1,32,45,12,1,34,112,12]
selection_sort(arr)

print(arr)


