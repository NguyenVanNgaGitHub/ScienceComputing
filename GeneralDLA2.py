import math

import numpy as np
import random as random
from math import pi, cos, sin, sqrt

from Configs import Configs
from utils import Helper


class GeneralDLA2():
    def __init__(self):
        self.particles = []

        self.particles = Configs.direction_bias.initCluster(self.particles)
        self.init_num_particles=len(self.particles)
        self.stick_distance = Configs.radius_particle * 2+ Configs.added_stick_distance_bias
        self.bias = 0

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
        dx = Configs.force_bias * cos(angle)
        dy = Configs.force_bias * sin(angle)
        x=x+dx
        y=y+dy
        x,y=Configs.direction_bias.addBiasForce(x,y)

        return x,y
        # if self.bias == 0:
        #     return x + dx, y + dx
        # else:
        #     dis = GeneralDLA2.distance((x, y))
        #     new_x = x + dx - self.bias * x / dis
        #     new_y = y + dy - self.bias * y / dis
        #     return new_x, new_y

    def bindingToAggregation(self, x, y):
        self.particles.append([x, y, Configs.radius_particle])
        print("Binding Particle ",len(self.particles)-self.init_num_particles)

    def randomGenPosition(self):
        # random_radius = random.randrange(self.gen+1, self.radius_kill)
        x = random.random() * Configs.width_size - Configs.width_size/2
        y = random.random() * Configs.height_size - Configs.height_size / 2
        return x, y

    def isBindingToAggregation(self, x, y):
        is_bounding = False
        for particle in self.particles:
            dx = x - particle[0]
            dy = y - particle[1]
            dis = GeneralDLA2.distance((dx, dy))
            if dis <= self.stick_distance:
                is_bounding = True
                break
        if is_bounding:
            if Configs.stick_distribution.can_stick((x, y)):
                return True
            return False
        return False

    def isInSafeArea(self, x, y):
        #print("Check safe area ", x, y,math.dist([x,y],[0,0]))
        if abs(x) >= Configs.width_size / 2:
            return False
        if abs(y) >= Configs.height_size / 2:
            return False
        return True

    def build(self):
        for index in range(Configs.num_particles):
            # Random position for particle
            x, y = self.randomGenPosition()
            # print('start x, y:', x, y)
            while not self.isBindingToAggregation(x, y):
                x, y = self.diffusion(x, y)
                #print(" Dis from center ",math.dist([x,y],[0,0]))
                if not self.isInSafeArea(x, y):
                    x, y = self.randomGenPosition()
            self.bindingToAggregation(x, y)
            # print('===========Particle:', index)

        for particle in self.particles:
            particle[0] = particle[0] + Configs.width_size / 2
            particle[1] = particle[1] + Configs.height_size / 2

    def simulate(self, file_name):
        self.build()
        Helper.simulate_dla(self.particles)


if __name__ == '__main__':
    print(GeneralDLA2.distance((3, 4)))
