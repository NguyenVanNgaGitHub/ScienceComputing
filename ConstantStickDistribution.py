from StickDistribution import StickDistribution

class ConstantStickDistribution(StickDistribution):
    def __init__(self, dla = None,proba : float=0.5):
        super(ConstantStickDistribution, self).__init__(dla=dla)
        self.proba = proba

    def compute_proba(self, pos : (int,int)) -> float:
        return self.proba