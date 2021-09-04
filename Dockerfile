from conanio/gcc10

COPY . .
RUN cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build --parallel 12

# Using "universal entrypoint" to make ctrl-c quit the application
ENTRYPOINT [ "/home/conan/docker-entrypoint.sh" ]
