from ConstantStickDistribution import ConstantStickDistribution
from DLA import DLA

stickDist = ConstantStickDistribution(proba=0.6)
dla = DLA(radius_limit=200,numParticles=5000,stickDistribution=stickDist)

dla.simulate()


