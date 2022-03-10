# Python3 code to Check for 
## balanced parentheses in an expression

**Implementation 1**

```python
def check(expression):
      
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []
  
    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"
  
# Driver code
string = "{[]{()}}"
print(string, "-", check(string))
  
string = "((()"
print(string,"-",check(string)
```

**Implementation 2**

```python
open_list = ["[","{","("]
close_list = ["]","}",")"]
  
# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
# Driver code
string = "{[]{()}}"
print(string,"-", check(string))
  
string = "[{}{})(]"
print(string,"-", check(string))
  
string = "((()"
print(string,"-",check(string))
```

### Source 

[**Mathing Parenthesis**](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/)
