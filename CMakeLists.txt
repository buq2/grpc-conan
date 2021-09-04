cmake_minimum_required(VERSION 3.15)
project(grpctest VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)

# Run conan install automatically, or display warning if conan is not installed
include(cmake/conan_config.cmake)
include(cmake/grpc_extras.cmake)

find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)

add_subdirectory(src)
