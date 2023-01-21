import numpy as np
import pandas as pd

#Ishigami parameters
a = 0.5
b = 0.7

class ANOVA:
    def __init__(self,df):
        self.df = df
        
    def linear_anova(self,beta1,beta2,beta3):
        
        #ANOVA 
        
        #Grand mean
        mu = np.mean(self.df['Y'])
        
        #main effects
        m1 = beta1*(self.df[0] - np.mean(self.df[0])) + beta3*(self.df[0] - np.mean(self.df[0]))*np.mean(self.df[1])
        m2 = beta2*(self.df[1] - np.mean(self.df[1])) + beta3*(self.df[1] - np.mean(self.df[1]))*np.mean(self.df[0])
        m12 = self.df['Y'] - m1 - m2 - mu
        
         #Variance contribution 
        print(self.df['Y'] -m1 -m2 -m12 -mu)
    
        V = np.var(self.df['Y'])
        sigma1 = np.var(m1)
        sigma2 = np.var(m2)
        sigma12 = np.var(m12)
        
        #print(V-sigma1-sigma2-sigma12)
        
        #Sanity check 2
        
        if abs(sigma1 + sigma2 + sigma12 - V) < 10e-3:
            print("Sufficient precision")#bis auf 5. Nachkommastelle
        
        #returns singleton main effects
        print('$\sigma$,$\sigma_{1}$,$\sigma_{2}$,$\sigma_{12}$')
        return [V,sigma1/V,sigma2/V,sigma12/V]
        
    
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