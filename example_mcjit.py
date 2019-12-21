from ullvm_c import *


mod = LLVMModuleCreateWithName("mod")

param_types = [LLVMInt32Type(), LLVMInt32Type()]
func_type = LLVMFunctionType(LLVMInt32Type(), param_types, False)
sum = LLVMAddFunction(mod, "sum", func_type)

entry = LLVMAppendBasicBlock(sum, "entry")

builder = LLVMCreateBuilder()
LLVMPositionBuilderAtEnd(builder, entry);

tmp = LLVMBuildAdd(builder, LLVMGetParam(sum, 0), LLVMGetParam(sum, 1), "tmp")
LLVMBuildRet(builder, tmp)

print("LLVMVerifyModule:", LLVMVerifyModule(mod, LLVMAbortProcessAction, None))

LLVMInitializeX86TargetInfo()
LLVMInitializeX86Target()
LLVMInitializeX86TargetMC()
LLVMInitializeX86AsmPrinter()

engine_ref = by_ref("P")
errstr_ref = by_ref("s")

res = LLVMCreateExecutionEngineForModule(engine_ref, mod, errstr_ref)
assert not res
print("CreateExecutionEngine:", res, errstr_ref[0])

engine = engine_ref[0]

addr = LLVMGetFunctionAddress(engine, "sum")
print("func addr:", addr)

f = ffi.func("i", addr, "ii")
print("result:", f(5, 10))
