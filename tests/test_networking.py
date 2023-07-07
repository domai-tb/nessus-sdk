from pytest import raises as should_raise

from core import NessusErrors, Networking


def test_validation_neg():
    with should_raise(NessusErrors.ValidationError):
        Networking("localhost")


def test_validation_pos():
    net = Networking("https://127.0.0.1:8834/#")
    assert net.base_url == "https://127.0.0.1:8834"


def test_request_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NessusErrors.NetworingError):
        net.get("/")


def test_request_pos():
    net = Networking("https://10.0.3.6:8834/")
    rep = net.get("/server/status")
    assert type(rep) is dict and rep["status"] == "ready"
