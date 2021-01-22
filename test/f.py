import os
import ctypes


lib = ctypes.CDLL("./hello.so", mode=ctypes.RTLD_GLOBAL)

print(lib.Add(2,1))