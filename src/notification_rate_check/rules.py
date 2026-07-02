from __future__ import annotations

from notification_rate_check.models import Rule

PROJECT_NAME = 'notification-rate-check'
SUMMARY = 'Audit notification plans for rate limits, quiet hours, and opt-out controls.'
SAMPLE_RISK = 'push alerts rate_limit none quiet_hours missing optout none'
SAMPLE_CLEAN = 'push alerts rate_limit 3/day quiet_hours enabled optout supported'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='no-rate-limit',
        severity='high',
        pattern='rate_limit\\s+(none|missing|unknown)',
        message='rate limit missing',
        recommendation='define max notifications',
    ),
    Rule(
        code='missing-quiet-hours',
        severity='medium',
        pattern='quiet_hours\\s+(missing|none|unknown)',
        message='quiet hours missing',
        recommendation='respect local quiet hours',
    ),
    Rule(
        code='missing-optout',
        severity='low',
        pattern='optout\\s+(none|missing|unknown)',
        message='opt-out missing',
        recommendation='provide opt-out control',
    ),
)
