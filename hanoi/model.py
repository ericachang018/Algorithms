# how do i create a model!!! >__< gah

# Game model - There are 3 towers all of which have unique names and how to solve the hanoi problem
class Hanoi(object):
    def __init__(self, num_disks):
        self.tower1 = Tower("Tower Of Doom")
        self.tower2 = Tower("Tower Of Power")
        self.tower3 = Tower("Tower of Life")

        for i in range(num_disks-1, -1, -1):
            self.tower1.add( Disk(i+1) )

        self.moves = []
        
    def solve(self):
        self._solve_towers(len(self.tower1.disks), self.tower1, self.tower2, self.tower3)
        
# private function which can only be used in this method. 
    def _solve_towers(self, n, start, holder, end):
        if n > 0:
            self._solve_towers(n-1, start, end, holder)

            if start.has_disks():
                disk = start.remove()
                self.moves.append("Moving disk of size %d from %s to %s"%(disk.size, start.name, end.name))
                end.add(disk)

            self._solve_towers(n-1, holder, start, end)

#build a tower class that has a name and can hold disks and the functions to add remove them. 
class Tower(object):

    def __init__(self, name):
        self.disks = []
        self.name = name
        
    def remove(self):
        disk = self.disks.pop()
        return disk

    def add(self, disk):
        self.disks.append(disk)

    def has_disks(self):
        return len(self.disks) > 0

# build a disk class that specifies size. 
class Disk(object):
    def __init__(self, size):
        self.size = size


# def main():
#     hanoi = Hanoi(5)
#     hanoi.solve()
#     print hanoi.moves

# if __name__ == "__main__":
#     main() 