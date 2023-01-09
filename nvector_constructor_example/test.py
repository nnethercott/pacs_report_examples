import numpy as np
from mpi4py import MPI #third-party
import sys

#import pyfex arraybind module
sys.path.insert(1, '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9')
from arrayBind import NVector

#start MPI environment
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

local_block = None
if rank == 0:
    local_block = np.array([0,1,2]) #rank 0 holds vector block with elements [0,1,2]
else:
    local_block = np.array([3,4]) #rank 1 holds vector block with elements [3,4]

n = NVector(local_block) #collective construction
n.print()
