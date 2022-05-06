#!/usr/bin/env python
# coding: utf-8

# # <center> Gauss Elimination Algorithm </center>

# In[3]:


# Importing NumPy Library
import numpy as np
import sys

#enter the size of the matrix A: n
n = int(input('Enter number of unknowns: '))

# initialize to zero an array of size n x n+1 for the augmented matrix A
a = np.zeros((n,n+1))

#initialize to zero an array of size n for the solution vector
x = np.zeros(n)

#read the coefficients of the augmented matrix entered by user
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0: #to avoid devide by zero error
        sys.exit('Divide by zero detected!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]
#Note: All array indexes are assumed to start from 1.

#Lets's see the results!
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

#Example:
#a=np.array([[1.0,1.0,1.0, 1.0],[1.0,-1.0,-1.0, 1.0],[1.0,-2.0,3.0, -5.0]])


# In[ ]:




