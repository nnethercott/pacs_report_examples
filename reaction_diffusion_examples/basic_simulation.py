import sys
sys.path.insert(1, '/mnt/c/Users/naten/pyfex/build/lib.linux-x86_64-3.9')
from CoupledReactionDiffusion import *
from arrayBind import NVector #for extracting sim solutions

from mpi4py import MPI #third-party
comm = MPI.COMM_WORLD

#instantiation
d = CoupledReactionDiffusion()
d.model = "reaction_diffusion" # reaction_diffusion | diffusion

# Initialization
d.refinement_reaction_diffusion = 3
d.alpha = 1.5
d.beta = 1

#simulation
d.make_grid()
d.setup_system()
#d.solve_system()

#d_solution = NVector(d.solution)
