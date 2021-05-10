import numpy as np
import random as random
from math import pi, cos, sin, sqrt
from StickDistribution import StickDistribution
from utils import Helper

class GeneralDLA():

    def __init__(self, num_particle, limit_radius, stick_distribution: StickDistribution,bias=0):

        self.num_particle = num_particle
        self.limit_radius = limit_radius
        self.particles = np.zeros((num_particle, 3))
        self.particles[0] = (0, 0, 0)
        self.stick_distribution = stick_distribution
        self.seed_particle_x = limit_radius
        self.seed_particle_y = limit_radius
        # Can change hype parameter in here
        self.radius_bounding = 0
        self.radius_gen = self.radius_bounding + 4
        self.radius_kill = self.radius_gen + 4
        self.radius_circle = 1
        self.radius_step = self.radius_circle
        self.stick_distance = self.radius_circle * 2
        self.particles[:, 2] = self.radius_circle
        self.bias = bias

    @staticmethod
    def distance(pos1: (int, int), pos2: (int, int) = None) -> float:
        if pos2 is not None:
            return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
        else:
            return sqrt((pos1[0]) ** 2 + (pos1[1]) ** 2)

    def brownian_motion(self, time):
        pass

    def diffusion(self, x, y):
        # Implementation for random walker
        angle = random.random() * 2 * pi
        dx = self.radius_step * cos(angle)
        dy = self.radius_step * sin(angle)
        if self.bias == 0:
            return x + dx, y + dx
        else:
            dis = GeneralDLA.distance((x, y))
            new_x = x + dx - self.bias * x / dis
            new_y = y + dy - self.bias * y / dis
            return new_x, new_y

    def bindingToAggregation(self, index, x, y):
        self.particles[index][0] = x
        self.particles[index][1] = y
        dis = GeneralDLA.distance((x, y))

        print('Pos in Bind ',index,x,y)
        if dis > self.radius_bounding:
            self.radius_bounding = dis
            self.radius_gen = self.radius_bounding + 4
            self.radius_kill = self.radius_gen + 4

    def randomGenPosition(self):
        # random_radius = random.randrange(self.gen+1, self.radius_kill)
        angle = random.random() * 2 * pi
        x = self.radius_gen * cos(angle)
        y = self.radius_gen * sin(angle)

        return x, y

    def isBindingToAggregation(self, index, x, y):
        is_bounding = False
        for pre_index in range(index):
            dx = x - self.particles[pre_index][0]
            dy = y - self.particles[pre_index][1]
            dis = GeneralDLA.distance((dx, dy))
            if dis <= self.stick_distance:
                is_bounding = True
                break
        if is_bounding:
            if self.stick_distribution.can_stick((x, y)):
                return True
            return False
        return False

    def isInSafeArea(self, x, y):
        dis = GeneralDLA.distance((x, y))
        if dis < self.radius_kill:
            return True
        return False

    def build(self):
        for index in range(self.num_particle - 1):
            index += 1
            # Random position for particle
            x, y = self.randomGenPosition()
            #print('start x, y:', x, y)
            while not self.isBindingToAggregation(index, x, y):
                x, y = self.diffusion(x, y)

                # if index == 10:
                #     print('Position X='+str(x)+', y = '+str(y))
                if not self.isInSafeArea(x, y):
                    x, y = self.randomGenPosition()
            self.bindingToAggregation(index, x, y)
            #print('===========Particle:', index)

        for index, particle in enumerate(self.particles):
            self.particles[index][0] = particle[0] + self.seed_particle_x
            self.particles[index][1] = particle[1] + self.seed_particle_y

    def simulate(self, file_name):
        self.build()
        Helper.simulate_dla(self.particles, self.limit_radius, file_name)


if __name__ == '__main__':
    print(GeneralDLA.distance((3, 4)))