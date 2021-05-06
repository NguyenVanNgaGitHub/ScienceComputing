import numpy as np
from StickDistribution import StickDistribution
from math import sqrt, pi, sin, cos
import random
import matplotlib.pyplot as plt
from GifRecorder import GifRecoder
from ImageRecorder import ImageRecoder
class DLA:
    def __init__(self, radius_limit: int, numParticles: int, stickDistribution: StickDistribution):
        self.radius_limit = radius_limit
        self.numParticles = numParticles
        self.stickDistribution = stickDistribution
        self.stickDistribution.dla = self

        size = 2*self.radius_limit+1
        self.surface_matrix = np.zeros((size,size),dtype=np.int32)

        self.num_hits = 1
        self.surface_matrix[self.radius_limit,self.radius_limit] = self.num_hits

        self.max_radius = 0
        self.gen_radius = self.max_radius+5
        self.remove_radius = self.max_radius+20

        self.nnStepsPos = [(1,0), (0,1), (-1,0), (0,-1)]
        self.nnStepsIndex = [(self.radius_limit+1,self.radius_limit),
                             (self.radius_limit,self.radius_limit+1),
                             (self.radius_limit - 1, self.radius_limit),
                             (self.radius_limit, self.radius_limit - 1)]

        self.recordIntervals = list(range(0,numParticles,50))
        self.recorders = {"gif": GifRecoder(dla=self),
                          "image": ImageRecoder(dla=self)}

    def inKeepCircle(self, pos: (int, int)) -> bool:
        if pos[0]**2 + pos[1]**2 <= self.remove_radius**2:
            return True
        else:
            return False

    def isNNOccupied(self, pos: (int, int)) -> bool:
        for stepIndex in self.nnStepsIndex:
            if self.surface_matrix[pos[0]+stepIndex[0],pos[1]+stepIndex[1]]:
                return True
        return False

    def hitUpdate(self, pos: (int, int)):
        self.num_hits += 1
        self.surface_matrix[pos[0]+self.radius_limit,pos[1]+self.radius_limit] = self.num_hits

        this_radius = int(sqrt(pos[0]**2 + pos[1]**2))
        if this_radius>self.max_radius:
            self.max_radius = this_radius
            self.gen_radius = min(self.max_radius+5,self.radius_limit-1)
            self.remove_radius = min(self.max_radius+20,self.radius_limit-1)

    def genStep(self, pos: (int, int)) -> (bool, (int, int)):
        step = random.choice(self.nnStepsPos)
        new_pos = (pos[0]+step[0],pos[1]+step[1])
        return self.inKeepCircle(new_pos), new_pos

    def checkAggregate(self, pos: (int, int)) -> bool:
        if self.isNNOccupied(pos):
            if self.stickDistribution.can_stick(pos):
                return True
            else:
                return False
        else:
            return False

    def random_pos(self):
        angle = random.random()*2*pi
        pos = (int(sin(angle) * self.gen_radius), int(cos(angle) * self.gen_radius))
        return pos

    def addWalker(self, max_try=10):
        flag = False
        while max_try:
            pos = self.random_pos()
            while True:
                isKeep, new_pos = self.genStep(pos)
                pos = new_pos
                if isKeep:
                    if self.checkAggregate(pos):
                        self.hitUpdate(pos)
                        flag = True
                        break
                else:
                    max_try-=1
                    break
            if flag:
                break
        return flag

    def simulate(self):
        for i in range(self.numParticles):
            self.addWalker()
            if i in self.recordIntervals:
                self.recorders["gif"].record()
        for key in self.recorders:
            self.recorders[key].export_result()


