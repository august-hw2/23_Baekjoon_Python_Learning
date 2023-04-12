h, m, s = map(int, input().split()); d=int(input())
re_h = d//3600; re_m = d%3600//60; re_s = d%3600%60
h+=re_h; m+=re_m; s+=re_s
if s > 59: s -= 60; m+=1
if m > 59: m -= 60; h+=1
print(f"{h%24} {m} {s}")