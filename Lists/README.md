# Lists - Basic Data Types

## Problem
Considering a an empty list, (`arr = []`), this challenge asks you to read an integer value `N` from input, followed by `N` lines of commands, where each command should perform their corresponding operation. Note that the very first value read from input is the number of commands itself.

Here is an overview of the commands, where `i` is the index of the list, and `e` is the element

1. `insert i e`
2. `print`
3. `remove e`
4. `append e`
5. `sort`
6. `pop`
7. `reverse`

## Solution
```python
if __name__ == '__main__':
    # 1. Assign the input value to `N` as an int, and declare an empty list.
    N = int(input())
    arr = []
    # 2. Loop from 0 to N and create a list with all the arguments
    for _ in range(N):
        args = input().split()
        command = args[0]
    # 3. Perform the corresponding operation for each command type. 
    # Note that match...case was only introduced in Python 3.10. Alternatively, you can use if...else and produce the same result.
        match command:
            case 'insert':
                arr.insert(int(args[1]), int(args[2]))
            case 'print':
                print(arr)
            case 'remove':
                arr.remove(int(args[1]))
            case 'append':
                arr.append(int(args[1]))
            case 'sort':
                arr.sort()
            case 'pop':
                arr.pop()
            case 'reverse':
                arr.reverse()
```

## How to run
- Clone this repository
- Run `python3 lists.py` to run the script
- Then follow a similar structure to this
  - $ 3
  - $ insert 0 5
  - $ insert 1 8
  - $ print