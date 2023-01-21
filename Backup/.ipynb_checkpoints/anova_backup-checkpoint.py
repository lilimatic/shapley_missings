
## ANOVA BACKUP

#Full variance (same of each, as Y is always observed)

df = pd.DataFrame(np.random.uniform(0,1,size=(n, d)))

df['Y'] =  np.sin(df[0]) + a* np.sin(df[1])**2  + b* np.sin(df[2])**4 


V = np.var(df['Y'])

#grand mean 
mu = np.mean(df['Y'])

#main effects

m1 = np.sin(df[0]) - np.mean(np.sin(df[0])) - mu  

m2 = a* np.sin(df[1])**2 - np.mean(a* np.sin(df[1])**2) - mu 

m3 = b* np.sin(df[2])**4  - np.mean(b* np.sin(df[2])**4) -mu

m12 = df['Y'] - m1 - m2 -m3 - mu

#ANOVA
anova = mu + m1 + m2 + m3 + m12

# Is decomposition successful ? 

np.max(abs(df['Y'] - anova)) < 10e-15 #Yes

#Variance decomposition check 

sigma1 = np.var(m1)
sigma2 = np.var(m2)
sigma12 = np.var(m12)
sigma3 = np.var(m3)

#Sanity check 
abs(sigma1 + sigma2 + sigma3 + sigma12 - V) < 10e-5 #bis auf 5. Nachkommastelle