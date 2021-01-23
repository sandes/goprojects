import os
import ctypes


lib = ctypes.CDLL("./hello.so", mode=ctypes.RTLD_GLOBAL)

print(lib.findLower([23,4,77,2,99]))