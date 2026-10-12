
import time
import math

pocet = 8

print("Kulička jede")


for i in range(pocet):
    print(" " * i + "O")
    time.sleep(0.1)


for i in range(pocet):
    print(" " * (pocet - i - 1) + "O")
    time.sleep(0.1)


print("Tabulka")

for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
