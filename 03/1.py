#!/usr/bin/env python3
import sys
from math import gcd


if len(sys.argv) < 3:
    print("Minimum 2 arguments required")
else:
    l = [int(x) for x in sys.argv[1:]]
    print(gcd(*l))
