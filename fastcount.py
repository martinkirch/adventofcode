"""
how to print integers real fast ?
 * naive implem at 16.2MiB/s
 * sys.stdout.buffer.write(b'%d\n' % i) instead of print() at 21MiB/s
"""
import sys
# 161MiB to 20000000

for i in range(20000000):
    sys.stdout.buffer.write(b'%d\n' % i)
