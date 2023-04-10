t = int(input());i=0;
while i < t:
    x, y = map(int, input().split())
    print(f"Case #{i+1}: {x} + {y} = {x+y}")
    i += 1