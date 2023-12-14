"""insert sort is like sorting the playing card 
starts with the second element check through the left side of the array and swap it"""


def inserion_sort(arr:list):
    n=len(arr)
    for i in range(1,n):
        
        
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key




arr=[12,3,45,123,34,2145,1,2]
inserion_sort(arr)
print(arr)