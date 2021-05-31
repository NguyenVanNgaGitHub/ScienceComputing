import math
from abc import ABC, abstractmethod
from Particle import Particle
from Configs import Configs


class DirectionalBias():
    def __init__(self, value='center'):
        self.value = value

    def createVerticalWall(self, particles, main_ax):

        for i in range(Configs.window_size):
            particles.append(Particle(main_ax, i, Configs.radius_particle))

        return particles

    def createHorizontalWall(self, particles, main_ax):
        for i in range(Configs.window_size):
            particles.append(Particle(i, main_ax, Configs.radius_particle))

        return particles

    def getTowardCenterForce(self, x, y):
        angle_rad = math.atan2(float(int(Configs.window_size/2)-y), float(int(Configs.window_size/2)-x))
        return math.cos(angle_rad) * Configs.force_bias, math.sin(angle_rad) * Configs.force_bias


    def addBiasForce(self, walker):
        if Configs.add_cluster_toward_force == False :
            return  walker.x,walker.y
        x,y=walker.x,walker.y
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
            return round(x + dx),round( y + dy)
        elif self.value == 'edges':
            dx, dy = self.getTowardCenterForce(x, y)
            return round(x - dx), round(y - dy)


    def initCluster(self):
        particles=[]
        if self.value == 'left':
            particles = self.createVerticalWall(particles,main_ax=0)
        elif self.value == 'right':
            particles = self.createVerticalWall(particles,main_ax=Configs.window_size-1)
        elif self.value == 'bottom':
            particles = self.createHorizontalWall(particles,main_ax=0)
        elif self.value == 'top':
            particles = self.createHorizontalWall(particles,main_ax=Configs.window_size-1)
        elif self.value == 'equator':
            particles = self.createHorizontalWall(particles,main_ax=int(Configs.window_size/2))
        elif self.value == 'meridian':
            particles = self.createVerticalWall(particles,main_ax=int(Configs.window_size/2))
        elif self.value == 'center':
            particles.append(Particle(int(Configs.window_size/2), int(Configs.window_size/2), Configs.radius_particle))
        elif self.value == 'edges':
            particles = self.createVerticalWall(particles, main_ax=Configs.window_size-1)
            particles = self.createVerticalWall(particles, main_ax=0)
            particles = self.createHorizontalWall(particles, main_ax=Configs.window_size-1)
            particles = self.createHorizontalWall(particles, main_ax=0)
        return particles

