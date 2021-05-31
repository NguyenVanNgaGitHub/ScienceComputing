from Recorder import Recorder
import matplotlib.pyplot as plt

class ImageRecoder(Recorder):
    def __init__(self, dla = None):
        super(ImageRecoder, self).__init__(dla=dla)

    def record(self):
        pass

    def export_result(self):
        label = "Final state: "+ str(self.dla.num_hits)+" particles in aggregation "
        plt.title(label, fontsize=20)
        plt.imshow(self.dla.surface_matrix, cmap='hot', interpolation='nearest')
        plt.savefig("images/final_result.png", dpi=200)
        plt.close()
