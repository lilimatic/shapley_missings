class sobol:
    def __init__(self,f):
        self.f = f
        
    def grand_mean(self):
        return lambda x: np.mean(self.f(x))
    
def main():
    
    def sin(x):
        return np.sin(x)

    trial = sobol(sin)

    trial.grand_mean()(pd.DataFrame(np.random.uniform(0,1,size=(100, 8)))[0])