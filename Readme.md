Example project how to use gRPC, Conan and CMake

# C++ side
```
cmake -S . -B build
cmake --build build --parallel 12 --config Release
./build/src/Release/main.exe
```

# Python side
```
python -m venv .venv
. .venv/Scripts/activate
python -m pip install -r requirements.txt
python src/client.py
```

# Docker

```
docker build -t grpctest .
docker run --rm -it -p 50051:50051 grpctest build/bin/main
```
