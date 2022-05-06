#!/usr/bin/env python
# coding: utf-8

# # <center>Crout's Algorithm</center>

# In[1]:


#calculate the time taken by the program to run
#use the time module
import time
#starting time
start = time.time()

import pprint #import pprint to print tables in a clearer way
import numpy as np #to manipulate numerical data

#DEFINITION OF THE CROUT FUNCTION (takes as arguments the matrix A)
def crout(A):
    #initialize an array of size n to L and U, with zeros.
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    #Crout's method is only possible if the determinant of A is not zero => A is an invertible matrix.
    if np.linalg.det(A)==0: #linalg function provides efficient low level implementations of standard linear algebra algorithms.
        #exit the program.
        sys.exit("A is not invertible!")
        
    #L and U are lower and upper triangular matrices respectively.
    #the elements on the diagonal of U must be = 1
    for i in range(0, n):
        U[i][i]=1.0
        
    #calculation of L and U: "crout's method". 
        for j in range(i, n):
            sum0= sum([L[j][k]*U[k][i] for k in range(0,j)])
            L[j][i]= A[j][i] - sum0
        for j in range(i+1, n):
            sum1= sum([L[i][k]*U[k][j] for k in range(0,j)])
            U[i][j]= (A[i][j]-sum1)/L[i][i]
            
    #print the two matrices L and U
    print("L:")
    pprint.pprint(L)
    
    print("U:")
    pprint.pprint(U)
    
#MAIN PROGRAM:

#enter the size of the matrix A: n
n=int(input('enter size of the matrix: '))

#initialize to zero an array of size n x n for the matrix A
A=np.zeros((n,n))

#read the coefficients of the augmented matrix entered by user
print('Enter Augmented Matrix Coefficients: ')
for i in range (n):
    for j in range (n):
        A[i][j]=float(input('a['+str(i)+']['+str(j)+'] = '))
        
#call the crout function and see the results!
crout(A)
#Example : n=3 and A=np.array([[60.0,30.0,20.0], [30.0,20.0,15.0], [20.0,15.0,12.0]])

#sleep for 1 second to let the program run
time.sleep(1)

#program body ends

#end time
end = time.time()

#total taken time = end_time - starting_time
print(f"Runtime of the program is {end - start} secondes")


# In[ ]:




