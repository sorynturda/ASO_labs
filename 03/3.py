#!/usr/bin/env python3

import os

with open("/etc/passwd", "r") as file:
    lines = [line.rstrip() for line in file]
ok = []

for line in lines:
    if "/usr/sbin/nologin" in line or "/bin/false" in line:
        continue
    ok.append(line)

print(len(ok), "users")
max_id = 0
user = ""
for line in ok:
    if max_id < int(line.split(":")[2]):
        max_id = int(line.split(":")[2])
        user = line.split(":")[0]

print(user)
