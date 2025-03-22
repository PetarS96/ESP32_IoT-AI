# Minimum required version of CMake
cmake_minimum_required(VERSION 3.16)

# Register the component (your application code)
idf_component_register(
    SRCS "app_main.cpp"              # List all your source files here
    INCLUDE_DIRS "."           # List all your include directories here
)