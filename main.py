from Configs import Configs
from ConstantStickDistribution import ConstantStickDistribution
from DLA import DLA
from DirectionalBias import DirectionalBias
from GeneralDLA import GeneralDLA
from GeneralDLA2 import GeneralDLA2

# stickDist = ConstantStickDistribution(proba=0.6)
# dla = DLA(radius_limit=200,numParticles=5000,stickDistribution=stickDist)
# dla.simulate()


# stickDist = ConstantStickDistribution(proba=0.6)
# dla = GeneralDLA(limit_radius=30,num_particle=100,stick_distribution=stickDist)
# dla.simulate("demo")

## 8 direction : left, right,bottom, top, equator, meridian, center, edges
Configs.direction_bias=DirectionalBias('edges')

dla=GeneralDLA2()
dla.simulate("result_general_dla")



