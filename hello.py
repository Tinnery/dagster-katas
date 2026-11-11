"""
Dagster Katas — Experiment 001: Atomic Hello World

This file is the target state of the kata.
Do NOT read ahead. Work through experiments 0–3 one at a time.

Target code (final form):

    import dagster as dg

    @dg.asset
    def hello() -> str:
        return "hello, dagster"

    if __name__ == "__main__":
        result = dg.materialize_to_memory([hello])
        assert result.success
        assert result.asset_value("hello") == "hello, dagster"
        print(f"Run ID: {result.run_id}")
"""

# --- Experiment 0: Python Baseline (Negative Control) ---
# Uncomment and run this first, without Dagster.
# print("hello")


# --- Experiment 1: Asset Definition ---
# Introduce @dg.asset. Observe that importing does NOT execute the function.
# import dagster as dg
#
# @dg.asset
# def hello() -> str:
#     return "hello, dagster"
#
# print("Asset defined:", hello)
# print("Asset key:", hello.key)


# --- Experiment 2: Materialization ---
# Execute the asset through Dagster's in-process materialization API.
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
# Modify the asset to raise, then run with raise_on_error=False.
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
