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
print(f"{compute_calls}")
assert compute_calls == [], f"Unexpected calls: {compute_calls}"
print("PASS: Asset definition did not execute the compute function")

# --- Experiment 2: Materialization ---
print("Before materialization:", compute_calls)
result = dg.materialize_to_memory([hello])

# Verify execution succeeded
assert result.success, "Materialization failed"
print("Run ID:", result.run_id)

# Verify compute function was called exactly once
assert compute_calls == ["hello"], f"Unexpected compute_calls: {compute_calls}"

# Verify asset value
value = result.asset_value("hello")
assert value == "hello, dagster", f"Unexpected value: {value}"
print("Value:", value)

# Inspect materialization events
materialization_events = [
    event
    for event in result.all_events
    if event.event_type_value == "ASSET_MATERIALIZATION"
]

assert len(materialization_events) == 1, f"Expected 1 materialization event, got {len(materialization_events)}"
print(f"Materialization events: {len(materialization_events)}")
for event in materialization_events:
    print(f"  - {event.event_type_value}")

print("PASS: Asset materialization succeeded")
