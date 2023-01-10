# pacs_report_examples
Collection of implemented &amp; tested examples as reported in the submitted project 

## Installation 

### Prereqs 
Before proceeding with the steps in this setup you need to first build [lifex/pyfex](https://gitlab.com/lifex/pyfex) locally according to the listed steps (assuming you have access privileges).

After this you can proceed with the cloning of the repo through 
```
git clone https://github.com/nnethercott/pacs_report_examples.git
```
and install from requirements with 
``` 
pip install -r requirements.txt
```

### Building examples
Within each example folder there is a mix of C++ and Python examples (this project dealt with exposing a Python interface to C++ libraries).  Running most of the Python examples is pretty straight forward except in the case where parallelism is employed.  For these scripts (indicated in the readme) execute as following:
```
mpirun -np j python3 ./file.py
```
where j is the number of processes you wish to execute on (for some examples we impose a maximum number of allowable ranks). 

For C++ executables and for building pybind modules we suggest you proceed through the use of cmake - and corresponding CMakeLists.txt files have been included to handled everything neatly.  Life will be extremely simple if you're using the suggested toolchain as was instructed in the pyfex build.  Please note that you will need to provide a path to the pyfex copy of the pybind11 project (or else you can clone it seperately from [here](https://github.com/pybind/pybind11).  To do this, simply run the following from within the example directory 
```
mkdir build && cd build && cmake ..
make 
```
Then run as you see fit!
