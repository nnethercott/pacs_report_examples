import sys
sys.path.insert(1, './build')

from hello_module import hello
from mpi4py import MPI #starts and terminates MPI environment

hello()
