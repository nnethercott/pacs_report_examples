#include <iostream>
#include "mpi.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

void hello()
{
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    std::cout << "hi from rank: " << rank << std::endl;
}

PYBIND11_MODULE(hello_module, m)
{
    m.doc() = "module for mpi hello world!";

    m.def("hello", &hello, "says hello from each rank");
}
