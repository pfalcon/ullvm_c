# ullvm - Lightweight bindings for LLVM C API
#
# This module is part of the Pycopy https://github.com/pfalcon/pycopy
# project.
#
# Copyright (c) 2018 Paul Sokolovsky
#
# The MIT License

import ffi
from uarray import array

import ullvm_c_conf


assert ullvm_c_conf.dynlib
L = ffi.open(ullvm_c_conf.dynlib)


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

# Type methods
F("P", "LLVMVoidType", "")
F("P", "LLVMInt32Type", "")
F("P", "LLVMIntType", "I")
F("P", "LLVMFloatType", "")
F("P", "LLVMDoubleType", "")
F("P", "LLVMPointerType", "PI")
F("P", "LLVMFunctionType", "PPIi")
# Struct type methods
F("P", "LLVMStructCreateNamed", "Ps")
F("v", "LLVMStructSetBody", "PpII")
# Module methods
F("P", "LLVMModuleCreateWithName", "s")
F("i", "LLVMVerifyModule", "PIp")
F("P", "LLVMAddGlobal", "PPs")
F("P", "LLVMAddFunction", "PsP")
# Function methods
F("P", "LLVMAppendBasicBlock", "Ps")
F("P", "LLVMGetParam", "PI")
# Builder methods
F("P", "LLVMCreateBuilder", "")
F("v", "LLVMPositionBuilderAtEnd", "PP")
F("P", "LLVMConstInt", "PQI")
F("P", "LLVMBuildAlloca", "PPs")
F("P", "LLVMBuildAdd", "PPPs")
F("P", "LLVMBuildNeg", "PPs")
F("P", "LLVMBuildRet", "PP")
# Codegeneration functions
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
