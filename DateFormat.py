#!/usr/bin/env python3

from datetime import date
today = date.today()

print()

D1 = today.strftime("%d/%m/%Y")
print("D1 = ", D1)
print()

D2 = today.strftime("%B %d, %Y")
print("D2 = ", D2)
print()

D3 = today.strftime("%m/%d/%y")
print("D3 = ", D3)
print()

D4 = today.strftime("%b-%d-%Y")
print("D4 = ", D4)
print()
