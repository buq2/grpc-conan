
get_filename_component(hw_proto "service.proto" ABSOLUTE)
get_filename_component(hw_proto_path "${hw_proto}" PATH)

set(hw_proto_srcs "${CMAKE_CURRENT_BINARY_DIR}/service.pb.cc")
set(hw_proto_hdrs "${CMAKE_CURRENT_BINARY_DIR}/service.pb.h")
set(hw_grpc_srcs "${CMAKE_CURRENT_BINARY_DIR}/service.grpc.pb.cc")
set(hw_grpc_hdrs "${CMAKE_CURRENT_BINARY_DIR}/service.grpc.pb.h")
add_custom_command(
      OUTPUT "${hw_proto_srcs}" "${hw_proto_hdrs}" "${hw_grpc_srcs}" "${hw_grpc_hdrs}"
      COMMAND ${Protobuf_PROTOC_EXECUTABLE}
      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
        --python_out "${CMAKE_CURRENT_BINARY_DIR}"
        -I "${hw_proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        "${hw_proto}"
      DEPENDS "${hw_proto}")
add_library(hw_proto_obj OBJECT ${hw_proto_srcs} ${hw_grpc_srcs})
include_directories("${CMAKE_CURRENT_BINARY_DIR}")


#add_custom_command(
#      OUTPUT "${hw_grpc_srcs}" "${hw_grpc_hdrs}"
#      COMMAND protobuf::protoc
#      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}" -I "${CMAKE_CURRENT_SOURCE_DIR}"
#        --plugin=protoc-gen-grpc="${gRPC_CPP_PLUGIN_EXECUTABLE}"
#        "${protos}"
#      DEPENDS "${protos}")

  #MESSAGE(${_PROTOBUF_PROTOC})
  #MESSAGE(${hw_grpc_srcs})
  #MESSAGE(${hw_grpc_srcs})
  #MESSAGE(${hw_grpc_srcs})

# Generated include directory
include_directories("${CMAKE_CURRENT_BINARY_DIR}")

add_executable(main main.cpp
    )

target_link_libraries(main
    hw_proto_obj
    gRPC::grpc++_unsecure
    #${CONAN_LIBS}
    #protobuf::libprotoc
    #protobuf
    #gRPC::grpc++_unsecure
    #${Protobuf_LIBRARIES}
    #grpc++_reflection
    #${CONAN_PKG_LIBS_ABSEIL}
    )
