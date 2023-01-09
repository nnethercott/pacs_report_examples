from mpi4py import MPI
import sys

#import pyfex arraybind module
sys.path.insert(1, '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9')
import arrayBind as ab

#start MPI environment
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

v = ab.NVector(5,0) #vector of global size 5 with fill value 0
w = v

if rank == 0:
    w[0] = 1
    print(f'v[0] = {v[0]}')

################## the solution ##################
from copy import deepcopy
u = deepcopy(w)

if rank == 0:
    u[0] = -999999999
    print(f'w[0] = {w[0]}')
