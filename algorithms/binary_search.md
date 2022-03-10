# Binary Search

### Required presorted array

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
