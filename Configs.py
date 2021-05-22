from ConstantStickDistribution import ConstantStickDistribution


class Configs:
    # Window Size
    width_size=200
    height_size=200

    # Number of particles (exclude particle on original cluster)
    num_particles=500

    num_walkers=100

    # Radius of particle
    radius_particle=1

    # Length per step
    force_bias=2

    # From to 0% to 100%
    delta_distance_percentage=10

    # Distribution determine probability stick when a walker collide a particle on cluster
    distribution=ConstantStickDistribution(proba=0.6)

    # Added toward-cluster force
    # Cluster in center => add a toward-center force on walker
    direction_bias=None

    # File show result
    file_name="demo"
