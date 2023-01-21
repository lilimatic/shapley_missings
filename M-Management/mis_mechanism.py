import numpy as np
import pandas as pd
import random

#Set seed 


class Missingness_mechanism:
    
    def __init__(self,d,n,p,df):
        #Dimension
        self.d = d
        #Number of observations
        self.n = n
        #MCAR Bernoulli prob.
        self.p = p
        
        random.seed(25)
        
        self.df = df
        
    def Hsample(self):
        return self.df
    
    def ishigami(self):
        return lambda a, b: np.sin(self.df[0]) + a * np.sin(self.df[1])**2 + b * (self.df[2])**4 * np.sin(self.df[0])
        
    #MCAR missing data mechanism
    def mcar(self):
        return pd.DataFrame(np.random.binomial(size=(self.n,self.d), n=1, p= self.p))
    
    #Callable function that depends on missingness mechanism
    def data_missing(self):
        return lambda x: self.df[x == 1]
    
    def sample(self, a, b):
        return self.data_missing()(self.mcar()).assign(Y = self.ishigami()(a, b))
    
    #Complete case analysis
    def cc(self,a,b):
        return lambda x: self.sample(a,b).dropna()
    
    def grand_mean(self,a,b,method,mechanism):
        if method == 'h-sample':
            return np.mean(self.ishigami()(a, b))
        elif method == 'cc':
            #print('Complete case')
            return np.mean(self.cc(a,b)(mechanism)['Y'])


        
        
        #Sanity check 1 
        #if (self.df['Y']-(mu + m1 + m2 +m12))<1e-3:
         #   print("Sufficient precision")
        #Variance contribution 
        
        