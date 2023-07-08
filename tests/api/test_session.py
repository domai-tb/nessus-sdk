from pytest import raises as should_raise

from api import SessionAPI
from core import NErrors


def test_create_pos():
    resp = SessionAPI("https://10.0.3.6:8834/").create("domai-tb", "PASSWORD")
    assert type(resp) is dict and "token" in resp


def test_create_neg():
    with should_raise(NErrors.AuthenticationError):
        SessionAPI("https://10.0.3.6:8834/").create("domai-tb", "PASSWORD")
