from ConstantStickDistribution import ConstantStickDistribution
from LocalCurvatureAtThePointOfContactStickDistribution import LocalCurvatureAtThePointOfContactStickDistribution
from NumberOfNeighboringParticlesStickDistribution import NumberOfNeighboringParticlesStickDistribution

from DLA import DLA

# stickDist = ConstantStickDistribution(proba=0.6)

# stickDist = LocalCurvatureAtThePointOfContactStickDistribution(A = 1, B = 0.1, percent_box= 80)

stickDist = NumberOfNeighboringParticlesStickDistribution(A = 0.6, B = 0.4, percent_box=75)

dla = DLA(radius_limit=100,numParticles=1000,stickDistribution=stickDist)

dla.simulate()


