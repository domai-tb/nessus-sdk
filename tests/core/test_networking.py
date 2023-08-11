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
    with should_raise(NErrors.NetworingError):
        net.GET("/")


def test_request_pos():
    net = Networking("https://10.0.3.6:8834/")
    rep = net.GET("/server/status")
    assert type(rep) is dict and rep["status"] == "ready"


def test_get_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.NetworingError):
        net.GET("/")


def test_post_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.NetworingError):
        net.POST("/", params={})


def test_put_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.NetworingError):
        net.PUT("/", params={})


def test_delete_neg():
    net = Networking("https://127.0.0.1:8834/#")
    with should_raise(NErrors.NetworingError):
        net.DELETE("/")


def test_header_pos():
    net = Networking("https://127.0.0.1:8834/#")
    net.headers = {"test": "test"}
    assert Networking("http://example.com").headers == {"test": "test"}

    net.headers = {}
    net.headers.update({"test2": "test2"})
    assert Networking("http://example123.com").headers == {"test2": "test2"}


def test_header_neg():
    net = Networking("https://127.0.0.1:8834/#")
    net.headers = {"test": "test"}
    assert Networking("http://example.com").headers != {}
