import PyPluMA

class PhyloSeqNormalizePlugin:
    def input(self, filename):
      infile = open(filename, 'r') 
      self.ADJ = []
      for line in infile:
           contents = line.strip().split(',')
           self.ADJ.append(contents)

    def run(self):
       self.N = len(self.ADJ)
       self.M = len(self.ADJ[0])

       for i in range(1, self.M):
          sum = 0.0
          for j in range(1, self.N):
             sum += float(self.ADJ[j][i])
          for j in range(1, self.N):
             self.ADJ[j][i] = float(self.ADJ[j][i]) / sum

    def output(self, outputfile):
       outfile = open(outputfile, 'w')
       for i in range(self.N):
          for j in range(self.M):
             outfile.write(str(self.ADJ[i][j]))
             if (j != self.M-1):
                outfile.write(",")
             else:
                outfile.write("\n")
