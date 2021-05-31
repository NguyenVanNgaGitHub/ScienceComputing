from Recorder import Recorder
import matplotlib.pyplot as plt

class ImageRecoder(Recorder):
    def __init__(self, dla = None, name_file=None):
        super(ImageRecoder, self).__init__(dla=dla)
        self.name_file = name_file

    def record(self):
        pass

    def export_result(self):
        label = "Final state: Number particles in aggregation " + str(self.dla.num_hits)
        plt.title(label, fontsize=20)
        plt.imshow(self.dla.surface_matrix, cmap='hot', interpolation='nearest')
        plt.savefig("images/" + self.name_file + ".png", dpi=200, bbox_inches = 'tight')
        plt.close()
