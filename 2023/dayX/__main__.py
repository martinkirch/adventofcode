from os.path import dirname, join
from . import today

with open(join(dirname(__file__), 'input.txt')) as f:
    real_input = f.readlines()

print(today(real_input))
