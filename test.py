import random as random
from math import  pi,cos,sin
from Configs import  Configs
from Particle import Particle
from DirectionalBias import DirectionalBias
def testRange():
    for i in range(4):
        print(i);


def testRanPos():
    for i in range(1000):
        x = int(random.random() * 10)
        y = int(random.random() * 10)
        print(x,y)

def testDiffusion():
    # Implementation for random walker
    d_bias= DirectionalBias("top")
    count_idle=0;
    count_far=0;
    for i in range(1000):
        force_bias=1
        angle = random.random() * 2 * pi
        step_length = random.randint(1, force_bias)
        dx = round(step_length * cos(angle))
        dy = round(step_length * sin(angle))

        #print(int(Configs.window_size/2)+dx,int(Configs.window_size/2)+dy)

        dx,dy=d_bias.addBiasForce(Particle(int(Configs.window_size/2)+dx,int(Configs.window_size/2)+dy,1))
        print(dx,dy)
        # if (abs(dx)+abs(dy))==0:
        #     count_idle = count_idle+1
        # if (abs(dx)>=2) or (abs(dy)>=2):
        #     count_far = count_far+1
    # print("Idle ",count_idle)
    # print("Far ",count_far)
        #print(dx,dy)
        #x, y = Configs.direction_bias.addBiasForce(walker)

testDiffusion()