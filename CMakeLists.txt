cmake_minimum_required(VERSION 3.22)
project(template)

set(DEFAULT_WARNINGS -Wall -Wextra)
set(CMAKE_CXX_STANDARD 20)

# Set up clang-tidy
find_program(CLANG_TIDY_EXE NAMES "clang-tidy")
set(CPLUS_INCLUDE_PATH "/usr/include/c++/11:/usr/include/x86_64-linux-gnu/c++/11")
set(CLANG_TIDY_COMMAND "${CLANG_TIDY_EXE}")

add_subdirectory(deps)
add_subdirectory(src)
add_subdirectory(lib)
add_subdirectory(test)

# Create main program target
add_executable(template main.cpp)
target_include_directories(template PRIVATE .)
target_compile_options(template PRIVATE ${DEFAULT_WARNINGS})
# Run clang-tidy when building the main target
set_target_properties(template PROPERTIES CXX_CLANG_TIDY "${CLANG_TIDY_COMMAND}")
