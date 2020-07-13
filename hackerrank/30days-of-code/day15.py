class Difference:
    def __init__(self, a):
        self.__elements = a
    
    # Add your code here
    maximumDifference = 0

    def computeDifference(self):
        md = 0
        for i in self.__elements:
            for j in self.__elements:
                #print(md, self.maximumDifference)
                if (abs(i - j) > md):
                    md = abs(i - j)
            if (md > self.maximumDifference):
                self.maximumDifference = md
        return self.maximumDifference
            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
