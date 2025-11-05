import pathlib
import re
import pytest
from validator.validator import validate_email_payload
from validator.rules import ERR

FIXTURES = pathlib.Path(__file__).parent.parent / "fixtures"

def read_template():
    return (FIXTURES / "email_template.html").read_text(encoding="utf-8")

def test_payload_happy_path():
    html = read_template()
    validate_email_payload(
        sender_name="Marketing @T-Shoes",
        sender_addr="marketing@tshoes.com",
        receiver_name="Jane Doe",
        receiver_addr="janedoe5511@gmail.com",
        html=html,
        replacements={"first_name": "Jane"},
    )

def test_payload_missing_placeholder():
    # Remove {first_name} from template
    html = re.sub(r"\{first_name\}", "friend", read_template())
    with pytest.raises(ValueError) as e:
        validate_email_payload(
            sender_name="Marketing Team",
            sender_addr="marketing@tshoes.com",
            receiver_name="Jane Doe",
            receiver_addr="janedoe5511@gmail.com",
            html=html,
            replacements={"first_name": "Jane"},
        )
    assert str(e.value) == ERR["placeholders_missing"]

def test_payload_surplus_replacements():
    html = read_template()
    with pytest.raises(ValueError) as e:
        validate_email_payload(
            sender_name="Marketing Team",
            sender_addr="marketing@tshoes.com",
            receiver_name="Jane Doe",
            receiver_addr="janedoe5511@gmail.com",
            html=html,
            replacements={"first_name": "Jane", "last_name": "Doe"},
        )
    assert str(e.value) == ERR["placeholders_surplus"]
