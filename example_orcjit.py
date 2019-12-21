from ullvm_c import *
import ffi


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

def_triple = LLVMGetDefaultTargetTriple()
print("default triple:", def_triple)

target_ref = by_ref("P")
error_ref = by_ref("s")
print("LLVMGetTargetFromTriple:", LLVMGetTargetFromTriple(def_triple, target_ref, error_ref))
#print(target_ref[0], error_ref[0])

target = target_ref[0]

print("target has JIT:", LLVMTargetHasJIT(target))

target_mach = LLVMCreateTargetMachine(
    target, def_triple, "", "",
    LLVMCodeGenLevelDefault, LLVMRelocDefault, LLVMCodeModelJITDefault
)

orc = LLVMOrcCreateInstance(target_mach)

def orc_sym_resolver(name, ctx):
    print("orc_sym_resolver")
    addr = by_ref("Q")
    err = LLVMOrcGetSymbolAddress(orc, addr, name)
    return addr[0]
orc_sym_resolver_cb = ffi.callback("Q", orc_sym_resolver, "sp")

shmod = LLVMOrcMakeSharedModule(mod)
#print("mod", mod, "shmod", shmod)

orc_mod_ref = by_ref("P")
LLVMOrcAddLazilyCompiledIR(orc, orc_mod_ref, shmod, orc_sym_resolver_cb, None)

addr_ref = by_ref("Q")
err = LLVMOrcGetSymbolAddress(orc, addr_ref, "sum")
addr = addr_ref[0]
#print(err, addr)

f = ffi.func("i", addr, "ii")
print("result", f(5, 10))
