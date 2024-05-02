# Note: this only output the expect hash in PyPy 3
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))    
    