import sys
import numpy as np
import os
from mpi4py import MPI

sys.path.insert(1, '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9')
import arrayBind as ab

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
################################################

#Let's instantiate the vector in 3 ways and use some of the functions we proposed

#Vector block-wise init -- same convention as dealii vectors
v_data = None
if(rank == 0):
    v_data = np.array([1,2,3,4]) #unbalanced
elif(rank == 1):
    v_data = np.array([5])
else:
    v_data = np.empty(0)

v = ab.NVector(v_data)

#now balance & print
v.balance()
#v.print()


#Vector init with default size and fill value
w = ab.NVector(5, -1)
#w.print()



#Vector default init & populate with collective append()/concat
z = ab.NVector()
z.append(1);
z.concat([5,4,3,2])
#z.print()


#################################################

#misc utility functions
norms_equal = v.l2_norm() == z.l2_norm()
v_dot_w = v*w
z_manual_2norm = np.sqrt(z*z)
z_2norm = z.l2_norm()

if(rank == 0):
    print(f'norms of v and w equal? ->{norms_equal}')
    print(f'v dot w = {v_dot_w}')
    print(f'z 2-norm by hand: {z_manual_2norm}; built in: {z_2norm}')
    #print(dir(z))
