cmake_minimum_required(VERSION 3.22)
project(template)

set(DEFAULT_WARNINGS -Wall -Wextra)
set(CMAKE_CXX_STANDARD 20)

add_subdirectory(deps)
add_subdirectory(src)
add_subdirectory(lib)
add_subdirectory(test)

# Build main program
add_executable(template main.cpp)
target_include_directories(template PRIVATE .)
target_compile_options(template PRIVATE ${DEFAULT_WARNINGS})
