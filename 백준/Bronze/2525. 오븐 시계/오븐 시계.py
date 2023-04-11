h, m = map(int, input().split()); user=int(input())
m += user;
re_h = m // 60; m = m % 60
if(h + re_h > 23):
    h = h+re_h - 24
else:
    h += re_h
print(h, m)