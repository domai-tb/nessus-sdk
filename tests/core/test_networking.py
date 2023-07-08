from pytest import raises as should_raise

from core import NErrors, Networking


def test_validation_neg():
    with should_raise(NErrors.ValidationError):
        Networking("localhost")


def test_validation_pos():
    net = Networking("https://127.0.0.1:8834/#")
    assert net.base_url == "https://127.0.0.1:8834"


def test_request_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.UnexpectedNetworingError):
        net.get("/")


def test_request_pos():
    net = Networking("https://10.0.3.6:8834/")
    rep = net.get("/server/status")
    assert type(rep) is dict and rep["status"] == "ready"


def test_get_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.UnexpectedNetworingError):
        net.get("/")


def test_post_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.UnexpectedNetworingError):
        net.post("/", params={})


def test_put_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.UnexpectedNetworingError):
        net.put("/", params={})


def test_delete_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.UnexpectedNetworingError):
        net.delete("/")


def test_header_pos():
    net = Networking("https://127.0.0.1:8834/#")
    net.headers = {"test": "test"}
    assert Networking("http://example.com").headers == {"test": "test"}


def test_header_neg():
    net = Networking("https://127.0.0.1:8834/#")
    net.headers = {"test": "test"}
    assert Networking("http://example.com").headers != {}
