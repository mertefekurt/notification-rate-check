![Notification Rate Check cover](assets/readme-cover.svg)

# Notification Rate Check

> Audit notification plans for rate limits, quiet hours, and opt-out controls

This is a review desk for notification quality. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `notification-rate-check`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `no-rate-limit` | high | rate limit missing |
| `missing-quiet-hours` | medium | quiet hours missing |
| `missing-optout` | low | opt-out missing |

## Try the sample

```bash
git clone https://github.com/mertefekurt/notification-rate-check.git
cd notification-rate-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
notification-rate-check examples/sample.txt
notification-rate-check examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
