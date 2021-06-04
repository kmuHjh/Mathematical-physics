import numpy as np
import pylab as pl
print("17.1")
arr = np.array([8.8,9.5,9.8,9.4,10.0,9.4,10.1,9.2,11.3,9.4,10.0,10.4,7.9,10.4,9.8,9.8,9.5,8.9,8.8,10.6,10.1,9.5,9.6,10.2,8.9])
print("the mean :" , np.mean(arr))
print("the standard deviation :", np.std(arr, ddof=1))
print("the variance : ", np.var(arr,ddof=1))
print("the coefficient of variation : ", np.var(arr,ddof=1)/np.mean(arr))
print("the 95% confidence interval for the mean : " , np.mean(arr)-2*np.std(arr, ddof=1),"~",np.mean(arr)+2*np.std(arr, ddof=1) )
b = np.array([7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5])
pl.hist(arr, bins=b, rwidth=0.5)

