import numpy as np
import random as random
from math import pi, cos, sin, sqrt

from Particle import Particle
from Configs import Configs


class GeneralDLA2():
    def __init__(self):
        self.initSurfaceMatrix()
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1],[0, 1], [1, -1], [1, 0], [1, 1]]
        self.bias = 0

        self.walkers = [];

    def transformValue(self):
        return  int((Configs.num_particles-self.sticked_num)/(Configs.num_particles/Configs.color_num)+1)

    def initSurfaceMatrix(self):
        self.surface_matrix = np.zeros((Configs.window_size , Configs.window_size), dtype=np.int32)
        self.empty_cells = []
        for i in range(Configs.window_size):
            for j in range(Configs.window_size):
                self.empty_cells.append([i,j]);

        arr = Configs.direction_bias.initCluster()
        self.sticked_num = 0;
        for p in arr:
            self.surface_matrix[p.x][p.y] = self.transformValue();
            #print("Value cell ",self.surface_matrix[p.x][p.y])
            #print("Remove empty cells :",p.x,p.y)
            if [p.x,p.y] in self.empty_cells:
                self.empty_cells.remove([p.x,p.y])


    def recoveryWalkers(self):
        walker_num=len(self.walkers)
        while walker_num < Configs.num_walkers:
            walker = self.generateWalker()
            self.walkers.append(walker)
            walker_num =walker_num+1

    def generateWalker(self):
        cell = random.choice(self.empty_cells)
        return Particle(cell[0], cell[1], Configs.radius_particle)

    @staticmethod
    def distance(pos1: (int, int), pos2: (int, int) = None) -> float:
        if pos2 is not None:
            return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
        else:
            return sqrt((pos1[0]) ** 2 + (pos1[1]) ** 2)

    def brownian_motion(self, time):
        pass

    def diffusion(self, walker):
        # Implementation for random walker
        angle = random.random() * 2 * pi
        step_length = random.randint(1, Configs.force_bias)
        dx = round(step_length * cos(angle))
        dy = round(step_length * sin(angle))
        walker.x = walker.x + dx
        walker.y = walker.y + dy
        x, y = Configs.direction_bias.addBiasForce(walker)

        walker.x = x
        walker.y = y
        return walker

    def bindingToAggregation(self, walker):
        self.surface_matrix[walker.x][walker.y] = self.transformValue();
        #print("Value cell ",self.surface_matrix[walker.x][walker.y])
        self.sticked_num = self.sticked_num + 1
        self.walkers.remove(walker)

        if [walker.x,walker.y] in self.empty_cells:
            self.empty_cells.remove([walker.x,walker.y])


    def isContactAggregation(self, walker):
        for dir in self.directions:
            tx = walker.x + dir[0]
            ty = walker.y + dir[1]
            if self.isInSafeArea(tx, ty):
                if self.surface_matrix[tx][ty] > 0:
                    return True
        return False

    def isBindAggregation(self, walker):
        return Configs.distribution.can_stick((walker.x, walker.y))

    def isInSafeArea(self, x, y):
        # #print("Check safe area ", x, y,math.dist([x,y],[0,0]))
        if x < 0:
            return False
        if x >= Configs.window_size:
            return False
        if y < 0:
            return False
        if y >= Configs.window_size:
            return False
        return True

    def moveWalkers(self):
        for i in range(len(self.walkers)):
            walker =self.walkers[i]
            self.walkers[i] = self.diffusion(walker)

    def isPruned(self,walker):
        if not self.isInSafeArea(walker.x, walker.y):
            return True
        elif self.surface_matrix[walker.x][walker.y] > 0 :
            return  True
        return  False

    def bindWalker(self):
        for walker in self.walkers:
            if self.isPruned(walker):
                self.walkers.remove(walker)
            else:
                if self.isContactAggregation(walker):
                    # print("Collide Detect")
                    if self.isBindAggregation(walker):
                        self.bindingToAggregation(walker)

    def getRealBindedParticles(self):
        return self.sticked_num

    def simulate(self):
        while self.getRealBindedParticles() <= Configs.num_particles:
            #print("Start ",self.getRealBindedParticles(),"   ,To ",Configs.num_particles)
            self.iterate()

    def iterate(self):
        self.recoveryWalkers()
        self.moveWalkers()
        self.bindWalker()

# Configs.direction_bias=DirectionalBias('center')
# Configs.distribution
# dla=GeneralDLA2()
# dla.simulate()
