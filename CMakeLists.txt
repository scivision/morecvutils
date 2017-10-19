cmake_minimum_required(VERSION 2.8.12)
project( morecvutils Fortran )

add_compile_options(-O3 -mtune=native)

if(${CMAKE_Fortran_COMPILER_ID} MATCHES "GNU")
  add_compile_options(-Wall -Wextra -Wpedantic -Werror=array-bounds -fexceptions -fstack-protector-all)
endif()

add_library(lineclip lineclipping.f90)

add_executable(RunLineclip DemoLineclip.f90)
target_link_libraries(RunLineclip lineclip)
