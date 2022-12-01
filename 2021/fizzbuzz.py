"""
High Thoughput FizzBuzz - Python edition
as from https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz

on battery:
 * naive implem peaks around 10Mb/s
 * modulo 3 and 5 only once and sys.stdout.write("Fizz"/"Buzz") peaks around 6Mb/s
 * same but in py3 gets back to 10mb/s
 * and integrating the \n to all outputted strings (to avoid a call to `write`) peaks at 13.5Mb/s
 * using sys.stdout.buffer.write(b'Buzz') and sys.stdout.buffer.write(b'%d' % i) peaks around 9.5Mb/s
 * itertools.cycle over a the fizzbuzz cycle and sys.stdout.buffer.write(b'%d' % i) peaks at 11Mb/s
 * integrating \n to each sys.stdout.buffer.write peaks at 15Mb/s !!

"""

import sys

# 20000000 does 153MiB

from itertools import cycle
loop = cycle([
    b'FizzBuzz\n',
    None,
    None,
    b'Fizz\n',
    None,
    b'Buzz\n',
    b'Fizz\n',
    None,
    None,
    b'Fizz\n',
    b'Buzz\n',
    None,
    b'Fizz\n',
    None,
    None,
])

for i in range(20000000):
    current = next(loop)
    if current:
        sys.stdout.buffer.write(current)
    else:
        sys.stdout.buffer.write(b'%d\n' % i)
