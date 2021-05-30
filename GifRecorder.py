from Recorder import Recorder
import imageio
import matplotlib.pyplot as plt
import os

class GifRecoder(Recorder):
    def __init__(self, dla = None):
        super(GifRecoder, self).__init__(dla=dla)
        self.states = []
        self.count = 0

    def record(self):
        label = "Number particles "+str(self.dla.num_hits)
        plt.title(label, fontsize=20)
        plt.imshow(self.dla.surface_matrix, cmap='hot', interpolation='nearest')
        plt.savefig("images/cluster{}.png".format(self.count), dpi=200)
        plt.close()
        self.count+=1

    def export_result(self):
        self.record()
        with imageio.get_writer('images/movie.gif', mode='I') as writer:
            for i in range(self.count):
                filename="images/cluster"+str(i)+".png"
                image = imageio.imread(filename)
                writer.append_data(image)
                os.remove(filename)
