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
| 001 | Asset Definition & Materialization (Atomic Hello World) | ✅ |
| 002 | Asset Dependency | 🔜 |
| 003 | Definitions & Code Location | 🔜 |
| 004 | Jobs & Runs | 🔜 |
| 005 | Resources | 🔜 |
| 006 | IO Managers | 🔜 |

## Quick Start

```bash
# Prerequisites: Python 3.13, uv
uv sync
.venv/Scripts/python hello.py
```

## Environment

- Python 3.13.14
- Dagster 1.13.29
- uv (lockfile committed for reproducibility)
