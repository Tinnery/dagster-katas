# --- Experiment 0: Python Baseline (Negative Control) ---
# Question: What can plain Python do on its own?
print("hello")


# --- Experiment 1: Asset Definition ---
# Question: What does @dg.asset add to a plain Python function?
# Uncomment the block below, then run this file again.

# import dagster as dg
#
# @dg.asset
# def hello() -> str:
#     return "hello, dagster"
#
# print("Asset defined:", hello)
# print("Asset key:", hello.key)


# --- Experiment 2: Materialization ---
# Question: How does Dagster actually execute an asset and record the result?
# Replace Experiment 1 with the block below, then run.

# import dagster as dg
#
# @dg.asset
# def hello() -> str:
#     return "hello, dagster"
#
# if __name__ == "__main__":
#     result = dg.materialize_to_memory([hello])
#     assert result.success, "Materialization failed"
#     value = result.asset_value("hello")
#     assert value == "hello, dagster", f"Unexpected value: {value}"
#     print(f"Run ID:    {result.run_id}")
#     print(f"Success:   {result.success}")
#     print(f"Value:     {value}")
#     print(f"Events:    {len(result.all_events)}")
#     for event in result.all_events:
#         print(f"  - {event.event_type_value}")


# --- Experiment 3: Controlled Failure ---
# Question: How does Dagster report a computation that raises an exception?
# Replace the asset body with a raise, then run with raise_on_error=False.

# import dagster as dg
#
# @dg.asset
# def hello() -> str:
#     raise RuntimeError("CONTROLLED_FAILURE")
#
# if __name__ == "__main__":
#     result = dg.materialize_to_memory([hello], raise_on_error=False)
#     assert not result.success, "Expected failure but got success"
#     print(f"Run ID:    {result.run_id}")
#     print(f"Success:   {result.success}")
#     for event in result.all_events:
#         print(f"  - {event.event_type_value}: {event.message or ''}")
