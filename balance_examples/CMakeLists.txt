#boilerplate
cmake_minimum_required(VERSION 3.8)
project(IMBALANCED VERSION 1.0 LANGUAGES CXX)

# Force compiler to use C++17 standard.
set(CMAKE_CXX11_STANDARD_COMPILE_OPTION -std=c++17)
set(NATE_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS "${NATE_FLAGS}")

################### deal.II ##################################
# Locate deal.II and initialize its variables.
find_package(deal.II 9.2.0 REQUIRED
  HINTS ${DEAL_II_DIR} $ENV{DEAL_II_DIR} $ENV{mkDealiiPrefix}
)
deal_ii_initialize_cached_variables()

##############################################################
add_executable(imap ./imbalanced_index_map.cpp)
DEAL_II_SETUP_TARGET(imap)
