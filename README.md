# template
Contains a standard project structure with template files for a C++ project.
CMake is configured to run `clang-tidy` when building the main-executable.

### Build
Use `scripts/build.py` when building this project.

`./scripts/build.py -a` will run all configured tools: `clang-format`, `CMake`, `clang-tidy` and then build the project.