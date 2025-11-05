SENDER_NAME_MIN = 5
SENDER_NAME_MAX = 30
RECEIVER_NAME_MIN = 5
RECEIVER_NAME_MAX = 60
EMAIL_MAX_TOTAL = 254
EMAIL_LOCAL_MAX = 64
EMAIL_DOMAIN_MAX = 251
EMAIL_ALLOWED_CHARS = set(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "@-."
)
ALLOWED_TLDS = (".com", ".net", ".org")
ERR = {
    "name_len": "Invalid name length",
    "name_type": "Name must be a string",
    "email_type": "Email must be a string",
    "email_at_count": "Email must contain exactly one @",
    "email_len_total": "Email length exceeds 254 bytes",
    "email_len_local": "Local part length exceeds 64 bytes",
    "email_len_domain": "Domain part length exceeds 251 bytes",
    "email_charset": "Email contains invalid characters",
    "email_local_edge": "Local part cannot start or end with '-' or '.'",
    "email_tld": "Email must end with .com, .net, or .org",
    "placeholders_missing": "HTML placeholders missing replacements",
    "placeholders_surplus": "Replacements contain surplus keys",
}
