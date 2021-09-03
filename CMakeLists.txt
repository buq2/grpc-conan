cmake_minimum_required(VERSION 3.15)
project(libalgo VERSION 1.0.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)

#enable_testing()

# Run conan install automatically, or display warning if conan is not installed
include(cmake/conan_config.cmake)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()

if(MSVC)
  add_definitions(-D_WIN32_WINNT=0x600)
endif()
#set(CMAKE_CXX_STANDARD 11)


set(protobuf_MODULE_COMPATIBLE TRUE)
find_package(Protobuf REQUIRED)
message(STATUS "Using protobuf ${protobuf_VERSION}")

#set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
#set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)

# Find gRPC installation
find_package(gRPC REQUIRED)
#find_package(protoc REQUIRED)
message(STATUS "Using gRPC ${gRPC_VERSION}")
#
set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)


get_filename_component(GRPC_PLUGIN_DIRECTORY ${GRPC_CPP_PLUGIN_PROGRAM} DIRECTORY)
find_program(GRPC_PYTHON_PLUGIN_PROGRAM 
  NAMES grpc_python_plugin 
  PATHS ${GRPC_PLUGIN_DIRECTORY}
  NO_DEFAULT_PATH)

add_subdirectory(src)

#option(BUILD_TESTS "Test with code coverage" TRUE)
#IF (BUILD_TESTS)
#    add_subdirectory(test)
#ENDIF()
