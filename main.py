import time
from ConstantStickDistribution import ConstantStickDistribution
from DLA import DLA
from GeneralDLA import GeneralDLA

stickDist = ConstantStickDistribution(proba=0.6)

# dla = DLA(radius_limit=200, numParticles=5000, stickDistribution=stickDist, result_name_file='result_2')
#
# start = time.time()
# dla.simulate()
# end = time.time()
# print('Time dla:', end - start)
# print(dla.num_hits)


g_dla = GeneralDLA(limit_radius=200, num_particle=100, stick_distribution=stickDist, bias=0)
g_dla.simulation(file_name='test_general_dla')