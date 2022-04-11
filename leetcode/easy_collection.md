# Questions - Easy Collection

## Index
1. Arrays
2. Strings
3. LinkedLists
4. Trees
5. Sorting & Searching
6. Dynamic Programming
7. Design
8. Math

## 1. Arrays

```python
# Remove Duplicates from an array
 def removeDuplicates(nums: List[int]) -> int:
        prev = nums[0]
        for curr in nums[1:][:]:
            if curr == prev:
                nums.remove(curr)
            else:
                prev = curr
        return len(nums)
```

