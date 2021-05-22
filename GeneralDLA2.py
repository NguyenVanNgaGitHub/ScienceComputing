import math

import numpy as np
import random as random
from math import pi, cos, sin, sqrt

from DirectionalBias import DirectionalBias
from Particle import Particle
from Configs import Configs
from utils import Helper
import matplotlib.pyplot as plt

from IPython import display
from time import sleep


class GeneralDLA2():
    def __init__(self):

        self.particles = Configs.direction_bias.initCluster()
        self.init_num_particles = len(self.particles)
        self.delta_distance = Configs.delta_distance_percentage / 100 * Configs.radius_particle

        #print("Init Particles",self.init_num_particles)
        #print("Delta Distance",self.delta_distance)
        self.bias = 0

        self.walkers = [];

    def recoveryWalkers(self):
        while len(self.walkers) < Configs.num_walkers:
            self.walkers.append(self.generateWalker())

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
        dx = Configs.force_bias * cos(angle)
        dy = Configs.force_bias * sin(angle)
        walker.x = walker.x + dx
        walker.y = walker.y + dy
        x, y = Configs.direction_bias.addBiasForce(walker)

        walker.x = x
        walker.y = y
        return walker
        # if self.bias == 0:
        #     return x + dx, y + dx
        # else:
        #     dis = GeneralDLA2.distance((x, y))
        #     new_x = x + dx - self.bias * x / dis
        #     new_y = y + dy - self.bias * y / dis
        #     return new_x, new_y

    def bindingToAggregation(self, walker):
        self.particles.append(walker)
        # print("Binding Particle ",len(self.particles)-self.init_num_particles)

    def generateWalker(self):
        # random_radius = random.randrange(self.gen+1, self.radius_kill)
        x = random.random() * Configs.width_size - Configs.width_size / 2
        y = random.random() * Configs.height_size - Configs.height_size / 2

        return Particle(x, y, Configs.radius_particle)

    def isCollideAggregation(self, walker):
        max_delta_distance = 0
        is_exist_collide=False
        for particle in self.particles:
            dx = walker.x - particle.x
            dy = walker.y - particle.y
            dis = GeneralDLA2.distance((dx, dy))

            p = Configs.radius_particle * 2 - dis
            if p >= 0:
                is_exist_collide=True
                if max_delta_distance <= p:
                    max_delta_distance = p
        if is_exist_collide:
            if max_delta_distance <= self.delta_distance:
                #print("Max_delta_distance",max_delta_distance)
                return True,True
            return True,False
        return False,False

    def isBindAggregation(self, walker):
        return Configs.distribution.can_stick((walker.x, walker.y))

    def isInSafeArea(self, walker):
        # print("Check safe area ", x, y,math.dist([x,y],[0,0]))
        if abs(walker.x) >= Configs.width_size / 2:
            return False
        if abs(walker.y) >= Configs.height_size / 2:
            return False
        return True

    def moveWalkers(self):
        for index, walker in enumerate(self.walkers):
            self.walkers[index] = self.diffusion(walker)

    def pruneWalkers(self):
        for walker in self.walkers:
            if not self.isInSafeArea(walker):
                # print("Before remove",len(self.walkers))
                self.walkers.remove(walker)
                # print("After remove",len(self.walkers))

    def bindWalker(self):
        for walker in self.walkers:
            # print('Check Bind ',walker)
            is_collide,is_safe_distance= self.isCollideAggregation(walker)
            if is_collide:
                if is_safe_distance:
                    if self.isBindAggregation(walker):
                        self.bindingToAggregation(walker)
                        self.walkers.remove(walker)
                else:
                    self.walkers.remove(walker)

    def getRealBindedParticles(self):
        return len(self.particles) - self.init_num_particles

    def simulate(self):
        while self.getRealBindedParticles() <= Configs.num_particles:
            #print("Start ",self.getRealBindedParticles())
            #print("To ",Configs.num_particles)
            self.iterate()

    def iterate(self):
        self.recoveryWalkers();
        self.moveWalkers()
        self.pruneWalkers()
        self.bindWalker()

# Configs.direction_bias=DirectionalBias('edges')
# Configs.distribution
# dla=GeneralDLA2()
# dla.simulate()
