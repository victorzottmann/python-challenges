# sWAP cASE - Strings

## Problem
The objective of this challenge is to swap the cases of a string. For example, if you input "HellO woRLD!", it should return hELLo WOrld!

## Solution
Based on the initial structure for this challenge:
```python
def swap_case(s):
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```
What we need to do is split the string by characters (including spaces), check whether or not each character is either capitalized, apply the corresponding operations to each one of them, and then join the array to create a new string and return it.

Initially, I went with a simple `for loop` to have a better idea of what was going on, and then converted it into a `list comprehension` purely for practice purposes.

### Solution with `For Loop`
```python
def swap_case(s):
    arr = []
    for char in s:
        if char.isupper():
            arr.append(char.lower())
        else:
            arr.append(char.upper())
    result = "".join(arr)
    return result
```

### Solution with `List Comprehension`
```python
def swap_case(s):
    arr = [char.lower() if char.isupper() else char.upper() for char in s]
    return "".join(arr)
```
This essentially reads as `a if condition else b`. In other words, convert to lower case if the character is upper cased, otherwise if the character is lower cased, convert it to upper case, for every character in the string `s`.

