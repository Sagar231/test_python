import pytest
from validator.validator import validate_name
from validator.rules import (
    SENDER_NAME_MIN, SENDER_NAME_MAX,
    RECEIVER_NAME_MIN, RECEIVER_NAME_MAX,
    ERR,
)

def test_sender_name_trim_and_bounds_ok():
    validate_name("   Alice Liddel   ", min_len=SENDER_NAME_MIN, max_len=SENDER_NAME_MAX)

@pytest.mark.parametrize("bad", ["a"*4, "a"*31, "", "   a   ", "a"*200])
def test_sender_name_bad_lengths(bad):
    with pytest.raises(ValueError) as e:
        validate_name(bad, min_len=SENDER_NAME_MIN, max_len=SENDER_NAME_MAX)
    assert str(e.value) == ERR["name_len"]

def test_receiver_name_bounds_ok():
    validate_name("Marketing Team", min_len=RECEIVER_NAME_MIN, max_len=RECEIVER_NAME_MAX)

@pytest.mark.parametrize("bad", ["a"*4, "a"*61])
def test_receiver_name_bad_lengths(bad):
    with pytest.raises(ValueError) as e:
        validate_name(bad, min_len=RECEIVER_NAME_MIN, max_len=RECEIVER_NAME_MAX)
    assert str(e.value) == ERR["name_len"]

def test_name_type_error():
    with pytest.raises(ValueError) as e:
        validate_name(None, min_len=SENDER_NAME_MIN, max_len=SENDER_NAME_MAX)  # type: ignore
    assert str(e.value) == ERR["name_type"]
