import numpy as np
import pandas as pd

#Ishigami parameters
a = 0.5
b = 0.7

class ANOVA_ishigami:
    def __init__(self,df):
        self.df = df
    
    def functional_anova(self):
        #main effects
        mu = np.mean(self.df['Y'])
        m1 = np.sin(self.df[0]) - np.mean(np.sin(self.df[0])) - mu 
        m2 = a* np.sin(self.df[1])**2 - np.mean(a* np.sin(self.df[1])**2) - mu 
        m3 = b* (self.df[2])**4  - np.mean(b* (self.df[2])**4) -mu
        m12 = self.df['Y'] - m1 - m2 -m3 - mu
        #if (self.df['Y']-(mu + m1 + m2 + m3 +m12)):
        #raise ValueError():
        return [mu,m1,m2,m3,m12]
        
    def variance_anova(self):
        V = np.var(self.df['Y'])
        sigma1 = np.var(self.functional_anova()[1])
        sigma2 = np.var(self.functional_anova()[2])
        sigma3 = np.var(self.functional_anova()[3])
        sigma12 = np.var(self.functional_anova()[3])
        #Sanity check 
        if abs(sigma1 + sigma2 + sigma3 + sigma12 - V) < 10e-3:
            print("Sufficient precision")#bis auf 5. Nachkommastelle
        #returns singleton main effects
        return [sigma1/V,sigma2/V,sigma3/V]