#!/usr/bin/env python3
l = [1,2,1,2,2,3,4,5,4,7]

d = {}
for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
