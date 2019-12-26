ullvm_c
=======

This is a project to wrap LLVM C API using a Pycopy's
[ffi](https://pycopy.readthedocs.io/en/latest/library/ffi.html) module,
thus producing pure-Python bindings to a sufficiently large subset of LLVM
functionality. [Pycopy](https://github.com/pfalcon/pycopy) is a minimalist
implementation of the Python language. Pycopy's `ffi` module was also
[ported to CPython](https://github.com/pfalcon/pycopy-lib/tree/master/cpython-ffi),
so `ullvm_c` is compatible with CPython too (or any other Python
implementation which provides `ctypes` module).

Two examples are included, JIT-generating a simple function, using both
older MCJIT, and newer ORC LLVM JIT engines:

```
pycopy example_mcjit.py
pycopy example_orcjit.py
```

Licensing and copyright
-----------------------

Copyright (c) 2019 Paul Sokolovsky. Released under the terms of MIT license.
