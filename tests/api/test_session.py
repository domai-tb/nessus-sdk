from pytest import raises as should_raise

from api import SessionAPI
from core import NErrors

PASSWORD = "PASSWORD"


def test_create():
    session = SessionAPI("https://10.0.3.6:8834/")
    resp = session.create("domai-tb", PASSWORD)
    assert type(resp) is dict and "token" in resp

    with should_raise(NErrors.AuthenticationError):
        SessionAPI("https://10.0.3.6:8834/").create("domai-tb", "")


def test_destroy():
    # authenticated
    session = SessionAPI("https://10.0.3.6:8834/")
    token = session.create("domai-tb", PASSWORD)["token"]
    session.headers.update({"X-Cookie": f"token={token}"})
    session.destroy()

    # unauthenticated if no exception
    with should_raise(NErrors.AuthenticationError):
        session.destroy()
