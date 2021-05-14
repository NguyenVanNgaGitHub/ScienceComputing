from StickDistribution import StickDistribution

class LocalCurvatureAtThePointOfContactStickDistribution(StickDistribution):#extends
    def __init__(self, dla = None, A: float = 1.0, B: float = 0.5, percent_box = 10):   #this
        super(LocalCurvatureAtThePointOfContactStickDistribution, self).__init__(dla=dla)
        self.A = A #ko truyền gì vào ở main.py thì mới là 1.0
        self.B = B #ko truyền gì vào ở main.py thì mới là 0.5
        self.percent_box = percent_box/100

    def compute_proba(self, pos : (int,int)) -> float:

        #
        n1 = 1
        n2 = 1
        surface_matrix = self.dla.surface_matrix
        x = pos[0]+self.dla.radius_limit
        y = pos[1]+self.dla.radius_limit
        L = int((2*self.dla.radius_limit+1)*min(self.percent_box,1))
        up_left_small = [max(int(x - (L-1)/4), 0), max(int(y - (L-1)/4), 0)]
        up_right_small = [min(int(x + (L-1)/4), L - 1), max(int(y - (L-1)/4), 0)]
        down_left_small = [max(int(x - (L-1)/4), 0), min(int(y + (L-1)/4), L - 1)]
        down_right_small = [min(int(x + (L-1)/4), L - 1), min(int(y + (L-1)/4), L - 1)]

        up_left_big = [max(int(x - (L-1)/2), 0), max(int(y - (L-1)/2), 0)]
        up_right_big = [min(int(x + (L-1)/2), L - 1), max(int(y - (L-1)/2), 0)]
        down_left_big = [max(int(x - (L-1)/2), 0), min(int(y + (L-1)/2), L - 1)]
        down_right_big = [min(int(x + (L-1)/2), L - 1), min(int(y + (L-1)/2), L - 1)]

        for i in range(up_left_small[0], up_right_small[0]):
            for j in range(up_left_small[1], down_left_small[1]):
                if (surface_matrix[i][j] != 0):
                    n1 = n1 + 1

        for i in range(up_left_big[0], up_right_big[0]):
            for j in range(up_left_big[1], down_left_big[1]):
                if (surface_matrix[i][j] != 0):
                    n2 = n2 + 1
        A = self.A
        B = self.B

        print("tại x,y = ",x,y,"n1 = ",n1,"n2 = ",n2,"A - 1.0*B*n1/n2 = ",A - 1.0*B*n1/n2)
        #
        return A - 1.0*B*n1/n2
