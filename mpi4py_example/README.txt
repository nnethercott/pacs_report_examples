second example from report illustrating the use of mpi4py as a surrogate for MPI on the python side.
in the CMakeLists we leverage the DEAL_II_SETUP_TARGET macro to resolve mpi symbols instead of changing compiler settings from the script itself.

run test script using "mpirun -np j python3 ./test.py"
