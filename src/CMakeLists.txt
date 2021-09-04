protobuf_generate_grpc_cpp(GRPC_SRCS GRPC_HDRS service.proto)

add_executable(main main.cpp
    ${GRPC_SRCS} ${GRPC_HDRS}
    )

target_include_directories(main PUBLIC "${_gRPC_PROTO_GENS_DIR}")

target_link_libraries(main
    gRPC::grpc++_unsecure
    )
