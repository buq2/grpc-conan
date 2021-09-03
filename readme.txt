
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
