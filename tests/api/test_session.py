from pytest import raises as should_raise

from api import SessionAPI
from core import NErrors

PASSWORD = "nUEGy9$!5e@J5we#Eh5!4fMw$7syfoYQk6aYZCg!WiZHG4r3zJmLp2#XJzDk"


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


def test_keys():
    # authenticated
    session = SessionAPI("https://10.0.3.6:8834/")
    token = session.create("domai-tb", PASSWORD)["token"]
    session.headers.update({"X-Cookie": f"token={token}"})
    keys = session.keys()

    assert "accessKey" in keys and "secretKey" in keys

    # unauthenticated if no exception
    session.destroy()
    with should_raise(NErrors.AuthenticationError):
        session.destroy()


def test_get():
    # authenticated
    session = SessionAPI("https://10.0.3.6:8834/")
    token = session.create("domai-tb", PASSWORD)["token"]
    session.headers.update({"X-Cookie": f"token={token}"})
    keys = session.keys()
    session.headers.update(
        {"X-ApiKeys": f"accessKey={keys['accessKey']}; secretKey={keys['secretKey']}"}
    )

    r = session.get()
    assert "id" in r and "username" in r and "name" in r and "permissions" in r

    # unauthenticated if no exception
    session.destroy()
    with should_raise(NErrors.AuthenticationError):
        session.destroy()
