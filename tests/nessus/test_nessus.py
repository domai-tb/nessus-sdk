from nessus import Nessus

PASSWORD = "PASSWORD"


def test_authenticate():
    n = Nessus("https://10.0.3.6:8834/")
    assert n.authenticate(user_pass=("domai-tb", PASSWORD))
    assert n.authenticate(
        api_keys=(
            "ACCESS-KEY",
            "SECRET-KEY",
        )
    )
