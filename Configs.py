from ConstantStickDistribution import ConstantStickDistribution


class Configs:
    # Window Size
    width_size=200
    height_size=200

    # Number of particles (exclude particle on original cluster)
    num_particles=500

    # Radius of particle
    radius_particle=1

    # Length per step
    force_bias=2

    # Added To Stick Distance (between 2 particle,  default = 2 * radius_particle
    added_stick_distance_bias=0

    # Distribution determine probability stick when a walker collide a particle on cluster
    stick_distribution=ConstantStickDistribution(proba=0.6)

    # Added toward-cluster force
    # Cluster in center => add a toward-center force on walker
    direction_bias=None

    # File show result
    file_name="demo"
