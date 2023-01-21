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
        print('Decomposition precision:' + str(max(self.df['Y'] -m1 -m2 -m12 -mu)))
    
        V = np.var(self.df['Y'])
        sigma1 = np.var(m1)
        sigma2 = np.var(m2)
        sigma12 = np.var(m12)
        
        print('Percentage of total variance : $\sigma$,$\sigma_{1}$,$\sigma_{2}$,$\sigma_{12}$')
        return [V/V,sigma1/V,sigma2/V,sigma12/V]