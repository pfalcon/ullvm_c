# ullvm - Lightweight bindings for LLVM C API
#
# This module is part of the Pycopy https://github.com/pfalcon/pycopy
# project.
#
# Copyright (c) 2018 Paul Sokolovsky
#
# The MIT License

import ffi
from array import array


L = ffi.open("/usr/lib/llvm-6.0/lib/libLLVM.so")

def F(ret, name, params):
    globals()[name] = L.func(ret, name, params)

LLVMAbortProcessAction = 0
LLVMPrintMessageAction = 1
LLVMReturnStatusAction = 2

F("P", "LLVMInt32Type", "")
F("P", "LLVMFunctionType", "PPIi")
F("P", "LLVMModuleCreateWithName", "s")
F("i", "LLVMVerifyModule", "PIp")
F("P", "LLVMAddFunction", "PsP")
F("P", "LLVMAppendBasicBlock", "Ps")
F("P", "LLVMCreateBuilder", "")
F("v", "LLVMPositionBuilderAtEnd", "PP")
F("P", "LLVMGetParam", "PI")
F("P", "LLVMBuildAdd", "PPPs")
F("P", "LLVMBuildRet", "PP")
F("v", "LLVMInitializeX86TargetInfo", "")
F("v", "LLVMInitializeX86Target", "")
F("v", "LLVMInitializeX86TargetMC", "")
F("v", "LLVMInitializeX86AsmPrinter", "")
F("v", "LLVMInitializeX86AsmParser", "")
F("i", "LLVMCreateExecutionEngineForModule", "pPp")
F("P", "LLVMCreateGenericValueOfInt", "Pqi")
F("P", "LLVMRunFunction", "PPIP")
F("Q", "LLVMGetFunctionAddress", "Ps")


def by_ref(type):
    if type in ("p", "P", "s"):
        type = "L"
    return array(type, [0])
