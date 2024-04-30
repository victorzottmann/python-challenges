if __name__ == '__main__':
    N = int(input())
    arr = []
  
    for _ in range(N):
        args = input().split()
        command = args[0]
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