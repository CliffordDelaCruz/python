#collatz.py
#Collatz's hypothesis
""" 
The hypothesis says that regardless of the initial value of c0
it will always go to 1.

Used while-else in this code
"""
c0 = int(input("Enter any non-negative, non-zero value: "))
steps = 0
while c0 > 1:
    print(c0)
    steps += 1
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
else:
    print(c0)
    steps += 1
print("steps = {}".format(steps))