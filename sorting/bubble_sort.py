"""compare the element with the adjacent element and swap it . 
at the end of a single iteration last element of the array will be sorted"""

def bubble_sort(arr:list):
    n=len(arr)
    

    for i in range(n):

        for j in range(n-1-i):

            if arr[j] > arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[12,3,45,123,34,2145,1,2]
bubble_sort(arr)
print(arr)