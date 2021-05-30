import random
import math
from DLA import DLA
from StickDistribution import StickDistribution
from math import sqrt


def get_round(x):
    q = math.floor(x)
    r = x - q
    if r < random.random():
        return q
    else:
        return q + 1


class DLABias(DLA):
    def __init__(self, radius_limit: int, numParticles: int, stickDistribution: StickDistribution, bias_type='center',
                 angle_value=0, bias_force=2):
        DLA.__init__(self, radius_limit, numParticles, stickDistribution)
        self.bias_force = bias_force
        self.bias_type = bias_type
        self.angle_value = angle_value / 180 * math.pi

    def genStep(self, pos: (int, int)) -> (bool, (int, int)):
        step = random.choice(self.nnStepsPos)
        if self.bias_type == 'center':
            if pos[0] == 0 and pos[1] == 0:
                alpha = 0
            else:
                alpha = 1 - self.bias_force / sqrt(pos[0] * pos[0] + pos[1] * pos[1])
            new_pos = (get_round(pos[0] * alpha) + step[0], get_round(pos[1] * alpha) + step[1])
        elif self.bias_type == 'up':
            new_pos = (get_round(pos[0] + step[0] + self.bias_force), get_round(pos[1] + step[1]))
        elif self.bias_type == 'down':
            new_pos = (get_round(pos[0] + step[0] - self.bias_force), get_round(pos[1] + step[1]))
        elif self.bias_type == 'right':
            new_pos = (get_round(pos[0] + step[0]), get_round(pos[1] + step[1] - self.bias_force))
        elif self.bias_type == 'left':
            new_pos = (get_round(pos[0] + step[0]), get_round(pos[1] + step[1] + self.bias_force))
        elif self.bias_type == 'angle':
            new_pos = (get_round(pos[0] + step[0] + math.sin(self.angle_value)),
                       get_round(pos[1] + step[1] - math.cos(self.angle_value)))

        return self.inKeepCircle(new_pos), new_pos
