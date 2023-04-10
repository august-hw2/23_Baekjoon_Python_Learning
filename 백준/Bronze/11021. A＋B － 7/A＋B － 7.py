t = int(input())
arr=[[*map(int, input().split())] for _ in range(t)]
i=0
while i < len(arr):
    x, y = arr[i]
    print(f"Case #{i+1}: {x+y}")
    i += 1