import matplotlib.pyplot as plt

from Configs import Configs


class Helper:

    @staticmethod
    def simulate_dla(particles: (float, float, float)):
        fig, ax = plt.subplots()

        for particle in particles:
            x = particle[0]
            y = particle[1]
            r = particle[2]
            #print(x, y, r)
            circle = plt.Circle((x, y), r, color='r', clip_on=False)
            ax.add_patch(circle)
        ax.set_xlim((0, Configs.width_size))
        ax.set_ylim((0, Configs.height_size))
        plt.show()
        plt.savefig('images/' + Configs.file_name + '.png', dpi=200, bbox_inches = 'tight')
