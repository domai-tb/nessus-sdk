from nessus import Nessus

PASSWORD = "nUEGy9$!5e@J5we#Eh5!4fMw$7syfoYQk6aYZCg!WiZHG4r3zJmLp2#XJzDk"


def test_authenticate():
    n = Nessus("https://10.0.3.6:8834/")
    assert n.authenticate(user_pass=("domai-tb", PASSWORD))
    assert n.authenticate(
        api_keys=(
            "ACCESS-KEY",
            "SECRET-KEY",
        )
    )
