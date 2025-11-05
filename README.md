
# Email Validation Challenge

## Goal

Implement robust validation for:

1. **Names** (sender/receiver)
2. **Email addresses** (sender/receiver)
3. **HTML payload placeholders** (e.g., `{first_name}`)

All logic must be written in `src/validator/validator.py`. The file currently contains empty function bodies — you must implement them so the tests pass.

---

## What to implement (requirements)

### Task 1: Validate Names

* **Sender name** length: 5–30 characters (inclusive).
* **Receiver name** length: 5–60 characters (inclusive).
* Ignore **leading/trailing spaces** before checking length.
* Raise **ValueError** for each validation failure:

  * Use message `ERR["name_type"]` if input is not a string.
  * Use message `ERR["name_len"]` if length is outside the allowed range.

### Task 2: Validate Email Addresses

Apply these rules to **both** sender and receiver email addresses:

* Must contain **exactly one** `@`.
* **Total length** ≤ **254 bytes**.
* **Local part** (before `@`) ≤ **64 bytes**.
* **Domain part** (after `@`) ≤ **251 bytes**.
* Allowed characters: **A–Z**, **a–z**, **0–9**, `@`, `-`, `.` (no others).
* The **local part** must **not** start or end with `-` or `.`.
* Domain must end with one of: **.com**, **.net**, **.org**.
* Ignore **leading/trailing spaces** before validating.
* Raise **ValueError** with the exact messages from `src/validator/rules.py`:

  * `email_type`, `email_at_count`, `email_len_total`, `email_len_local`,
    `email_len_domain`, `email_charset`, `email_local_edge`, `email_tld`.

### Task 3: Validate HTML Payload Placeholders

Given an HTML string and a `replacements` dict:

* Extract all placeholders of the form `{placeholder}` from the HTML.
* If **any placeholder** in HTML is **missing** in `replacements`, raise `ValueError(ERR["placeholders_missing"])`.
* If `replacements` contains **extra keys** not present as placeholders in HTML, raise `ValueError(ERR["placeholders_surplus"])`.

---

## Where to code

Edit **only**:

```
src/validator/validator.py
```

Implement the functions:

* `validate_name(name: str, *, min_len: int, max_len: int) -> None`
* `_check_email_chars(addr: str) -> None`
* `validate_email_addr(addr: str) -> None`
* `validate_email_payload(sender_name, sender_addr, receiver_name, receiver_addr, html, replacements) -> None`

Do **not** change the tests or constants.

---

## Project structure

```
email-validation-challenge/
├─ README.md
├─ requirements.txt
├─ pyproject.toml           # pytest config to add src/ to PYTHONPATH
├─ fixtures/
│  └─ email_template.html
├─ src/
│  └─ validator/
│     ├─ __init__.py
│     ├─ rules.py          # constants + error messages
│     └─ validator.py      # implement here
└─ tests/
   ├─ test_names.py
   ├─ test_emails.py
   └─ test_payload.py
```

---

## Setup & run (Windows PowerShell / CMD)

> Note: Your folder is called **email-validation-challenge**.
> (If you used “email-validation-challange” by mistake, `cd` into that exact name.)
> Initially tests will fail.

```bat
cd email-validation-challenge

python -m venv .venv
venv\Scripts\activate

pip install -r requirements.txt

pytest -q
```

---

## Setup & run (macOS/Linux)

```bash
cd /path/to/email-validation-challenge

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

pytest -q
```

---

## Expected outcome

* Initially, tests **fail** because `validator.py` is unimplemented.
* After you implement all rules correctly, running `pytest -q` should **pass** all tests.

---

## Notes

* Use **exact** error messages from `rules.py` (`ERR[...]`) so tests match.
* Length limits for emails are in **bytes** (encode to UTF-8 before measuring).
* Trimming (for names and emails) applies only to **leading/trailing** spaces.
