from StickDistribution import StickDistribution

class NumberOfNeighboringParticlesStickDistribution(StickDistribution):#extends
    def __init__(self, dla = None, A: float = 1.0, B: float = 0.5, percent_box = 10):   #this
        super(NumberOfNeighboringParticlesStickDistribution, self).__init__(dla=dla)
        self.A = A #ko truyền gì vào ở main.py thì mới là 1.0
        self.B = B #ko truyền gì vào ở main.py thì mới là 0.5
        self.percent_box = percent_box/100

    def compute_proba(self, pos : (int,int)) -> float:

        #
        surface_matrix = self.dla.surface_matrix
        x = pos[0] + self.dla.radius_limit
        y = pos[1] + self.dla.radius_limit
        L = int((2*self.dla.radius_limit+1)*min(self.percent_box,1))
        n0 = (L-1)/(2*L)

        up_left = [max(int(x - (L - 1) / 2), 0), max(int(y - (L - 1) / 2), 0)]
        up_right = [min(int(x + (L - 1) / 2), L - 1), max(int(y - (L - 1) / 2), 0)]
        down_left = [max(int(x - (L - 1) / 2), 0), min(int(y + (L - 1) / 2), L - 1)]
        down_right = [min(int(x + (L - 1) / 2), L - 1), min(int(y + (L - 1) / 2), L - 1)]

        NL = 1
        for i in range(up_left[0], up_right[0]):
            for j in range(up_left[1], down_left[1]):
                if (surface_matrix[i][j] != 0):
                    NL = NL + 1

        nL = NL/(L**2)
        A = self.A
        B = self.B

        print("tại x,y = ",x,y,"nL = ",nL,"n0 = ",n0,"A*(nL - n0) + B = ",A*(nL - n0) + B)#A*(NL/(L**2) - (L-1)/2L) + B
        #
        return A*(nL - n0) + B