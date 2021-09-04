
get_filename_component(hw_proto "service.proto" ABSOLUTE)
get_filename_component(hw_proto_path "${hw_proto}" PATH)

set(hw_proto_srcs "${_gRPC_PROTO_GENS_DIR}/service.pb.cc")
set(hw_proto_hdrs "${_gRPC_PROTO_GENS_DIR}/service.pb.h")
set(hw_grpc_srcs "${_gRPC_PROTO_GENS_DIR}/service.grpc.pb.cc")
set(hw_grpc_hdrs "${_gRPC_PROTO_GENS_DIR}/service.grpc.pb.h")

#add_custom_command(
#      OUTPUT "${hw_proto_srcs}" "${hw_proto_hdrs}" "${hw_grpc_srcs}" "${hw_grpc_hdrs}"
#      COMMAND ${Protobuf_PROTOC_EXECUTABLE}
#      ARGS --grpc_out "${CMAKE_CURRENT_BINARY_DIR}"
#        --cpp_out "${CMAKE_CURRENT_BINARY_DIR}"
#        --python_out "${CMAKE_CURRENT_BINARY_DIR}"
#        -I "${hw_proto_path}"
#        --plugin=protoc-gen-grpc="${GRPC_CPP_PLUGIN_PROGRAM}"
#        #--plugin=protoc-gen-grpc="${GRPC_PYTHON_PLUGIN_PROGRAM}"
#        "${hw_proto}"
#      DEPENDS "${hw_proto}")

protobuf_generate_grpc_cpp(service.proto)
add_library(hw_proto_obj OBJECT ${hw_proto_srcs} ${hw_grpc_srcs})
target_include_directories(hw_proto_obj PUBLIC "${_gRPC_PROTO_GENS_DIR}")

add_executable(main main.cpp
    )

target_link_libraries(main
    hw_proto_obj
    gRPC::grpc++_unsecure
    )
