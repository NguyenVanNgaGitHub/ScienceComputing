from ConstantStickDistribution import ConstantStickDistribution


class Configs:
    # Window Size
    window_size=100

    figure_size=5

    # Number of particles (exclude particle on original cluster)
    num_particles=1000

    radius_particle=1
    num_walkers=50

    # Length per step
    force_bias=1

    add_cluster_toward_force = False
    color_num = 5

    # Distribution determine probability stick when a walker collide a particle on cluster
    distribution=ConstantStickDistribution(proba=0.6)

    # Added toward-cluster force
    # Cluster in center => add a toward-center force on walker
    direction_bias=None

    # File show result
    file_name="demo"

    enable_log= True
