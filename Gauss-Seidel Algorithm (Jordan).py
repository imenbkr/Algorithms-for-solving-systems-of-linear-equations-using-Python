#!/usr/bin/env python
# coding: utf-8

# # <center>Gauss-Seidel Algorithm: Jordan</center>

# In[12]:


#calculate the time taken by the program to run
#use the time module
import time
#starting time
start = time.time()


import numpy as np
#Definition of gauss_seidel function which takes as arguments: matrixes(A and b), tolerance error (tolerance),
# maximum of iterations (max_iterations) and the solution vector (x).

def gauss_seidel(A, b, tolerance, max_iterations, x):
    
    iter1 = 0
    #Iterate
    for k in range(max_iterations):
        iter1 = iter1 + 1
        print ("The solution vector in iteration", iter1, "is:", x)    
        x_old  = x.copy()
        
        #Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
            
        #Stop condition :
        #LnormInf corresponds to the absolute value of the greatest element of the vector.
        
        with np.errstate(divide='ignore'):  #to avoid "RuntimeWarning: divide by zero encountered in true_divide"
            LnormInf =np.array(max(abs((np.array(x) - np.array(x_old)))/max(abs(np.array(x_old)))  ))

        print ("The L infinity norm in iteration", iter1,"is:", LnormInf)
        if  LnormInf < tolerance: #stop condition
            break
    
           
    return x

# initialize tolerance
tol= 1e-15
# initialize maximum iterations number
max_iterations = 1000
# initialize solution vector
x = [0.0, 0.0, 0.0, 0.0] 

# initialize the matrix
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6.0, 25.0, -11.0, 15.0])

gauss_seidel(A, b, tol, max_iterations, x)

#sleep pendant 1 seconde pour laisser le programme s'exécuter
time.sleep(1)

#program body ends

#end time
end = time.time()

#total taken time = end_time - starting_time
print(f"Runtime of the program is {end - start} secondes")


# In[ ]:




