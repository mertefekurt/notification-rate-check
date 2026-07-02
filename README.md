# notification-rate-check

> Audit notification plans for rate limits, quiet hours, and opt-out controls.

## Spec sheet Overview

Audit notification plans for rate limits, quiet hours, and opt-out controls. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts notification plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
notification-rate-check examples/sample.txt
notification-rate-check examples/sample.txt --json --fail-on medium
python -m notification_rate_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `no-rate-limit` | high | rate limit missing |
| `missing-quiet-hours` | medium | quiet hours missing |
| `missing-optout` | low | opt-out missing |

## Validation Notes

```bash
ruff check .
pytest
python -m notification_rate_check --help
```

Example risky input:

```text
push alerts rate_limit none quiet_hours missing optout none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
