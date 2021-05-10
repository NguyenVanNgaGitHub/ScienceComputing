import math
from abc import ABC, abstractmethod

from Configs import Configs


class DirectionalBias():
    def __init__(self, value='center'):
        self.value = value

    def createVerticalWall(self, particles, main_ax):
        init_other_ax = -Configs.height_size / 2

        for i in range(0, math.floor(Configs.height_size / Configs.radius_particle)):
            #print("Generate Wall ", main_ax, init_other_ax + Configs.radius_particle * i)
            particles.append([main_ax, init_other_ax + Configs.radius_particle * i, Configs.radius_particle])

        return particles

    def createHorizontalWall(self, particles, main_ax):
        init_other_ax = -Configs.width_size / 2
        for i in range(0,math.floor( Configs.height_size / Configs.radius_particle)):
            particles.append([init_other_ax + Configs.radius_particle * i, main_ax, Configs.radius_particle])

        return particles

    def getTowardCenterForce(self, x, y):
        angle_rad = math.atan2(float(-y), float(-x))
        #print("angle_rad ",math.degrees(angle_rad))
        #rint("angle_rad Cos",math.cos(angle_rad))
        return math.cos(angle_rad) * Configs.force_bias, math.sin(angle_rad) * Configs.force_bias


    def addBiasForce(self, x, y):
        if self.value == 'left':
            return x-Configs.force_bias,y
        elif self.value == 'right':
            return x+Configs.force_bias,y
        elif self.value == 'bottom':
            return x,y-Configs.force_bias
        elif self.value == 'top':
            return x,y+Configs.force_bias
        elif self.value == 'equator':
            if y>0 :
                return x,y-Configs.force_bias
            else :
                return x,y+Configs.force_bias
        elif self.value == 'meridian':
            if x > 0:
                return x - Configs.force_bias,y
            else:
                return x + Configs.force_bias,y
        elif self.value == 'center':
            dx, dy = self.getTowardCenterForce(x, y)
            return x + dx, y + dy
        elif self.value == 'edges':
            dx, dy = self.getTowardCenterForce(x, y)
            return x - dx, y - dy


    def initCluster(self, particles):
        if self.value == 'left':
            particles = self.createVerticalWall(particles,main_ax=-Configs.width_size/2)
        elif self.value == 'right':
            particles = self.createVerticalWall(particles,main_ax=Configs.width_size/2)
        elif self.value == 'bottom':
            particles = self.createHorizontalWall(particles,main_ax=-Configs.height_size/2)
        elif self.value == 'top':
            particles = self.createHorizontalWall(particles,main_ax=Configs.height_size/2)
        elif self.value == 'equator':
            particles = self.createHorizontalWall(particles,main_ax=0)
        elif self.value == 'meridian':
            particles = self.createVerticalWall(particles,main_ax=0)
        elif self.value == 'center':
            particles.append([0, 0, Configs.radius_particle])
        elif self.value == 'edges':
            particles = self.createVerticalWall(particles, main_ax=Configs.width_size/2)
            particles = self.createVerticalWall(particles, main_ax=-Configs.width_size / 2)
            particles = self.createHorizontalWall(particles, main_ax=Configs.height_size / 2)
            particles = self.createHorizontalWall(particles, main_ax=-Configs.height_size / 2)
        return particles


d_bias=DirectionalBias('left')
x,y=-1,5
print(d_bias.addBiasForce(x,y))