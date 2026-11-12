# dagster-katas

Minimal, executable Dagster exercises. Learn one concept at a time, from first principles.

## Philosophy

A *kata* is a focused, repeatable exercise that isolates one concept. This repository applies that idea to Dagster:

- One exercise = one Dagster concept.
- Each exercise is self-contained, runnable, and verifiable.
- Start from the atomic Hello World; increase complexity only after the previous concept is proven.
- No premature data platform, no over-abstraction.

## Exercises

| # | Concept | Status |
|---|---------|--------|
| 001 | Asset Definition & Materialization (Atomic Hello World) | 🚧 |
| 002 | Asset Dependency | 🔜 |
| 003 | Definitions & Code Location | 🔜 |
| 004 | Jobs & Runs | 🔜 |
| 005 | Resources | 🔜 |
| 006 | IO Managers | 🔜 |

## Scratch 001 — Atomic Hello World

This exercise establishes the fundamental relationship between a Python function, a Dagster Asset Definition, and Asset Materialization.

### Prerequisites

- Python 3.13
- uv

### Setup

```bash
uv sync --locked
```

### Experiment 0: Python Baseline (Negative Control)

**Question:** What can plain Python do on its own?

To run Experiment 0 in isolation, comment out Experiments 1 and 2, then run:
```bash
uv run hello.py
```

Expected output:
```
hello
```

This is the baseline. Python executes code and prints output, but provides no asset tracking, no execution context, no materialization events.

---

### Experiment 1: Asset Definition

**Question:** What does `@dg.asset` add to a plain Python function?

The current `hello.py` runs Experiment 1 first, then Experiment 2 in sequence.

Focus on the first part of the output:

```bash
uv run hello.py
```

Expected output (Experiment 1 portion):
```
Asset key path: ['hello']
[]
PASS: Asset definition did not execute the compute function
```

**Observation:** The function is now a Dagster asset definition. Defining the asset does NOT execute the function body. The `compute_calls` list remains empty. This is the distinction between *definition time* and *execution time*.

---

### Experiment 2: Materialization

**Question:** How does Dagster actually execute an asset and record the result?

The second part of `hello.py` calls `materialize_to_memory([hello])` and verifies the result.

Expected output (Experiment 2 portion):
```
Before materialization: []
COMPUTE FUNCTION EXECUTED
Run ID: <uuid>
Value: hello, dagster
Materialization events: 1
  - ASSET_MATERIALIZATION
PASS: Asset materialization succeeded
```

**Observation:** Dagster provides:
- A Run ID for this execution
- A success/failure status (via `result.success`)
- The computed asset value (via `result.asset_value("hello")`)
- Materialization events (via `result.all_events`)

This is what Dagster adds beyond plain Python.

---

### Experiment 3: Controlled Failure

**Question:** How does Dagster report a computation that raises an exception?

Replace the asset body with `raise RuntimeError("CONTROLLED_FAILURE")` and use `raise_on_error=False`.

Run:
```bash
uv run hello.py
```

Expected output:
```
Run ID:    <uuid>
Success:   False
  - <event_type>: <error message>
```

**Observation:** Dagster captures the exception, marks the run as failed, and records the failure in events. This is why orchestration systems cannot rely solely on print statements.

---

### Definition of Done

You have completed Scratch 001 when:

1. ✅ Python baseline observed (Experiment 0)
2. ✅ Asset defined without execution (Experiment 1)
3. ✅ In-memory materialization succeeds (Experiment 2)
4. ✅ Asset value matches expected literal
5. ✅ Materialization events observed
6. ⬜ Controlled failure correctly reported (Experiment 3)
7. ⬜ You can explain the difference between Python execution and Dagster materialization

## Environment

- Python 3.13
- Dagster 1.13.29
- uv (lockfile committed for reproducibility)
