import pytest
from validator.validator import validate_email_addr
from validator.rules import ERR

@pytest.mark.parametrize("addr", [
    "marketing@tshoes.com",
    "User.Name-99@Example-Store.net",
    "A12345@sub.domain.org",
    "  simple@host.com  ",  # leading/trailing spaces ignored
])
def test_email_valid(addr):
    validate_email_addr(addr)

@pytest.mark.parametrize("addr,expected", [
    (None, ERR["email_type"]),
    ("nosymbol.example.com", ERR["email_at_count"]),
    ("double@@example.com", ERR["email_at_count"]),
])
def test_email_at_and_type(addr, expected):
    with pytest.raises(ValueError) as e:
        validate_email_addr(addr)  # type: ignore
    assert str(e.value) == expected

def test_email_length_total():
    local = "a"*64
    domain = "b"*185 + ".com"   # 64 + 1 + 189 + 4 = 258 > 254
    with pytest.raises(ValueError) as e:
        validate_email_addr(f"{local}@{domain}")
    assert str(e.value) == ERR["email_len_total"]

def test_email_length_local():
    local = "a"*65
    with pytest.raises(ValueError) as e:
        validate_email_addr(f"{local}@example.com")
    assert str(e.value) == ERR["email_len_local"]

def test_email_length_domain():
    domain = "b"*252 + ".com"  # 256 > 251
    with pytest.raises(ValueError) as e:
        validate_email_addr(f"abc@{domain}")
    assert str(e.value) == ERR["email_len_domain"]

@pytest.mark.parametrize("addr", [
    "bad char@host.com",
    "user+plus@host.com",
    "user@host!.com",
])
def test_email_charset(addr):
    with pytest.raises(ValueError) as e:
        validate_email_addr(addr)
    assert str(e.value) == ERR["email_charset"]

@pytest.mark.parametrize("addr", [
    ".start@host.com",
    "-start@host.com",
    "end.@host.com",
    "end-@host.com",
])
def test_email_local_edge(addr):
    with pytest.raises(ValueError) as e:
        validate_email_addr(addr)
    assert str(e.value) == ERR["email_local_edge"]

@pytest.mark.parametrize("addr", [
    "user@host.io",
    "user@host.xyz",
    "user@host.co",
])
def test_email_bad_tld(addr):
    with pytest.raises(ValueError) as e:
        validate_email_addr(addr)
    assert str(e.value) == ERR["email_tld"]

def test_email_good_tld_cases():
    for addr in ("u@h.com", "u@h.net", "u@h.org"):
        validate_email_addr(addr)
