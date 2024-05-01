def swap_case(s):    
    arr = [char.lower() if char.isupper() else char.upper() for char in s]
    return "".join(arr)       
      
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
   
