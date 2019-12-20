# ullvm - Lightweight bindings for LLVM C API
#
# This module is part of the Pycopy https://github.com/pfalcon/pycopy
# project.
#
# Copyright (c) 2019 Paul Sokolovsky
#
# The MIT License

dynlib = "/usr/lib/x86_64-linux-gnu/libLLVM-6.0.so"

def init(lib):
    global dynlib
    dynlib = lib
