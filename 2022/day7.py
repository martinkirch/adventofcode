from __future__ import annotations
lines = open("day7_input.txt").readlines()

line_i = None

class Folder:
    def __init__(self, name:str, parent:Folder):
        self.parent = parent
        self.name = name
        self.content = dict()
        self.ownsize = 0
        self.size = None

    def cd(self, dir) -> Folder:
        if dir == '..':
            if self.parent:
                return self.parent
            else:
                print("Warning - it's weird to cd .. from root")
                return self
        else:
            return self.content[dir]

    def compute_size(self) -> int:
        self.size = self.ownsize + sum(c.compute_size() for c in self.content.values())
        if not self.content:
            assert self.size == self.ownsize
        return self.size

    def total_below(self, below) -> int:
        small = sum(c.total_below(below) for c in self.content.values())
        if self.size < below:
            small += self.size
        return small

    def smallest_above(self, above):
        smallest = 999999999999
        if self.size >= above:
            smallest = self.size
        for c in self.content.values():
            smallest = min(smallest, c.smallest_above(above))
        return smallest

    def ls(self):
        global line_i
        if self.content:
            raise ValueError("holup we've been there already")
        while line_i < len(lines) and not lines[line_i].startswith('$'):
            splitted = lines[line_i].split()
            if splitted[0] == 'dir':
                name = splitted[1].strip()
                if name in self.content:
                    raise ValueError("duplicate folder")
                self.content[name] = Folder(name, self)
            else:
                self.ownsize += int(splitted[0])
            line_i += 1

root = Folder('/', None)
line_i = 1 # first line is the only `cd /`
cwd = root
while line_i < len(lines):
    line = lines[line_i].strip()
    if line.startswith('$'):
        match line[2:4]:
            case 'cd':
                cwd = cwd.cd(line[5:])
                line_i += 1
            case ls:
                line_i += 1
                cwd.ls()
    else:
        raise ValueError(f"wat ? reading line {line_i}:{line}")

root.compute_size()
print(f"root size is {root.size}")
print(f"total smallest are {root.total_below(100000)}")

#root.print()
# 8921709 too high -- haha because in the real input, needed size is not 8381165
needed = 30000000 - (70000000 - root.size)
print(f"Smallest big enough folder is {root.smallest_above(needed)}")
