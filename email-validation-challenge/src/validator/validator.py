from __future__ import annotations
from typing import Dict
from .rules import (
    SENDER_NAME_MIN, SENDER_NAME_MAX,
    RECEIVER_NAME_MIN, RECEIVER_NAME_MAX,
    EMAIL_MAX_TOTAL, EMAIL_LOCAL_MAX, EMAIL_DOMAIN_MAX,
    EMAIL_ALLOWED_CHARS, ALLOWED_TLDS, ERR,
)

def validate_name(name: str, *, min_len: int, max_len: int) -> None:
    # TODO: validate type and length after stripping spaces
    pass

def _check_email_chars(addr: str) -> None:
    # TODO: ensure only valid characters from EMAIL_ALLOWED_CHARS are used
    pass

def validate_email_addr(addr: str) -> None:
    # TODO: implement all email validation rules
    pass

def validate_email_payload(
    sender_name: str,
    sender_addr: str,
    receiver_name: str,
    receiver_addr: str,
    html: str,
    replacements: Dict[str, str],
) -> None:
    # TODO: validate names, emails, and placeholders
    pass
