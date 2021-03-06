import numpy as np

class BaseLoader:

    def __init__(self,  filename):
        self.file = open(filename, "r")
        self.parse()
        self.close()

    def _readline(self):
        return self.file.readline().rstrip('\n')

    def _readlines(self, n):
        return list(map(lambda x: self._readline(), range(n)))

    def _readlinesAndSplit(self, n):
        return list(map(lambda x: self._readline().split(), range(n)))

    def _loadIntegers(self):
        return list(map(lambda x: int(x), self._readline().split()))

    def _loadIntegerMatrix(self, rows):
        return list(map(
            lambda x: list(map(lambda y: int(y), self._readline().split())), 
            range(rows)
        ))

    def _toNumpyArray(self, data, dtype=str):
        return np.array(data, dtype=dtype)
        

    def parse(self):
        pass

    def close(self):
        self.file.close()


class Loader(BaseLoader):

    def parse(self):

        self.N = self._loadIntegers()[0]
        self.photos = self._readlinesAndSplit(self.N)
        self.photos = list(map(
            lambda x: [x[0], x[1], x[2:2+int(x[1])]], self.photos)
        )

class Writer:

    def __init__(self, filename):
        self.file = open(filename, "w+")

    def writeSlidesLength(self, length):
        self.file.write(str(length)+"\n")
    
    def writeVerticalsAndHorizontals(self, verticals, horizontals):
        count = 0
        for h in horizontals:
            self.file.write(str(h)+"\n")
        for x in verticals:
            if count< len(verticals):
                self.file.write(str(verticals[count])+" "+str(verticals[count+1])+"\n")
                count=count+2
        

    def close(self):
        self.file.close()
        
#example = Loader("files/a_example.in")
#print(example.tm)