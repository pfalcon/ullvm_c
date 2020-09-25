# ullvm - Lightweight bindings for LLVM C API
#
# This module is part of the Pycopy https://github.com/pfalcon/pycopy
# project.
#
# Copyright (c) 2018-2020 Paul Sokolovsky
#
# The MIT License

import ffi
from uarray import array

import ullvm_c_conf


assert ullvm_c_conf.dynlib
L = ffi.open(ullvm_c_conf.dynlib)


def F(ret, name, params):
    globals()[name] = L.func(ret, name, params)

# Initializer for functions which need Python wrappers.
def F_(ret, name, params):
    globals()[name + "_"] = L.func(ret, name, params)


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
F("P", "LLVMInt8Type", "")
F("P", "LLVMInt16Type", "")
F("P", "LLVMInt32Type", "")
F("P", "LLVMInt64Type", "")
F("P", "LLVMIntType", "I")
F("P", "LLVMFloatType", "")
F("P", "LLVMDoubleType", "")
F("P", "LLVMPointerType", "PI")
F_("P", "LLVMFunctionType", "PPIi")
F("P", "LLVMGetElementType", "P")
# Struct type methods
F("P", "LLVMStructCreateNamed", "Ps")
F("v", "LLVMStructSetBody", "PpII")
# Value methods
F("s", "LLVMGetValueName", "P")
F("v", "LLVMSetValueName", "Ps")
F("P", "LLVMTypeOf", "P")
F("P", "LLVMConstInt", "PQI")
F("P", "LLVMConstString", "sII")
F("P", "LLVMConstIntToPtr", "PP")
F("v", "LLVMSetInitializer", "PP")
# Module methods
F("P", "LLVMModuleCreateWithName", "s")
F("i", "LLVMVerifyModule", "PIp")
F("v", "LLVMDumpModule", "P")
F_("s", "LLVMPrintModuleToString", "P")
F("i", "LLVMWriteBitcodeToFile", "Ps")
F("P", "LLVMAddGlobal", "PPs")
F("P", "LLVMAddFunction", "PsP")
# Function methods
F("P", "LLVMAppendBasicBlock", "Ps")
F("I", "LLVMCountParams", "P")
F("P", "LLVMGetParam", "PI")
# Builder methods
F("P", "LLVMCreateBuilder", "")
F("v", "LLVMPositionBuilderAtEnd", "PP")
F("P", "LLVMBuildAlloca", "PPs")
F("P", "LLVMBuildLoad", "PPs")
F("P", "LLVMBuildStore", "PPP")
F_("P", "LLVMBuildGEP", "PPPIs")
F("P", "LLVMBuildAdd", "PPPs")
F("P", "LLVMBuildSub", "PPPs")
F("P", "LLVMBuildAnd", "PPPs")
F("P", "LLVMBuildOr", "PPPs")
F("P", "LLVMBuildXor", "PPPs")
F("P", "LLVMBuildAShr", "PPPs")
F("P", "LLVMBuildLShr", "PPPs")
F("P", "LLVMBuildShl", "PPPs")
F("P", "LLVMBuildNeg", "PPs")
F_("P", "LLVMBuildCall", "PPPIs")
F("P", "LLVMBuildRet", "PP")
F("P", "LLVMBuildBr", "PP")
F("P", "LLVMBuildCondBr", "PPPP")
# Context methods
F("P", "LLVMGetGlobalContext", "")
# Memory and resource management
F("v", "LLVMDisposeMessage", "P")
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
F("i", "LLVMCreateMCJITCompilerForModule", "pPpLp")
F("v", "LLVMAddModule", "PP")
F("P", "LLVMCreateGenericValueOfInt", "Pqi")
F("P", "LLVMRunFunction", "PPIP")
F("Q", "LLVMGetFunctionAddress", "Ps")

# LLVMOrcMakeSharedModule is removed in LLVM 7 as apparently no longer needed
try:
    F("P", "LLVMOrcMakeSharedModule", "P")
except OSError:  # ENOENT
    LLVMOrcMakeSharedModule = lambda x: x

F("P", "LLVMOrcCreateInstance", "P")
F("i", "LLVMOrcAddEagerlyCompiledIR", "PpPCp")
F("i", "LLVMOrcAddLazilyCompiledIR", "PpPCp")
F("i", "LLVMOrcGetSymbolAddress", "Pps")


def by_ref(type):
    if type in ("p", "P", "s"):
        type = "L"
    return array(type, [0])


def reflist2array(l):
    return array("L", l)


# Note: param_count is not accepted as in raw C API
def LLVMFunctionType(return_type, params, var_arg=False):
    func_type = LLVMFunctionType_(
        return_type, reflist2array(params), len(params), var_arg
    )
    return func_type


# Note: NumIndices is not accepted as in raw C API
def LLVMBuildGEP(builder, ptr, indices, name=None):
    val = LLVMBuildGEP_(
        builder, ptr, reflist2array(indices), len(indices), name
    )
    return val


# Note: NumArgs is not accepted as in raw C API
def LLVMBuildCall(builder, func, args, name=""):
    val = LLVMBuildCall_(
        builder, func, reflist2array(args), len(args), name
    )
    return val


def LLVMPrintModuleToString(m):
    s = LLVMPrintModuleToString_(m)
    # Would need uctypes.str_at(), or alternatively, strlen(). For now just
    # use ffi's "s" return type. TODO: Fix memory leak.
    #LLVMDisposeMessage(s)
    return s
