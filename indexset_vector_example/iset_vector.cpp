/*
A quick test script to make sure we can correctly link dealii objects within the
cluster environment
*/

// dealii
#include <deal.II/base/index_set.h>
#include <deal.II/lac/trilinos_vector.h>

// standard
#include <iostream>
#include "mpi.h"

void example()
{
    using dealii::IndexSet, dealii::TrilinosWrappers::MPI::Vector;

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    IndexSet parallel_partitioning(size * 5);
    parallel_partitioning.add_range(rank * 5, (rank + 1) * 5);

    parallel_partitioning.print(std::cout);

    Vector v(parallel_partitioning);
}

int main()
{
    MPI_Init(NULL, NULL);
    example();
    MPI_Finalize();
}
