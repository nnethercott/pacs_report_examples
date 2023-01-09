#include <iostream>
#include <deal.II/lac/trilinos_vector.h>
#include <deal.II/base/index_set.h>
#include "mpi.h"

using dealii::TrilinosWrappers::MPI::Vector, dealii::IndexSet;

void example(){
  IndexSet i(3); //index sets of global size: 3
  IndexSet j(3);

  //process info
  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  //different index partitions
  if(rank == 0){
      i.add_index(0);
      i.add_index(1);

      j.add_index(0);
  }
  else{
      i.add_index(1);

      j.add_index(1);
      j.add_index(2);
  }

  //both are vectors of global size 3
  Vector v(i);
  Vector w(j);

  //populate vectors ...
  for(auto e: v.locally_owned_elements()){
    v[e] = 1;
  }
  for(auto e: w.locally_owned_elements()){
    w[e] = 1;
  }

  double inner_product = v*w; //operator defined within class
  if(rank == 0){
    std::cout<<inner_product<<std::endl;
  };
}

int main(){
  MPI_Init(NULL, NULL);
  example();
  MPI_Finalize();
}
