#boilerplate
cmake_minimum_required(VERSION 3.8)
project(EXAMPLE1 VERSION 1.0 LANGUAGES CXX)

# Force compiler to use C++17 standard.
set(CMAKE_CXX11_STANDARD_COMPILE_OPTION -std=c++17)
set(NATE_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS "${NATE_FLAGS}")


################### pybind11 ##################################
include_directories(SYSTEM pybind11/include)
include_directories(SYSTEM $ENV{mkPythonInc})
add_subdirectory(/root/lifex_mnt/pyfex/pybind11 ../)
set(PYBIND11_LTO_CXX_FLAGS "OFF" CACHE INTERNAL "")
set(PYBIND11_LTO_LINKER_FLAGS "OFF" CACHE INTERNAL "")

##############################################################
pybind11_add_module(BaseDerived ./pybind_example.cpp)

