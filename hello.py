# --- Experiment 0: Python Baseline ---
# print("hello")

# --- Experiment 1: Asset Definition ---
import dagster as dg

# 用于观察 Asset 函数是否真的被执行
compute_calls = []

@dg.asset
def hello() -> str:
    compute_calls.append("hello")
    print("COMPUTE FUNCTION EXECUTED")
    return "hello, dagster"

# 只检查 Asset Definition，不启动物化
print("Asset key path:", hello.key.path)

# 验证函数体没有被调用
assert compute_calls == [], f"Unexpected calls: {compute_calls}"
print("PASS: Asset definition did not execute the compute function")
