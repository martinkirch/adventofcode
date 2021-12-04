"""
High Thoughput FizzBuzz - Python edition
as from https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz

on battery:
 * naive implem peaks around 10Mb/s
 * modulo 3 and 5 only once and sys.stdout.write("Fizz"/"Buzz") peaks around 6Mb/s
 * same but in py3 gets back to 10mb/s

"""

import sys

# 20000000 does 153MiB

for i in range(20000000):
    flag = True
    if i % 3 == 0:
        flag = False
        sys.stdout.write("Fizz")
    if i % 5 == 0:
        flag = False
        sys.stdout.write("Buzz")
    if flag:
        sys.stdout.write(str(i))
    sys.stdout.write("\n")
