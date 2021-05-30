from ConstantStickDistribution import ConstantStickDistribution
from dla_bias import DLABias

stickDist = ConstantStickDistribution(proba=0.6)
dla = DLABias(radius_limit=200, numParticles=5000, stickDistribution=stickDist, bias_type='angle', angle_value=45,
              bias_force=1)

dla.simulate()
