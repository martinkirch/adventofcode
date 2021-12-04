"""
High Thoughput FizzBuzz - Python edition
as from https://codegolf.stackexchange.com/questions/215216/high-throughput-fizz-buzz

on battery:
 * naive implem peaks around 10Mb/s
 * modulo 3 and 5 only once and sys.stdout.write("Fizz"/"Buzz") peaks around 6Mb/s
 * same but in py3 gets back to 10mb/s
 * using sys.stdout.buffer.write(b'Buzz') and sys.stdout.buffer.write(b'%d' % i) peaks around 9.5Mb/s

"""

import sys

# 20000000 does 153MiB

for i in range(20000000):
    if i % 3 == 0:
        written = sys.stdout.buffer.write(b'Fizz')
    if i % 5 == 0:
        written = sys.stdout.buffer.write(b'Buzz')
    if written == 1:
        sys.stdout.buffer.write(b'%d' % i)
    # sets written to 1
    written = sys.stdout.buffer.write(b'\n')
