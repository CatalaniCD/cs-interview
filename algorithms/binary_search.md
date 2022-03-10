# Binary Search

### Required presorted array

**Implementation 1**

```python

def binary_search(elem, low, high):
    
    mid = ((high - low) // 2) + low  
    
    if array[mid] == elem: 
        print(f'Found : {elem}')
        return mid    
    
    elif (high - low) == 1:
        print(f'Not Found : {elem}')
        return None
   
    elif elem < array[mid]:
        return binary_search(elem, low, mid)
    
    elif elem > array[mid]:
        return binary_search(elem, mid, high)
  ```
  
**Implementation 2**

```python
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)
```

**Iterative Implementation**

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
```
