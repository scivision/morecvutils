cmake_minimum_required(VERSION 2.8.12)
project( morecvutils Fortran )

add_compile_options(-mtune=native -Wall -Wextra -pedantic -Werror=array-bounds -fexceptions -fstack-protector-all)

add_library(lineclip lineclipping.f90)

add_executable(run_lineclip test_lineclipping.f90)
target_link_libraries(run_lineclip lineclip)
