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

# LLVMCodeGenOptLevel;
LLVMCodeGenLevelNone = 0
LLVMCodeGenLevelLess = 1
LLVMCodeGenLevelDefault = 2
LLVMCodeGenLevelAggressive = 3

# LLVMRelocMode;
LLVMRelocDefault = 0
LLVMRelocStatic = 1
LLVMRelocPIC = 2
LLVMRelocDynamicNoPic = 3

# LLVMCodeModel;
LLVMCodeModelDefault = 0
LLVMCodeModelJITDefault = 1
LLVMCodeModelSmall = 2
LLVMCodeModelKernel = 3
LLVMCodeModelMedium = 4
LLVMCodeModelLarge = 5

F("P", "LLVMInt32Type", "")
F("P", "LLVMFunctionType", "PPIi")
F("P", "LLVMModuleCreateWithName", "s")
F("i", "LLVMVerifyModule", "PIp")
F("P", "LLVMAddFunction", "PsP")
F("P", "LLVMAppendBasicBlock", "Ps")
F("P", "LLVMCreateBuilder", "")
F("v", "LLVMPositionBuilderAtEnd", "PP")
F("P", "LLVMGetParam", "PI")
F("P", "LLVMConstInt", "PQI")
F("P", "LLVMBuildAdd", "PPPs")
F("P", "LLVMBuildNeg", "PPs")
F("P", "LLVMBuildRet", "PP")
F("v", "LLVMInitializeX86TargetInfo", "")
F("v", "LLVMInitializeX86Target", "")
F("v", "LLVMInitializeX86TargetMC", "")
F("v", "LLVMInitializeX86AsmPrinter", "")
F("v", "LLVMInitializeX86AsmParser", "")
F("s", "LLVMGetDefaultTargetTriple", "")
F("i", "LLVMGetTargetFromTriple", "spp")
F("i", "LLVMTargetHasJIT", "P")
F("P", "LLVMCreateTargetMachine", "PsssIII")
F("i", "LLVMCreateExecutionEngineForModule", "pPp")
F("P", "LLVMCreateGenericValueOfInt", "Pqi")
F("P", "LLVMRunFunction", "PPIP")
F("Q", "LLVMGetFunctionAddress", "Ps")

F("P", "LLVMOrcMakeSharedModule", "P")
F("P", "LLVMOrcCreateInstance", "P")
F("i", "LLVMOrcAddEagerlyCompiledIR", "PpPCp")
F("i", "LLVMOrcAddLazilyCompiledIR", "PpPCp")
F("i", "LLVMOrcGetSymbolAddress", "Pps")


def by_ref(type):
    if type in ("p", "P", "s"):
        type = "L"
    return array(type, [0])
