from api import NessusAPI


def test_base1():
    result = NessusAPI().base.request("GET", "/")
    assert result == {}


def test_base2():
    result = NessusAPI().base.get("/")
    assert result == {}


def test_base3():
    result = NessusAPI().base.post("/", {})
    assert result == {}


def test_auth1():
    result = NessusAPI().auth.login()
    assert result is False
